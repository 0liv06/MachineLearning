from model import WorkoutProgram, Exercise, Program, Recipe, DailyDiet, Diet, AggregatedWorkoutDiet

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

def recipe_to_json(recipe: Recipe) -> dict:
    return {
        'ingredients': recipe.ingredients,
        'steps': recipe.steps
    }

def dailydiet_to_json(daily_diet: DailyDiet) -> dict:
    result = {}

    result['breakfast'] = recipe_to_json(daily_diet.breakfast)
    result['lunch'] = recipe_to_json(daily_diet.lunch)
    result['dinner'] = recipe_to_json(daily_diet.dinner)

    return result

def diet_to_json(diet: Diet) -> dict:
    diet_list = []
    for daily_diet in diet.week:
        diet_list.append(dailydiet_to_json(daily_diet))

    return  { 'week' : diet_list }

def aggregate_workout_to_json(aggregate_wkout: AggregatedWorkoutDiet) -> dict:
    return {
        'workout': workout_program_to_json(aggregate_wkout.workout),
        'diet': diet_to_json(aggregate_wkout.diet)
    }