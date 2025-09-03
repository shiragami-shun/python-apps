import time
import random
import math

print("名前を入力してください。")
name = input()
li = []
z = 100

print("反射神経テストを始めます。！！！！！という合図が見えたらenterを押してください")
while True:
    n = random.randint(5, 15)
    print("準備ができたらenterを押してください")
    y = input()
    print("スタート！")
    time.sleep(n)
    print("！！！！！")
    s = time.time()
    a = input()
    e = time.time()
    r = e - s
    b = math.floor(r * 10000) / 10000
    if b <= 0.01:
        print("不正を検知しました。正しい方法でのテストのみ結果を表示します")
    elif b < 0.16:
        print(f"反応速度は{b}秒でした。あなたの反応速度は速いでしょう")
        f = r
        li.append(b)
    elif b < 0.18:
        print(f"反応速度は{b}秒でした。あなたの反応速度は平均より速いでしょう")
        f = r
        li.append(b)
    elif b < 0.2:
        print(f"反応速度は{b}秒でした。あなたの反応速度は平均的でしょう")
        f = r
        li.append(b)
    elif b < 0.22:
        print(f"反応速度は{b}秒でした。あなたの反応速度は平均より遅いでしょう")
        f = r
        li.append(b)
    else:
        print(f"反応速度は{b}秒でした。あなたの反応速度は遅いでしょう")
        f = r
        li.append(b)
    time.sleep(2)
    import mysql.connector

    conn = mysql.connector.connect(
        host="localhost", user="root", password="Shun13579", database="work04"
    )

    cursor = conn.cursor()

    # データを挿入
    sql = "INSERT INTO record (name, record_time, started_at) VALUES (%s, %s, %s)"
    values = (name, f, time.strftime("%Y-%m-%d %H:%M:%S"))
    cursor.execute(sql, values)
    conn.commit()  # ← これが必要

    cursor.close()
    conn.close()
    import mysql.connector

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shun13579",
        database="work04"
    )

    cursor = conn.cursor()

    # id が大きい順に並べて最新の1件を取得
    cursor.execute("SELECT * FROM record ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()

    if row:
        print(f"前回の記録: id={row[0]}, name={row[1]}, time={row[2]}秒, at={row[3]}")
    else:
        print("データがありません。")

    cursor.close()
    conn.close()

    import mysql.connector

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shun13579",
        database="work04"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM record ORDER BY record_time ASC LIMIT 1")
    rows = cursor.fetchall()

    for row in rows:
        print(f"これまでの最速記録: id={row[0]}, name={row[1]}, time={row[2]}秒, at={row[3]}")

    cursor.close()
    conn.close()

    print("もう一度行いますか？続ける場合はYesを終わる場合はNoを入力してください。")
    d = input()
    if d.lower() == "yes":
        print("それではもう一度行います")
    else:
        z = min(li)
        print(f"最高記録は{z}秒でした。")
        time.sleep(1)
        print("それではこのゲームを終了します。ありがとうございました！")
        break