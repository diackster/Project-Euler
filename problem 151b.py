def cut(sheet):
    if sheet == 1:
        return ()
    if sheet > 1:
        tempsheets = []
        while sheet > 1:
            tempsheets.append(sheet/2)
            sheet /= 2
        return tuple(tempsheets)


variants = {}


def get_single_num(a):
    result = 0.0
    b = tuple(a)
    if b not in variants:
        if len(b) > 0:
            for i in range(len(b)):
                sheet = b[i]
                tempsheets = list(b)
                del tempsheets[i]
                tempsheets += cut(sheet)
                tempsheets.sort()
                result += get_single_num(tuple(tempsheets))
            result /= len(b)
            if len(b) == 1:
                result += 1.0
        variants[b] = result
    return variants[b]

print("{:.6f}".format(get_single_num((16,))-2))