ch = input().strip()
kb = "qwertyuiopasdfghjklzxcvbnm"
i = kb.index(ch)
r = kb[(i + 1) % len(kb)]
print(r)
