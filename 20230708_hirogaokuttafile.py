import tkinter as tk
import openai

openai.api_key = ''

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )

    if response.choices:
        return response.choices[0].text.strip()
    else:
        return ''

def send_message():
    message = input_text.get("1.0", tk.END).strip()
    if message:
        response = chat_with_gpt(message)
        full_response = message + response
        display_message("You: " + message)
        display_message("AI: " + full_response)
        input_text.delete("1.0", tk.END)


def display_message(message):
    chat_history.insert(tk.END, message + "\n")
    chat_history.see(tk.END)

# GUIの作成
window = tk.Tk()
window.title("Chat with GPT")
window.geometry("400x500")

# チャット履歴を表示するテキストボックス
chat_history = tk.Text(window)
chat_history.pack(fill=tk.BOTH, expand=True)

# メッセージの入力を行うテキストボックス
input_text = tk.Text(window, height=3)
input_text.pack(fill=tk.BOTH)

# 送信ボタン
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# メインループの開始
window.mainloop()

