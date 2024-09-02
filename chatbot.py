# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:07:19 2024

@author: yash
"""

## load the Groq API key

import streamlit as st
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

api_key=os.getenv("NVIDIA_API_KEY")

search=DuckDuckGoSearchRun(name="Search")

llm = ChatNVIDIA(model="writer/palmyra-med-70b")

st.title("🔎 🖥️ 🧪 🧬 👩🏻‍💻 LangChain_NVIDIA_BIOINFORMATICS_CHATBOT")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

## Sidebar for settings
#st.sidebar.title("Settings")
#api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question):
    api_key=os.getenv("NVIDIA_API_KEY")
    api_key=api_key

    llm=ChatNVIDIA(model="writer/palmyra-med-70b")
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## Adjust response parameter


## MAin interface for user input


st.write("Goe ahead and ask any question")
user_input=st.text_input("You:")
if user_input:
    response=generate_response(user_input)
    st.write(response)

elif user_input:
    st.warning("Please enter the Groq aPi Key in the sider bar")
else:
    st.write("Please provide the user input")

