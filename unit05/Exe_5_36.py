#!/usr/bin/env python3

# Exe 36: （游戏：石头剪刀布）编写程序让用户不断玩直到计算机或
# 用户中某一方能赢得游戏超过两次。

from random import randrange

check = {0: 'Scissor', 1: 'Rock', 2: 'Paper'}

def win(pc, user):
    # -1 for pc win
    # 0 for draw
    # 1 for user win
    res = None
    if pc == 0:
        if user == 0:
            res = 0
        elif user == 1:
            res = 1
        elif user == 2:
            res = -1
    elif pc == 1:
        if user == 0:
            res = -1
        elif user == 1:
            res = 0
        elif user == 2:
            res = 1
    elif pc == 2:
        if user == 0:
            res = 1
        elif user == 1:
            res = -1
        elif user == 2:
            res = 0
    if res == -1:
        print("You're {} and CPU is {}, you lose.".format(check[user], check[pc]))
    elif res == 0:
        print("You're {} and CPU is {}, it's a draw.".format(check[user], check[pc]))
    else:
        print("You're {} and CPU is {}, you win.".format(check[user], check[pc]))            

    return res


def main(args):
    winCnt = 0
    while True:
        pc = randrange(3)
        user = randrange(3)
        if win(pc, user) == 1:
            winCnt += 1
            if winCnt >= 2:
                break
        else:
            winCnt = 0
    print("You win twice continuously, game over.")
    return 0
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
