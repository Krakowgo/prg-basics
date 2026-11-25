
def f(sentence):
    result = ""

    for i in range(len(sentence)):
        if sentence[i] != " ":
            result += sentence[i]

    return result


print(f("integrated development environment"))

print(f("A programming language is a system of notation for writing computer programs"))