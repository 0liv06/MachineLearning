import os
import sys
import logging

from openai import OpenAI

sys.path.append(os.getcwd())
from model import WorkoutProgram, Diet, AggregatedWorkoutDiet, WorkoutProgramExtraction
from converter import aggregate_workout_to_json

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

    completion = client.beta.chat.completions.parse(
        model='gpt-4o-mini',
        messages=[
            {
                "role": "system",
                "content": f" Analyze if the text describes a workout program for the participants and a clear objective.",
            },
            {"role": "user", "content": user_input},
        ],
        response_format=WorkoutProgramExtraction,
    )
    result = completion.choices[0].message.parsed
    logger.info(
        f"Extraction complete - Is calendar event: {result.is_workout_program}, Confidence: {result.confidence_score:.2f}"
    )

    return not result.is_workout_program or result.confidence_score < 0.7

def generate_diet(program: WorkoutProgram) -> Diet:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Generate a diet plan to achieve the objective"},
            {
                "role": "user",
                "content": f'The workout program objective is {program.objective}',
            },
        ],
        response_format=Diet,
    )
    return completion.choices[0].message.parsed

def generate_program(user_input: str) -> dict:
    # See if program is parsable
    if validate_program_prompt(user_input):
        logger.error(f'Gate check failed, could not generate workout program from [{user_input}]')
        raise Exception('Could not generate program...')

    # Generate program
    logger.info('Successfully passed gate check, generating workout program !')
    workout_program = get_program(user_input)

    # Generate Diet and Calendar
    return aggregate_workout_to_json(AggregatedWorkoutDiet(workout_program, generate_diet(workout_program)))