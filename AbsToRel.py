#!/usr/bin/python

from numpy import genfromtxt
import sys

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]

if __name__ == '__main__':

    RECEIVED_SIGNAL[0] = genfromtxt(sys.argv[1], dtype='f8', delimiter=";", usecols = (0))
    RECEIVED_SIGNAL[1] = genfromtxt(sys.argv[1], dtype='f8', delimiter=";", usecols = (1))

    lastSampleTime = RECEIVED_SIGNAL[0][0];
    print 'Processing samples...'
    for i in range(len(RECEIVED_SIGNAL[0])):
        currentSignal = RECEIVED_SIGNAL[0][i]
        RECEIVED_SIGNAL[0][i] = currentSignal - lastSampleTime
        lastSampleTime = currentSignal
    
    repetitions = 1
    if len(sys.argv) > 3:
        repetitions = int(sys.argv[3])
        
    with open(sys.argv[2], 'w') as out:
        for j in range(repetitions):
            for i in range(len(RECEIVED_SIGNAL[0])):
                out.write("%d;%d\n" % ((RECEIVED_SIGNAL[0][i] + j*RECEIVED_SIGNAL[0][-1]), RECEIVED_SIGNAL[1][i]))
    
