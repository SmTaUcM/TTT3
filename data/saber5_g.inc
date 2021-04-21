//////////////////////////////////////////////////////////
//                                                      //
//  TIE Corps Dress Uniform                             //
//  Lighsaber model 5 'Kamjin' - FA Turtle Jerrar       //
//                                                      //
//  Settings in this file are not affected by TTT       //
//                                                      //
//////////////////////////////////////////////////////////

// DESCRIPTION Kamjin's Saber

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

// saber5 materials
#declare T_def_mat = T_black
#declare T_ButtonOuter = T_black
#declare T_ButtonInner = T_silver
#declare T_KnobGrip = T_black
#declare T_Base = T_black
#declare T_KnobOuter = T_black
#declare T_KnobInner = T_silver
#declare T_Top = T_metal
#declare T_Emitter = T_metal
#declare T_Lights = T_red

#include "saber5_o.inc";
#include "saber_metal_o.inc";

#declare saber5_left =
union
{
  object { P_saber5_obj rotate <1.402,179.407,45.226> translate <123.207,-116.545,-208.833> }
  object { P_metal_left }
}
#declare saber5_right =
union
{
  object { P_saber5_obj rotate <1.861,-179.494,140.274> translate <-119.629,-114.971,-209.923> }
  object { P_metal_right }
}