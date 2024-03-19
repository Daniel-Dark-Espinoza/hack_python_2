"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    delete = ["f", "b", "n"]
    lista = []

    for items in result:
        if items not in delete:
         lista.append(items)

    result = "".join(lista)            
    return result
