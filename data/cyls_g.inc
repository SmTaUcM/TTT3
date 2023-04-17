 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Duty Uniform                         //
//  Position cylinders                             //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "cyls_o.inc";


#declare P_cylinder_1_1 =
union
{
  object { P_body }
  object { P_cap }
  object { P_clip }
  rotate <-172.965,10.19,-209.434>
  translate <-172.818,-85.226,259.015>
}

#declare P_cylinder_1_2 =
union
{
  object { P_body }
  object { P_cap }
  object { P_clip }
  rotate <-172.465,8.731,-191.302>
  translate <-157.788,-91.488,258.043>
}

#declare P_cylinder_1_3 =
union
{
  object { P_body }
  object { P_cap }
  object { P_clip }
  rotate <186.882,-9.916,-158.518>
  translate <166.425,-91.091,259.128>
}

#declare P_cylinder_1_4 =
union
{
  object { P_body }
  object { P_cap }
  object { P_clip }
  rotate <184.393,-11.894,-131.718>
  translate <181.509,-82.602,260.156>
}

#declare P_cylinder_2_1 =
union
{
  object { P_body2 }
  object { P_ring2 }
  object { P_cap2 }
  object { P_clip }
  rotate <-172.965,10.19,-209.434>
  translate <-172.818,-85.226,259.015>
}

#declare P_cylinder_2_2 =
union
{
  object { P_body2 }
  object { P_ring2 }
  object { P_cap2 }
  object { P_clip }
  rotate <-172.465,8.731,-191.302>
  translate <-157.788,-91.488,258.043>
}

#declare P_cylinder_2_3 =
union
{
  object { P_body2 }
  object { P_ring2 }
  object { P_cap2 }
  object { P_clip }
  rotate <186.882,-9.916,-158.518>
  translate <166.425,-91.091,259.128>
}

#declare P_cylinder_2_4 =
union
{
  object { P_body2 }
  object { P_ring2 }
  object { P_cap2 }
  object { P_clip }
  rotate <184.393,-11.894,-131.718>
  translate <181.509,-82.602,260.156>
}
     

#declare P_FM = object { P_cylinder_1_3 }

#declare P_FL = object { P_cylinder_2_3 }  

#declare P_SQXO = object { P_cylinder_2_3 }  

#declare P_CMDR = object { P_cylinder_2_2 } 

#declare P_WC =
union
{
  object { P_cylinder_1_2 }
  object { P_cylinder_1_3 }
}

#declare P_COM =
union
{
  object { P_cylinder_1_2 }
  object { P_cylinder_2_3 }
}

#declare P_BGCOM =
union
{
  object { P_cylinder_2_2 }
  object { P_cylinder_2_3 }
}

#declare P_TCCS =
union
{
  object { P_cylinder_2_2 }
  object { P_cylinder_2_3 }
}

#declare P_IA =
union
{
  object { P_cylinder_2_2 }
  object { P_cylinder_1_3 }
  object { P_cylinder_2_4 }
}

#declare P_CA =
union
{
  object { P_cylinder_2_1 }
  object { P_cylinder_1_2 }
  object { P_cylinder_2_3 }
}

#declare P_GCO =
union
{
  object { P_cylinder_1_1 }
  object { P_cylinder_1_2 }
  object { P_cylinder_1_3 }
  object { P_cylinder_1_4 }
}

#declare P_CS =
union
{
  object { P_cylinder_2_1 }
  object { P_cylinder_1_2 }
  object { P_cylinder_1_3 }
  object { P_cylinder_2_4 }
}

#declare P_XO =
union
{
  object { P_cylinder_2_1 }
  object { P_cylinder_1_2 }
  object { P_cylinder_2_3 }
  object { P_cylinder_2_4 }
}

#declare P_FC =
union
{
  object { P_cylinder_2_1 }
  object { P_cylinder_2_2 }
  object { P_cylinder_2_3 }
  object { P_cylinder_2_4 }
}

