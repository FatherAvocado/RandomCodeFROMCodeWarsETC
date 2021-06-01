
import string

def to_jaden_case(x):
    # ...
    #jadencase = string.lower()
    jadencase = string.capwords(x, sep = None)
    return jadencase

print(to_jaden_case("How Can Mirrors Be Real If Our Eyes Aren'T Real"))