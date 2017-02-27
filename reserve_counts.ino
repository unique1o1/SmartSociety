#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
//unsigned long currenttime;
char x;
char slot;
int no_of_slot;
int space=0;
//unsigned long futuretime=0;

void setup() {
  // put your setup code here, to run once:
            lcd.begin(16, 4);
            lcd.clear();
  pinMode(8, OUTPUT);
            Serial.begin(9600);

              }

void loop() {
  digitalWrite(8, HIGH);

      x= Serial.read();
            if(x=='r')
            {
              lcd.clear();
              lcd.print("Parking spots");
              lcd.setCursor(0,1);
              lcd.print("reserved are: ");
               no_of_slot=Serial.read();
               for(int i=0;i<no_of_slot;i++)
               { 
                lcd.setCursor(space,2);
                         lcd.noCursor();
                        slot=Serial.read();
                        
                          lcd.noCursor();
                          if(slot=='a'){
                            lcd.print(1);
                             space++;
                            lcd.print(0);
                            }
                          else{
                            lcd.print(slot);
                          }
                          
                          space++;
                          lcd.setCursor(space,2);
                          space++; 
                          lcd.print(",");
                          
                          lcd.noCursor();
               }
               space=0;
              
              
            }
            else if(x=='c'){
               lcd.clear();
              lcd.print("Parking spots");
              lcd.setCursor(0,1);
              lcd.print("reserved are: ");
              lcd.setCursor(0,2);
              lcd.print("NONE");
              
              }
          
            
            
            }

