def playorhome():
  z = input("Would you like to continue playing or take the amount and go home (play/go home) : ")
  if z == 'play':
    print("Then lets continue the game !")
  elif z == 'go home':
    print("Thank you for playing !")
    exit()

def lifelines():
  y = input("""You have three life lines:
  1. 50-50
  2. Ask the audience
  3. Ask an expert
  which life line would you like to use ? (1/2/3) : """)
  if y == '1':
    print("removing two wrong answers !")
    print
a = input("Enter your name : ")
print("WELCOME TO KAUN BANEGA CROREPATI !, MR.", a.upper(), "!")
print("You will be asked 5 questions. first question is of 1000 rupees, second is of 10,000 rupees and rest we will tell you as the game progresses.")
b = input("are you ready to play KAUN BANEGA CROREPATI ? (yes/no) : ")
if b == 'yes':
    print("Then lets start the game !")
else:
    print("Thank you for visiting !")
    exit()

print("The first question is on your screen !")
c = input("""
Q1. Who is known as the father of our nation ?\na) Mahatma Gandhi\nb) Jawaharlal Nehru\nc) Subhash Chandra Bose\nd) None
your answer: """)
if c == 'a':
    print("Congratulations ! You have won 1000 rupees !")
else:
  print("Sorry ! You have lost the game !")
  exit()
  
playorhome()

d = input("""Q.2 Which popular social media platform was founded by Mark Zuckerberg in 2004?
a) Twitter
b) Facebook
c) Instagram
d) LinkedIn
your answer: """)

if d == 'b':
  print("Congratulations ! You have won 10,000 rupees !")
else:
  print("Sorry ! You have lost the game !")
  exit()

playorhome()

e = input("""Q.3 Which planet is known as the Red Planet?
a) Mars
b) Venus
c) Jupiter
d) Saturn
your answer: """)
if e == 'a':
  print("Congratulations ! You have won 1,00,000 rupees !")
else:
  print("Sorry ! You have lost the game !")
  exit()

playorhome()

f = input("""Q.4 Which is the largest ocean on Earth?
a) Atlantic Ocean
b) Indian Ocean
c) Arctic Ocean
d) Pacific Ocean
your answer: """)
if f == 'd':
  print("Congratulations ! You have won 5,00,000 rupees !")
else: 
  print("Sorry ! You have lost the game !")

playorhome()

g = input("""Q.5 Which is the largest mammal in the world?
a) Elephant
b) Blue Whale
c) Giraffe
d) Lion
your answer: """)

if g == 'b':
  print("Congratulations ! You have won 1,00,00,000 rupees !")
else:
  print("Sorry ! You have lost the game !")
  exit()

print("Thank you for playing KAUN BANEGA CROREPATI !")