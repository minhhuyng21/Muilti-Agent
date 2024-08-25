from CrewAI.BioAgent import BioAgent
from CrewAI.Task import BioTask
from crewai import Crew, Process
from textwrap import dedent, fill

class BioCrew:
    def __init__(self,topic):
        self.topic = topic
    def run(self):
        agents = BioAgent()
        tasks = BioTask()
         
        agent1 = agents.agent1()
        agent2 = agents.agent2()
        agent_syn = agents.synthesizer_agent()
        task1 = tasks.research_task(agent1,self.topic)
        task2 = tasks.research_task(agent2,self.topic)
        synthesis_task = tasks.synthesis_task(agent_syn,self.topic)
        crew = Crew(
            agents=[agent1,agent2,agent_syn],
            tasks=[task1,task2,synthesis_task],
            verbose=True,
            process=Process.sequential
        )
        result = crew.kickoff()
        return result

if __name__ == '__main__':
    print("welcome to multi agent system")
    topic = input(dedent("""
        Which biology knowledge you want to know
    """))
    bio_crew = BioCrew(topic=topic)
    results = bio_crew.run()
    print(results)

