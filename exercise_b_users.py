

users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Edinbrugh",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  },
  "Oscar": {
    "twitter": "catstuff",
    "lottery_numbers": [45, 2, 55, 13, 47, 1],
    "home_town": "Uddingston",
    "pets": "None"
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
monty_species = users["Avril"]["pets"][0]["species"]

# 5. Get the smallest of Erik's lottery numbers
erik_lotto_num = users["Erik"]["lottery_numbers"]
print(min(erik_lotto_num))

# 6. Return an list of Avril's lottery numbers that are even
avril_lotto_num = users["Avril"]["lottery_numbers"]
even_num = []
for number in avril_lotto_num:
  if number % 2 == 0: #1 instead of 0 for odd numbers
    even_num.append(number)

print(even_num)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
numbers = users["Erik"]["lottery_numbers"]
numbers.append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]['home_town'] = 'Edinburgh'

# 9. Add a pet dog to Erik called "fluffy"
eriks_pets = users["Erik"]["pets"] #list
new_pet = {"name": "Fluffy", "Species": "Dog"}
eriks_pets.append(new_pet)

# 10. Add another person to the users dictionary
users["Randolph"] = {

}