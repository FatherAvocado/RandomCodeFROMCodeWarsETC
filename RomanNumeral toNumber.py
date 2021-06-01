def romanToInt(s):
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    min_ = None
    total = 0
    for c in s:
        val = mapping[c]
        print(min_, "Min at start")
        if min_ and val > min_:
            print(val, "Executed if")
            print(min_)
            print(total, "Total on if")
            total = total - min_ * 2
            print(total, " Total Number after calculation")
        else:
            print(val, "ELSE")
            min_ = val
            print(min_, " MIN is val")
        total += val
        print(total, "After IF")

    return total

print(romanToInt("MMIV"))