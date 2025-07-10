import time

a = time.strftime("%Y")
b = time.strftime("%m")
c = time.strftime("%d")
times = []
events = []
while True:
    print("時間を入力してください。(例:12:00~18:00)")
    d = input()
    times.append(d)
    print("本日行う予定を入力してください。(例:買い物,勉強)")
    e = input()
    events.append(e)
    if len(times) != 0:
        for i in range(len(times)):
            if i == 0:
                print(f"{a}-{b}-{c}-{times[i]},{events[i]}")
            else:
                print(f"{times[i]},{events[i]}")
    else:
        print(f"{a}-{b}-{c}-{times[0]},{events[0]}")
    print("もう一度入力しますか？続ける場合はYesを終わる場合はNoを入力してください。")
    f = input()
    if f.lower() == "yes":
        print("それではもう一度入力します。")
    else:
        print("それではこのプログラムを終了します。ありがとうございました！")
        break