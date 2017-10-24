import matplotlib as mpl
mpl.use('Agg')
from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO
import sys

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 5
RECEIVE_PIN = 22

if __name__ == '__main__':
    fileName = sys.argv[1];
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    cumulative_time = 0
    beginning_time = datetime.now()
    print '**Started recording**'
    while cumulative_time < MAX_DURATION:
        time_delta = datetime.now() - beginning_time
        RECEIVED_SIGNAL[0].append(time_delta)
        RECEIVED_SIGNAL[1].append(GPIO.input(RECEIVE_PIN))
        cumulative_time = time_delta.seconds
    print '**Ended recording**'
    print len(RECEIVED_SIGNAL[0]), 'samples recorded'
    GPIO.cleanup()

    print '**Processing results**'
    for i in range(len(RECEIVED_SIGNAL[0])):
        RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i].seconds*1000000 + RECEIVED_SIGNAL[0][i].microseconds

    print '**Writing results**'
    #pyplot.plot(RECEIVED_SIGNAL[0], RECEIVED_SIGNAL[1])
    #pyplot.axis([0, MAX_DURATION, -1, 2])
    #pyplot.savefig("rf_sniff.png", dpi=1200)
    lastValue=0
    with open(fileName, 'w') as out:
        for i in range(len(RECEIVED_SIGNAL[0])):
            if RECEIVED_SIGNAL[1][i] != lastValue:
                out.write("%d;%d\n" % (RECEIVED_SIGNAL[0][i], lastValue))
                out.write("%d;%d\n" % (RECEIVED_SIGNAL[0][i]+1, RECEIVED_SIGNAL[1][i]))
                lastValue = RECEIVED_SIGNAL[1][i]

