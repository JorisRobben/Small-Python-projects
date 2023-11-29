import random

HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
POSSIBLE_SYMBOLS = [HEARTS, DIAMONDS, SPADES, CLUBS]

def generate_card_deck():
  card_deck = []
  for i in range(1,53):
    card_deck.append(i)
  return card_deck

def draw_card(card_deck):
  card = int(random.choice(card_deck))
  if card in range(1,14):
    symbol = HEARTS
    value = card
  elif card in range(14,27):
    symbol = DIAMONDS
    value = card - 13
  elif card in range(27,40):
    symbol = SPADES
    value = card - 26
  elif card in range(40,53):
    symbol = CLUBS
    value = card - 39
  if value in range(1,11):
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
      bet = input(f"How much would you like to bet (max. ${balance})?\n>>> ")
      if bet.isnumeric() and 0 < int(bet) <= balance:
        card_deck = generate_card_deck()
        dealer_points = 0
        dealer_hand = {}
        player_points = 0
        player_hand = {}
        dealer_hand[1] = draw_card(card_deck)
        dealer_points = dealer_points + dealer_hand[1][2]
        player_hand[1] = draw_card(card_deck)
        player_points = player_points + player_hand[1][2]
        player_hand[2] = draw_card(card_deck)
        player_points = player_points + player_hand[2][2]
        print("Dealer:")
        paint_card(dealer_hand[1][0], dealer_hand[1][1])
        print("You:")
        paint_card(player_hand[1][0], player_hand[1][1])
        paint_card(player_hand[2][0], player_hand[2][1])
        print(f"\nThe dealer has {dealer_points} points, and you have {player_points} points. What is your next move?")
      else:
        print("Please make a valid bet.")
        continue
main()
    
