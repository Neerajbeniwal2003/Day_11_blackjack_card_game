import random
import logo
"""make a function for choose random card from deck"""
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

"""make the calculater score function to calculate the score of the user cards
and computer cards and if it cotain 11 and has score greater then 21 it will replce 11 
to 1"""
def calculate_score(card_list):
    if sum(card_list)==21 and len(card_list)==2:
        return 0
    elif 11 in card_list and sum(card_list)>21:
            card_list.remove(11)
            card_list.append(1)
    return sum(card_list)

"""adding a compare function that compare two list scores"""
def compare(score1,score2):
    if score2==score1:
        return "its a draw"
    elif score1==0:
        return "you win its a blackjack"
    elif score2==0:
        return "you lose computer has a blackjack"
    elif score1>21:
        return "you went over you lose"
    elif score2>21:
        return "you win computer went over"
    elif score1>score2:
        return "you win"
    else:
        return "you lose"
def play_blackjack():
    print(logo.logo)
    """add random card to the list of user cards and computer cards"""
    user_cards=[]
    com_cards=[]
    game_over=False
    for i in range(2):
        user_cards.append(deal_cards())
        com_cards.append(deal_cards())

    #calculating the score using calculate function
    while game_over==False:
        user_score=calculate_score(user_cards)
        com_score=calculate_score(com_cards)
        print(f"your cards : {user_cards}   current score : {user_score}")
        print(f"computer first card : {com_cards[0]}")
        if user_score==0 or com_score==0 or user_score>21:
            game_over=True
        else:
            want_another_card=input("Type 'y' to get another card, type 'n' to pass:").lower()
            if want_another_card=="y":
                user_cards.append(deal_cards())
                game_over=False
            else:
                game_over=True
    while com_score!=0 and com_score<17:
        com_cards.append(deal_cards())
        com_score=calculate_score(com_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {com_cards}, final score: {com_score}")
    print(compare(user_score,com_score))
play_again="y"
while play_again=="y":
    play_again=input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    print("\n"*50)
    play_blackjack()

    




        
     
     



