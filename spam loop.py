spam = 0
while spam < 5:
    spam = spam +1
    if spam == 3:
        continue  #continue line jumps back to the start loop so spam==3 never happens
    print('spam is ' + str(spam))

