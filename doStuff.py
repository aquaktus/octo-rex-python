import string, random
import time
from time import sleep

while (True):
	sentence = ''
	for i in range(random.randint(0,9)):
		sentence += ' ' + ''.join(random.choice(string.ascii_lowercase) for _ in xrange(random.randint(4,17)))
	
	print sentence
	sleep (random.randint(0,700)/1000.0)
