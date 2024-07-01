from time import sleep

string:str = "Hello, world! I am appearing right now."

def typewriter(string:str,interval:float=0.025) -> None:
	for char in string: print(char,end="",flush=True); sleep(interval)

typewriter(string)
