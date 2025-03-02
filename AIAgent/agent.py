from openai import OpenAI
from pydantic import BaseModel
import os

openapi_key = ''
with open(os.path.expanduser('~') + '/.openai/api.key') as f:
    openapi_key = f.read().rstrip('\n')
    f.close()

client = OpenAI(api_key=openapi_key)

class Weight(BaseModel):
    weight: int
    unit: str

class Exercise(BaseModel):
    sets: int
    name: str
    reps: int
    weights: Weight

class Program(BaseModel):
    day: str
    exercises: list[Exercise]

class WorkoutProgram(BaseModel):
    participants: list[str]
    program: list[Program]

def get_program(prompt: str):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Generate the workout program for the participants."},
            {
                "role": "user",
                "content": prompt,
            },
        ],
        response_format=WorkoutProgram,
    )
    return completion.choices[0].message.parsed
