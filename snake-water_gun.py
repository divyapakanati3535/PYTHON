import random
def swg(comp,mine):
    if (comp==mine):
        return None
    if(comp=='s' and mine=='g'):
        return True
    elif(comp=='w' and mine=='s'):
        return True
    elif(comp=='g'and mine=='s'):
        return True
    else:
        return False

choice=('s','w','g')
comp=random.randint(0,2)
comp=choice[comp]
mine=input('choose either s,w or g:')
win=swg(comp,mine)
if win is None:
    print("match drawn")
if win:
    print("you win")
else:
    print(f"you choose {mine} and the computer choose {comp}")
    print("you loose")



