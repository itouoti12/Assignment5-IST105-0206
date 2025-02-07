import sys
import random

vowels = "aeiouAEIOU"
birth = sys.argv[1]
word = sys.argv[2]

# The Python script performs the following tasks:
# Task 1: Number Puzzle
#   Check if the number is even or odd.
#   If the number is even, calculate its square root.
#   If the number is odd, calculate its cube.
# Task 2: Text Puzzle
#   Convert the text message to binary.
#   Count the number of vowels in the text.
# Task 3: Treasure Hunt
#   Generate a random number between 1 and 100.
#   Use a while loop to let the user guess the number (simulated in Python, not user input).
#   If the user guesses correctly within 5 attempts, they win the treasure!

print("<h3>Number Puzzle:</h3>")
num = int(birth)
if (num%2) == 0:
    result = num**0.5
    print(f"The number {num} is even. Its square root is {result}")
else:
    result = num**3
    print(f"The number {num} is odd. Its cube is {result}")


print("<h3>Text Puzzle:</h3>")
binaryWord = ''.join(format(ord(i),'08b') for i in word)
vowelsCount = sum(word.count(vowel) for vowel in vowels)

print(f"<div>- Binary: {binaryWord}</div>")
print(f"<div>- Vowel Count: {vowelsCount}</div>")


print("<h3>Tresure Hunt:</h3>")
attempts = 1
treasure = random.randrange(1,101)
print(f"<div>- The secret number is {treasure}</div>")
while attempts < 6:
    randnum = random.randrange(1,101)
    if randnum == treasure:
        # win the game
        print(f"<div>- Attempt {attempts}: {randnum}(Correct!)</div>")
        print(f"<div>- You found the treasure in {attempts} attempts!</div>")
        break
    elif randnum > treasure:
        #  lose the game
        print(f"<div>- Attempt {attempts}: {randnum}(Too high!)</div>")
    
    elif randnum < treasure:
        #  lose the game
        print(f"<div>- Attempt {attempts}: {randnum}(Too low!)</div>")
    attempts += 1
    


