from langchain_openai import ChatOpenAI
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

st.header("Research Tool")

user_input = st.text_input("Enter your prompt") #this is static prompt

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
    
    
    
