import random

mylist = []

# リストにランダムな値を追加
for i in range(10):  # 0から9までの範囲でループ
    mylist.append(random.randrange(10))  # appendでリストに値を追加
    print(mylist[i])

mojiretu = ""

# リストの値を文字列に変換して結合
for h in range(10):  # 0から9までの範囲でループ
    mojiretu += str(mylist[h])

mojiretu = int(mojiretu)  # 文字列を整数に変換
mojiretu += 1  # 1を足す
print(mojiretu)

