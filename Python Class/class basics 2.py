class enemy:
    power = 10

    def hit(help,x):
        help.rover = "haaaammu"
        help.hari=x
        print(help.hari)
        print("oh my god i got hit")
        help.power-=2
        print(help.rover)

    def health(help):
        if help.power >=5:
            print("you are still strong",(help.power))
        elif help.power in range (1,5):
            print("you are running out of power",(help.power))
        else:
            print("you are dead")
e1=enemy()
e2=enemy()
e1.hit(5)
e1.health()
