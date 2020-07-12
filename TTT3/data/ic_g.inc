 ////////////////////////////////////////////////////
//                                                 //
//  Imperial Cross                                 //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "one_neck_o.inc";

#declare P_ic_cloth = object { P_cloth texture { T_ic_cloth } }
#declare P_ic_rings = object { P_rings texture { T_gold } }


#include "ic_o.inc";

#declare P_ic_base =
union
{
  object { P_ic_gold }
  object { P_ic_blue }
  object { P_ic_green } 
}  

#declare P_ic =
union
{
  object { P_ic_rings }
  object { P_ic_cloth }
  object { P_ic_base rotate <50.365,0,0> translate <0,-98.836,275.902> }
}  


object { P_ic }
