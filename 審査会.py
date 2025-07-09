import time

a = time.strftime("%Y")
b = time.strftime("%m")
c = time.strftime("%d")
num = 0
y = []
j = []
while True:
    print("時間を入力してください。(例:12:00~18:00)")
    d = input()
    y.append(d)
    print("本日行う予定を入力してください。(例:買い物,勉強)")
    e = input()
    j.append(e)
    if num != 0:
        for i in range(len(y)):
            if i == 0:
                print(f"{a}-{b}-{c}-{y[i]},{j[i]}")
            else:
                print(f"{y[i]},{j[i]}")
    else:
        print(f"{a}-{b}-{c}-{y[0]},{j[0]}")
    print("もう一度入力しますか？続ける場合はYesを終わる場合はNoを入力してください。")
    f = input()
    if f.lower() == "yes":
        print("それではもう一度入力します。")
        num += 1
    else:
        print("それではこのプログラムを終了します。ありがとうございました！")
        break