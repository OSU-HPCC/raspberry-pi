#include<iostream>
#include<fstream>
#include "fractalEngine.h"

using namespace std;

struct point;
int halfWayPoint(point, point);

int main(int argc, char *argv[]){
  
  point p1 = argv[0], p2 = argv[1], p3 = argv[2], seed = argv[3];
  int iterations = argv[4];
  point plot[iterations];
  
  srand(time(NULL));			//Seed random variable.
  int dice;				//Variable for random numbers.
  point pos = seed;			//First step of iteration.

  for(int i; i < iterations; i++){
    dice = rand() % 6;			//Imitate a dice roll.
    switch(dice) {			//Plot fractal points.
      case 0 :
      case 1 : pos = halfWayPoint(p1, pos);
               plot[i] = pos;
               break;
      case 2 :
      case 3 : pos = halfWayPoint(p2, pos);
               plot[i] = pos;
               break;
      case 4 :
      case 5 : pos = halfWayPoint(p3, pos);
               plot[i] = pos;
               break;
    }
  }

  ofstream plotFile;
  plotFile.open("fractalpoints.txt");
  for(int j; j < iterations; j++){
    plotFile << "(" << plot[j].x << ", " << plot[j].y << ")\n";
  }
  plotFile.close();
  

  return 0;

}
