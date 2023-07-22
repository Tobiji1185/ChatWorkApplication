import tkinter as tk
from tkinter import messagebox

def show_selected_choice():
    selected_choice = var.get()
    if selected_choice == 1:
        messagebox.showinfo("選択", "選択肢1が選ばれました！")
    elif selected_choice == 2:
        messagebox.showinfo("選択", "選択肢2が選ばれました！")
    elif selected_choice == 3:
        messagebox.showinfo("選択", "選択肢3が選ばれました！")

app = tk.Tk()
app.title("選択肢を選ぶアプリ")

var = tk.IntVar()

label = tk.Label(app, text="以下の選択肢から選んでください:")
label.pack()

choice1 = tk.Radiobutton(app, text="選択肢1", variable=var, value=1)
choice1.pack()

choice2 = tk.Radiobutton(app, text="選択肢2", variable=var, value=2)
choice2.pack()

choice3 = tk.Radiobutton(app, text="選択肢3", variable=var, value=3)
choice3.pack()

button = tk.Button(app, text="選択", command=show_selected_choice)
button.pack()

app.mainloop()
