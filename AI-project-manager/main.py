
from typing import TypedDict,Literal
from langgraph.graph import StateGraph, END,START
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver  


### define LLM and Embeddings
llm = ChatOllama(model="llama3.2:latest")





# -------------------------
# State Definition
from langgraph.checkpoint.memory import InMemorySaver  


# -------------------------
class AgentState(TypedDict):
    task: str
    history: str
    final_output: str

checkpointer = InMemorySaver()  


# -------------------------
# Agent Implementations
# -------------------------

def performer_agent(state: AgentState):
    prompt = f"""
    You are the Performer Agent.
    Your role:
    - Understand the original user task
    - define requirements 
    - required output format
    {state['task']}
    """
    result =llm.invoke(prompt)
    return {"history": state["history"] + "\n\n[PERFORMER]\n" + result.content}


def research_agent(state: AgentState):
    prompt = f"""
You are the Research Agent.
Your role:
    -Collect technical insights, best practices, and architecture ideas for:

{state['task']}

Provide concise, high-value research notes.
"""
    result = llm.invoke(prompt)
    return {"history": state["history"] + "\n\n[RESEARCH]\n" + result.content}




def developer_agent(state: AgentState):
    prompt = f"""
You are the Developer Agent.
Your role:
    - Leverage research insights to design a solution for the given task
    - create implementation ideas, architecture design, and example code snippets
    - write code snippets in python
    - complexity level should be appropriate for the task
    - task should be achievable with provided code snippets

Task:
{state['task']}

Research & Context:
{state['history']}

Produce implementation ideas, architecture design, and example code snippets.
"""
    result = llm.invoke(prompt)
    return {"history": state["history"] + "\n\n[DEVELOPER]\n" + result.content}


def analyst_agent(state: AgentState):
    prompt = f"""
You are the Analyst Agent.

Analyze and optimize the solution below.
Focus on scalability, performance, security, and cost efficiency.
Analyze efficiency and scalability of the proposed solution.
Define the cost for this solution.

{state['history']}
"""
    result = llm.invoke(prompt)
    return {"history": state["history"] + "\n\n[ANALYST]\n" + result.content}


def performerFinal_agent(state: AgentState):
    prompt = f"""
You are the PerformerFinal Agent.

Your role:

- Synthesize all agent outputs
- Produce a structured, professional final answer
- Ensure clarity, coherence, and completeness
- include code snippets of the task

User Task:
{state['task']}

Collected Outputs:
{state['history']}

Generate a high-quality final response:
"""
    result = llm.invoke(prompt)
    return {"final_output": result.content}

# -------------------------
# LangGraph Workflow
# -------------------------

builder = StateGraph(AgentState)

#graph = builder.compile(checkpointer=checkpointer)  

#graph.invoke(builder, {"configurable": {"thread_id": "1"}})

builder.add_node("research", research_agent)
builder.add_node("developer", developer_agent)
builder.add_node("analyst", analyst_agent)
builder.add_node("performer", performer_agent)
builder.add_node("performerFinal", performerFinal_agent)

builder.set_entry_point("performer")


builder.add_edge("performer", "research")
builder.add_edge("research", "developer")
builder.add_edge("developer", "analyst")
builder.add_edge("analyst", "performerFinal")
builder.add_edge("performerFinal", END)

graph = builder.compile(checkpointer=checkpointer)

#executor = builder.compile()

# -------------------------
# Execution Runner
# -------------------------

if __name__ == "__main__":
    task = input("\nEnter your task: ")

    result = graph.invoke({
        "task": task,  
        "history": "",
        "final_output": ""
    },
    {"configurable": {"thread_id": "1"}}
    )

    print("\n" + "="*80)
    print("FINAL OUTPUT\n")
    print(result["final_output"])
    print("="*80)
