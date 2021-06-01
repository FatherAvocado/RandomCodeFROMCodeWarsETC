def is_isogram(string):
    return len(set(string.lower())) == len(string)


print(is_isogram("aaaa"))
string1 = "AAAA"
print(set(string1))