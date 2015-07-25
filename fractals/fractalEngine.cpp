#include<iostream>
#include<fstream>
#include "fractalheader.h"

using namespace std;

struct point;
int halfWayPoint(point, point);

int main(int argc, char *argv[]){
  
  point p1, p2, p3, seed;
  int iterations = argv[8];
  point plot[iterations];

  p1.x = argv[0]; p1.y = argv[1];
  p2.x = argv[2]; p2.y = argv[3];
  p3.x = argv[4]; p3.y = argv[5];
  seed.x = argv[6] ; seed.y = argv[7];

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
