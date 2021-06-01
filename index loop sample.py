weather = ["rainy" "cloudy", "sunny", "foggy"]

for condition in weather:
    print("The word is ", len(condition), "characters")
    first_char = condition[0]
    last_char = condition[-1]
    print("First char is ", first_char)
    print("Last char is ", last_char)