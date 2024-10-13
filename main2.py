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

template_org = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know".

Context: {context1}

Question: {question1}
"""

template = """
group the context sentence based on the best json format for question below. 

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

#translation full pipeline
val = translation_chain.invoke(
    {
        "context1": "Mary's sister is Susana. She doesn't have any more siblings.",
        "question1": "How many sisters does Mary have?",
        "language1": "English",
    }
)

# QA pipeline
val2 = chain.invoke(
    {
        "context1": "Mary's sister is Susana. She doesn't have any more siblings.",
        "question1": "How many sisters does Mary have?",
    }
)

print(f'tranlation output: {val}')


# Download and extract transcript 

# YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=cdiD-9MMpb0"

# import tempfile
# import whisper
# from pytube import YouTube


# # Let's do this only if we haven't created the transcription file yet.
# if not os.path.exists("transcription.txt"):
#     youtube = YouTube(YOUTUBE_VIDEO)
#     audio = youtube.streams.filter(only_audio=True).first()

#     # Let's load the base model. This is not the most accurate
#     # model but it's fast.
#     whisper_model = whisper.load_model("base")

#     with tempfile.TemporaryDirectory() as tmpdir:
#         file = audio.download(output_path=tmpdir)
#         transcription = whisper_model.transcribe(file, fp16=False)["text"].strip()

#         with open("transcription.txt", "w") as file:
#             file.write(transcription)


from langchain_openai.embeddings import OpenAIEmbeddings

with open("transcription_org.txt") as file:
    transcription = file.read()

transcription[:100]



embeddings = OpenAIEmbeddings()
embedded_query = embeddings.embed_query("Who is Mary's sister?")

print(f"Embedding length: {len(embedded_query)}")
print(embedded_query[:10])



print("done")