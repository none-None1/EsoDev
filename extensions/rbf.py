cmd = "RandomBrainfuck.exe %1"
name = "Random Brainfuck"
filext = "*.rb *.rbf"


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
        "?": "#7F0000",
    }
    result = []
    for i in text:
        if i in colors:
            result += [(colors[i], i)]
        else:
            result += [("#7F7F7F", i)]
    return result
