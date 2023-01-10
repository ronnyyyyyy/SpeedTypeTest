 #Names:  Ronn
#Date:  December 15, 2022
#Program Name:  SpeedTypeTest
#Purpose: Display the WPM depending on how quickly the user types a sentence

import curses
from curses import wrapper

# COLORS
light_blue = (168, 218, 220)



# the code for curses color pairs
ERROR_CODE = 1
CORRECT_CODE = 2
HIGHLIGHT_CODE = 3
PROMPT_CODE = 4


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



def init_color(stdscr):
	'''
	initialize the color pairs that will be used throughout the application
	'''
	stdscr.clear()

	# initating colors

	
	curses.init_color(2, 843,372,372) # ERROR COLOR CODE (RED)
	curses.init_pair(ERROR_CODE, 2, curses.COLOR_BLACK)
	stdscr.addstr("HELLO", curses.color_pair(ERROR_CODE) | curses.A_BOLD)

	curses.init_color(2, 372,843,686) # CORRECT COLOR CODE (AQUA)
	curses.init_pair(CORRECT_CODE, 2, curses.COLOR_BLACK)
	stdscr.addstr("HELLO", curses.color_pair(CORRECT_CODE) | curses.A_BOLD)
	
	curses.init_color(4, 843,843,1000) # PROMPT COLOR CODE (LIGHT PURPLE)
	curses.init_pair(PROMPT_CODE, 4, curses.COLOR_BLACK)
	stdscr.addstr("HELLO", curses.color_pair(ERROR_CODE) | curses.A_BOLD)

	curses.init_color(4, 843,686,372) # HIGHLIGHT COLOR CODE (GOLDEN)
	curses.init_pair(HIGHLIGHT_CODE, 4, curses.COLOR_BLACK)
	stdscr.addstr("HELLO", curses.color_pair(HIGHLIGHT_CODE) | curses.A_BOLD)


	
def main(stdscr):
	''' 
	main function
	'''
	stdscr.clear()
	curses.init_color(2, 843,686,372)
	curses.init_pair(ERROR_CODE, 2, curses.COLOR_BLACK)
	stdscr.addstr("HELLO", curses.color_pair(ERROR_CODE) | curses.A_BOLD)
	stdscr.refresh()
	stdscr.getch()


curses.wrapper(main)
