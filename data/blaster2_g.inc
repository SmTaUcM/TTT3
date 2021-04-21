/////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Duty Uniform                         //
//  Blaster model 2 - SE-14r                       //
//  2021 - LT Braz Ile / FA Turtle Jerrar          //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
/////////////////////////////////////////////////////

// DESCRIPTION SE-14r Pistol

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

#declare T_test = 
//texture 
//{
//    pigment { color rgb <0.4,0.4,0.4> }
//    finish { fin_T_dullmetal }
//}
texture { T_wear scale 0.75 }

#declare T_metal = 
texture
{
  pigment { color rgb <0.25,0.25,0.27> }
  finish  { fin_T_metal } 
}

#declare T_def_mat = T_dullmetal;
#declare T_Leather = T_leather;
#declare T_Metal = T_metal;
#declare T_Rough = T_wear;
#declare T_Metallic = T_test;

#include "blaster2_o.inc";
#include "blaster2_left_o.inc";

#declare blaster2_right = P_blaster2_obj;
#declare blaster2_left = P_blaster2_left_obj;