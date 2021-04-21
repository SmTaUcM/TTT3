/////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Duty Uniform                         //
//  Blaster model 1 - DH17                         //
//  2021 - LT Braz Ile / FA Turtle Jerrar          //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
/////////////////////////////////////////////////////

// DESCRIPTION DH-17 Blaster

#declare fin_T_reallydullmetal = 
finish 
{            
  reflection 0.1
  ambient 0.6
  metallic
  specular 0.7
}

#declare T_wear = 
texture
{
  pigment { color rgb <0.08,0.08,0.08> }
}
texture
{
  pigment
  {
    image_map
    {
      //png ".\misc\wear.png"
      jpeg ".\misc\wear2.jpg"
      transmit all 0.95
    }
  }
  finish  { fin_T_reallydullmetal } 
}

#declare fin_T_plastic2 =
finish
{
  diffuse 0.8
  reflection 0
  ambient 0.3
  specular 0.05
  roughness 0.6
  emission 0
}

#declare T_leather =
texture
{
  pigment { color rgb <0.05,0.05,0.05> }
  finish  { fin_T_plastic2 }
}

#declare T_def_mat = T_dullmetal;
#declare T_Base = T_wear;
#declare T_Accent = T_metal;
#declare T_Grip = T_wear;
#declare T_Leather = T_leather;
#declare T_Metal = T_metal;

#include "blaster1_o.inc";
#include "blaster1_left_o.inc";

#declare blaster1_right =
union
{
  object { P_blaster1_obj }
}

#declare blaster1_left =
union
{
  object { P_blaster1_left_obj }
}