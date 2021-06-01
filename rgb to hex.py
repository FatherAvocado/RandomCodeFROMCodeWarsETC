

def rgb(r, g, b):
    # your code here :)
    color = [r, g, b]
    hexes = ""
    for hexa in color:
        hexa = int(hexa)
        if hexa > 255:
            hexa = 255
        elif hexa < 0:
            hexa = 0
        hexa = str(format(hexa, '02x'))
        hexes = (hexes + hexa).upper()
    return hexes
        #print(hexa)
    #print(hexes)
print(rgb(256,10,0))
