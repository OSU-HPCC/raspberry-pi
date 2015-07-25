#include<iostream>
#include<fstream>
#include<cstdlib>
#include "fractalheader.h"

using namespace std;

int main(int argc, char *argv[]){

  char *firstx, *firsty, *secondx, *secondy, *thirdx, *thirdy, *origx, *origy;
  char *specIter;

  for(int i; i < argc; i++){			//Read in arguments from user.
    if(argc != 19){			//Check for the right number of arguments.
      cout << "Incorrect number of arguments.";
      return 1;
    }
    if(i + 1 != argc){				//Check for remaining arguments.
      if(argv[i] == "-fx"){			//First x-coordinate.
        firstx = argv[i+1];
      }
      else if(argv[i] == "-fy"){		//First y-coordinate.
        firsty = argv[i+1];
      }
      else if(argv[i] == "-sx"){		//Second x-coordinate.
        secondx = argv[i+1];
      }
      else if(argv[i] == "-sy"){		//Second y-coordinate.
        secondy = argv[i+1];
      }
      else if(argv[i] == "-tx"){		//Third x-coordinate.
        thirdx = argv[i+1];
      }
      else if(argv[i] == "-ty"){		//Third y-coordinate.
        thirdy = argv[i+1];
      }
      else if(argv[i] == "-ox"){		//Original x-coordinate.
        origx = argv[i+1];
      }
      else if(argv[i] == "-oy"){		//Original y-coordinate.
        origy = argv[i+1];
      }
      else if(argv[i] == "-i"){			//Number of iterations.
        specIter = argv[i+1];
      }
      else{
        cout << "Not enough or invalid arguments.";
        return 1;
      }
    }
  }
  
  point p1, p2, p3, seed;
  int iterations = (int)getMyNum(specIter);
  point plot[iterations];

  p1.x = getMyNum(firstx); p1.y = getMyNum(firsty);
  p2.x = getMyNum(secondx); p2.y = getMyNum(secondy);
  p3.x = getMyNum(thirdx); p3.y = getMyNum(thirdy);
  seed.x = getMyNum(origx) ; seed.y = getMyNum(origy);

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
