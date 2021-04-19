/////////////////////////////////////////////////////////
//                                                      //
//  TIE Corps Dress Uniform                             //
//  Lighsaber model 4 - SL Braz Ile / AD Turtle Jerrar  //
//                                                      //
//  Settings in this file are not affected by TTT       //
//                                                      //
//////////////////////////////////////////////////////////

// DESCRIPTION Style 4

#declare fin_T_flatmetal = 
finish 
{            
  phong 1
  phong_size 250
  ambient 0.6
  specular 0.6 
  roughness 0.05 
  brilliance 5 
  emission 0  
  reflection
  {
    0.1
    metallic  
    exponent 0.75 
  }
}

#declare T_saber4_metal = 
texture
{
  pigment { color rgb <0.2,0.2,0.2> }
  finish  { fin_T_flatmetal } 
}

// saber4 materials
#declare T_ButtonOuter = T_gold
#declare T_ButtonInner = T_silver
#declare T_Accents = T_gold
#declare T_Ridges = T_black
#declare T_Base = T_saber4_metal
#declare T_Emitter = T_gold
#declare T_def_mat = T_black
     
#include "saber4_o.inc";
#include "saber_metal_o.inc";

#declare saber4_left =
union
{
  object { P_saber4 rotate <1.402,179.407,-0.226> translate <123.207,-116.545,-208.833> }
  object { P_metal_left }
}
#declare saber4_right =
union
{
  object { P_saber4 rotate <1.861,-179.494,0.274> translate <-119.629,-114.971,-209.923> }
  object { P_metal_right }
}