"""Write a function called bisection that takes in a list and a value and returns the index in the list of where that value appears or None if it does not appear"""
import math
class bisection:
    def __init__(self, list):
        self.list = sorted(list)

    def bisect(self, value):
        lower = 0
        upper = len(self.list)
        middle = (upper - lower)/2
        while (lower <= upper):
            print lower, middle, upper
            middleVal = self.list[middle]
            print "middleVal", middleVal
            if middleVal == value:
                return middle
            if value < middleVal:
                upper = middle
                middle = (upper - lower)/2 + lower
            if (value >= middleVal):
                lower = middle
                middle = (upper - lower)/2 + lower
        return -1

def main(script, *args):
    l1 = [2,3,4,5,9,11]
    bis = bisection(l1)
    bis.bisect(11)
    # print bis.bisection(0,len(l1)-1,l1,9)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
