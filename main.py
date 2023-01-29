import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return cards[random.randint(0, 12)]


def calculate_score(card_list):
    n = len(card_list)
    if n == 2:
        if card_list[0] + card_list[1] == 21:
            return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


def compare(user_score_final, computer_score_final):
    if user_score_final == computer_score_final:
        return "Draw"
    elif computer_score_final == 0:
        return "Computer Wins"
    elif user_score_final == 0:
        return "User Wins"
    elif user_score_final > 21:
        return "Computer Wins"
    elif computer_score_final > 21:
        return "User Wins"
    elif computer_score_final > user_score_final:
        return "Computer Wins"
    else:
        return "User Wins"


user_cards = []
computer_cards = []
is_game_over = False

user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

while not is_game_over:
    print(f"Your cards : {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        choice = input("Do you want to take another card (y/n) ?")
        if choice == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
