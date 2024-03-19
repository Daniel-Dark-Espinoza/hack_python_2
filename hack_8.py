"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    lista = []
    longitud = len(result)

    if longitud % 2 == 0:
        for i, elemento in enumerate(reversed(result), start=1):
            lista.append(str(i))
        lista.reverse()

    else:
        for i, elemento in enumerate(reversed(result), start=1):
            lista.append(f"{elemento}-{longitud - i + 1}")

    return lista
