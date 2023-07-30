import tkinter as tk
import json
import random

file_path = 'C:/Users/takah/00_開発環境/Github/ChatWorkApplocation/choices.txt'

def read_choices_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        choices = [line.strip() for line in file.readlines()]
    return choices

def save_response():
    selected_choice = var.get()
    selected_text = random_choices[selected_choice - 1]  # 選択された選択肢のテキストを取得

    response_data = {
        "question": "こんにちは",
        "answer": selected_text
    }

    with open("responses.json", "w", encoding="utf-8") as json_file:
        json.dump(response_data, json_file, ensure_ascii=False, indent=4)
        
def list_response():
    selected_choice = var.get()
    list_text = random_choices[selected_choice -1] #選択されて選択肢のテキストを取得
    response_list = {
        "question": "こんにちは",
        "list化": list_text
    }   

    with open("responses_list.json", "w", encoding="utf-8") as json_file:
        json.dump(response_list, json_file, ensure_ascii=False, indent=4)

app = tk.Tk()
app.title("回答を保存するアプリ")

font = ("Yu Gothic", 12)
app.option_add("*Font", font)

choices = read_choices_from_file("choices.txt")
var = tk.IntVar()

label = tk.Label(app, text="こんにちはに対する回答を選んでください:")
label.pack()

random_choices = random.sample(choices, 3)
for i, choice in enumerate(random_choices, 1):
    tk.Radiobutton(app, text=choice, variable=var, value=i).pack()

button = tk.Button(app, text="回答を保存", command=save_response)
button.pack()

app.mainloop()
