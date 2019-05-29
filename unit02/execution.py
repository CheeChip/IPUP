# python3
# 问题：
#   有100名犯人，站成一排报数，枪毙掉报到奇数的人，
#   剩下的人进入下一轮报数，重复此过程，到只剩下一个
#   人为止，余下这个犯人会被释放。在整个过程中犯人的
#   相对次序不变，问：你要是其中一个犯人，一开始站到
#   第几位才能保证最后会被释放？

prisoner = [i for i in range(1, 101)]
next_turn = []
while len(prisoner) > 1:
    for i in range(len(prisoner)):
        if (i+1) % 2 == 0:
            next_turn.append(prisoner[i])
    prisoner = next_turn
    next_turn = []

print(prisoner[0])