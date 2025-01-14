import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_mentorship_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use "gpt-3.5-turbo" for chat or "gpt-4" if available
        prompt=f"You are a helpful mentor. {prompt}",
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
