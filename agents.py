from crewai import Agent
from tools.yt_tool import youtube_channel_search 


yt_tool = youtube_channel_search.as_tool() 

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
llm=ChatGroq(api_key=api_key,model_name="mixtral-8x7b-32768")

## Creating a senior bolg researchher
blog_researcher=Agent(
    role='Blog researcher from Youtube Videos',
    goal='get the relevant video content for the topic{topic} from YT channel',
    name='Senior Blog Content researcher',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understading video in AI, Data Scienc,Machine learning and Gen ai" 
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

## Creating a senior blog writer agent witj YT tool
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compleeing tech stories about the video {topic} from yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplifying complex topics,you craft" 
        "engaging narratives that captivate and educate , bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)