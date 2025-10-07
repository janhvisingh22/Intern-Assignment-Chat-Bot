AI Question & Answering Bot
A simple web application built for an internship assignment to demonstrate effort, resourcefulness, and the ability to build a small AI-powered tool. This app uses the Hugging Face Inference API to answer questions based on a user-provided context.

Features
Interactive UI: A clean and simple user interface built with Streamlit.

AI-Powered Q&A: Leverages the deepset/roberta-base-squad2 model from the Hugging Face Hub to perform extractive question-answering.

Secure API Key Handling: Manages the Hugging Face API token securely using environment variables and a .env file, which is kept private via .gitignore.

Tech Stack
Language: Python 3

Framework: Streamlit

API: Hugging Face Inference API

Libraries: requests, python-dotenv

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Python 3.8 or newer

Git

Installation & Setup
Clone the repository:

Bash

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
Create a requirements.txt file:
This file lists all the Python libraries needed for the project. Create a file named requirements.txt and paste the following into it:

streamlit
requests
python-dotenv
Install the dependencies:

Bash

pip install -r requirements.txt
Configuration
This project requires a Hugging Face API Token to function.

Create a file named .env in the root of the project directory.

Add your API token to the .env file as shown below:

API_TOKEN="hf_YOUR_REAL_API_KEY_HERE"
You can get your token from your Hugging Face profile settings.

Running the Application
Once the installation and configuration are complete, run the following command to start the Streamlit server:

Bash

streamlit run ui.py
Or, the more robust method:

Bash

python -m streamlit run ui.py
The application should automatically open in your web browser at http://localhost:8501.

📝 My Development Journey & Learnings
This section documents my journey in building this application as part of my internship assignment.

Project Choice
I chose the AI Q&A Bot project because I was excited by the idea of interacting with a real AI model through an API. It felt like a great opportunity to learn about how modern AI applications are built and connected.

Challenges Faced
Initial Setup Error: When I first tried to run Streamlit, I encountered a Fatal error in launcher. After some research, I learned that this was likely due to a misconfigured Python path. I solved it by using the python -m streamlit run ui.py command, which is a more direct and reliable way to execute the module.

API Key Security: I initially hardcoded my API key directly in the Python script. I quickly realized this was a major security risk, especially for a public GitHub repository. This led me to research best practices, and I learned how to use .env files and .gitignore to keep my secrets safe. This was a huge learning moment for me.

Key Learnings
API Integration: I learned the fundamental workflow of making API requests in Python using the requests library, including how to pass headers for authorization.

Virtual Environments: I learned the importance of using virtual environments to manage project dependencies and avoid conflicts.

Streamlit for Rapid Prototyping: I was amazed at how quickly I could build an interactive web UI with Streamlit. It's a powerful tool for data science and AI projects.

The Importance of Documentation: This assignment taught me that documenting your process, including failures and solutions, is just as important as writing the code itself. This README is a testament to that learning.
