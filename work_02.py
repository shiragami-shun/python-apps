import time
import random
import math

li = []
z = 100
print("反射神経テストを始めます。！！！！！という合図が見えたらenterを押してください")
while True:
    n = random.randint(5, 15)
    time.sleep(n)
    print("！！！！！")
    s = time.time()
    a = input()
    e = time.time()
    r = e - s
    r = math.floor(r * 10000) / 10000
    if r <= 0.01:
        print("不正を検知しました。正しい方法でのテストのみ結果を表示します")
    elif r < 0.16:
        print(f"反応速度は{r}秒でした。あなたの反応速度は速いでしょう")
    elif r < 0.18:
        print(f"反応速度は{r}秒でした。あなたの反応速度は平均より速いでしょう")
    elif r < 0.2:
        print(f"反応速度は{r}秒でした。あなたの反応速度は平均的でしょう")
    elif r < 0.22:
        print(f"反応速度は{r}秒でした。あなたの反応速度は平均より遅いでしょう")
    else:
        print(f"反応速度は{r}秒でした。あなたの反応速度は遅いでしょう")
    li.append(r)
    time.sleep(2)
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