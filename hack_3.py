"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""



def fn_hack_3(s):
    result = s
    lista = ["f", "z", "m", "n", "r", "u"]
    lista_3 = []

    for i in result:
        if i not in lista:
            contenedor = f"{i.replace('o', '0').replace('a', '@').replace('i', '¡').upper()}"
            lista_3.append(contenedor)
        else:
            lista_3.append(i.replace('f', 'F').replace('n', 'N').replace('R', 'r').replace('U', 'v'))

    result = "".join(lista_3)
    return result.replace('u', 'v')

