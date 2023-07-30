import tkinter as tk
import openai
import re
from tkinter import messagebox
import listing_def

openai.api_key = ''

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )

    if response.choices:
        return response.choices[0].text.strip()
    else:
        return ''

def send_message():
    message = input_text.get("1.0", tk.END).strip() #ここを選択肢に変えればよい
    
    if message:
        list_text = chat_with_gpt(message+"の回答を3個リスト化してください")
        choices = listing_def.get_choices_from_text(list_text) 
        listing_def.list_response(choices, str(var),)
        print(choices[0])
        
        choice1 = tk.Radiobutton(window, text=choices[0], variable=var, value=1)
        choice1.pack()
        choice2 = tk.Radiobutton(window, text=choices[1], variable=var, value=2)
        choice2.pack()
        choice3 = tk.Radiobutton(window, text=choices[2], variable=var, value=3)
        choice3.pack()
        
        button = tk.Button(window, text="選択", command=show_selected_choice())
        button.pack()
    
    if message:
        response = chat_with_gpt(message)
        full_response = message + response
       # if full_response = re.match(fu)
        display_message("You: " + message)
        display_message("AI: " + full_response)
        input_text.delete("1.0", tk.END)
        
def show_selected_choice():
    selected_choice = var.get()
    if selected_choice == 1:
        messagebox.showinfo("選択", "選択肢1が選ばれました！")
    elif selected_choice == 2:
        messagebox.showinfo("選択", "選択肢2が選ばれました！")
    elif selected_choice == 3:
        messagebox.showinfo("選択", "選択肢3が選ばれました！")
        
def display_message(message):
    chat_history.insert(tk.END, message + "\n")
    chat_history.see(tk.END)

# GUIの作成
window = tk.Tk()
window.title("Chat with GPT")
window.geometry("500x1000")

# チャット履歴を表示するテキストボックス
chat_history = tk.Text(window)
chat_history.pack(fill=tk.BOTH, expand=True)

# メッセージの入力を行うテキストボックス
input_text = tk.Text(window, height=3)
input_text.pack(fill=tk.BOTH)

# 送信ボタン
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

'''選択肢アプリを合体'''

var = tk.IntVar()

label = tk.Label(window, text="以下の選択肢から選んでください:")
label.pack()


"""
choice1 = tk.Radiobutton(window, text=choices[0], variable=var, value=1)
choice1.pack()

choice2 = tk.Radiobutton(window, text="選択肢2", variable=var, value=2)
choice2.pack()

choice3 = tk.Radiobutton(window, text="選択肢3", variable=var, value=3)
choice3.pack()


button = tk.Button(window, text="選択", command=show_selected_choice())
button.pack()
"""

# メインループの開始
window.mainloop()

