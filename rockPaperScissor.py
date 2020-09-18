import random, re

def RocKPaperScissor(user_choice):
    
    if user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissor"
    print("Your choice is: %s" %(user_choice_name))
    print("Now it's computer turn to initiate........")
    computer_choice = random.randint(1, 3)
    while computer_choice == user_choice:
        computer_choice = random.randint(1, 3) 
           
    if computer_choice == 1:
        computer_choice_name = "Rock"
    elif computer_choice == 2:
        computer_choice_name = "Paper"
    else:
        computer_choice_name = "Scissor"
    print("Computer choice is: %s " %(computer_choice_name))
    print(user_choice_name + " v//s " + computer_choice_name)
    
    if ((user_choice==1 and computer_choice==2) or (computer_choice==1 and user_choice==2)):
        print("Paper wins ==> ", end="")
        final_result ="Paper"

    elif ((user_choice==1 and computer_choice==3) or (user_choice==3 and computer_choice==1)):
        print("Rock wins ==> ", end="")
        final_result="Rock"
    else:
        print("Scissor wins ==> ", end="")
        final_result="Scissor"
            
    if final_result == user_choice_name:
        print("+++You are the Winner+++")
    else:
        print("+++Computer is winner+++")                

    print('''
    +==============================+
    +                              +
    +       Game Over              +
    +                              +
    +==============================+
    ''')



"""+++++++++++++++++++++++Code logic++++++++++++++++++++++++++"""
print('''
    +==============================+
    +                              +
    +       Welcome To RPS         +
    +                              +
    +==============================+
    ''')

print("""Game Rules:
    ++ Rock v/s Paper ==> Paper wins
    ++ Paper v/s Scissor ==> Scissor wins
    ++ Scissor v/s Rock ==> Rock wins\n""")

try:
    while True:
        print("Enter Your Choice:\n1 for Rock\n2 1for Paper\n3 for Scissor\n")


        user_choice = int(input("Your turn: ")) # Get input from a user (1 or 2 or 3) 
    


        while user_choice > 3 or user_choice < 1:
              # As while is true , if user inputs  wrong value choice
            user_choice = int(input("Enter valid choice: ")) # this method take value from user and pass into  the function call
     

        RocKPaperScissor(user_choice)
        print("Do you wanna play again? (Y/N)") 

     # If user don't wanna play anymore , he can quit the game by either  of N or n otherwise
     # player can continue game by using any of the keyboard key   
        answer = input()
        if (answer=="N" or answer == "n"):
            print("THank you playing with us ....")
            break 
        else:
            continue


except Exception as err:
    print(err)        
         
