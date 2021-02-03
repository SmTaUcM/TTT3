/////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Lighsaber model 3 - SL Braz Ile                //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
/////////////////////////////////////////////////////

#declare T_Grip = T_red;
#declare T_GripScrew_Ou = T_red;
#declare T_Base = T_metal;
#declare T_EndCap = T_metal;
#declare T_GripScrew_In = T_dullmetal;
#declare T_def_mat = T_black;
     
#include "saber3_o.inc";
#include "saber_metal_o.inc";

#declare saber3_left =
union
{ // -0.226
  object { P_saber3 rotate <1.402,179.407,240> translate <123.207,-116.545,-199.833> }
  object { P_metal_left }
}

#declare saber3_right =
union
{
  object { P_saber3 rotate <1.861,-179.494,0.274> translate <-122.629,-110.971,-198.923> }
  object { P_metal_right }
}