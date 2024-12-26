# LangSmith
LangChain's stateful graph framework to engage in interactive, context-aware conversations with users.

## Setup Instructions

### 1. Clone the repository:


```bash
git clone https://github.com/subhash-adak/LangSmith.git


cd Chatbot


```

### Create a virtual environment
## If you don't have a virtual environment set up yet, create one using venv:
```
python -m venv .venv
```
## Activate the virtual environment:

Windows:

```
.\.venv\Scripts\activate
```
macOS/Linux:

```
source .venv/bin/activate
```

### Install dependencies:
## Install the necessary Python packages using the requirements.txt file:
```
pip install -r requirements.txt
```


### Configure the .env file:
## Create a .env file in the root directory of the project if .env is not cloned, and add the following API keys and Project name:
```
OPENAI_API_KEY="ENTER YOUR OPENAI API KEY"
GROQ_API_KEY="ENTER YOUR GROQ API KEY"
LANGCHAIN_API_KEY="ENTER YOUR LANGCHAIN API KEY"
LANGCHAIN_PROJECT="SET YOUR PROJECT NAME FOR TRACING"
```
# Replace "ENTER YOUR OPENAI API KEY", "ENTER YOUR GROQ API KEY", and "ENTER YOUR LANGCHAIN API KEY" with your actual API keys. The LANGCHAIN_PROJECT should be the name of the project for Langchain tracing.


### Run the chatbot:
```
python main.py
```
## Interact with the chatbot:
Once the chatbot is running, you will be prompted to enter user input. Type your message, and the chatbot will provide a response. To exit, type "exit", "quit", or "bye".



### For LangSmith Tracing:
Open the Langchain Platform:

Open your preferred browser and go to the Langchain platform URL where you manage your projects. This is typically available through the Langchain documentation or the official platform URL.
Log In:

Log in using the same credentials (email or account) that you used to obtain your LANGCHAIN_API_KEY.
If you're already logged in, this step may not be necessary.
Navigate to the Observability Section:

Once logged in, find the Observability section in the Langchain dashboard. This is where you can track the performance and other details of your Langchain projects.
Locate Your Project:

Under Observability, locate the name of your project. This should be the project associated with the LANGCHAIN_PROJECT value that you set in your .env file.
Click on your project's name to access detailed information related to it.
Track the Necessary Details:

After opening your project, you will be able to track various metrics, logs, and performance details related to the project.
This may include request/response times, tracing information, model performance, and more.
