import hashlib


def calculate_md5(input_string):
    encoded_string = input_string.encode('utf-8')
    md5_hash = hashlib.md5()
    md5_hash.update(encoded_string)
    md5_digest = md5_hash.hexdigest()

    return md5_digest


if __name__ == '__main__':
    inp = "ojvtpuvg"
    add = 1469591
    cnt1, cnt2 = 8, 8
    lst, lst2 = [], list("********")
    while cnt1 or cnt2:
        md5 = calculate_md5(inp + str(add))
        if md5.startswith("00000"):
            if cnt1:
                lst.append(md5[5])
                cnt1 -= 1
            if md5[5].isdigit() and 0 <= int(md5[5]) <= 7 and lst2[int(md5[5])] == '*':
                lst2[int(md5[5])] = md5[6]
                cnt2 -= 1
        add += 1
    p1, p2 = ''.join(lst), ''.join(lst2)
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")
