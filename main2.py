import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from operator import itemgetter

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

parser = StrOutputParser()

template = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know".

Context: {context1}

Question: {question1}
"""

QA_prompt = ChatPromptTemplate.from_template(template)

chain = QA_prompt | model | parser

translation_prompt = ChatPromptTemplate.from_template(
    "Translate {answer} to {language1}"
)

translation_chain = (
    {"answer": chain, "language1": itemgetter("language1")} | translation_prompt | model | parser
)

val = translation_chain.invoke(
    {
        "context1": "Mary's sister is Susana. She doesn't have any more siblings.",
        "question1": "How many sisters does Mary have?",
        "language1": "Bengali",
    }
)

print(f'tranlation output: {val}')

print("XXX...done...XXX")