from langchain import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from tools.tools import get_google_result

def twitter_lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')
    template = '''given the company name {name_of_company} I want you to find their Twitter profile page and extract their username from that page. Your final answer should only contain a name that starts with the @ character'''
    # the last sentence in the template is an Output Indicator
    tools = [Tool(name="Search Google for Twitter username"
                  , func=get_google_result
                  , description="useful for when you need to get the Twitter profile page"
                  )
             ]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt_template = PromptTemplate(input_variables=["name_of_company"], template=template)
    twitter_username = agent.run(prompt_template.format_prompt(name_of_company=name))
    return twitter_username
    # description parameter is optional but recommended for the agent to know when to use the tool
