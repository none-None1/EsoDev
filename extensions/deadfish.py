cmd = "Deadfish.exe %1"
name = "Deadfish"
filext = "*.df"


def syntaxhighlighter(text):
    colors = {
        "i": "#0D66AB",
        "d": "#0D17AB",
        "s": "#414DF1",
        "o": "#41A5F1",
    }
    result = []
    for i in text:
        if i in colors:
            result += [(colors[i], i)]
        else:
            result += [("#7F7F7F", i)]
    return result
