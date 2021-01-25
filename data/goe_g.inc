 ////////////////////////////////////////////////////
//                                                 //
//  Grand Order of the Emperor                     //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "dagger_g.inc";


#include "one_neck_o.inc";

#declare P_goe_cloth = object { P_cloth texture { T_goe_cloth } }
#declare P_goe_rings = object { P_rings texture { T_silver } }


#include "goe_o.inc";

#declare P_goe =
union
{
  object { P_goe_rings }
  object { P_goe_cloth }
  object { P_goe_base rotate <50.465,0,0> translate <0,-95.824,279.751> }
}  
   
