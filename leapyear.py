
def leap_year(year):
    if year % 400 == 0:
        print("Yes")
        return True

    elif year % 4 == 0:
        print("Yes")
        return True

    else:
        print("No")
        return False
year = int(input("Pleas input a year"))
leap_year(year)