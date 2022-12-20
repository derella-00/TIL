#print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120 :
    print("You can ride the rollercoaster!")
    age = int(input("Age? "))
    if age >44 and age <= 55 :
        print("Everything is going to be ok. Have a free ride on us!")
    elif age > 18 :
        bill = 12
    elif age > 12 :
        bill = 7
    else :
        bill = 5
    photo = input("Do you want to take picture? Y or N ")
    if photo == "Y" :
        bill += 3
    print(f'${bill}')
    # if가 참일 때 bill += 3 만해주고 print는 밖으로 빼면 else를 쓰지 않아도 된다..!

else :  
    print("You could't enter the rollercoaster.")


    



