percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []
for rain in percent_rain:

    if rain > 90:
        resps.append("Bring an umbrella")
    elif rain > 80:
        resps.append("Good for the flowers?")
    elif rain > 50:
        resps.append("Watch out fro clouds!")
    else:
        resps.append("Nice day!")
print(resps)