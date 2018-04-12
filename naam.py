import random

NAMES = ['Stephen', 'Daan', 'Kees']

def get_name():
	return random.choice(NAMES)
print("Hallo, ik ben {naam}".format(naam=get_name()))