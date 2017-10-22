/*
 * blink.c:
 *      blinks the first LED
 *      Gordon Henderson, projects@drogon.net
 */
 
#include <stdio.h>
#include <wiringPi.h>
#include <sys/time.h>

#define PIN 3
#define MAX_SAMPLES 1000000
#define MAX_T_SAMPLES 30000000

int main ( int argc, char *argv[] )
{
	printf ("Raspberry Pi RF sniffer\n");
 
	int delays[MAX_SAMPLES];
	int samples[MAX_SAMPLES];
	
	if (wiringPiSetup () == -1)
		return 1 ;

	pinMode (PIN, INPUT) ;         // aka BCM_GPIO pin 17

	printf("**Started recording**\n");

	struct timeval currentTime, startTime;
	gettimeofday(&startTime,NULL);
	int val, lastVal=0, count=0;
	for(int i=0; i<MAX_T_SAMPLES; i++) {
		val = digitalRead(PIN);
		if(val != lastVal) {
			gettimeofday(&currentTime,NULL);
			delays[count] = 1000000 * (currentTime.tv_sec - startTime.tv_sec) + (currentTime.tv_usec - startTime.tv_usec);
			samples[count] = val;
			lastVal = val;
			count++;
		}
	}
    printf("**Ended recording**\n");

    printf("**Writing results**\n");
	FILE* stream = fopen(argv[1], "w");

	for(int i=0; i<count; i++) {
		fprintf(stream, "%06d;%d\n", delays[i], !samples[i]);
		fprintf(stream, "%06d;%d\n", delays[i]+1, samples[i]);
	}
	
	fclose(stream);
	
	return 0;
}
