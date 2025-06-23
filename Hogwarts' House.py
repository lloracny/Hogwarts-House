# Write code below 💖
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('Do you like Dawn or Dusk?')
print('1 for Dawn')
print('2 for Dusk')
q1 = int(input('Enter your answer (1 or 2): '))

if q1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Wrong Input")

print("\nWhen I’m dead, I want people to remember me as:")
print('1 for The Good')
print('2 for The Great')
print('3 for The Wise')
print('4 for The Bold')
q2 = int(input('Enter your answer (1 to 4): '))

if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print("Wrong Input")

print("\nWhich kind of instrument most pleases your ear?")
print('1 for The Violin')
print('2 for The Trumpet')
print('3 for The Piano')
print('4 for The Drum')
q3 = int(input('Enter your answer (1 to 4): '))

if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print("Wrong Input")

print('-----------------------------------')
print(" FINAL SCORES ")
print('-----------------------------------')
print(f"Slytherin points: {slytherin}")
print(f"Hufflepuff points: {hufflepuff}")
print(f"Ravenclaw points: {ravenclaw}")
print(f"Gryffindor points: {gryffindor}")

print('-----------------------------------')

if slytherin > hufflepuff and slytherin > ravenclaw and slytherin > gryffindor:
  print("You are from Slytherin!")
elif hufflepuff > slytherin and hufflepuff > ravenclaw and hufflepuff > gryffindor:
  print("You are from Hufflepuff!")
elif ravenclaw > hufflepuff and ravenclaw > slytherin and ravenclaw > gryffindor:
  print("You are from Ravenclaw!")
elif gryffindor > hufflepuff and gryffindor > slytherin and gryffindor > ravenclaw:
  print("You are from Gryffindor!")