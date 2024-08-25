from crewai import Task
from textwrap import dedent
class BioTask():
    def research_task(self,agent,topic):
        return Task(
            description=dedent(f"""
                Research the topic: {topic}. Provide detailed information based on your area of expertise.
            """),
            expected_output="A comprehensive report detailing your findings, including key insights, data, and relevant conclusions specific to your perspective.",
            agent=agent,
        )
    def synthesis_task(self,agent, topic):
        return Task(
            description=f"Synthesize the findings from both perspectives on the topic: {topic}. Provide a well-rounded and accurate conclusion.",
            expected_output="A synthesized report that combines the key points from both perspectives, offering a balanced and comprehensive understanding of the topic.",
            agent=agent
        )
    

    def initial_research_task(self,agent1,topic):
        return Task(
            description=dedent(f"""
                Debate the pros of the following topic: {topic}
            """),
            expected_output="A comprehensive research report on the specified biology topic, including current knowledge, recent discoveries, major theories, controversies, and areas for future research.",
            agent=agent1
    )
    def critical_analysis_task(self,agent2,topic):
        return Task(
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
        expected_output="A critical analysis report that evaluates the initial research, identifies potential biases or limitations, suggests alternative interpretations, and proposes additional theories or hypotheses.",
        agent=agent2
    )
    def debate(self,agent1):
        return Task(
        description=dedent("""
        Engage in a structured scientific debate based on the initial research and critical analysis. Your task includes:
        1. Address each of the key points and questions raised in the previous tasks.
        2. Present arguments and counter-arguments for major theories or hypotheses.
        3. Discuss the implications of recent discoveries and how they shape our understanding.
        4. Explore potential resolutions to any controversies identified.
        5. Collaborate to identify the most promising areas for future research.
        6. Work towards a consensus on the current state of knowledge, noting any points of continued disagreement.
        7. Synthesize the debate into a comprehensive summary of the topic, including:
        - Key agreed-upon facts
        - Major theories and their supporting evidence
        - Unresolved questions and controversies
        - Recommendations for future studies
        
        Conduct this debate in a respectful, scientific manner, focusing on evidence-based arguments and logical reasoning. The goal is to reach the most accurate and comprehensive understanding of [specific biology topic] possible.
        """),
        expected_output="A comprehensive debate summary that addresses key points, presents arguments and counter-arguments, discusses implications, explores resolutions to controversies, and provides a synthesis of the current state of knowledge on the topic.",
        agent=agent1  # Both will participate, but one needs to be assigned for CrewAI
)
    