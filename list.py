def longest(a1, a2):
    a1n = "".join(sorted(set(a1)))
    a2n = "".join(sorted(set(a2)))

    if len(a1n) > len(a2n):
        print(a1n, " ", a2n)
        return a1n

    elif len(a1n) < len(a2n):
        print(a1n, " ", a2n)
        return a2n
    else:
        print(a1n , " " , a2n)

print(longest(("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu"))