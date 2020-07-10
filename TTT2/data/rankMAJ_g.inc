 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Major's rank badge                             //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


// MAJ


#include "rank24_o.inc";

#declare P_MAJ =
union
{
  object { P_panel }
  object { P_box11 texture { T_rankblue } translate <0,10,0> }
  object { P_box12 texture { T_rankblue } translate <0,10,0> }
  object { P_box13 texture { T_rankblue } translate <0,10,0> }
  object { P_box14 texture { T_rankblue } translate <0,10,0> }
  object { P_box21 texture { T_rankblue } translate <0,10,0> }
  object { P_box22 texture { T_rankblue } translate <0,10,0> }
  object { P_box23 texture { T_rankblue } translate <0,10,0> }
  object { P_box24 texture { T_rankred } translate <0,10,0> }
  scale 0.05175
}

object { P_MAJ rotate rankrotate translate ranktranslate }   




