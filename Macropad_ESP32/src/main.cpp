#include <Arduino.h>

int gpio_Pins[12] = {};

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i<12; i++){
    pinMode(gpio_Pins[i], INPUT_PULLUP);
  }

  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.write(0x00);
}