from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
import os
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

llm = ChatGroq(temperature=0, model="llama3-8b-8192")
search = TavilySearchResults()

class BioAgent():
    def agent1(self):
        return Agent(
            role="Biological Expert - Perspective 1",
            goal="Research and present findings on the biological topic with a focus on one perspective.",
            backstory="An expert biologist with a deep understanding of biological systems, focusing on the molecular mechanisms.",    
            verbose=True,
            # tools=[search],
            llm=llm,
        )
    def agent2(self):
        return Agent(
            role="Biological Expert - Perspective 2",
            goal="Research and present findings on the same biological topic but from another perspective.",
            backstory="An experienced biologist specializing in ecological and evolutionary aspects of biological systems.",
            # backstory="An expert in biology, specializing in critical analysis and finding potential weaknesses in biological theories.",
            verbose=True,
            # tools=[search],
            llm=llm,
        )
    def synthesizer_agent(self):
        return Agent(
            role="Biological Expert - Synthesizer",
            goal="Combine the findings from both perspectives to produce a comprehensive and balanced outcome.",
            backstory="An expert in synthesizing information from multiple biological fields to provide a holistic view.", 
            llm=llm,
            verbose=True,
        )

if __name__ == '__main__':
    agents = BioAgent()
    agent1 = agents.agent1()