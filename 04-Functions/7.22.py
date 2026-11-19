def f(name):
    names = name
    acronym = names.split(" ")
    result = ''

    for i in acronym:
        result += i[0:1]
    return result
print(f("Internet of Things"))