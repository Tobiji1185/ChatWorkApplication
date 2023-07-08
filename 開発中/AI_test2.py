import openai

# OpenAI APIキーの設定
openai.api_key = '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'

def chat_with_gpt(prompt):
    # ChatGPTに対するリクエストの送信
    response = openai.Completion.create(
        engine='text-davinci-003',  # 使用するモデルのエンジンを指定します
        prompt=prompt,
        max_tokens=50,  # 応答の最大トークン数を指定します
        temperature=0.7,  # 応答の多様性を調整する温度パラメータを指定します
        n=1,  # 返される応答の数を指定します
        stop=None,  # 応答の停止条件を指定します（Noneの場合は自動的に応答が終了します）
    )

    # 応答の抽出
    if response.choices:
        return response.choices[0].text.strip()
    else:
        return ''

# ChatGPTをテストする例
prompt = "Windowsアプリの簡単な作り方は？"
response = chat_with_gpt(prompt)
print("AI: " + response)
