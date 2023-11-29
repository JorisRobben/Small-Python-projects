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

def draw_card(card_deck, points):
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
  points = points + value
  return (symbol, sym, points)
    
def paint_card(symbol, sym):
    print(" ___ ")
    print(f"|{sym}  |")
    print(f"| {symbol} |")
    print(f"|__{sym}|")

def main():
  balance = 0
  while True:
    player_move = input("Welcome to the Blackjack table! What do you want to do? Press D to make a deposit, P to play, or Q to quit!\n>>> ")
    if player_move not in ("D", "P", "Q"):
      print("Please enter valid move.")
      continue
    elif player_move == "Q":
      print(f"Thanks for playing! Your balance is ${balance}.")
      break
    elif player_move == "D":
      deposit = input("How much would you like to deposit (max. $1000)\n>>> ")
      if deposit.isnumeric() and  0 < int(deposit) < 1000:
        balance = balance + int(deposit)
        print(f"Deposit accepted. Your balance is now ${balance}.")
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
          dealer_points = 0
          dealer_hand = {}
          player_points = 0
          player_hand = {}
          time.sleep(1)
          print ("The dealer is drawing cards...")
          time.sleep(1)
          dealer_hand[1] = draw_card(card_deck, dealer_points)
          dealer_points = dealer_hand[1][2]
          player_hand[1] = draw_card(card_deck, player_points)
          player_points = player_hand[1][2]
          player_hand[2] = draw_card(card_deck, player_points)
          player_points = player_hand[2][2]
          print("Dealer:")
          paint_card(dealer_hand[1][0], dealer_hand[1][1])
          time.sleep(1)
          print("You:")
          paint_card(player_hand[1][0], player_hand[1][1])
          time.sleep(1)
          paint_card(player_hand[2][0], player_hand[2][1])
          print(f"\nThe dealer has {dealer_points} points, and you have {player_points} points.")
          while True:
            #Loop voor het verder spelen
            next_move = input("What is your next move? D to draw, S to stop!\n>>> ")
            if next_move not in ("D", "S"):
              print("Please enter a valid move!")
              continue
            elif next_move == "D":
              player_hand[3] = draw_card(card_deck, player_points)
              player_points = player_hand[3][2]
              paint_card(player_hand[3][0], player_hand[3][1])
              if player_points > 21:
                balance = balance - int(bet)
                print(f"\nYou have {player_points} points... You've lost your bet! Your balance is now ${balance}.")
                break
              elif player_points == 21:
                balance = balance + int(bet)
                print(f"\nYou have {player_points} points... You've won your bet! Your balance is now ${balance}.")
                break
              else:
                print(f"\nYou have {player_points} points... What is your next move? D to draw, S to stop!\n>>> ")
                continue
            elif next_move == "S":
              print(f"\nYou have {player_points} points... Now let's see what the dealer gets!")
              break
main()
