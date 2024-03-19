"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    dict = {}

    for key, value in result.items():
        if key == "foo":
            dict["Foo"] = value.capitalize().replace("k","")

    return dict
