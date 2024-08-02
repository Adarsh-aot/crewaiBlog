from crewai import Agent, Task, Crew
from agent import planner, writer, editor
from task import plan, write, edit

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})

print(result)