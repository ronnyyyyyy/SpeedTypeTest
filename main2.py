

import random
import time
import colors as c
from tabulate import tabulate
import sqlite3


# connect to a database
conn = sqlite3.connect('typing_data.db')

# create a cursor
cu = conn.cursor()

# create a table
cu.execute("""CREATE TABLE typing_data (
		WPM text,
		Errors text,
		Accuracy text
	)""")

# typing_data Team data
typing_data = []

# inserting values on the typing database
cu.executemany("INSERT INTO typing_data VALUES (?,?)",typing_data)

# grabbing all the values from databsae
items = cu.fetchall()
table = items


"""
Function adds a record, ensures no duplicate student number
inputs:array database
outputs:array database
"""
def add(WPM,Errors,):

	
	# create a cursor
	cu = conn.cursor()
	cu.execute("SELECT * FROM typing_data")

	# appending values (first second,jersey_no into table)
	cu.execute("INSERT INTO typing_data VALUES (?,?)", (WPM,Errors))

	
def display():
	# selecting all items from database
	cu.execute("SELECT * FROM typing_data")
	
	items = cu.fetchall()
	
	table = items
	
	# formatting data into simple table
	f_table = tabulate(table, headers=['WPM', 'Errors'], tablefmt='psql')
	print(f_table)
	


def prompt_replay():
	'''
	prompt if user wants to replay, if not then quit immediately
	'''
	while True:
		response = input("Do you want to replay? (Y/N): ")

		if response == "Y" or response == "y":
				return
		elif response == "N" or response == "n":
				exit(0)
		else:
			print(f"{c.Red+c.bold}***INVALID*** {c.reset}enter either '{c.green}Y' {c.reset}or '{c.green}N' {c.reset}")
			print("\n")
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




while True:
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
	wpm = int(total_words / elapsed_time * 60)
	
	# Print the WPM and error count
	print(f'WPM: {wpm}')
	print(f'Errors: {errors}')
	
	
	add(wpm,errors)
	display()
	prompt_replay()