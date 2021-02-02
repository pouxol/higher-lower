from art import logo
from art import vs

from game_data import data

from replit import clear
import random

lost = False
score = 0

while lost == False:
  clear()
  print(logo)

  if score == 0:
    dict_a = random.choice(data)
    name_a = dict_a.get("name")
    follower_a = dict_a.get("follower_count")
    desc_a = dict_a.get("description")
    country_a = dict_a.get("country")
    print(f"Compare A: {name_a}, a {desc_a} from {country_a}")
  else:
    print(f"You're right! Current score: {score}")
    dict_a = dict_b
    name_a = name_b
    follower_a = follower_b
    desc_a = desc_b
    country_a = country_b
    print(f"Compare A: {name_a}, a {desc_a} from {country_a}")

  print(vs)
  dict_b = random.choice(data)
  name_b = dict_b.get("name")
  follower_b = dict_b.get("follower_count")
  desc_b = dict_b.get("description")
  country_b = dict_b.get("country")
  print(f"Against B: {name_b}, a {desc_b} from {country_b}")

  bet = input("Who has more followers? Type 'A' or 'B': ")
  if follower_a > follower_b:
    higher = "A"
  elif follower_a < follower_b:
    higher = "B"

  if bet == higher:
    score += 1
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final Score: {score}")
    lost = True