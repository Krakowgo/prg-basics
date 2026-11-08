facebook = True
twitter = True
instagram = True

account_number = int(facebook) + int(twitter) + int(instagram)

if account_number >= 2:
    print(f'Facebook={facebook}')
    print(f'Twitter={twitter}')
    print(f'Instagram={instagram}')
    print('You are a good influencer!')
else:
    print(f'Facebook={facebook}')
    print(f'Twitter={twitter}')
    print(f'Instagram={instagram}')
    print('You are not a good influencer!') 

