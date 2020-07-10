 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Captain's rank badge                           //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


// CPT


#include "rank23_o.inc";

#declare P_CPT =
union
{
  object { P_panel }
  object { P_box11 texture { T_rankblue } translate <0,10,0> }
  object { P_box12 texture { T_rankblue } translate <0,10,0> }
  object { P_box13 texture { T_rankblue } translate <0,10,0> }
  object { P_box21 texture { T_rankred } translate <0,10,0> }
  object { P_box22 texture { T_rankred } translate <0,10,0> }
  object { P_box23 texture { T_rankred } translate <0,10,0> }
  scale 0.05175
}

object { P_CPT rotate rankrotate translate ranktranslate }   




