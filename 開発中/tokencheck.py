import openai

openai.api_key = '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'
response = openai.Completion.create(model="text-davinci-003", prompt="Hello, world!", max_tokens=10)

usage = response['usage']['total_tokens']
print("使用トークン数:", usage)

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

methods = dir(openai)
for method in methods:
    print(method)
