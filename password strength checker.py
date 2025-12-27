pas=input("enter your password")
specialcharacters="!@#$%^&*()_+{}:<>-=[];',./?"

def rules():
    score=0
    o = 0
    u = 0
    n = 0
    s = 0
    l=len(pas)
    for i in pas:
        if i == i.lower() and i != i.upper():
            o += 1
        elif i == i.upper() and i != i.lower():
            u += 1
        elif str.isdigit(i):
            n += 1
        elif i in specialcharacters:
            s += 1
        else:
            print("wrong password")

    if o>0 and u>0 and n>0 and s>0 and l<=8:
        if o>=1 and u==1 and n>=1 and s==1 and l<=8:
            score+=10
        elif o>=1 and u>=1 and n>=1 and s==1 and l<=8:
            score+=5
        else:
            score+=2
        if score==10:
            print("very strong password")
        if score==5:
            print("strong password")
        if score==2:
            print("weak password")
    else:
        print("Try something else with one number one uppercase one lower case one one special character and with length of 8")

print(rules())