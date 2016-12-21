import sys
import math
import time


def println(x):
	sys.stdout.write('\r'+str(x))
    	sys.stdout.flush()


def bar(value, max, length=15, char="="):
	delta = math.floor((float(value)/float(max))*length)
	bar = "<"
	for i in range(1,length+1):
		if (i<=delta):
			bar = bar + char
		else:
			bar = bar + " "
	bar = bar + ">"
	return bar


def printSlow(text, halt=0.04):
	out = ""
	for i in text:
		out = out + i
		println(out)
		time.sleep(halt)
	print
