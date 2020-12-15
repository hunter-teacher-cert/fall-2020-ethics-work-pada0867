#~~~~~!@#$%^&*()~Notes~()*&^%$#@!~~~~~#
# Use this password generator to create and store new passwords
# for all your accounts!

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_characters = ['!','@','#','$','%','^','&','*','~','?','{','}']
vowels = ['a','e','i','o','u']
site_name_list = []

site_name = input('Enter site name. ')

# turn site into a list
for i in site_name:
  site_name_list.append(i.lower())
# reverse the letters
site_name_list.reverse()
# remove all vowels
vowels_in_name = 0
for i in site_name_list:
  if i in vowels:
    vowels_in_name += 1
while vowels_in_name > 0:
  for i in site_name_list:
    if i in vowels:
      site_name_list.remove(i)
      vowels_in_name -= 1
length = len(site_name_list)
# add numbers
while True:
  answer = input('Does the password need to contain numbers (y/n)? ')
  if answer == 'y':
    if length <= 9:
      site_name_list.append(length)
      break
    else:
      site_name_list.append(9)
      break
  elif answer == 'n':
    break
  else:
    print('Please answer y/n')
length = len(site_name_list)
# add special characters
while True:
    answer = input('Does the password need to contain special characters (y/n)? ')
    if answer == 'y':
      if length <= 10:
        symbol = special_characters[length]
        site_name_list.append(symbol)
        break
      else:
        site_name_list.append('!')
        break
    elif answer == 'n':
        break
    else:
      print('Please answer y/n')
length = len(site_name_list)
# meet length requirement
while True:
    answer = input('Does the password have a length requirement (y/n)? ')
    if answer == 'y':
        try:
          l_req = int(input('How many characters must the password have? '))
          if length == l_req:
            pass
            break
          elif length < l_req:
            counter = 0
            while length < l_req:
              site_name_list.insert(0,letters[counter])
              counter += 1
              length += 1
            break
          elif length > l_req:
            while length > l_req:
              item = site_name_list[0]
              site_name_list.remove(item)
              length -= 1
            break
        except:
            print('Please enter a number.')
    elif answer == 'n':
        break
    else:
        print('Please answer y/n')
length = len(site_name_list)

# convert list to string
password = ''
for i in site_name_list:
  password += str(i)
# add a capital letter
answer = input('Does the password require a capital letter (y/n)? ')
if answer == 'y':
  password = password.title()
# final password
username = input('What is your username for this site? ')
print('\nNew password info:\n\n{}:\nUsername: {}\nPassword: {}\n'.format(site_name,username,password))
while True:
  answer = input("Would you like to add this information to the file 'Passwords.txt' (y/n)? ")
  if answer == 'y':
    with open("Passwords.txt", "a") as f:
      f.write("\n{}:\nUsername: {}\nPassword: {}".format(site_name,username,password))
    print("\nPassword added to file 'Passwords.txt'.")
    break
  elif answer == 'n':
    break
  else:
    print('Please enter y/n')
