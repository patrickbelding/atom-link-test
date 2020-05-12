import pandas as pd

user_data = {'UID': ['base'],'PW': ['test']}
user_data = pd.DataFrame(user_data)
while True:
    choice1 = input("(1) New Account\n(2) Existing Account? ")
    if choice1 == '1':
        type = 'New Account'
        break
    elif choice1 == '2':
        type = 'Existing Account'
        break
    else:
        print("not a valid answer")

if type == 'New Account':
    while True:
        uid = input("User ID? ")
        pw1 = input("Password? ")
        pw2 = input("Repeat Password? ")
        if pw1 == pw2:
            new_row = {'UID':uid, 'PW':pw1}
            user_data = user_data.append(new_row, ignore_index=True)
            print("Congrats on the new account!")
            break
        else:
            print("pw don't match")
else:
    print("xxxxxxx")


# print(user_data)
