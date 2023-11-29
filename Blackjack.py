import random
import time

HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
POSSIBLE_SYMBOLS = [HEARTS, DIAMONDS, SPADES, CLUBS]

def generate_card_deck():
  card_deck = []
  for i in range(2,54):
    card_deck.append(i)
  return card_deck

def draw_card(card_deck):
  card = int(random.choice(card_deck))
  if card in range(2,15):
    symbol = HEARTS
    value = card
  elif card in range(15,28):
    symbol = DIAMONDS
    value = card - 13
  elif card in range(28,41):
    symbol = SPADES
    value = card - 26
  elif card in range(41,54):
    symbol = CLUBS
    value = card - 39
  if value in range(2,11):
    sym = value
  elif value == 11:
    value = 10
    sym = "J"
  elif value == 12:
    value = 10
    sym = "Q"
  elif value == 13:
    value = 10
    sym = "K"
  elif value == 14:
    value = 11
    sym = "A"
  card_deck.remove(card)
  return (symbol, sym, value)
    
def paint_card(symbol, sym):
    print(" ___ ")
    print(f"|{sym}  |")
    print(f"| {symbol} |")
    print(f"|__{sym}|")

def main():
  balance = 0
  print(f"Welcome to the blackjack table!\nYour balance is ${balance}.")
  while True:
    player_move = input("What do you want to do?\nPress D to make a deposit, P to play, or Q to quit!\n>>> ")
    if player_move not in ("D", "P", "Q"):
      print("Please enter valid move.")
      continue
    elif player_move == "Q":
      print(f"Thanks for playing!\nYour balance is ${balance}.")
      break
    elif player_move == "D":
      deposit = input("How much would you like to deposit (max. $1000)\n>>> ")
      if deposit.isnumeric() and  0 < int(deposit) < 1000:
        balance = balance + int(deposit)
        print(f"Deposit accepted.\nYour balance is now ${balance}.")
        continue
      else:
        print("Please make a valid deposit.")
        continue
    elif player_move == "P":
      while True:
        bet = input(f"How much would you like to bet (max. ${balance})?\n>>> ")
        if not bet.isnumeric() or not 0 < int(bet) <= balance:
          print("Please make a valid bet.")
          continue
        else:
          #Loop voor het trekken van de eerste kaarten
          #1 voor dealer, 2 voor speler
          card_deck = generate_card_deck()
          dealer_cards = 0
          dealer_points = 0
          dealer_hand = {}
          player_cards = 0
          player_points = 0
          player_hand = {}
          time.sleep(1)
          print ("The dealer is drawing cards...")
          time.sleep(1)
          #dealer draws its first card
          dealer_cards += 1
          dealer_hand[dealer_cards] = draw_card(card_deck)
          dealer_points += dealer_hand[1][2]
          #player draws its first card
          player_cards += 1
          player_hand[player_cards] = draw_card(card_deck)
          player_points += player_hand[player_cards][2]
          #player draws its second card
          player_cards += 1
          player_hand[player_cards] = draw_card(card_deck)
          player_points += player_hand[player_cards][2]
          #print and paint everything
          print("Dealer:")
          paint_card(dealer_hand[1][0], dealer_hand[1][1])
          time.sleep(1)
          print("You:")
          paint_card(player_hand[1][0], player_hand[1][1])
          time.sleep(1)
          paint_card(player_hand[2][0], player_hand[2][1])
          time.sleep(1)
          print(f"\nThe dealer has {dealer_points} points, and you have {player_points} points.")
          #next move for the player
          next_move = input("What is your next move? D to draw, S to stop!\n>>> ")
          while True:
            #loop where the player can continue or stop playing
            if next_move not in ("D", "S"):
              next_move = input("Please enter a valid move! D to draw, S to stop!\n>>>")
              continue
            elif next_move == "D":
              time.sleep(1)
              print("Taking another card...")
              time.sleep(1)
              player_cards +=1
              player_hand[player_cards] = draw_card(card_deck)
              player_points += player_hand[player_cards][2]
              paint_card(player_hand[player_cards][0], player_hand[player_cards][1])
              time.sleep(1)
              if player_points > 21:
                print(f"\nYou have {player_points} points...")  
                player_wins = False
                break
              elif player_points == 21:
                print(f"\nYou have {player_points} points...\nThat's perfect!")
                next_move = "S"
                continue
              else:
                next_move = input(f"\nYou have {player_points} points...\nWhat's your next move? Do to draw, S to stop!\n>>>")
                continue
            elif next_move == "S":
              print(f"\nYou have {player_points} points... Now let's see what the dealer gets!")
              while True:
                #loop for the dealer to draw cards until he reaches 17 or more, or goes above 21
                time.sleep(1)
                print(f"The dealer has {dealer_points} points\nTaking another card...")
                dealer_cards += 1
                dealer_hand[dealer_cards] = draw_card(card_deck)
                dealer_points += dealer_hand[dealer_cards][2]
                time.sleep(1)
                paint_card(dealer_hand[dealer_cards][0], dealer_hand[dealer_cards][1])
                time.sleep(1)
                if dealer_points < 17:
                    continue
                elif 17 <= dealer_points <= 21:
                    print(f"The dealer has {dealer_points} points, and will stop!")
                    if player_points > dealer_points:
                        player_wins = True
                    elif player_points == dealer_points:
                        player_wins = None
                    else:
                        player_wins = False
                    break
                elif dealer_points > 21:
                    player_wins = True
                    print(f"The dealer has {dealer_points} points!")
                    break
            break  
        break
    if player_wins == True:
        balance = balance + int(bet)
        print(f"You win! You've won ${bet}.\nYour balance is ${balance}.")
    elif player_wins == False:
        balance = balance - int(bet)
        print(f"You lose! You've lost ${bet}.\nYour balance is ${balance}.")
    else:
        print("It's a tie. Your balance is still ${balance}.")
main()
     
