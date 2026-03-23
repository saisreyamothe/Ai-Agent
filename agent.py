#Importing the required modules
from typing import Annotated,TypedDict
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode,tools_condition
from tools import search_tool
#1.Define the state(what the agent remembers during the conversation)
class State(TypedDict):
    messages: Annotated[list,add_messages]

def create_agent():
    #2.Initializing the local LLM
    llm=ChatOllama(model="llama3.1",temperature=0)
    #3.We will get our tools from tools.py and bind them here.
    tools=[search_tool]
    llm_with_tools=llm.bind_tools(tools)
    #4.Defining the assistant node(The Thinking step)
    def chatbot(state:State):
        return{"messages":[llm_with_tools.invoke(state["messages"])]}
    #5.Building the graph workflow
    workflow=StateGraph(State)
    #6.Adding the workstations(Nodes)
    workflow.add_node("chatbot",chatbot)
    workflow.add_node("tools",ToolNode(tools))
    #7.Defining the movement
    workflow.add_edge(START,"chatbot")
    #8.Logic:The LLM decides to use 'tools' or 'END'
    workflow.add_conditional_edges("chatbot",tools_condition)
    #9.After using the tool the agent must think again
    workflow.add_edge("tools","chatbot")
    return workflow.compile()