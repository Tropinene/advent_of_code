# generate a key with below 3 steps:
#   step0: MD5[salt+idx]
#   step1: find a MD5 which contains 3 consecutive letters
#   step2: check the next 1000 MD5 whether it has the same 5 consecutive letters
# part1: given the salt [qzyelonm] find [idx] of the 64th key
# part2: step0 => MD5[MD5[...[MD5(salt+idx)]]] <= MD5 for 2017 times
import hashlib


def MD5(s):
    return hashlib.md5(s.encode()).hexdigest()


def check_3letters(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return True, s[i]
    return False, None


def check_5letters(s, c):
    for i in range(len(s) - 4):
        if s[i] == c:
            if s[i] == s[i + 1] == s[i + 2] == s[i + 3] == s[i + 4]:
                return True
    return False


if __name__ == '__main__':
    salt = 'qzyelonm'
    idx, cnt = 0, 0
    while True:
        md5 = MD5(salt+str(idx))
        flag, c = check_3letters(md5)
        is_key = False
        if flag:
            for i in range(idx+1, idx+1001):
                md5 = MD5(salt+str(i))
                if check_5letters(md5, c):
                    is_key = True
                    break
        if is_key:
            cnt += 1
            if cnt == 64:
                break
        idx += 1
    print(f"[Part1] : {idx}")

    idx, cnt = 0, 0
    while True:
        md5 = MD5(salt + str(idx))
        for _ in range(2016):
            md5 = MD5(md5)
        flag, c = check_3letters(md5)
        is_key = False
        if flag:
            for i in range(idx + 1, idx + 1001):
                md5 = MD5(salt + str(idx))
                for _ in range(2016):
                    md5 = MD5(md5)
                if check_5letters(md5, c):
                    is_key = True
                    break
        if is_key:
            cnt += 1
            if cnt == 64:
                break
        idx += 1
    print(f"[Part2] : {idx}")


