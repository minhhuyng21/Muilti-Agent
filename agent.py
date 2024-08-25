from crewai import Task, Agent, Crew, Process
from langchain_community.tools.tavily_search import TavilySearchResults
from textwrap import dedent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_groq import ChatGroq
import os
topic = input(dedent("""what topic you want"""))
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

llm = ChatGroq(temperature=0, model="llama3-8b-8192")
search = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
agent = Agent(
    role="Biological Expert",
    goal="Provide expert knowledge in biology, initiate scientific discussions, and synthesize findings",
    backstory="You are a seasoned biologist with 20 years of experience across various subfields including molecular biology, ecology, and genetics. Your expertise allows you to provide in-depth insights and propose innovative ideas in biological research.",
    verbose=True,
    tools=search,
    llm=llm,
)

research_task = Task(
    description=dedent(f"""
        Critically examine the findings presented by another Biologist on {topic}. Your task includes:
        1. Evaluate the strength of the evidence presented for each major point.
        2. Identify any potential biases or limitations in the research methodology.
        3. Suggest alternative interpretations of the data where applicable.
        4. Point out any gaps in the current understanding of the topic.
        5. Propose additional theories or hypotheses that weren't considered.
        6. Formulate at least three critical questions or challenges to the initial research.
        
        Provide a detailed analysis, backing your critiques with scientific reasoning and, where possible, contradictory evidence from other studies.
        """),
    expected_output="You are a seasoned biologist with 20 years of experience across various subfields including molecular biology, ecology, and genetics. Your expertise allows you to provide in-depth insights and propose innovative ideas in biological research.",
    agent=agent
)

research_crew = Crew(
    agents=[agent],
    tasks=[research_task],
    verbose=True,
    process=Process.sequential,  # Đảm bảo các task được thực hiện tuần tự
)

result = research_crew.kickoff()

r = search.invoke({"query":"what is dna",
               "include_ansewr": False})
print(r)