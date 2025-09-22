from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI()

chat_template = ChatPromptTemplate(
    [
        ('system','You are a helpful {domain} expert.'),
        ('human','Explain in simple terms what is {topic}')
        #SystemMessage(content="You are helpful {domain} expert."),
        #HumanMessage(content="Explain in simple terms what is {topic}")
    ]
)

prompt = chat_template.invoke({'domain':'Cricket','topic':'Dusra'})

print(prompt)

result = model.invoke(prompt)
print(result.content)