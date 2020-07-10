import os
pl=[]
ss=[]
qw=[]
zxx=[]
s=""
tri=[]
logo="""script made by Fighteros at Telegram @fighteros
 ____________
< manshit  >
 ------------
       \   ,__,
        \  (oo)____
           (__)    )\
           
             ||--|| *
             
                        """

def manshit(liss):
    with open ("manshit.txt","w") as bg:
        for i in range(len(liss)):
            if not liss[i] :
                pass
            else:
                bg.write(liss[i]+'\n')
def main():
    print(logo)
    filename=input("what's the list name ?:")               
    with open (filename.strip(),'r') as b:
        pl=b.readlines()
    for i in range(len(pl)):
        s=pl[i]
        ss=s.split(":")
        us=ss[1]
        qw=us.split("@")
        #print(ss[0])
        dsd=qw[1]
        zxx=dsd.split(";")
        ip_use=ss[0]+"|"+zxx[0]
        try:
            done=ip_use+"|"+zxx[1]
            
        except:
            done=ip_use+"|"
        tri.append(done)

    manshit(tri)    
    print("done splitting and formating enjoy")
                
    print("result is saved in 'manshit.txt'")
if __name__ =="__main__":
    main()
