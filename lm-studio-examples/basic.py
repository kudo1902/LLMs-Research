import time
from openai import OpenAI

client = OpenAI(
#   base_url="http://localhost:1234/v1",
  base_url="http://127.0.0.1:1234/v1",
  api_key="something-doesnt-matter",
)

start = time.perf_counter()
response = client.chat.completions.create(
  model="gemma-4-e4b",
  messages=[
    {
      "role": "system",
      "content": "You are a helpful and friendly assistant."
    },
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ],
  temperature=0.7,
)
end = time.perf_counter()

print(response.choices[0].message.content)
print(f"Execution time: {end - start:.3f} seconds")
