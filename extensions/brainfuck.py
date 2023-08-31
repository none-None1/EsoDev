cmd = "brainfuck.exe %1"
name = "brainfuck"
filext = "*.b *.bf"


def syntaxhighlighter(text):
    colors = {
        "+": "#0D66AB",
        "-": "#0D66AB",
        ",": "#0D17AB",
        ".": "0D17AB",
        ">": "#414DF1",
        "<": "#414DF1",
        "[": "#41A5F1",
        "]": "#41A5F1",
    }
    result = []
    for i in text:
        if i in colors:
            result += [(colors[i], i)]
        else:
            result += [("#7F7F7F", i)]
    return result
