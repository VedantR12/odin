#include <Wire.h>
#include <U8g2lib.h>

U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0);

String emotion = "idle";

void drawIdle() {

  u8g2.clearBuffer();

  u8g2.drawBox(30, 22, 20, 20);
  u8g2.drawBox(78, 22, 20, 20);

  u8g2.sendBuffer();
}

void drawHappy() {

  u8g2.clearBuffer();

  // left eye
  u8g2.drawLine(30, 35, 40, 25);
  u8g2.drawLine(40, 25, 50, 35);

  // right eye
  u8g2.drawLine(78, 35, 88, 25);
  u8g2.drawLine(88, 25, 98, 35);

  u8g2.sendBuffer();
}

void drawThinking() {

  u8g2.clearBuffer();

  // left eye
  u8g2.drawDisc(40, 32, 5);

  // right eye
  u8g2.drawDisc(88, 32, 5);

  u8g2.drawCircle(40, 32, 10);
  u8g2.drawCircle(88, 32, 10);

  u8g2.sendBuffer();
}

void drawListening() {

  u8g2.clearBuffer();

  u8g2.drawFrame(25, 18, 30, 30);
  u8g2.drawFrame(73, 18, 30, 30);

  u8g2.sendBuffer();
}

void drawTalking() {

  u8g2.clearBuffer();

  // left eye
  u8g2.drawBox(30, 18, 20, 28);

  // right eye
  u8g2.drawBox(78, 18, 20, 28);

  u8g2.sendBuffer();
}

void drawSleepy() {

  u8g2.clearBuffer();

  u8g2.drawLine(30, 32, 50, 32);
  u8g2.drawLine(78, 32, 98, 32);

  u8g2.sendBuffer();
}

void setup() {

  Serial.begin(115200);

  u8g2.begin();
}

void loop() {

  // read laptop command
  if (Serial.available()) {

    emotion = Serial.readStringUntil('\n');

    emotion.trim();

    Serial.println("Emotion: " + emotion);
  }

  // render emotion
  if (emotion == "happy") {
    drawHappy();
  } else if (emotion == "thinking") {
    drawThinking();
  } else if (emotion == "sleepy") {
    drawSleepy();
  } else if (emotion == "talking") {
    drawTalking();
  } else if (emotion == "listening") {
    drawListening();
  } else {
    drawIdle();
  }

  delay(30);
}