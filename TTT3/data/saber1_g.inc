 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Lighsaber model 1                              //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////

         
#declare T_bright = T_dullmetal;
#declare T_button1 = T_copper;
#declare T_button_round = T_copper;
#declare T_ring = T_red;
#declare T_arrow = T_red;
#declare T_screw = T_gold;
#declare T_screw_cap = T_red;
  
#declare T_button2 = 
texture
{
  pigment { color rgb <0.86,0.73,0.52> }
  finish  { fin_T_metal } 
}

         
#include "saber1_o.inc";
    
    
#declare saber1_left =
union
{
  object { P_saber rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_saber_dark rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_ring rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_button1 rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_button2 rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_button_round rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_arrow rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_screw rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_screw_cap rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_metal_left }
}

#declare saber1_right =
union
{
  object { P_saber rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_saber_dark rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_ring rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_button1 rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_button2 rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_button_round rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_arrow rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_screw rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_screw_cap rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_metal_right }
}


