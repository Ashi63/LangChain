from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()

# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

#load chat history

chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    
print("Chat History:",chat_history)
    
# create prompt
prompt = chat_template.invoke({'chat_history':chat_history,'query':'where is my refund'})
print("Prompt:",prompt)

result = model.invoke(prompt)
print("Result: ",AIMessage(content=result.content))

