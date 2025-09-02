from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor  # Runtime just like a for loop
from langchain.agents.react.agent import create_react_agent
# from langchain.chains.question_answering.map_rerank_prompt import output_parser
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.output_parsers.pydantic import PydanticOutputParser # Get response fromm llm and parse that response in pydantic model object
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse


load_dotenv()
tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
output_parser = PydanticOutputParser(pydantic_object=AgentResponse) # Commented previous output Parser to run our Pydantic parser
react_prompt_with_format_instructions = PromptTemplate(
    template= REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad","tool_names"]
).partial(format_instructions=output_parser.get_format_instructions())
# Getting a ReAct Prompt pull
react_prompt = hub.pull("hwchase17/react")

# Creating Reasoning Agent -> returning us a chain
# this chain is simply going to receive the tool, user query and will send everything to llm. LLM Is going to return response and
# executor maybe call a tool or maybe new llm call
agent = create_react_agent(llm, tools=tools, prompt=react_prompt_with_format_instructions) # removed react_prompt to run our own formatted prompt

# Executing Agent -> Maybe call a tool or maybe new llm call
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
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
