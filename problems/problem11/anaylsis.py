f = open("tmp.txt", "r")
start = False
r = 0
c = 0
for x in f:

    if not start and "SORTED" in x:
        start = True
        continue
    if "Random" in x:
        r += 1
    elif "Class" in x:
        c += 1

print(r)
print(c)
