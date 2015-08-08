#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstring>
#include "fractalheader.h"

using namespace std;

int main(int argc, char *argv[]){

  char *firstx, *firsty, *secondx, *secondy, *thirdx, *thirdy, *origx, *origy;
  char *specIter;
  char *pointIndicator;

  if(argc != 21){			//Check for the right number of arguments.
    cout << "Incorrect number of arguments.\n";
    return 1;
  }
  for(int i = 1; i < argc; i++){			//Read in arguments from user.
    if(i + 1 != argc){				//Check for remaining arguments.
      if(std::string(argv[i]) ==  "-fx"){			//First x-coordinate.
        firstx = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-fy"){		//First y-coordinate.
        firsty = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-sx"){		//Second x-coordinate.
        secondx = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-sy"){		//Second y-coordinate.
        secondy = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-tx"){		//Third x-coordinate.
        thirdx = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-ty"){		//Third y-coordinate.
        thirdy = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-ox"){		//Original x-coordinate.
        origx = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-oy"){		//Original y-coordinate.
        origy = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-i"){		//Number of iterations.
        specIter = argv[i+1];
        i++;
      }
      else if(std::string(argv[i]) == "-p"){		//Indicates whether or not computer generates random steps.
        pointIndicator = argv[i+1];
        i++;
      }
      else{
        cout << "Invalid arguments.\n";
        return 1;
      }
    }
  }
  
  point p1, p2, p3, seed;
  int iterations = (int)getMyNum(specIter);
  int movetoPoint = (int)getMyNum(pointIndicator);
  point plot[iterations];

  p1.x = getMyNum(firstx); p1.y = getMyNum(firsty);
  p2.x = getMyNum(secondx); p2.y = getMyNum(secondy);
  p3.x = getMyNum(thirdx); p3.y = getMyNum(thirdy);
  seed.x = getMyNum(origx); seed.y = getMyNum(origy);

  srand(time(NULL));			//Seed random variable.
  int dice;				//Variable for random numbers.
  point pos = seed;			//First step of iteration.

  for(int i = 0; i < iterations; i++){
    if(movetoPoint == 0){		//Let computer select random path.
      dice = rand() % 6;		//Imitate a dice roll.
    }
    else if (movetoPoint == 1){
      dice = 1;
    }
    else if (movetoPoint == 2){
      dice = 3;
    }
    else if (movetoPoint == 3){
      dice = 5;
    }
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

/*
  for(int j = 0; j < iterations; j++){
    cout << "(" << plot[j].x << ", " << plot[j].y << ")\n";
}
*/

  return 0;

}
