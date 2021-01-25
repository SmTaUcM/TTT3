 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Right shoulder with two braids                 //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "pad_braids_o.inc";


#declare P_pad =
union
{
  object { P_shoulder_right }
  object { P_trim_right }
  object { P_pad_right }
  object { P_braid_short }
  object { P_braid_long }
}
