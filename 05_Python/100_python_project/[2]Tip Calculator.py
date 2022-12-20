#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Wecome to the tip calculator!")
bill = float(input("What was the total bill?: "))

percent = float(input("How much tip would you like to give? 10, 12 or 15?: "))
# 백분율을 쓸 일이 있어도 정수에 % 문자열을 함께 쓰지 말자
# 같이 쓰면 정수나 실수로 변환하기 어려워진다.

people = int(input("How many people to spilt the bill?: "))

pay = round((bill/people)*(1+percent/100), 2)
print(f'Each person should pay: ${pay}')
