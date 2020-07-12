 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Sub-Lieutenant's rank badge                    //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


// SL


#include "rank22_o.inc";

#declare P_SL =
union
{          
  object { P_panel }
  object { P_box11 texture { T_rankblue } translate <0,10,0> }
  object { P_box12 texture { T_rankblue } translate <0,10,0> }
  object { P_box21 texture { T_rankblue } translate <0,10,0> }
  object { P_box22 texture { T_rankred } translate <0,10,0> }
  scale 0.05175
}

object { P_SL rotate rankrotate translate ranktranslate }   


