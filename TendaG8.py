#!/usr/bin/env python

import time
import pigpio

class TendaG8():
    """
    A class to drive courtains made by G8 Motori through wireless codes on 433 MHz
    """
    def __init__(self, pi, gpio):
        self.pi = pi
        self.gpio = gpio
        self.bits = 40
        self.repeats = 3

        self._make_waves()

        pi.set_mode(gpio, pigpio.OUTPUT)

    def _make_waves(self):
        """
        Generates the basic waveforms needed to transmit codes.
        """
        wf = []
        wf.append(pigpio.pulse(1<<self.gpio, 0, 4770))
        wf.append(pigpio.pulse(0, 1<<self.gpio, 1550))
        self.pi.wave_add_generic(wf)
        self.waveIdPreamble = self.pi.wave_create()

        wf = []
        wf.append(pigpio.pulse(1<<self.gpio, 0, 300))
        wf.append(pigpio.pulse(0, 1<<self.gpio, 775))
        self.pi.wave_add_generic(wf)
        self.waveId0 = self.pi.wave_create()

        wf = []
        wf.append(pigpio.pulse(1<<self.gpio, 0, 650))
        wf.append(pigpio.pulse(0, 1<<self.gpio, 425))
        self.pi.wave_add_generic(wf)
        self.waveId1 = self.pi.wave_create()

    def send(self, code):
        # Transmits the code        
        chain = [255, 0, self.waveIdPreamble]

        bit = (1<<(self.bits-1))
        for i in range(self.bits):
            if code & bit:
                chain += [self.waveId1]
            else:
                chain += [self.waveId0]
            bit = bit >> 1

        chain += [255, 1, self.repeats, 0]

        print "Invio catena"
        print chain
        
        self.pi.wave_chain(chain)

        while self.pi.wave_tx_busy():
            time.sleep(0.1)
    
    def cancel(self):
        """
        Cancels the wireless code transmitter.
        """
        self.pi.wave_delete(self.waveIdPreamble)
        self.pi.wave_delete(self.waveId0)
        self.pi.wave_delete(self.waveId1)

if __name__ == "__main__":
    import sys
    import time
    import pigpio
    import TendaG8

    TX_PIN=27

    pi = pigpio.pi() # Connect to local Pi.

    args = len(sys.argv)

    if args > 1:
        # If the script has arguments they are assumed to codes
        # to be transmitted.
        
        sender = TendaG8.TendaG8(pi, gpio=TX_PIN)

        print("sending {}".format(sys.argv[1]))
        sender.send(long(sys.argv[1], 16))

        sender.cancel() # Cancel the transmitter.

    pi.stop() # Disconnect from local Pi.
