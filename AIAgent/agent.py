import os
import logging

from openai import OpenAI

from AIAgent.model import AggregatedWorkoutDiet
from model import WorkoutProgram, Diet, AggregatedWorkoutDiet

openaiapi_key_path = os.path.expanduser('~') + '/.openai/api.key'

with open(openaiapi_key_path) as f:
    openapi_key = f.read().rstrip('\n')
    f.close()

if not openapi_key:
    raise Exception(f'Could not get OpenAI API key, generate a key and place it in [{openaiapi_key_path}]')

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
    return completion.choices[0].message.parsed

def validate_program_prompt(user_input: str) -> bool:
    return False

def generate_diet(program: WorkoutProgram) -> Diet:
    pass

def generate_calendar_invite(program: WorkoutProgram):
    pass

def generate_program(user_input: str) -> AggregatedWorkoutDiet:
    # See if program is parsable
    if validate_program_prompt(user_input):
        logger.error(f'Gate check failed, could not generate workout program from [{user_input}]')
        raise Exception('Could not generate program...')

    # Generate program
    logger.info('Successfully passed gate check, generating workout program !')
    workout_program = get_program(user_input)

    # Generate Diet and Calendar
    return AggregatedWorkoutDiet(generate_diet(workout_program), generate_calendar_invite(workout_program))