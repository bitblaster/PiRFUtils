/*
 * blink.c:
 *      blinks the first LED
 *      Gordon Henderson, projects@drogon.net
 */
 
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
 
#define PIN 2
#define MAX_SAMPLES 100000

int main ( int argc, char *argv[] )
{
	printf ("Raspberry Pi Send RF\n") ;
 
	FILE* stream = fopen(argv[1], "r");

	int delays[MAX_SAMPLES];
	int samples[MAX_SAMPLES];
	
	int ret;
	int count=0;
	while((ret = fscanf(stream,"%d;%d", &delays[count], &samples[count])) != EOF) {
		count++;
	}
	fclose(stream);
	
	printf("%d\n", count);
	for(int i=0; i<10; i++)
		printf("%d,%d\n", delays[i], samples[i]);
		
	if (wiringPiSetup () == -1)
		return 1 ;

	pinMode (PIN, OUTPUT) ;         // aka BCM_GPIO pin 17

	int repeat = atoi(argv[2]);
	float lastTime=delays[0];
	for(int j=0; j<repeat; j++) {
		for(int i=0; i<count; i++) {
			delayMicroseconds(delays[i]-lastTime);
			digitalWrite (PIN, samples[i]);
			lastTime=delays[i];
		}
	}
	
	return 0;
}
