def to_camel_case(text):
    #your code here
    #remove - and _
    if not text:
        return text
    else:
        text = text.replace("-"," ")
        text = text.replace("_"," ")
        text = text.split()
        first = text[0]
        text = text[1:]
        print(text)
        acc = ""
        for word in text:

            acc = acc + word.capitalize()


        print(first + acc)

to_camel_case("Return The_Slab" , "Hot_Pants")

#other answers
#def to_camel_case(text):
    #removed = text.replace('-', ' ').replace('_', ' ').split()
    #if len(removed) == 0:
    #    return ''
    #return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])


