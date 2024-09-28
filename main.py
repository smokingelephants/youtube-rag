import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print(os.environ.get("OPEN_AI_KEY"))

# This is the YouTube video we're going to use.
YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=cdiD-9MMpb0"

print("hello world")

from langchain_openai.chat_models import ChatOpenAI

model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")



model.invoke("What MLB team won the World Series during the COVID-19 pandemic?")








print("XXX...done...XXX")