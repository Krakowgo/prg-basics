def f(text):
    output = ''
    next_word = ''
    final_output = ''
    if len(text) > 1:
        for i in range(1,len(text),1):
            next_word = "-" + text[i]
            output += next_word
            final_output = text[0] + output
    elif len(text) == 0:
        final_output = ""
    else:
        final_output = text
    return final_output
print(f("Univesity"))