import tkinter as tk
from tkinter import messagebox

# ウィンドウの作成
root = tk.Tk()
root.title("予定帳")
root.geometry("420x550")

# 予定データ（日付ごとに管理）
schedule_data = {}  # {"2025-09-17": [("12:00~13:00", "勉強"), ...]}


def add_placeholder(entry, placeholder):
    """Entryにプレースホルダーを追加"""
    entry.insert(0, placeholder)
    entry.config(fg="gray")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


# ラベル
label_intro = tk.Label(root, text="日付・時間・予定を入力してください", font=("Arial", 12))
label_intro.pack(pady=10)

# 日付入力
entry_date = tk.Entry(root, width=30)
entry_date.pack()
add_placeholder(entry_date, "例: 2025-09-17")

# 時間入力
entry_time = tk.Entry(root, width=30)
entry_time.pack()
add_placeholder(entry_time, "例: 12:00~18:00")

# イベント入力
entry_event = tk.Entry(root, width=30)
entry_event.pack()
add_placeholder(entry_event, "例: 買い物, 勉強")

# 予定表示用
text_output = tk.Text(root, height=18, width=50)
text_output.pack(pady=10)


# 予定追加処理
def add_schedule():
    d = entry_date.get()
    t = entry_time.get()
    e = entry_event.get()

    # 入力チェック
    if d in ["例: 2025-09-17", ""] or t in ["例: 12:00~18:00", ""] or e in ["例: 買い物, 勉強", ""]:
        messagebox.showwarning("入力エラー", "日付・時間・予定のすべてを入力してください")
        return

    # 日付ごとに予定を保存
    if d not in schedule_data:
        schedule_data[d] = []
    schedule_data[d].append((t, e))

    messagebox.showinfo("追加完了", f"{d} の予定を追加しました！")

    # 入力欄リセット
    entry_date.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_event.delete(0, tk.END)
    add_placeholder(entry_date, "例: 2025-09-17")
    add_placeholder(entry_time, "例: 12:00~18:00")
    add_placeholder(entry_event, "例: 買い物, 勉強")


# 予定表示処理
def show_schedule():
    d = entry_date.get()
    if d in ["例: 2025-09-17", ""]:
        messagebox.showwarning("入力エラー", "表示したい日付を入力してください")
        return

    text_output.delete(1.0, tk.END)  # 一度クリア

    if d not in schedule_data or not schedule_data[d]:
        text_output.insert(tk.END, f"{d} の予定はありません。\n")
        return

    text_output.insert(tk.END, f"📅 {d} の予定:\n")
    for t, e in schedule_data[d]:
        text_output.insert(tk.END, f"  {t} - {e}\n")


# ボタン追加
btn_add = tk.Button(root, text="予定を追加", command=add_schedule)
btn_add.pack(pady=5)

btn_show = tk.Button(root, text="予定を表示", command=show_schedule)
btn_show.pack(pady=5)

# 終了ボタン
btn_quit = tk.Button(root, text="終了", command=root.quit)
btn_quit.pack(pady=5)

# GUIスタート
root.mainloop()
