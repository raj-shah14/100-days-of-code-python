from art import logo, vs
from game_data import data
import random

print(logo)

def get_profile(id):
    profile = data[id]
    return profile

score = 0
correct = True

while correct:
  print(f"Score: {score}")
  a, b = random.sample(range(0, len(data)-1), 2)
  profile_a, profile_b  = get_profile(a), get_profile(b)
  print(f"Option A: {profile_a["name"]}, {profile_a["description"]}, {profile_a["country"]}")
  a_followers, b_followers = profile_a["follower_count"], profile_b["follower_count"]
  correct_answer = "A" if (a_followers > b_followers) else "B"
  print(vs)
  print(f"Option B: {profile_b["name"]}, {profile_b["description"]}, {profile_b["country"]}")

  user_input = input("Who has more followers on Instagram?\n")
  if user_input == correct_answer:
      score += 1
  else:
      print(f"Your final Score: {score}")
      score = 0
      correct = False
