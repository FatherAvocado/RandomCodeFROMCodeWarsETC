def likes(names):
    # your code here
    if not names:
        return "no one likes this"
    else:
        acc = ""
        if len(names) == 1:
            return names[0] + " likes this"
        elif len(names) == 2:
            return names[0] + " and " + names[-1] + " like this"
        elif len(names) == 3:
            return names[0] + ", " + names[1] + " and "+ names[-1] + " like this"
        else:
            return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"

    pass

print(likes(['Jacob', 'Alex']))