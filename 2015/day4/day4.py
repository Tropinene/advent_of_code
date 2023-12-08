import hashlib

line = 'yzbqklnj'

i, s = 1, ''
while True:
    s = line + str(i)
    hl = hashlib.md5()
    hl.update(s.encode(encoding='utf-8'))
    if hl.hexdigest()[:5] == '00000':
        break
    i += 1

print(f"[Part1] : {i}")

i, s = 1, ''
while True:
    s = line + str(i)
    hl = hashlib.md5()
    hl.update(s.encode(encoding='utf-8'))
    if hl.hexdigest()[:6] == '000000':
        break
    i += 1
print(f"[Part2] : {i}")
