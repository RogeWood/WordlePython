import random
words = []
with open("word.txt") as f: # 讀單字庫檔
    data = list(f.read().split())
for w in data: # 將單字長度分類
    while len(words) <= len(w):
        a = []
        words.append(a)
    words[len(w)].append(w)

# print(words[0])
# print(words[1])
print(ord('a'))
length = 5
ans = words[length][random.randint(1, len(words[length])-1)]
# print(ans)
