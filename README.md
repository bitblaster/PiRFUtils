# PiRFUtils
Various Raspberry PI RF Utilities

SniffAndPlay.py 
	It's a smart sniffer for most standard 433Mhz remote controls. It is one of the Python examples of the PIGPIO library.
	Launched without parameters it recognizes and logs: received code, initial sync-gap, "0" duration, "1" duration.
	Passing a code as command line argument, it will send it out (using sync-gap and duration currently hard-coded).
	Usage: python SniffAndPlay.py [code to send]

ReceiveRF.c
	It's a simple sniffer written by me. It outputs the received waveform to the command-line-specified file, in the following CSV format:
		microseconds_from_launch;input_value
	Rows are written only when input changes, so the output file is tipically tiny.
	Usage: ReceiveRF output.csv

ReceiveRF.py
	Programma analogo a ReceiveRF.c ma scritto in Python con WiringPi, quindi ha una minore accuratezza sui dati campionati
	Uso: python ReceiveRF.py output.csv
	
SendRF.c
	It's a transmitter of signals captured by ReceiveRF.c and ReceiveRF.py.
	Usage: SendRF input.csv N_repetitions

Plot.py
	Allows to display signals captured by ReceiveRF.c and ReceiveRF.py as a navigable graph.
	Can be used only on GUI-provided machines!
	Uso: python Plot.py input.csv
	
RebaseAndDuplicate.py
	Allows to process signals captured by ReceiveRF.c and ReceiveRF.py, shifting the samples time such as the first sample always start to time 0.
	It can also duplicate the signal if the last parameter is specified.
	Usage: python RebaseAndDuplicate.py input.csv output.csv [N_repetitions]
