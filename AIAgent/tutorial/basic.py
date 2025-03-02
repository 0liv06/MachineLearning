from openai import OpenAI
import os

print()

openapi_key = ''
with open(os.path.expanduser('~') + '/.openai/api.key') as f:
    openapi_key = f.read().rstrip('\n')
    f.close()

client = OpenAI(api_key=openapi_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)