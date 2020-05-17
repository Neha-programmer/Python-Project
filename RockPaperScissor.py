import random
Draws=0
Wins=0
Losses=0
is_ended=False
prompt="Choose Rock(r),Paper(p),Scissor(s) or 'q' for quit: "
while(True):
    user_choice=input(prompt)
    while user_choice not  in ['p','s','r','q']:
        user_choice=input(prompt)
    if user_choice=='q':
        break
    else:
        computer_choice=random.choice(['r','p','s'])
        if computer_choice=='r':
            move='Rock'
        elif computer_choice=='p':
            move='Paper'
        else:
            move='Scissor'
        print('Computer gives a ' + move)
        if computer_choice==user_choice:
            print('Draw')
            Draws += 1
        elif(computer_choice=='r' and user_choice=='p') or (computer_choice=='p' and user_choice=='s') or (computer_choice=='s' and user_choice=='r'):
            print("You Win!")
            Wins += 1
        else:
            print("You Lose!")
            Losses +=1
print('You have ' + str(Wins) +' Wins, ' +str(Draws) + ' Draws, and ' + str(Losses) +' Losses.')