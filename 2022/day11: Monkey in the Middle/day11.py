# the data is more convenient if we just type it by ourselves.

# old*3 | 11 (7 ? 2)
m0 = [75, 63]
# old+3 | 2 (2 ? 0)
m1 = [65, 79, 98, 77, 56, 54, 83, 94]
# old+5 | 5 (7 ? 5)
m2 = [66]
# old*19 | 7 (6 ? 4)
m3 = [51, 89, 90]
# old+1 | 17 (6 ? 1)
m4 = [75, 94, 66, 90, 77, 82, 61]
# old+2 | 19 (4 ? 3)
m5 = [53, 76, 59, 92, 95]
# old*old | 3 (0 ? 1)
m6 = [81, 61, 75, 89, 70, 92]
# old+8 | 13 (3 ? 5)
m7 = [81, 86, 62, 87]

c = [0, 0, 0, 0, 0, 0, 0, 0]


def operation(round, div):
    for _ in range(round):
        c[0] += len(m0)
        for stuff in m0:
            stuff = (stuff * 3) // div
            if stuff % 11:
                m2.append(stuff)
            else:
                m7.append(stuff)
        m0.clear()

        c[1] += len(m1)
        for stuff in m1:
            stuff = (stuff + 3) // div
            if stuff % 2:
                m0.append(stuff)
            else:
                m2.append(stuff)
        m1.clear()

        c[2] += len(m2)
        for stuff in m2:
            stuff = (stuff + 5) // div
            if stuff % 5:
                m5.append(stuff)
            else:
                m7.append(stuff)
        m2.clear()

        c[3] += len(m3)
        for stuff in m3:
            stuff = (stuff * 19) // div
            if stuff % 7:
                m4.append(stuff)
            else:
                m6.append(stuff)
        m3.clear()

        c[4] += len(m4)
        for stuff in m4:
            stuff = (stuff + 1) // div
            if stuff % 17:
                m1.append(stuff)
            else:
                m6.append(stuff)
        m4.clear()

        c[5] += len(m5)
        for stuff in m5:
            stuff = (stuff + 2) // div
            if stuff % 19:
                m3.append(stuff)
            else:
                m4.append(stuff)
        m5.clear()

        c[6] += len(m6)
        for stuff in m6:
            stuff = (stuff * stuff) // div
            if stuff % 3:
                m1.append(stuff)
            else:
                m0.append(stuff)
        m6.clear()

        c[7] += len(m7)
        for stuff in m7:
            stuff = (stuff + 8) // div
            if stuff % 13:
                m5.append(stuff)
            else:
                m3.append(stuff)
        m7.clear()


if __name__ == '__main__':
    operation(20, 3)
    c.sort()
    print(f'[Part1] : {c[-1]*c[-2]}')

    c = [0, 0, 0, 0, 0, 0, 0, 0]
    operation(10000, 1)
    c.sort()
    print(f'[Part2] : {c[-1] * c[-2]}')
