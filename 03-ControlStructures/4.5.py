###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    code = int(ord(char))
    # add one to the character's code
    added_encrypted_text = code + 1
    # replace new character code with its
    # corresponding character (use chr())
    new_code = (chr(added_encrypted_text))
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + new_code 

print(f'plain_text: {plain_text}')
print(f'encrypted_text: {encrypted_text}')