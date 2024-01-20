import re

def is_valid(s):
    fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    return all(field in s for field in fields)


def is_valid2(s):
    byr = int(s["byr"])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(s["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(s["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    if "cm" in s["hgt"]:
        hgt = int(s["hgt"].replace("cm", ""))
        if hgt < 150 or hgt > 193:
            return False
    else:
        hgt = int(s["hgt"].replace("in", ""))
        if hgt < 59 or hgt > 76:
            return False

    hcl = s["hcl"]
    pattern = re.compile(r'^#[0-9a-f]{6}$')
    if not bool(pattern.match(hcl)):
        return False

    ecl = s["ecl"]
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl not in valid_ecl:
        return False

    pid = s["pid"]
    pattern = re.compile(r'^[0-9]{9}$')
    if not bool(pattern.match(pid)):
        return False

    return True


def make_passport(raw):
    lines = raw.strip().split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    passport = {}

    for line in lines:
        for chunk in line.split(" "):
            key, value = chunk.split(":")
            passport[key] = value

    return passport


def make_passports(raw):
    chunks = raw.split("\n\n")
    return [make_passport(chunk) for chunk in chunks if chunk.strip()]


if __name__ == '__main__':
    lines = open('input.txt', 'r').read()

    passports = make_passports(lines)

    p1 = sum(is_valid(passport) for passport in passports)
    print(f"[Part1] : {p1}")

    p2 = sum(is_valid(passport) and is_valid2(passport) for passport in passports)
    print(f"[Part2] : {p2}")

