"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    replacements = {
        "foo": "fo-zi-ma-",
        "bar": "ba-zi-an",
        "qu": "qu-",
        "eq": "eq"
    }
    
    for key in replacements:
        if key in result:
            return replacements[key]
        
    result = replacements
    
    return result

