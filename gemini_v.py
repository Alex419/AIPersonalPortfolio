import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available Gemini models that support 'generateContent':")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name} (Description: {m.description})")

print("\nAvailable Gemini models that support 'embedContent':")
for m in genai.list_models():
    if 'embedContent' in m.supported_generation_methods:
        print(f"- {m.name} (Description: {m.description})")