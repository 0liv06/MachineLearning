import os
import logging

from openai import OpenAI
from model import WorkoutProgram, workout_program_to_json

openapi_key = ''
with open(os.path.expanduser('~') + '/.openai/api.key') as f:
    openapi_key = f.read().rstrip('\n')
    f.close()

client = OpenAI(api_key=openapi_key)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

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
    return workout_program_to_json(completion.choices[0].message.parsed)

def process_program_request(user_input: str):
    pass