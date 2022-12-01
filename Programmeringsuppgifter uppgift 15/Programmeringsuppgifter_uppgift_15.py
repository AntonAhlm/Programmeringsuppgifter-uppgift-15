import random 

list=["+","+","+","+","+","+","+","-"]

list1=["Bra","Duger","Ok","k bry"]
list2=["Samst","Du suger dahri","Du suger dahri","Du suger dahri","Adam Jamal ar smartare an dig","Gahba","Gahba"]

text1=random.choice(list1)
text2=random.choice(list2)

math=random.choice(list) 

TalA=random.randint(2,10)
TalX=random.randint(1,10)
TalB=random.randint(1,10)

if math=="+":
    TalC=TalA*TalX+TalB

if math=="-":
    TalC=TalA*TalX-TalB

print("Los Ekvationen ",TalA,"x",math,TalB," = ",TalC)

# Fusk för idioter print("TalX=",TalX,"\n")

svar=int(input("X = "))

if svar==TalX:
    print(text1)
else:
    print(text2)
