from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer


## Reaserch task
research_task=Task(
    description=(
        "Identify the video {topic}"
        "Get detailed information about the video from the channel"
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the topic {topic} of video content',
    tools=[yt_tool],
    agent=blog_researcher 
)


## write task
write_task=Task(
    description=("get the info from the youtube channel on the topic {topic}"
    ),
    expected_outputs = 'summarize the info from the yt channerl video on the topic {topic} and generate create the content for the blog',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'

)