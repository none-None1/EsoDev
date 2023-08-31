cmd = "wee %1"
name = "Weeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
filext = "*.wee *.w"


def syntaxhighlighter(text):
    colors = {
        "Start epidemic": "#0D66AB",
        "Infect person": "#007F00",
        "Deinfect person": "#0D17AB",
        "Bulk infect": "#0DAD51",
        "Check number of infections": "#414DF1",
        "Bulk deinfect": "#0DABA0",
        "Skip next if no one infected": "#41A5F1",
        "Delevop vaccine": "#11E4D6",
    }
    result = []
    for i in text.split("\n")[:-1]:
        if i in colors:
            result += [(colors[i], i)]
        else:
            result += [("#000000", i)]
        result += [("#000000", "\n")]
    if text.split("\n")[-1] in colors:
        result += [(colors[text.split("\n")[-1]], text.split("\n")[-1])]
    else:
        result += [("#000000", text.split("\n")[-1])]
    return result
