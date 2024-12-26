# Import necessary libraries
from langchain_openai import ChatOpenAI  # OpenAI LLM
# from langchain_groq import ChatGroq  # Optional: Uncomment if using Groq LLM
from typing import Annotated  # For type annotations
from typing_extensions import TypedDict  # Extend built-in typing for flexibility
from langgraph.graph import StateGraph, START, END  # For graph-based logic
from langgraph.graph.message import add_messages  # Message processing
from dotenv import load_dotenv  # For loading environment variables
import os  # For OS-level operations

# Load environment variables from a .env file
load_dotenv()

# Get API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
# groq_api_key = os.getenv("GROQ_API_KEY")      # Optional: Uncomment if using Groq LLM
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# Set API keys as environment variables
os.environ["OPENAI_API_KEY"] = openai_api_key
# os.environ["GROQ_API_KEY"] = groq_api_key       # Optional: Uncomment if using Groq LLM
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"  # Enable tracing for Langchain
os.environ["LANGCHAIN_PROJECT"] = "LangSmithTracing"  # Set project name

# Initialize the OpenAI model (uncomment ChatGroq initialization if needed)
llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    model_name="gpt-3.5-turbo",     # Model name for OpenAI
    verbose=True,
    temperature=0.7
)

# Optional: Initialize the Groq model
# llm = ChatGroq(
#     groq_api_key=groq_api_key,
#     model_name="llama3-8b-8192",      # Model name for Groq
#     verbose=True,
#     temperature=0.7 
# )

# Define a State class to structure the graph's state
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Create a state-based graph builder
graph_builder = StateGraph(State)

# Define the chatbot function for graph processing
def chatbot(state: State):
    """
    Process the user input through the LLM and return responses.
    """
    return {"messages": llm.invoke(state['messages'])}

# Add a chatbot node to the graph
graph_builder.add_node("chatbot", chatbot)

# Define graph edges for start and end points
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile the graph
graph = graph_builder.compile()

# Save the graph as a PNG file
try:
    # Generate the graph as a Mermaid PNG and save it
    with open("graph_image.png", "wb") as f:
        f.write(graph.get_graph().draw_mermaid_png())  # Ensure this method exists
    print("Graph saved successfully as 'graph_image.png'. Open the file to view the graph.")
except Exception as e:
    print(f"An error occurred while saving the graph: {e}")

# Interactive chatbot loop
while True:
    user_input = input("\n\nUser : ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("I hope to see you again,😊 Goodbye...")
        break  # Exit the loop
    # Process user input through the graph
    for event in graph.stream({'messages': ("user", user_input)}):
        print("\n\n", event.values())  # Debugging output for events
        for value in event.values():
            print("\n\n", value['messages'])  # Debugging output for messages
            print("\n\n\nResponse :", value["messages"].content)  # Display response
