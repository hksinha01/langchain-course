## Install packages ##
        
    langchain (Core framework for building language model applications using modular components (e.g., chains, agents, tools). Use when building LLM-powered workflows.)
    langchain-openai (Integration package that connects LangChain with OpenAI’s models (e.g., GPT-4, embeddings). One of the AI-venders or LLM provider.)
    langchain-community (Collection of community-contributed integrations and utilities (e.g., retrievers, text splitters, tools).  Use for extra features like file loaders, chunkers, and connectors.)
    langchainhub  (Client for accessing LangChain Hub, a shared repository of prompts, chains, and agents.  Use to fetch reusable components and templates from the cloud.)

    Installed black : Formatter, After install Run black in terminal it will format
    python-dotenv : To use .env file and access its values


## PromptTemplate ## :  
    LLM Recives input in format of Prompt ( text input that we gave ). In Prompt template We want to give parameters in it so we use Prompt Template. We Can pass variable input

## Chat Models ## : 

    Wrappers around LLM which help us interact with them as we use in chat message. What we send has a role of HumanMessage and , what llm send has a role of AiMessage.

        System Messsage
        Human Message
        Ai message
        Humman Message
        AI Message

## Chains ## : 

    Chains allows us to combine multiple components together to help us create one single coherent applications


## Invoking chat model ## 
    llm = ChatOpenAI(temperature= 0, model_name="gpt-4")
    
        here temperature is creativity of chatModel make the model answer more creatively. (Default: 0.8) , model_name, openai_api_key ,  max_tokens,etc can also be passed

            ** In newer / recent versions of LangChain (langchain-openai), the ChatOpenAI constructor no longer accepts model_name instead uses "" model "" param **

    chain = summary_prompt_template | llm

            summary_prompt_template → something that takes in variables and formats them into a prompt.

            llm → the language model that takes that prompt and generates text.

            | → creates a sequential pipeline: output of the left-hand side is automatically fed as input to the right-hand side.

    res = chain.invoke(input = {"information" : information})

    For not to get tracing 403 error we need to add LANGCHAIN_TRACING_V2 as false in environment variables

## Using open Source Modals ##

    There are modals like Ollama, Llama3, Mistral  ... Good with codes like summary and basic stuff... For reasoning use 1st tier modals like cluade, OpenAi , etc
    For Deploy open source modal in our system we are going to use Ollama

## OutputParsers

    It is used to parse the output of AI and convert the data in json, string, pydantic, etc. 
        Ex: StrOutputParser() , gets .content from output and returns string in it



## AI Agents##
    
    Software system which uses LLM as a reasoning agent to decide what action to take and then execute these action.
    
    Chain : In chain developer defined control flow. Ex: Start ---> Step1 ---> Step 2 ---> End
    Agent : LLM defined control flow. Ex: Step 1 ---> LLM --> Back to step1 (When we have the actions go to step2) --> Step2 ---> END

    ReAct Agent Architecture (1st agent): Langchain and Langraphs comes with prebuild ReAct agent which we can use and customize and it can use tools, they can handle compact workflow and mantain state over long run flow
            
        Query ---> Thinking --> Action --> Tool --> Observation ---> Thinking ---> Answer