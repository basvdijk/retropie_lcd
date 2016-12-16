#!/usr/bin/python
from lcd_display import lcd
import sys

title = "BANY ARCADE"

def checkers():
	lcd.clear;

	for i in range(0,5):
	
		lcd.display_string("* * * * * * * * * *", 1);
		lcd.display_string(" * * * * * * * * * ", 2);
		lcd.display_string("* * * * * * * * * *", 3);
		lcd.display_string(" * * * * * * * * * ", 4);

		lcd.display_string("* * * * * * * * * *", 2);
		lcd.display_string(" * * * * * * * * * ", 3);
		lcd.display_string("* * * * * * * * * *", 4);
		lcd.display_string(" * * * * * * * * * ", 1);

def screen_game():

	system = sys.argv[1]
	emulator = sys.argv[2]
	rom = sys.argv[3].split('/')[-1].replace('.rom', '').replace('.zip', '')

	lcd.display_string(title,1)
	lcd.display_string(rom,2)
	lcd.display_string(system,3)
	lcd.display_string(emulator,4)


def screen_home():
	lcd.clear

	i=0
	bar=''
	for i in range(0,20):
		bar=bar+unichr(255)
		lcd.display_string(bar,1)
		i += 1	


	lcd.display_string(title,1)
	lcd.display_string("",2)
	lcd.display_string("CHOOSE A GAME",3)
	lcd.display_string("",4)


	
lcd = lcd()

if (len(sys.argv) > 1):
	screen_game()
else:
	screen_home()
