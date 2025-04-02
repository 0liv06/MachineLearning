from pydantic import BaseModel, Field

# Workout model
class Weight(BaseModel):
    weight: int
    unit: str

class Exercise(BaseModel):
    sets: int = Field(description='Number of sets to do for the exercise')
    name: str = Field(description='Name of the exercise')
    reps: int = Field(description='Number of repetitions to do for the exercise')
    weights: Weight = Field(description='Weight in kg to carry to perform the exercise')

class Program(BaseModel):
    day: str = Field(description='The day the exercise list will be executed')
    exercises: list[Exercise] = Field(description='The list of workout exercise to be performed on the day of the workout')

class WorkoutProgram(BaseModel):
    participants: list[str] = Field(description='The workout participants')
    program: list[Program] = Field(description='The program to be executed by the participants')
    objective: str = Field(description='The objective of the participants')

# Diet model
class Recipe(BaseModel):
    ingredients: list[str] = Field(description='Ingredients of the recipe')
    steps: list[str] = Field(description='Steps to cook the recipe')

class DailyDiet(BaseModel):
    breakfast: Recipe = Field(description='Recipe to eat at breakfast')
    lunch: Recipe = Field(description='Recipe to eat at lunch time')
    dinner: Recipe = Field(description='Recipe to eat for dinner')

class Diet(BaseModel):
    week: list[DailyDiet] = Field(description='List of daily meals to prepare to optimise the workout effects')

# Aggregated model
class AggregatedWorkoutDiet:
    workout: WorkoutProgram
    diet: Diet

    def __init__(self, workout: WorkoutProgram, diet: Diet):
        self.workout = workout
        self.diet = diet

# Gate model
class WorkoutProgramExtraction(BaseModel):
    description: str = Field(description='Raw description of the workout program with the participants objective')
    is_workout_program: bool = Field(description='Whether description describes a workout program with an objective')
    confidence_score: float = Field(description='Confidence score between 1 and 0')

