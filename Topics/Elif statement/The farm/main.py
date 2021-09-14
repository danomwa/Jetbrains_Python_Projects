
money = int(input())
if money < 23:
    print("None")
elif money < 678:
    money = money // 23
    if money == 1:
        print("{} chicken".format(money))
    print("{} chicken".format(money))
elif money < 1296:
    money = (money // 678)
    if money == 1:
        print("{} goat".format(money))
    print("{} goats".format(money))
elif money < 3848:
    money = (money // 1296)
    if money == 1:
        print("{} pig".format(money))
    print("{} pigs".format(money))
elif money < 6769:
    money = (money // 3848)
    if money == 1:
        print("{} cow".format(money))
    print("{} cows".format(money))
elif money > 6769:
    money = (money // 6769)
    print("{} sheep".format(money))
