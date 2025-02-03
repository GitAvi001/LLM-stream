from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic  import BaseModel
import os


os.environ["OPENAI_API_KEY"]="<API_KEY>"

client = OpenAI()

app=FastAPI()

#Pydantic is a Python library for data validation and settings management using Python-type annotations
class TranslationRequest(BaseModel): 
    input_str: str

def translate_text(input_str: str):
    completion = client.chat.completions.create(
        model="gpt-4.0-mini",
        messages = [
            {

                "role":"system",
                "content":"You are a great assistant for text generation."
            },
            {
                "role":"user",
                "content":input_str
            }
        ]
    )
    return completion.choices[0].message.content #Returning the generated content text by LLM(OpenAI)


@app.post("/translate/")

async def translate(request: TranslationRequest):
    try:
        return {"output": translate_text(request.input_str)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))