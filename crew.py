from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from task import research_task ,write_task

## Forming the crew
crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    map_rpm=100,
    share_crew=True
)

## Start the  task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI vs ML vs Data science'})
print(result)