
class RomanNumerals:

    def to_roman(self, num):
        num_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                   (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        roman = ''
        self.num = num
        while num > 0:
            for romNum, letter in num_map: #i is number while r is letter
                while num >= romNum: #check if inserted value is greater than nummap number
                    roman = roman + letter #accumulator adds the letter
                        #print(roman)
                        #print(num)
                    num = num - romNum #goes to the next letter set?
                       #print(num)
            return roman
    def from_roman(self, Romletter):
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
        for iterate in Romletter:
            val = mapping[iterate]
            if min_ and val > min_:
                total = total - min_ * 2
            else:
                #print(val, "ELSE")
                min_ = val
                #print(min_, " MIN is val")
            total += val
            #print(total, "After IF")

        return total


a = RomanNumerals()
print(a.to_roman(1000))
print(a.from_roman("MMIX"))

import string
from collections import OrderedDict
#
# ROMANS = {
#     'M': 1000,
#     'CM': 900,
#     'D': 500,
#     'C': 100,
#     'XC': 90,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'IV': 4,
#     'I': 1,
# }
#
#
# class RomanNumerals:
#
#     def to_roman(n):
#         s = ''
#         for key, value in ROMANS.items():
#             while n % value != n:
#                 n = n - value
#                 s += key
#         return s
#
#     def from_roman(r):
#         s = 0
#         for key, value in ROMANS.items():
#             while r.startswith(key):
#                 r = r[len(key):]
#                 s += value
#         return s