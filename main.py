 #Names:  Ronn
#Date:  December 15, 2022
#Program Name:  SpeedTypeTest
#Purpose: Display the WPM depending on how quickly the user types a sentence

import curses
from curses import wrapper
import time
import random
# COLORS
light_blue = (168, 218, 220)



# the code for curses color pairs
ERROR_CODE = 1
CORRECT_CODE = 2
HIGHLIGHT_CODE = 3
PROMPT_CODE = 4


SENTENCES  = [
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



def init_color(stdscr):
	'''
	initialize the color pairs that will be used throughout the application
	'''
	stdscr.clear()

	# initating colors

	
	curses.init_color(2, 843,372,372) # ERROR COLOR CODE (RED)
	curses.init_pair(ERROR_CODE, 2, curses.COLOR_BLACK)

	curses.init_color(2, 372,843,686) # CORRECT COLOR CODE (AQUA)
	curses.init_pair(CORRECT_CODE, 2, curses.COLOR_BLACK)
	
	curses.init_color(4, 843,843,1000) # PROMPT COLOR CODE (LIGHT PURPLE)
	curses.init_pair(PROMPT_CODE, 4, curses.COLOR_BLACK)

	curses.init_color(4, 843,686,372) # HIGHLIGHT COLOR CODE (GOLDEN)
	curses.init_pair(HIGHLIGHT_CODE, 4, curses.COLOR_BLACK)
	stdscr.addstr("HELLO", curses.color_pair(HIGHLIGHT_CODE) | curses.A_BOLD)



def prompt_input(stdscr):

	'''
	prompt the user for the number of sentences to be typed
	args:
			stdscr: the standard screen
	return:
			number of sentences to type
	'''

	usr_input = ""
	while True:
		stdscr.addstr(0, 0, f"Please enter the # of sentences to type:\n",
									curses.color_pair(PROMPT_CODE) | curses.A_BOLD)
		stdscr.move(1, len(usr_input))
		c = stdscr.getch()
	
		if c == 10: # if user presses enter break
			break

		elif c == 127: # if user presses backspace
			usr_input = usr_input[:-1]
		elif 48 <= c <= 57: 
			usr_input += chr(c)
			# input must not exceed 50
			if int(usr_input) > 50:
				usr_input = usr_input[:-1]

		stdscr.clear()
		stdscr.addstr(1, 0, usr_input)

	return int(usr_input)



    
def get_random_sentences(amount):
    result = list()
    added = set()
    for _ in range(amount):
        rand_idx = random.randint(0, len(SENTENCES) - 1)
        while rand_idx in added:
            rand_idx = random.randint(0, len(SENTENCES) - 1)
        result.append(SENTENCES[rand_idx])
        added.add(rand_idx)
    return result



		
def typing_test(stdscr) -> None:
	''' 
	main function
	'''
	init_color(stdscr)
	stdscr.clear()
	curses.noecho()


	''' start the typing test '''

	start_time = time.time()
	total_words = 0
	words_typed = 0
	wrong_words = 0
	wpm = 0
  
	num_of_sentences = prompt_input(stdscr)
	sentences = get_random_sentences(num_of_sentences)

	curses.echo()
	for i in range(len(sentences)):
		user_sentence = ""
		sentence = sentences[i]
		total_words += len(sentence.split())
		time.sleep(2)
		
		centralize_text(stdscr, sentence)


		stdscr.refresh()
		while True:
			# show the remaining sentences and the current wpm
			stdscr.move(0, 0)
			# print the target sentence
			x, y = centralize_text(stdscr, sentence)

			# print the user sentence on top of the target sentence
			stdscr.move(x, y)
		
			for j in range(len(user_sentence)):
				color = curses.color_pair(CORRECT_CODE)
				if j >= len(sentence) or user_sentence[j] != sentence[j]:
					color = curses.color_pair(ERROR_CODE)

				stdscr.addstr(user_sentence[j], color)
				time.sleep(2)

				stdscr.addstr(1,1, "HELLO")



def centralize_text(stdscr, text:str, color:int=1):
    '''
		centers text
    '''
    sc_height, sc_width = stdscr.getmaxyx()

    x = sc_height // 2
    y = (sc_width // 2 - len(text) // 2) if (len(text) < sc_width) else 0

    stdscr.addstr(x, y, text, color)
    return (x, y)

def mainloop():
	try:
		while True:
			wrapper(typing_test)
	except KeyboardInterrupt:
			print("Program has ended due to key board interupt")





if __name__ == "__main__":
	mainloop()

	

