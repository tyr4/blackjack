from random import randint
import time


def symbol(name):
    s = ''
    if name == "spades":
        s = "♠"
    elif name == "hearts":
        s = "♥"
    elif name == "clubs":
        s = "♣"
    elif name == "diamonds":
        s = "♦"
    return s


def matrice(symbol):
    all_cards = [[2, ".-----------.", "|2          |", f"|     {symbol}     |", "|           |", "|           |", f"|     {symbol}     |", "|          2|", "`-----------'"],
                 [3, ".-----------.", f"|3    {symbol}     |", "|           |", f"|     {symbol}     |", "|           |", f"|     {symbol}     |", "|          3|", "`-----------'"],
                 [4, ".-----------.", f"|4          |", f"|  {symbol}     {symbol}  |", "|           |", "|           |", f"|  {symbol}     {symbol}  |", "|          4|", "`-----------'"],
                 [5, ".-----------.", f"|5  {symbol}   {symbol}   |", "|           |", "|           |", f"|     {symbol}     |", "|           |", f"|   {symbol}   {symbol}"
                                                                                                                                                  f"  5|", "`-----------'"],
                 [6, ".-----------.", f"|6          |", f"|   {symbol}   {symbol}   |", "|           |", f"|   {symbol}   {symbol}   |", "|           |",
                  f"|   {symbol}   {symbol}  6|", "`-----------'"],
                 [7, ".-----------.", "|7          |", f"|  {symbol}     {symbol}  |", f"|     {symbol}     |", f"|  {symbol}     {symbol}  |", f"|  {symbol}"
                                                                                                                                                f"     {symbol}  |", "|          7|", "`-----------'"],
                 [8, ".-----------.", f"|8  {symbol}   {symbol}   |", f"|     {symbol}     |", f"|   {symbol}   {symbol}   |", f"|     {symbol}     |",
                  f"|   {symbol}   {symbol}   |", "|          8|", "`-----------'"],
                 [9, ".-----------.", "|9          |", f"|   {symbol}     {symbol} |", f"|   {symbol}     {symbol} |",
                  f"|   {symbol}  {symbol}  {symbol} |", f"|   {symbol}     {symbol} |", "|          9|", "`-----------'"],
                 [10, ".-----------.", f"|10 {symbol}     {symbol} |", f"|   {symbol}     {symbol} |", f"|   {symbol}     {symbol} |",
                  f"|   {symbol}     {symbol} |", f"|   {symbol}     {symbol} |", "|         10|", "`-----------'"],
                 [11, ".-----------.", "|J          |", f"|{symbol}    J     |", "|     A     |", "|     C     |", f"|     K    {symbol}|", "|          J|", "`-----------'"],
                 [12, ".-----------.", "|Q          |", f"|{symbol}    Q     |", "|     U     |", "|     E     |", f"|     E    {symbol}|", "|     N    Q|", "`-----------'"],
                 [13, ".-----------.", "|K          |", f"|{symbol}    K     |", "|     I     |", "|     N     |", f"|     G    {symbol}|", "|          K|", "`-----------'"],
                 [14, ".-----------.", "|A          |", f"|{symbol}    A     |", "|     C     |", "|     E     |", f"|          {symbol}|", "|          A|", "`-----------'"],
                 [15, ".-----------.", "|?          |", "|?    ?     |", "|     ?     |", "|     ?     |", "|     ?    ?|", "|          ?|", "`-----------'"]
                 ]
    return all_cards


def print_card(cards_in_hand):
    ceva = ''
    counter = 0
    if counter + 6 < len(cards_in_hand):
        while counter + 5 <= len(cards_in_hand):
            for i in range(1, 9):
                for j in range(counter, min(len(cards_in_hand), counter + 6)):
                    # if j > len(cards_in_hand):
                    #     break
                    s = symbol(cards_in_hand[j][1])
                    all_cards = matrice(s)
                    if j < len(cards_in_hand) and j < counter + 5 and j != len(cards_in_hand) - 1:
                        ceva += all_cards[cards_in_hand[j][0] - 2][i][:7]
                    else:
                        ceva += all_cards[cards_in_hand[j][0] - 2][i]
                    ceva += "  "
                ceva += "\n"
            counter += 6
            ceva += "----------------------------------------\n"
    if counter < len(cards_in_hand):
        for i in range(1, 9):
            for j in range(counter, len(cards_in_hand)):
                s = symbol(cards_in_hand[j][1])
                all_cards = matrice(s)
                if j + 1 < len(cards_in_hand):
                    ceva += all_cards[cards_in_hand[j][0] - 2][i][:7]
                else:
                    ceva += all_cards[cards_in_hand[j][0] - 2][i]
                ceva += " "
            ceva += "\n"

    print(ceva)


def add_cards(player_cards, dealer_cards, mode, hidden_card):
    while True:
        lista = []
        cards_rando = randint(2, 14)
        symbols_rando = randint(0, 3)
        lista.append(cards_rando)
        lista.append(symbols[symbols_rando])
        if lista not in player_cards and lista not in dealer_cards and lista not in hidden_card:
            if mode == 0:
                player_cards.append(lista)
                return player_cards
            else:
                if lista not in player_cards and lista not in hidden_card and lista not in dealer_cards:
                    if not hidden_card:
                        hidden_card.append(lista)
                        dealer_cards.append([15, 'clubs'])
                        return hidden_card, dealer_cards
                    else:
                        dealer_cards.append(lista)
                        return dealer_cards


def suma(player_cards, hidden_card):
    lista = []
    ace = False
    for card in player_cards:
        if card[0] == 14:
            if ace:
                aux = 1
            else:
                ace = True
                aux = 11 if ace else 1
        elif card[0] in range(11, 14):
            aux = 10
        else:
            aux = card[0]
        lista.append(aux)
    # print(lista)
    # print(player_cards)
    suma = sum(card for card in lista)
    if hidden_card:
        pass
    else:
        suma -= 10 if suma > 21 and ace else 0
    return suma


def rules(player_cards, dealer_cards, player_sum, dealer_sum, hidden_card):
    won, lost, tie = False, False, False
    global score
    global bet
    global insurance

    # decide the game idk
    if not hidden_card:
        if dealer_sum == player_sum:
            tie = True
        elif dealer_sum < player_sum or dealer_sum > 21 or player_sum == 21 and player_sum <= 21:
            score += bet
            won = True
        else:
            score -= bet
            score = max(0, score)
            lost = True

        dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
        if lost:
            print(f"\nYou lost {bet} points! Your total score is now {max(0, score)} points.")
        elif won:
            print(f"\nYou won {bet} points! Your total score is now {max(0, score)} points.")
        elif tie:
            print("\nNobody wins!")
        time.sleep(2)
        return 1

    # if player over 21
    if player_sum > 21:
        score -= bet
        score = max(0, score)
        dealer_cards[0][0] = hidden_card[0][0]
        dealer_cards[0][1] = hidden_card[0][1]
        hidden_card = []
        dealer_sum = suma(dealer_cards, hidden_card)
        dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
        print(f"Total sum of the cards exceeded 21, you lost {bet} points. Your total score is now {max(0, score)}")
        time.sleep(2)
        return 10000

    # insurance
    if dealer_cards[1][0] == 14 and not insurance:
        insurance = True
        dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
        extra_bet = int(input("----- Insurance -----\nIf the dealer's hidden card is a 10-card, you win 50% extra points, or lose 50% extra if not. "
                              "Do you wish to bet 50% extra points?\n1 - Yes\n2 - No "))
        if extra_bet == 1:
            bet += (bet // 2)
            if hidden_card[0][0] in range(10, 14):
                score += (bet // 3 + bet)
                dealer_cards[0][0] = hidden_card[0][0]
                dealer_cards[0][1] = hidden_card[0][1]
                hidden_card = []
                dealer_sum = suma(dealer_cards, hidden_card)
                dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
                print(f"\nYou won {bet} points! Your total score is now {max(0, score)} points.")
                time.sleep(2)
                return 10000
            else:
                dealer_cards[0][0] = hidden_card[0][0]
                dealer_cards[0][1] = hidden_card[0][1]
                hidden_card = []
                dealer_sum = suma(dealer_cards, hidden_card)
                score -= bet
                score = max(0, score)
                dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
                print(f"\nYou lost {bet} points! Your total score is now {max(0, score)} points.")
                time.sleep(2)
                return 10000

    # if natural
    if player_sum == 21:
        dealer_cards[0][0] = hidden_card[0][0]
        dealer_cards[0][1] = hidden_card[0][1]
        hidden_card = []
        dealer_sum = suma(dealer_cards, hidden_card)
        if dealer_sum == 21:
            dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
            print("Nobody wins!")
        else:
            score += bet
            dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
            print(f"\nYou won {bet} points! Your total score is now {max(0, score)} points.")
        time.sleep(2)
        return 10000
    else:
        if dealer_sum == 21 or dealer_sum + hidden_card[0][0] == 21:
            if player_sum == 21:
                print("Nobody wins!")
                time.sleep(2)
                return 10000
            else:
                dealer_cards[0][0] = hidden_card[0][0]
                dealer_cards[0][1] = hidden_card[0][1]
                hidden_card = []
                dealer_sum = suma(dealer_cards, hidden_card)
                dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
                score -= bet
                score = max(0, score)
                print(f"\nYou lost {bet} points! Your total score is now {max(0, score)} points.")
                time.sleep(2)
                return 10000

    return 0


def dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum):
    print("--------------------------------------------------------")
    print("Your cards:")
    print(f"Total sum: {player_sum}")
    print_card(player_cards)
    print(f"-------------------------\nDealer's cards:\nTotal sum: {dealer_sum}")
    print_card(dealer_cards)
    print("--------------------------------------------------------")


print("""
         _       __   ______   __       ______   ____     __  ___   ______     ______   ____     
        | |     / /  / ____/  / /      / ____/  / __ \   /  |/  /  / ____/    /_  __/  / __ \ 
        | | /| / /  / __/    / /      / /      / / / /  / /|_/ /  / __/        / /    / / / /    
        | |/ |/ /  / /___   / /___   / /___   / /_/ /  / /  / /  / /___       / /    / /_/ /     
        |__/|__/  /_____/  /_____/   \____/   \____/  /_/  /_/  /_____/      /_/     \____/ 

            ____     __       ___       ______   __  __        __   ___       ______   __  __      
           / __ )   / /      /   |     / ____/  / / /_/       / /  /   |     / ____/  / / /_/     
          / __  |  / /      / /| |    / /      / ,<      __  / /  / /| |    / /      / ,<         
         / /_/ /  / /___   / ___ |   / /___   / /\ \    / /_/ /  / ___ |   / /___   / /\ \ 
        /_____/  /_____/  /_/  |_|   \____/  /_/  \_\   \____/  /_/  |_|   \____/  /_/  \_\ 

GAME OBJECTIVE:
- Try to reach the total sum of your cards higher than the dealer's, without going over 21.
- ඞ
""")
symbols = ["clubs", "diamonds", "hearts", "spades"]
player_cards, dealer_cards, hidden_card = [], [], []
insurance = False
keep_playing, stance, max_score, score = 0, 0, 1000, 1000
# main loop
while True:
    print(f"\nCurrent points: {score}")
    bet = 0
    while bet == 0:
        try:
            bet = int(input("Bet (in points): "))
            bet = score if bet > score else bet
        except ValueError:
            print("Choose a valid option")
            time.sleep(2)
            bet = 0

    print("\nShuffling...")
    time.sleep(2)
    if not player_cards:
        player_cards = add_cards(player_cards, dealer_cards, 0, hidden_card)
        hidden_card, dealer_cards = add_cards(player_cards, dealer_cards, 1, hidden_card)
        player_cards = add_cards(player_cards, dealer_cards, 0, hidden_card)
        dealer_cards = add_cards(player_cards, dealer_cards, 1, hidden_card)

    player_sum = suma(player_cards, 0)
    dealer_sum = suma(dealer_cards, hidden_card) - 15

    while not rules(player_cards, dealer_cards, player_sum, dealer_sum, hidden_card):
        stance = 0
        dealer_and_player_cards_print(player_cards, dealer_cards, player_sum, dealer_sum)
        while stance == 0:
            try:
                stance = int(input("1 - Draw a card\n2 - It's enough\nYour choice? "))
                if stance not in [1, 2]:
                    print("Choose a valid option")
                    time.sleep(2)
                    stance = 0
            except ValueError:
                print("Choose a valid option")
                time.sleep(2)
                stance = 0
        if stance == 1:
            player_cards = add_cards(player_cards, dealer_cards, 0, hidden_card)
            player_sum = suma(player_cards, 0)
        elif stance == 2:
            # dealer behaviour
            dealer_cards[0][0] = hidden_card[0][0]
            dealer_cards[0][1] = hidden_card[0][1]
            hidden_card = []
            dealer_sum = suma(dealer_cards, hidden_card)
            while suma(dealer_cards, hidden_card) < 17:
                dealer_cards = add_cards(player_cards, dealer_cards, 1, [1000, 'idk'])
                dealer_sum = suma(dealer_cards, hidden_card)
        else:
            print("Choose a valid option\n")
            time.sleep(3)

    max_score = max(max_score, score)

    if score == 0:
        print("""
   ______   ___       __  ___   ______   
  / ____/  /   |     /  |/  /  / ____/   
 / / __   / /| |    / /|_/ /  / __/      
/ /_/ /  / ___ |   / /  / /  / /___      
\____/  /_/  |_|  /_/  /_/  /_____/ 

   ____     _    __   ______   ____      
  / __ \   | |  / /  / ____/  / __ \ 
 / / / /   | | / /  / __/    / /_/ /     
/ /_/ /    | |/ /  / /___   / _, _/      
\____/     |___/  /_____/  /_/ |_| 
            """)
        print(f"Maximum score: {max_score}")
        score, max_score = 1000, 1000
    while keep_playing == 0:
        try:
            keep_playing = int(input("\n1 - Yes\n2 - No\nDo you wish to play again? "))
            if keep_playing not in [1, 2]:
                print("Choose a valid option")
                time.sleep(2)
                keep_playing = 0
        except ValueError:
            print("Choose a valid option")
            time.sleep(2)
            keep_playing = 0

    if keep_playing == 1:
        player_cards, dealer_cards, hidden_card = [], [], []
        insurance = False
        keep_playing, stance = 0, 0
    else:
        print(f"Maximum score: {max_score}")
        break
