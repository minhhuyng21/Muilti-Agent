import os
from autogen import AssistantAgent,ConversableAgent, UserProxyAgent, GroupChat, GroupChatManager
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
# query = input("input: ")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY
config_list = [{
        "model": "llama3-8b-8192",  # Groq's Mixtral model
        "api_key": GROQ_API_KEY,
        "api_type": "groq",
    }]
llm_config = {
    "config_list": config_list,
    "cache_seed": 42  # Optional: for reproducibility
}

agent1 = ConversableAgent(
    name="BiologicalExpertJason",
    system_message="You are a Biological Expert specializing in molecular biology. Contribute your expertise to the discussion, but allow others to speak as well. Don't provide a full answer alone.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

agent2 = ConversableAgent(
    name="BiologicalExpertElon",
    system_message="You are a Biological Expert specializing in ecology. Contribute your expertise to the discussion, focusing on ecological aspects. Engage with other experts' points.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)
student = ConversableAgent(
    name="Student",
    system_message="You are a curious student. Ask follow-up questions to the experts to gain a deeper understanding of the topic.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

moderator = ConversableAgent(
    name="Moderator",
    system_message="You are a moderator. Ensure all experts contribute to the discussion. Summarize key points and guide the conversation towards a consensus.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)


# user_proxy = UserProxyAgent(
#     name="User",
#     llm_config=False,
#     human_input_mode="NEVER",
#     # max_consecutive_auto_reply=1,
#     code_execution_config=False,
#     is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
# )

def expert_debate(user_message):
    # Create a group chat
    groupchat = GroupChat(
        agents=[agent1, agent2, student, moderator],
        messages=[],
        max_round=4
    )
    
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # Initiate the group chat
    student.initiate_chat(
        manager,
        message=f"Experts, please discuss this biology question: {user_message}\nModerator, please ensure all experts contribute and guide the discussion towards a consensus. When a consensus is reached, clearly state 'FINAL ANSWER:' followed by the consensus."
    )

    # Print the chat history
    print("\nChat History:")
    final_answer = None
    for msg in student.chat_messages[manager]:
        sender = msg.get('name', msg.get('role', 'Unknown'))
        content = msg['content']
        print(f"{sender}: {content}\n")
        
        # Check for final answer
        if "FINAL ANSWER:" in content:
            final_answer = content.split("FINAL ANSWER:")[-1].strip()

    # Print the final answer
    if final_answer:
        print("\nFinal Answer:")
        print(final_answer)
    else:
        print("\nNo clear final answer was provided.")

    return final_answer

while True:
    user_message = input("What do you want to ask? (type 'exit' to end): ")
    if user_message.lower() == 'exit':
        break
    
    expert_debate(user_message)
    print("\n---")

print("Chat ended. Goodbye!")
