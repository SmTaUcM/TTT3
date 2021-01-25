 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Lieutenant's rank badge                        //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


// LT


#include "rank22_o.inc";

#declare P_LT =
union
{
  object { P_panel }
  object { P_box11 texture { T_rankblue } translate <0,10,0> }
  object { P_box12 texture { T_rankblue } translate <0,10,0> }
  object { P_box21 texture { T_rankred } translate <0,10,0> }
  object { P_box22 texture { T_rankred } translate <0,10,0> }
  scale 0.05175
}

object { P_LT rotate rankrotate translate ranktranslate }   




