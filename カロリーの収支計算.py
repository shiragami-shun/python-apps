# まだ完成してないです。
import time

print(
    "このプログラムはカロリーの収支計算を行ってくれます。まずは必要な情報を入力してください。"
)
time.sleep(3)
print("性別をmかfで入力してください。mが男性でfが女性です。")
a = input()
if a.lower() != "m" or a.lower() != "f":
    print("性別の入力を間違えています。mかfで正しく入力してください。")
print("年齢を半角数字で入力してください。")
b = int(input())
print("身長を半角数字で入力してください。")
c = int(input())
print("体重を半角数字で入力してください。")
d = int(input())
print("今日の歩数を半角数字で入力してください。")
e = int(input())
print("今日の計算カロリーを半角数字で入力してください。(単位はkcal)")
f = int(input())
print("必要な情報の入力が終わりました。計算を行っています。しばらくお待ちください")
time.sleep(5)
print(
    "まずはあなたの基礎代謝を表示します。出てきた数字があなたの基礎代謝です。(単位はkcal)"
)
time.sleep(2)
if a.lower() == "m":
    print(13.397 * d + 4.799 * c - 5.667 * b + 88.362)
elif a.lower() == "f":
    print(9.247 * d + 3.098 * c - 4.33 * b + 447, 593)
time.sleep(3)
print(
    "次にあなたの歩数による消費カロリーを表示します。出てきた数字があなたの歩行による消費カロリーです。(単位はkcal)"
)
time.sleep(2)
print(e * (0.07 * d))
time.sleep(3)
print("合計の消費カロリーを表示します。(単位はkcal)")
time.sleep(2)
if a.lower() == "m":
    print((13.397 * d + 4.799 * c - 5.667 * b + 88.362) + (e * (0.07 * d)))
elif a.lower() == "f":
    print(((9.247 * d + 3.098 * c - 4.33 * b + 447, 593) + (e * (0.07 * d))))
time.sleep(2)
print("最後にカロリーの収支を発表します。")
g = f - ((13.397 * d + 4.799 * c - 5.667 * b + 88.362) + (e * (0.07 * d)))
h = f - ((9.247 * d + 3.098 * c - 4.33 * b + 447, 593) + (e * (0.07 * d)))
time.sleep(2)
if a.lower() == "m":
    print(f"今日のカロリー収支は{g}です。")
elif a.lower() == "f":
    print(f"今日のカロリー収支は{h}です。")
time.sleep(1)
print("以上でカロリー収支計算を終わります。ご利用いただきありがとうございました。")