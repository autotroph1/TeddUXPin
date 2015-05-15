#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
// build with cc -o myprog myprog.c -lwiringPi -lpthread
#define M1PWM   12
#define M2PWM   13
#define M1PH    5
#define M2PH    6

#define PWMSPEED 200

int main ( int argc, char *argv[] )
{

if ( argc != 3 ) /* argc should be 2 for correct execution */
    {
        /* We print argv[0] assuming it is the program name */
        printf( "usage: %s motor-nume[1/2] left/right[1/0]", argv[0] );
    }
    //setup GPIO
    if (wiringPiSetupGpio() < 0)
    {   
        printf("error setting up wiring pi");
        return 1; // setup wiring Pi
    }
    //setup PWM I/Os
    pinMode(M1PWM, OUTPUT);
    pinMode(M2PWM, OUTPUT);
    pinMode(M1PH, OUTPUT);
    pinMode(M2PH, OUTPUT);
    digitalWrite(M1PWM, LOW);
    digitalWrite(M2PWM, LOW);
    digitalWrite(M1PH, LOW);
    digitalWrite(M2PH, LOW);

    //Create PWM for the PWM lines
    softPwmCreate(M1PWM, 0, PWMSPEED);
    softPwmCreate(M2PWM, 0, PWMSPEED);
    softPwmWrite(M1PWM, 90);
    softPwmWrite(M2PWM, 90);

    if (atol(argv[1]) == 1) // motor 1
    {
        if (atol(argv[2]) == 1)
        {
            digitalWrite(M1PH, HIGH);
            printf ("m1 high");
        }
        else
        {
            digitalWrite(M1PH, LOW);
            printf("m1 low");
        }
    }
    else if (atoi(argv[1]) == 2)
    {
        if (atoi(argv[2]) == 1)
        {
            printf ("m2 hih");
            digitalWrite(M2PH, HIGH);
        }
        else
        {
            printf ("m2 low");
            digitalWrite(M2PH, LOW);
        }
    }

    delay (1000); 
    softPwmWrite(M1PWM,0);
    softPwmWrite(M2PWM,0);
//digitalWrite(M1PWM,HIGH);
//  digitalWrite(M2PWM,HIGH);
  digitalWrite(M1PH,LOW);
  digitalWrite(M2PH,LOW);
    return 0;
}
