 ////////////////////////////////////////////////////
//                                                 //
//  Order of the Renegade                          //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "oor_o.inc"     


#declare P_oor_base =
union
{
  object { P_oor_gold }
  object { P_oor_blue }
  object { P_oor_green }  
}

#declare P_oor = object { P_oor_base rotate <93.09,1.337,-22.693> translate <-145.791,-94.901,128.626> }  

object { P_oor }
