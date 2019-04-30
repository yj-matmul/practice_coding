sugar = int(input())
bag_5 = sugar//5
sugar %= 5
bag_3 = 0

while bag_5 >= 0:
    if sugar % 3 == 0:
        bag_3 = sugar//3
        sugar %= 3
        break
    bag_5 -= 1
    sugar += 5

if sugar == 0 :
    print(bag_5+bag_3)
else:
    print(-1)