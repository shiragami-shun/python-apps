import time
# timeモジュールをインポート
a = time.strftime("%Y")
b = time.strftime("%m")
c = time.strftime("%d")
# 現在の年、月、日を取得
times = []
events = []
# ユーザーが入力した時間と予定を格納するリスト
print("このプログラムは、今日の予定帳を作成するプログラムです")
time.sleep(1)
# プログラムの説明を表示
while True:
    # 無限ループで繰り返し入力を受け付ける
    print("時間を入力してください。(例:12:00~18:00)")
    d = input()
    times.append(d)
    time.sleep(1)
    # 予定の時間を入力
    print("本日行う予定を入力してください。(例:買い物,勉強)")
    e = input()
    events.append(e)
    time.sleep(1)
    # 予定の内容を入力
    if len(times) != 0:
        for i in range(len(times)):
            if i == 0:
                print(f"{a}-{b}-{c}-{times[i]},{events[i]}")
                time.sleep(1)
            else:
                print(f"{times[i]},{events[i]}")
                time.sleep(1)
    else:
        print(f"{a}-{b}-{c}-{times[0]},{events[0]}")
    # 入力された時間と予定を表示

    print("もう一度入力しますか？続ける場合はYesを終わる場合はNoを入力してください。")
    f = input()
    if f.lower() == "yes":
        time.sleep(1)
        print("それではもう一度入力します。")
    else:
        print("それではこのプログラムを終了します。ありがとうございました！")
        break
    # ユーザーが続けるかどうかを確認

    # 工夫したポイント
    # 1. 最初の予定にだけ日付を表示し、以降は時間と予定のみを表示するようにしました。
    # 2. 例を書いたり、time.sleepを使って、ユーザーが理解しやすいようにしました。