# AI Agent
## Introduction
Agentic AI is a concept that while not new to the research field, has recently gained public visibility due to the explosion of AI.
In this project, I am exploring how to create AI Agents and how to integrate them in web applications that can be used by end users.
The goal of this project is to build a simple AI Agent capable of generate a Workout program for some participants. The program will
be generated by prompting a text field from a webapp and displaying the result to users via a web page. Once the basic feature is created,
I will enrich the Agent's capabilities by adding a feature allowing to integrate with calendars. I will then be exploring several prompts
and ways to interact with the agent to evaluate its performance. Finally, a discussion will be made about the rise of AI Agents, their
use by the public, what benefits do they offer and what risks could they cause.

## How to configure
First, get an OpenAI API key https://openai.com/index/openai-api/

Create a `.openai/api.key` file under your user's directory `~/` and write your API key inside

Then, install Flask https://flask.palletsprojects.com/en/stable/installation/

Finally, run `flask --app app.py run` from the project's directory

## Workflow
```mermaid
 flowchart LR
    A[In] --> B[Get Program]
    B --> C{Gate}
    C --> |Pass| D[Generate Calendar Invite]
    C --> |Pass| E[Get Diet]
    E --> F[Aggregator]
    D --> F[Aggregator]
    F --> G[Out]
    C --> H[Fail]
    F --> G{Out}
    
 ```
### Get Program
Step that generates a workout program from user input, keeping track of the user objective.

### Get Diet
If successfully generated, the objective from `Get Program` is reused to generate a food diet program to pair up with the workout.

### Generate Calendar Invite
Generates a calendar invite using the days the user specified.

## Technologies
Flask, OpenAI, pydantic

## TODO
- Work on better UI for program and prompt
- Do Calendar integration
- Add a framework ?Add