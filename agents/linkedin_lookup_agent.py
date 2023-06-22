from langchain import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from tools.tools import get_google_result


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')
    template = '''given the company name {name_of_company} I want you to get me the URL for their Linkedin page. Your answer should contain only a URL'''
    # the last sentence in the template is an Output Indicator
    tools = [Tool(name="Search Google for LinkedIn Profile"
                  , func=get_google_result
                  , description="useful for when you need to get the Linkedin URL"
                  )
             ]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt_template = PromptTemplate(input_variables=["name_of_company"], template=template)
    linkedin_url = agent.run(prompt_template.format_prompt(name_of_company=name))
    return linkedin_url
    # description parameter is optional but recommended for the agent to know when to use the tool
