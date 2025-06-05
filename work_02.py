import time
import random
import math
n = random.randint(5,15)
print("反射神経テストを始めます。今!という文字が見えたらenterを押してください")
time.sleep(n)
print("今！")
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