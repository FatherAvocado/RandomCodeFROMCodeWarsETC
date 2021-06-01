week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")
weeklen = len(week_temps_f)
counter = 0
avg_temp = 0

for temp in week_temps_f:
    temp = float(temp)
    avg_temp = avg_temp + temp
    counter = counter + 1
    if counter == weeklen:
        avg_temp = avg_temp / counter
