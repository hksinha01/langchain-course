from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor # Runtime just like a for loop
from langchain.agents.react.agent import  create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()
tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")

# Getting a ReAct Prompt pull
react_prompt = hub.pull("hwchase17/react")

# Creating Reasoning Agent -> returning us a chain
# this chain is simply going to receive the tool, user query and will send everything to llm. LLM Is going to return response and
# executor maybe call a tool or maybe new llm call
agent = create_react_agent(
    llm,
    tools=tools,
    prompt=react_prompt)

# Executing Agent -> Maybe call a tool or maybe new llm call
agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=True)
chain = agent_executor


def main():
    result = chain.invoke(
        input={
            "input": "Search for 5 job posting for MEAN stack developer , ai engineer using python and langchain in india (remote or hybrid) and list their details"
        }
    )

    print(result)


if __name__ == "__main__":
    main()
