 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Right shoulder with one braid                  //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "pad_braid_o.inc";


#declare P_pad =
union
{
  object { P_shoulder_right }
  object { P_trim_right }
  object { P_pad_right }
  object { P_braid_short }
}
