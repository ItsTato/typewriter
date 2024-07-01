from time import sleep
from numpy import linspace
from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits

random_chars = ascii_lowercase+ascii_uppercase+digits

def _intervaled(string:str,interval:float=0.025) -> None:
	for char in string:
		print(char,end="",flush=True)
		sleep(interval)
	print()

def _multivaled(string:str,lowest_interval:float=0.005,highest_interval:float=0.05) -> None:
	intervals:list[float] = linspace(lowest_interval,highest_interval,int((highest_interval-lowest_interval)*1000)+1).tolist()
	for char in string:
		print(char,end="",flush=True)
		sleep(choice(intervals))
	print()