 ////////////////////////////////////////////////////
//                                                 //
//  Medal of Honor                                 //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "moh_o.inc"     


#declare P_moh_base =
union
{
  object { P_moh_gold }
  object { P_moh_white }
  object { P_moh_green }  
  object { P_moh_silver }  
}

#declare P_moh = object { P_moh_base rotate <88.6,-0.322,-21.705> translate <-151.914,-94.575,189.906> }  

object { P_moh }