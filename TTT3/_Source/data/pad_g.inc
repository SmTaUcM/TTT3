 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Right shoulder (without braids)                //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "pad_o.inc";

#declare P_pad =
union
{
  object { P_shoulder_right }
  object { P_trim_right }
  object { P_pad_right }
}
