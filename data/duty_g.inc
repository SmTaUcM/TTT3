 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Duty Uniform                         //
//  Master include file                            //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////

#include "dutydress_g.inc"


// UNIFORM

   
#declare T_uniform = 
texture
{
  pigment
  {
    color rgb <0.185, 0.218, 0.185>
  }
  finish  { fin_T_uni } 
  normal  { norm_T_uni } 
}
texture { T_unilayer scale .05 }


// POSITION


#declare fin_T_body = 
finish 
{            
  phong 1
  phong_size 250
  reflection 0.2
  ambient rgb 0.3
  metallic
  specular 0.6
  emission 0
}

#declare T_body = 
texture
{
  pigment
  {
    color rgb <0.34,0.34,0.34>
  }
  finish  { fin_T_body } 
}

#declare T_body2 = 
texture
{
  pigment
  {
    color rgb <0.33,0.33,0.33>
  }
  finish  { fin_T_body } 
}

#declare T_ring = 
texture
{
  pigment
  {
    color rgb <0.5,0.5,0.55>
  }
  finish  { fin_T_body } 
}

#declare T_cap = 
texture
{
  pigment
  {
    color rgb <0,0,0.5>
  }
  finish  { fin_T_body } 
}

#declare T_cap2 = 
texture
{
  pigment
  {
    color rgb <0.4,0.15,0>
  }
  finish  { fin_T_body } 
}

#declare T_clip = 
texture
{
  pigment
  {
    color rgb <0.56,0.43,0.32>
  }
  finish  { fin_T_body } 
}


// METALS

#declare fin_T_dullmetal =
finish
{
  reflection 0.2
  ambient 0.3
  metallic
  specular 0.5
  emission 0
}

#declare T_blackmetal =
texture
{
  pigment { color rgb <0.5,0.5,0.5> }
  finish  { fin_T_metal }
}

#declare T_bronze =
texture
{
  pigment { color rgb <0.35,0.2,0> }
  finish  { fin_T_metal }
}

#declare T_silver =
texture
{
  pigment { color rgb <0.4,0.4,0.42> }
  finish  { fin_T_metal }
}

#declare T_gold =
texture
{
  pigment { color rgb <0.80,0.57,0.28> }
  finish  { fin_T_metal }
}

#declare T_metal =
texture
{
  pigment { color rgb <0.25,0.25,0.27> }
  finish  { fin_T_metal }
}

#declare T_copper =
texture
{
  pigment { color rgb <0.56,0.43,0.32> }
  finish  { fin_T_dullmetal }
}

#declare T_red =
texture
{
  pigment { color rgb <0.25,0,0> }
  finish { fin_T_dullmetal }
}

#declare T_green =
texture
{
  pigment { color rgb <0,0.15,0> }
  finish { fin_T_dullmetal }
}

#declare T_blue =
texture
{
  pigment { color rgb <0.1,0.117,0.348> }
  finish { fin_T_dullmetal }
}

#declare T_dullmetal =
texture
{
  pigment { color rgb <0.5,0.5,0.52> }
  finish  { fin_T_dullmetal }
}

#declare T_white =
texture
{
  pigment { color rgb <0.7,0.7,0.7> }
  finish { fin_T_dullmetal }
}

#declare T_flatblack =
texture
{
  pigment { color rgb <0.1,0.1,0.1> }
  finish  { fin_T_dullmetal }
}

// PLASTIC

#declare fin_T_plastic =
finish
{
  diffuse 0.8
  reflection 0.05
  ambient 0.3
  specular 0.05
  roughness 0.6
  emission 0
}

#declare T_black =
texture
{
  pigment { color rgb <0.02,0.02,0.02> }
  finish { fin_T_plastic }
}

#declare T_grey =
texture
{
  pigment { color rgb <0.4,0.4,0.42> }
  finish  { fin_T_plastic }
}

