import os, requests
from dotenv import load_dotenv

load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

TEXT_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
HF_TEXT_URL = f"https://api-inference.huggingface.co/models/{TEXT_MODEL}"

IMAGE_MODEL = "stabilityai/sd-turbo"
HF_IMG_URL = f"https://api-inference.huggingface.co/models/{IMAGE_MODEL}"

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def generate_text(prompt:str):
    response = requests.post(
        HF_TEXT_URL,
        headers=headers,
        json = {"inputs" : prompt, "parameters" : {"max_tokens":150, "temperature":0.9}},
    )
    return response.json[0]["generated_text"]
        
def generate_image(prompt:str):
    response = requests.post(
        HF_IMG_URL,
        headers=headers,
        json = {"inputs" : prompt}
    )
