#tkとしてtkinterをインポート
#Tkinterは、PythonのGUI（Graphical User Interface）ツールキットの標準ライブラリ
import tkinter as tk

#クラスを定義#チャット
class ChatClient:
    def __init__(self, master, username):
        """
        ChatClientクラスのコンストラクタ。
        Parameters:
            master (Tk): 親ウィンドウ(TkinterのTk()インスタンス)。
            username (str): チャットクライアントのユーザー名。
        """
        self.master = master
        self.username = username
        self.master.title(f'Chat Client ({username})')

        # チャット相手の名前表示
        partner_label_a = tk.Label(self.master, text="A:", width=10)
        partner_label_a.grid(row=0, column=0)

        partner_label_b = tk.Label(self.master, text="B:", width=10)
        partner_label_b.grid(row=0, column=2)  # カラム位置を修正

        # メッセージ表示用のリストボックス
        self.message_listbox_a = tk.Listbox(self.master, width=30, height=10)
        self.message_listbox_a.grid(row=1, column=0, padx=10, pady=5)

        self.message_listbox_b = tk.Listbox(self.master, width=30, height=10)
        self.message_listbox_b.grid(row=1, column=2, padx=10, pady=5)  # カラム位置を修正

        # メッセージ入力用のテキストボックス
        self.input_entry_a = tk.Entry(self.master, width=30)
        self.input_entry_a.grid(row=2, column=0, padx=10, pady=5)

        self.input_entry_b = tk.Entry(self.master, width=30)
        self.input_entry_b.grid(row=2, column=2, padx=10, pady=5)  # カラム位置を修正

        # 送信ボタン
        send_button_a = tk.Button(self.master, text='Send', command=self.send_message_a)
        send_button_a.grid(row=3, column=0, padx=10, pady=5)

        send_button_b = tk.Button(self.master, text='Send', command=self.send_message_b)
        send_button_b.grid(row=3, column=2, padx=10, pady=5)  # カラム位置を修正

    def send_message_a(self):
        """
        チャット相手Aにメッセージを送信するメソッド。
        """
        message = self.input_entry_a.get()
        self.message_listbox_a.insert(tk.END, f"A: {message}")
        self.message_listbox_b.insert(tk.END, f"A: {message}")  # チャット相手Bにも送信内容を表示
        self.input_entry_a.delete(0, tk.END)

    def send_message_b(self):
        """
        チャット相手Bにメッセージを送信するメソッド。
        """
        message = self.input_entry_b.get()
        self.message_listbox_b.insert(tk.END, f"B: {message}")
        self.message_listbox_a.insert(tk.END, f"B: {message}")  # チャット相手Aにも送信内容を表示
        self.input_entry_b.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()

    # チャットクライアントAを作成
    chat_client_a = ChatClient(root, "A")

    # チャットクライアントBを作成
    chat_client_b = ChatClient(root, "B")

    root.mainloop()
