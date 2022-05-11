#2. extract largest consecutive same character string from the given string 
#input - "000111111100000000000111100011111"
#output - "00000000000"

n="00011111110000000000011110001111"
one=0
count=1
zero=0
for i in  range(len(n)-1):
    if n[i]== n[i+1]:
        count=count+1
        if  n[i+1]== "0":

            if(count>zero):
                zero=count
        else:
            if(count>one):
                one=count
    else:
        count=1

if(zero< one):
    for i in range(one):
        print("1" , end="")

else:
  
    for i in range(zero):
        print("0" , end="")  