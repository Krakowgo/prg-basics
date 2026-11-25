
def count_letter(text, letter):
    count = 0

    for i in range(len(text)):
        if text[i] == letter:
            count += 1

    return count