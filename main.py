import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# This is the YouTube video we're going to use.


YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=cdiD-9MMpb0"

model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

# #model invoke test
# val = model.invoke("In financial markets, a call option gives the owner the right to purchase an asset such as shares of a common stock. Please eli5 this concept.")
# print(f'output from model: {val}')


#string parsing test
parser = StrOutputParser()

# chain = model | parser
# val = chain.invoke("What MLB team won the World Series during the COVID-19 pandemic?")

# print(f'output from parser: {val}')


from langchain.prompts import ChatPromptTemplate

template = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know".

Context: {context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
# prompt.format(context="Mary's sister is bose", question="Who is Mary's brother?")

chain = prompt | model | parser
# val = chain.invoke({
#     "context": "Mary's sister is bose",
#     "question": "Who is Mary's brother?"
# })

# print(f'chain invoke output: {val}')



translation_prompt = ChatPromptTemplate.from_template(
    "Translate {answer} to {language}"
)

from operator import itemgetter

translation_chain = (
    {"answer": chain, "language": itemgetter("language")} | translation_prompt | model | parser
)

val = translation_chain.invoke(
    {
        "context": "Mary's sister is Susana. She doesn't have any more siblings.",
        "question": "How many sisters does Mary have?",
        "language": "Bengali",
    }
)

print(f'tranlation output: {val}')

print("XXX...done...XXX")