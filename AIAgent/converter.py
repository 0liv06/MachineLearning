from model import WorkoutProgram, Exercise, Program

def exercise_to_json(exercise: Exercise):
    return {'sets': exercise.sets,
            'name': exercise.name,
            'reps': exercise.reps,
            'weight': exercise.weights.weight,
            'weight_unit': exercise.weights.unit
            }

def program_to_json(program: Program):
    result = {'day': program.day}
    exercises = []
    for exercise in program.exercises:
        exercises.append(exercise_to_json(exercise))

    result['exercises'] = exercises

    return result

def workout_program_to_json(workout_program: WorkoutProgram):
    result = {'participants': workout_program.participants}
    programs = []
    for program in workout_program.program:
        programs.append(program_to_json(program))
    result['program'] = programs
    return result