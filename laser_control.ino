#include<Servo.h>

Servo serX;
Servo serY;

String serialData;

void setup() {
  serX.attach(10);
  serY.attach(11);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  //Loop function is required, for some reason...?
}

void serialEvent() {
  serialData = Serial.readString();

  //Switched them around because it wasn't working right...whoops
  serY.write(parseDataX(serialData));
  serX.write(parseDataY(serialData));
}

//Getting data in format X{x}Y{y}
int parseDataX(String data) {
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();  
}

int parseDataY(String data) {
  data.remove(0, data.indexOf("Y") + 1);

  return data.toInt();
}
