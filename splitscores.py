# Count how many are equal or above 90

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
splitscores = scores.split()
total = 0

for score in splitscores:
    score = int(score)
    if score >= 90:
        total += 1

print(total)


print(splitscores)