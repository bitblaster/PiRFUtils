#!/usr/bin/python

from numpy import genfromtxt
import matplotlib as mpl
import matplotlib.pyplot as pyplot
import sys
import os

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 5
RECEIVE_PIN = 23

if __name__ == '__main__':

    RECEIVED_SIGNAL[0] = genfromtxt(sys.argv[1], dtype='f8', delimiter=";", usecols = (0))
    RECEIVED_SIGNAL[1] = genfromtxt(sys.argv[1], dtype='f8', delimiter=";", usecols = (1))

    print '**Processing results**'
    for i in range(len(RECEIVED_SIGNAL[0])):
        RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i]/1000000.0

    print '**Plotting results**'
    print str(RECEIVED_SIGNAL[0][0]) + "," + str(RECEIVED_SIGNAL[1][0])
    #pyplot.scatter(RECEIVED_SIGNAL[0],RECEIVED_SIGNAL[1])
    pyplot.title(os.path.basename(sys.argv[1]))
    pyplot.xlabel('time')
    pyplot.ylabel('value')
    pyplot.plot(RECEIVED_SIGNAL[0],RECEIVED_SIGNAL[1])
    pyplot.axis([0, MAX_DURATION, 0, 2])
    pyplot.show()
    #pyplot.savefig("rf_sniff.png", dpi=1200)
    
