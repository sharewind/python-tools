from timeit import timeit



def calc(end):
	s = 0
	for i in xrange(end):
		s = s + i
	print s


if __name__ =="__main__":
	#as a float measured in seconds.
    costtime = timeit("calc(100)", setup="from __main__ import calc", number =1) * 1000
    print costtime,"ms"
         