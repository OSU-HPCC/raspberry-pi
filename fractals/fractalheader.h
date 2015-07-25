#ifndef FRACTALSTUFF
#define FRACTALSTUFF

struct point{
  double x;
  double y;
};



int halfWayPoint(point p1, point p2){

  point meetIntheMiddle;
  meetIntheMiddle.x = max(p1.x, p2.x) - abs(p1.x - p2.x)/(2);
  meetIntheMiddle.y = max(p1.y, p2.y) - abs(p1.y - p2.y)/(2);

  return meetIntheMiddle;

}

#endif
