#import random
# n = random.randint(1,100)
# for i in range(5):
# a = int(input())
# if n == a:
# print("正解です")
# break
# else:
# print("不正解です")
# print(f"正解は{n}です")
#import random
#rn = random.randint(1,100)
#a = input().
#print(rn)
#print(a,rn)
#if rn == int(a):
  #print("正解")
#else:
  #print(f"不正解です。正解は{rn}でした")
import random
while True:
  n = random.randint(1,100)
  c = 0
  b = 4
  print("数当てゲームです。100以下の数字がランダムで答えに設定されています。あと5回答えることができます。")
  for i in range(5):
    a = input()
    if int(a) == n:
      print("正解です。")
      c += 1
      break
    elif int(a) > n+20:
      print(f"不正解です。答えよりかなり大きいです。あと{b}回答えることができます。")
      b -= 1
    elif int(a) < n-20:
      print(f"不正解です。答えよりかなり小さいです。あと{b}回答えることができます。")
      b -= 1
    elif int(a) > n:
      print(f"不正解です。答えより大きいです。あと{b}回答えることができます。")
      b -= 1
    elif int(a) < n:
      print(f"不正解です。答えより小さいです。あと{b}回答えることができます。")
      b -= 1
  print(f"正解は{n}でした。正解した回数は{c}回です")
  print("もう一度行いますか？続ける場合はYesを終わる場合はNoを入力してください。")
  d = input()
  if d.lower() == "yes":
    print("それではもう一度出題します！")
  else:
    print("それではこのゲームを終了します。ありがとうございました！")
    break