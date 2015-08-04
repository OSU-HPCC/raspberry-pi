#ifndef FRACTALHEADER_H
#define FRACTALHEADER_H 
#include<cmath>

struct point{
  double x;
  double y;
};



point halfWayPoint(point p1, point p2){

  point meetIntheMiddle;
  meetIntheMiddle.x = std::max(p1.x, p2.x) - std::abs(p1.x - p2.x)/(2);
  meetIntheMiddle.y = std::max(p1.y, p2.y) - std::abs(p1.y - p2.y)/(2);

  return meetIntheMiddle;

}

double getMyNum(char *input){
  
  int stringCount = 0;
  double finalNum = 0;
  int decimalPos = 0;
  int tensOrientation;
  bool decimal = false;
  bool negative = false;
  int startingChar = 0;

  if(input[0] == '-'){
    negative = true;
  }
  while((input[stringCount]) != '\0'){
    if((input[stringCount]) == '.'){
      decimal = true;
      decimalPos = stringCount;
    }
    stringCount++;    
  }
    if(decimal == true){
      tensOrientation = decimalPos;
    }
    else{
      tensOrientation = stringCount;
    }
    if(negative == true){
      startingChar = 1;
    }
    for(int i = startingChar; i <= stringCount; i++){
      if((input[i]) == '.'){
      }
      else if(negative == false){
        finalNum += (double) (input[i] - '0')*(double)pow(10, (tensOrientation - i - 1));
      }
      else{
        finalNum += (double) (input[i] - '0')*(double)pow(10, (tensOrientation - i - 2));
        finalNum = finalNum * -1;
      }
    }
  return finalNum;
  
}

#endif
