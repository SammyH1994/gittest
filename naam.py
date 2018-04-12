import random

NAMES = ['Stephen', 'Daan', 'Kees', 'Dennis', 'Gerard', 'Lisa']

def get_name():
	return random.choice(NAMES)
print("Hey, ik ben {naam}".format(naam=get_name()))