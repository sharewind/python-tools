# -*- coding: utf-8 -*-
__author__ = 'Caijanfeng'

def show_max_factor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' % (num, count)
            break
        count -= 1
    else:
        print num, ' is prime'

if __name__ =="__main__":
    for i in xrange(20):
        show_max_factor(i)
    else:
        print 'now i = ',i