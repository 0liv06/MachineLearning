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

def exercise_to_json(exercise: Exercise):
    result = {}

    result['sets'] = exercise.sets
    result['name'] = exercise.name
    result['reps'] = exercise.reps
    result['weight'] = exercise.weights.weight
    result['weight_unit'] = exercise.weights.unit

    return result

def program_to_json(program: Program):
    result = {}

    result['day'] = program.day
    exercises = []
    for exercise in program.exercises:
        exercises.append(exercise_to_json(exercise))

    result['exercises'] = exercises

    return result

def workout_program_to_json(workout_program: WorkoutProgram):
    result = {}

    result['participants'] = workout_program.participants
    programs = []
    for program in workout_program.program:
        programs.append(program_to_json(program))
    result['program'] = programs
    return result

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
