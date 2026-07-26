import random
option_1="makas"
option_2="taş"
option_3="kağıt"
user_score=0
computer_score=0
while(user_score<3 or computer_score<3):
    user_choice=input("Taş mı kağıt mı makas mı?")
    computer_choice=random.choice([option_1, option_2, option_3])
    print("bilgisayarın seçimi:", computer_choice)
    if user_choice=="makas"and computer_choice=="taş":
        computer_score+=1
    elif user_choice=="taş"and computer_choice=="kağıt":
        computer_score+=1
    elif user_choice==computer_choice:
        print("berabere"),
    elif user_choice=="makas"and computer_choice=="kağıt":
        user_score+=1
    else:
        user_score+=1
if user_score<computer_score:
    print("bilgisayar kazandı")
else:
    print("sen kazandın!!")