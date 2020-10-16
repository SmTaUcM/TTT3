 ////////////////////////////////////////////////////
//                                                 //
//  Imperial Cross and Grand Order of the Emperor  //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "dagger_g.inc";


#include "icgoe_neck_o.inc"


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
  object { P_ic_base rotate <58.301,3.914,-9.83> translate <-7.635,-101.603,278.866> }
}  


#include "goe_o.inc";

#declare P_goe =
union
{
  object { P_goe_rings }
  object { P_goe_cloth }
  object { P_goe_base rotate <51.347,-6.614,8.73> translate <7.397,-95.802,279.835> }
}  


object { P_ic }
object { P_goe }
