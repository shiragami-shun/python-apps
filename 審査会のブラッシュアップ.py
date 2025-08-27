import tkinter as tk
from tkinter import messagebox
import time

# ウィンドウの作成
root = tk.Tk()
root.title("今日の予定帳")
root.geometry("400x500")

# 日付の取得
a = time.strftime("%Y")
b = time.strftime("%m")
c = time.strftime("%d")

# 予定データの保存用
times = []
events = []

# ラベル
label_intro = tk.Label(root, text="時間と予定を入力してください", font=("Arial", 12))
label_intro.pack(pady=10)

# 時間入力
entry_time = tk.Entry(root, width=30)
entry_time.insert(0, "例: 12:00~18:00")
entry_time.pack()

# イベント入力
entry_event = tk.Entry(root, width=30)
entry_event.insert(0, "例: 買い物, 勉強")
entry_event.pack()

# 予定表示用
text_output = tk.Text(root, height=15, width=45)
text_output.pack(pady=10)


# ボタンの処理
def add_schedule():
    t = entry_time.get()
    e = entry_event.get()
    if not t or not e:
        messagebox.showwarning("入力エラー", "時間と予定の両方を入力してください")
        return
    times.append(t)
    events.append(e)

    text_output.insert(
        tk.END, f"{a}-{b}-{c} {t}, {e}\n" if len(times) == 1 else f"{t}, {e}\n"
    )
    entry_time.delete(0, tk.END)
    entry_event.delete(0, tk.END)


# ボタン追加
btn_add = tk.Button(root, text="予定を追加", command=add_schedule)
btn_add.pack(pady=5)

# 終了ボタン
btn_quit = tk.Button(root, text="終了", command=root.quit)
btn_quit.pack(pady=5)

# GUIスタート
root.mainloop()
