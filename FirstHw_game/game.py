import random  #引入random函数
#本次游戏设计：将每轮回合的游戏数据输出，其最终游戏结束输出游戏失败方和总共的游戏回合数
# my_hp 我的血量
# your_hp 对手的血量
# my_power 我的攻击力
# your_power 对手攻击力
# w  记录回合数
def fight(e,a,b,c,d):
    while True:   #因为不知道会进行多少轮，则使用while死循环
        e = e + 1    #w初始值为0，进入循环后先加1，后续只要循环继续就会加1
        c = random.randint(1,100)  #randint(1,100)生成整数型的随机数，生成随机的攻击力
        d = random.randint(1,100)
        print("第%s回合，我的血量：%s，我的攻击力：%s\n你的血量：%s，你的攻击力%s" %(e,a,b,c,d))
        #输出每回合的双方血量和攻击力
        a = a - d  # 我的血量=我的上一回的血量（第一回合为初始血量）-对方的攻击力
        b = b - c  # 对方的血量=对方的上一回的血量（第一回合为初始血量）-我的攻击力
        if a <= 0:           #如果我的血量小于或等于0，则我输了，并输出我输了！我的血量已空！！！
            print("我输了！我的血量已空！！！")
            break
        elif b <= 0:       #如果我的对方小于或等于0，则对方输了，并输出你输了！你的血量已空！！！
            print("你输了！你的血量已空！！！")
            break
    print("游戏结束！游戏进行了%s回合"%(e))  #输出游戏结束且总共的游戏回合数

def game():
    my_hp = 1000
    your_hp = 1000
    my_power = 0
    your_power = 0
    w = 0
    fight(w, my_hp, your_hp, my_power, your_power)

game()