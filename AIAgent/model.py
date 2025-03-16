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
