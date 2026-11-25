def f(palindrome):
    straight = ''
    backwards = ''

    for ched in palindrome:
        straight += ched
    for i in palindrome[::-1]:
        backwards += i
    if straight == backwards:
        is_palindrome = True
    else:
        is_palindrome = False
    return is_palindrome
print(f("book"))