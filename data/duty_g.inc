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

