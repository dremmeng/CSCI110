f = open(r"text.txt", "rb")
s = f.readlines()
f.close()
f = open(r"textreversed.txt", "wb")
s.reverse()
for line in s:
    f.write(line+b"\n")
f.close()
