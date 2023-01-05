#Names:  Ronn
#Date:  December 15, 2022
#Program Name:  SpeedTypeTest
#Purpose: Display the WPM depending on how quickly the user types a sentence


import random
import time


sentences  = [
	"The anaconda was the greatest criminal mastermind in this part of the neighborhood.",
	"I am my aunt's sister's daughter.",
	"There was no ice cream in the freezer, nor did they have money to go to the store.",
	"If you don't like toenails, you probably shouldn't look at your feet.",
	"She can live her life however she wants as long as she listens to what I have to say.",
	"Going from child, to childish, to childlike is only a matter of time.",
	"The old apple revels in its authority.",
	"He poured rocks in the dungeon of his mind.",
	"He barked orders at his daughters but they just stared back with amusement.",
	"You can't compare apples and oranges, but what about bananas and plantains?",
	"He decided to fake his disappearance to avoid jail.",
	"The external scars tell only part of the story.",
	"The best key lime pie is still up for debate.",
	"I only enjoy window shopping when the windows are transparent.",
	"Don't step on the broken glass.",
	"Don't piss in my garden and tell me you're trying to help my plants grow.",
	"He felt that dining on the bridge brought romance to his relationship with his cat.",
	"I'm not a party animal, but I do like animal parties.",
	"She says she has the ability to hear the soundtrack of your life.",
	"To the surprise of everyone, the Rapture happened yesterday but it didn't quite go as expected."
]


# Initialize variables to keep track of errors and typed text
errors = 0
total_words = 0

num_of_sentences = input("Please enter the # of sentences to type: ")

# start the timer
start_time = time.time()


for sentence in range(int(num_of_sentences)):
	SENTENCE = random.choice(sentences)
	# Print the sentence to the console
	print(SENTENCE)

	# Get the user's input
	typed_text = input()

	# Check for errors
	if typed_text != SENTENCE:
			errors += 1

	# Count the number of words typed
	total_words += len(typed_text.split())


# Stop the timer and calculate the WPM
end_time = time.time()
elapsed_time = end_time - start_time
wpm = total_words / elapsed_time * 60

# Print the WPM and error count
print(f'WPM: {int(wpm)}')
print(f'Errors: {errors}')