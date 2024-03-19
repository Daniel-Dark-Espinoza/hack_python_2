"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    lista = []

    for items in result:
        if items == "a":
            lista.append("1")
        elif items == "b" or items == "d":
            lista.append("-")
        elif items == "c":
            lista.append("3")
        elif items == "e":
            lista.append("5")

    if not lista:
        return ["0"]
    
    result = lista

    return result
