
cards = '7797946543'
numbers = list(cards)
count = {}

for card in numbers:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

# 가장 많이 나온 카드
for key, value in count.items():
    if value == max(count.values()):
        print(key)

# 횟수
print(max(count.values()))







