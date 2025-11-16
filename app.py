import os
from groq import Groq
import gradio as gr
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=API_KEY)

# Chatbot function
def chatbot(message):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
ui = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=2, label="Your Message"),
    outputs=gr.Textbox(lines=2, label="Groq Response"),
    title="Groq Chatbot",
    description="A simple chatbot powered by Groq API"
)

if __name__ == "__main__":
    ui.launch()
