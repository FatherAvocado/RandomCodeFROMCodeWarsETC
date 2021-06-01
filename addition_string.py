addition_str = "2+5+10+20"
addition_str = addition_str.split("+")
addend = 0

for addition in addition_str:
    print(addition)
    addition = int(addition)
    addend = addition + addend
    print(addend)