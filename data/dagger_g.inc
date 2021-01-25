 ////////////////////////////////////////////////////
//                                                 //
//  Dagger to the Grand Order of the Emperor       //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////

 
#declare T_leather = T_belt;

#declare T_cloth_red = 
texture
{
  pigment { colour rgb <0.45,0,0> }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 7}

#declare T_cloth_white = 
texture
{
  pigment { colour rgb <1,1,1> }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 6}


#include "dagger_o.inc";


#declare dagger_right =
union
{
  object { P_dagger }
  object { P_sheath }
  object { P_handle_red }
  object { P_handle_white }
  object { P_metal_right }
  object { P_straps_right }
}

#declare dagger_left =
union
{
  object { P_dagger scale <-1,1,1> }
  object { P_sheath scale <-1,1,1> }
  object { P_handle_red scale <-1,1,1> }
  object { P_handle_white scale <-1,1,1> }
  object { P_metal_left }
  object { P_straps_left }
}

