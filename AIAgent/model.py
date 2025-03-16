from pydantic import BaseModel

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