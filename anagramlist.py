def anagrams(word, words):
    #sorted("bbbaa") == sorted("aabbb")
    nlist = []
    for oneword in words:
        if sorted(word) == sorted(oneword):
            nlist.append(oneword)
    return nlist

print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
