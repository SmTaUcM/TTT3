 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Lighsaber model 4 - SL Braz Ile                //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////

#declare fin_T_test = 
finish 
{            
  phong 1
  phong_size 250
  ambient 0.6
  specular 0.6 
  roughness 0.05 
  brilliance 5   
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
  finish  { fin_T_test } 
}
     
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