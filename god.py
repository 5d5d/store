import random
def max(x,y):
    if x >= 1000 | x <= 2000:
        y = y + x + (y+x)*0.1
        return y
    elif x >= 2000:
        y = y + x + (y+x)*0.2
        return y
a, b, mon = 0, 0, 0
# a是循环控制值，b是充值金额，mon是账户余额
print("==========关注超慧不迷路 超慧带你上高速==========")
print("$             欢迎光临高速公路               $")
print("$   *    *      *         *     *       * $")
print("$   *     *   开车请按”1“     *       *     $")
print("$ *    *      *       *        *       *  $")
print("$   *     *   刹车请按”Q“      *        *   $")
print("============老铁请点个关注====================")
star = int(input("是否开始游戏"))
if star == 1:
    b = int(input("请输入充值金额"))
    mon = max(b, mon)
    run = random.randint(20, 90)
    print(run)
    print(mon)
    while a < 5:
        a += 1
        mon -= 500
        num = int(input("请输入一个数字"))
        if num == run:
            print("ok")
            break
        elif num > run:
            print("你猜大了")
        elif num < run:
            print("你猜小了")
        elif mon == 0:
            break