/////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Lightsaber model 2                             //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
/////////////////////////////////////////////////////

// DESCRIPTION Style 2

#declare T_bright = T_dullmetal;
#declare T_switches = T_copper;

#include "saber2_o.inc";

#declare saber2_left =
union
{
  object { P_saber rotate <0,-180,0> translate <124.164,-115.166,-209.319> }
  object { P_saber_dark rotate <0,-180,0> translate <124.164,-115.166,-209.319> }
  object { P_switches rotate <0,-180,0> translate <124.164,-115.166,-209.319> }
  object { P_button_red rotate <0,-180,0> translate <124.164,-115.166,-209.319> }
  object { P_button_green rotate <0,-180,0> translate <124.164,-115.166,-209.319> }
  object { P_metal_left }
}

#declare saber2_right =
union
{
  object { P_saber rotate <1.199,-179.65,0.188> translate <-118.525,-113.01,-209.923> }
  object { P_saber_dark rotate <1.199,-179.65,0.188> translate <-118.525,-113.01,-209.923> }
  object { P_switches rotate <1.199,-179.65,0.188> translate <-118.525,-113.01,-209.923> }
  object { P_button_red rotate <1.199,-179.65,0.188> translate <-118.525,-113.01,-209.923> }
  object { P_button_green rotate <1.199,-179.65,0.188> translate <-118.525,-113.01,-209.923> }
  object { P_metal_right }
}