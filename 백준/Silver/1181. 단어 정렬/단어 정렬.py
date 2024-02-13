import sys
input = sys.stdin.readline

n = int(input())
word = set()
for _ in range(n):
    w = input().rstrip()
    word.add((w, len(w)))

word = list(word)
word.sort(key= lambda x: (x[1], x[0]))
for x in word:
    print(x[0])