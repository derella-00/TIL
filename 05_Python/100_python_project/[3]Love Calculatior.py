# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cs = name1 + name2
lower_cs = cs.lower()

t = lower_cs.count("t")
r = lower_cs.count("r")
u = lower_cs.count("u")
e = lower_cs.count("e")

true = t + r + u + e

l = lower_cs.count("l")
o = lower_cs.count("o")
v = lower_cs.count("v")
e = lower_cs.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90 :
    print(f"Your love score is {love_score}, you go together like coke and metos.")
elif love_score >= 40 and love_score <= 50 :
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")

