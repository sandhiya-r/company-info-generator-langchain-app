from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import requests
import os
from agents.linkedin_lookup_agent import lookup
from output_parsers import *
import streamlit as st

os.environ['OPENAI_API_KEY']='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'


summary_template = """/
Given the LinkedIn information {linkedin_information} and Twitter information {twitter_information} you find about a company I want you to create:
1. A short summary about the company
2. 3 Skills that an individual would need to get a job at this company
\n{format_info}
"""

def scrape_linkedin(linkedin_company_url:str):
    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company'

    header_dic = {'Authorization': f'Bearer {"aPCEyxvZC8kwr4di0I_Yjw"}'}
    response = requests.get(api_endpoint,
                            params = {'url': linkedin_company_url},
                            headers=header_dic)
    data = response.json()
    data = { #clean the data to help with token limit
        k: v
        for k,v in data.items()
        if v not in ([], "", "", None) and k in ("description")

    }
    return data


def learn_about_company(name:str)->CompanyIntel:
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')  # this is a wrapper for the LLM, but its a chat model

    linkedin_company_url = lookup(name=name)
    linkedin_info = scrape_linkedin(linkedin_company_url)

    # twitter_company_name = twitter_lookup(name='Accenture')
    # twitter_info = scrape_tweets(twitter_company_name,5) #scrape for 5 tweets only to avoid token limitation

    prompt = PromptTemplate(
        input_variables=["linkedin_information"], template=summary_template, partial_variables={'format_info':parser.get_format_instructions()}

    )

    chain = LLMChain(llm=llm, prompt=prompt)  # first arg is a chat model which has the LLM model inside it

    return chain.run(linkedin_information=linkedin_info) # output of the chain


