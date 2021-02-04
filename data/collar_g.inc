/////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Collar layouts                                 //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
/////////////////////////////////////////////////////


// COLLAR PATCH

// Use TTT-provided Wing collar color, or fallback
#if (defined(ttt_wingcolour))
  #declare colour_wing = ttt_wingcolour;
#else
  #declare colour_wing = color rgbt <0, 0, 0, 1>;
#end

#declare T_collar_wing =
texture
{
  pigment
  {
    color colour_wing
  }
  finish  { fin_T_uni }
}
texture { T_unilayer }

#declare T_collarred =
texture
{
  pigment
  {
    color rgb <0.58, 0.075, 0.075>
  }
  finish  { fin_T_uni }
}
texture { T_unilayer }

#declare T_collarblue =
texture
{
  pigment
  {
    color rgb <0.1, 0.2, 0.55>
  }
  finish  { fin_T_uni }
}
texture { T_unilayer }

#declare T_collarpurple =
texture
{
  pigment
  {
    color rgb <0.25, 0.1, 0.45>
  }
  finish { fin_T_uni }
}
texture { T_unilayer }

#declare T_collargreen =
texture
{
  pigment
  {
    color rgb <0.15, 0.3, 0.15>
  }
  finish  { fin_T_uni }
}
texture { T_unilayer }

#declare T_collargray =
texture
{
  pigment
  {
    color rgb <0.16, 0.2, 0.2>
  }
  finish  { fin_T_uni }
}
texture { T_unilayer }

#declare T_collardred =
texture
{
  pigment
  {
    color rgb <0.25, 0.0, 0.0>
  }
  finish  { fin_T_uni }
}
texture { T_unilayer }

#declare T_collardblue =
texture
{
  pigment
  {
    color rgb <0.0, 0.09, 0.6>
  }
  finish  { fin_T_uni }
}
texture { T_unilayer }

#declare T_wing_border = T_trim_gold;
#declare T_com_border = T_trim_gold;
#declare T_number = T_white;


// FLAG COLLARS


#declare fin_T_collar =
finish
{
  ambient rgb 0.3
  diffuse 0.55
  specular 0.4
  roughness 0.1
  reflection 0.05
}

#declare pig_T_collar =
pigment
{
  waves
  frequency 26
  color_map { colour_gold }
}

#declare T_collar_com =
texture
{
  material_map
  {
    gif ".\collars\COM.gif"
    once
    interpolate 2
    texture
    { //index 0
      pigment { color rgbt <0, 0, 0, 1> }
      finish  { ambient 1 }
    }
    texture
    { //index 1
      pigment { pig_T_collar }
      finish { fin_T_collar }
      normal
      {
        bump_map
        {
          gif ".\collars\COM.gif"
          once
          bump_size 2
        }
      }
    }
  }
}

#declare T_collar_tccs =
texture
{
  material_map
  {
    gif ".\collars\TCCS.gif"
    once
    interpolate 2
    texture
    { //index 0
      pigment { color rgbt <0, 0, 0, 1> }
      finish  { ambient 1 }
    }
    texture
    { //index 1
      pigment { pig_T_collar }
      finish { fin_T_collar }
      normal
      {
        bump_map
        {
          gif ".\collars\TCCS.gif"
          once
          bump_size 2
        }
      }
    }
  }
}

#declare T_collar_ca_ia_sgcom =
texture
{
  material_map
  {
    gif ".\collars\CA_IA_SGCOM.gif"
    once
    interpolate 2
    texture
    { //index 0
      pigment { color rgbt <0, 0, 0, 1> }
      finish  { ambient 1 }
    }
    texture
    { //index 1
      pigment { pig_T_collar }
      finish { fin_T_collar }
      normal
      {
        bump_map
        {
          gif ".\collars\CA_IA_SGCOM.gif"
          once
          bump_size 2
        }
      }
    }
  }
}

#declare T_collar_cs =
texture
{
  material_map
  {
    gif ".\collars\CS.gif"
    once
    interpolate 2
    texture
    { //index 0
      pigment { color rgbt <0, 0, 0, 1> }
      finish  { ambient 1 }
    }
    texture
    { //index 1
      pigment { pig_T_collar }
      finish { fin_T_collar }
      normal
      {
        bump_map
        {
          gif ".\collars\CS.gif"
          once
          bump_size 2
        }
      }
    }
  }
}

#declare T_collar_fc =
texture
{
  material_map
  {
    gif ".\collars\FC.gif"
    once
    interpolate 2
    texture
    { //index 0
      pigment { color rgbt <0, 0, 0, 1> }
      finish  { ambient 1 }
    }
    texture
    { //index 1
      pigment { pig_T_collar }
      finish { fin_T_collar }
      normal
      {
        bump_map
        {
          gif ".\collars\FC.gif"
          once
          bump_size 2
        }
      }
    }
  }
}


#include "collar_o.inc"


#declare P_collar_omega =
object
{
  P_collar
  texture { T_collarred }
  no_shadow
}

#declare P_collar_prae =
object
{
  P_collar
  texture { T_collarpurple }
  no_shadow
}

#declare P_collar_wing01 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w01 }
}

#declare P_collar_wing02 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w02 }
}

#declare P_collar_wing03 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w03 }
}

#declare P_collar_wing04 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w04 }
}

#declare P_collar_wing05 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w05 }
}

#declare P_collar_wing06 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w06 }
}

#declare P_collar_wing07 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w07 }
}

#declare P_collar_wing08 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w08 }
}

#declare P_collar_wing09 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w09 }
}

#declare P_collar_wing10 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w10 }
}

#declare P_collar_wing11 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w11 }
}

#declare P_collar_wing12 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w12 }
}

#declare P_collar_wing13 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w13 }
}

#declare P_collar_wing14 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w14 }
}

#declare P_collar_wing15 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w15 }
}

#declare P_collar_wing16 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w16 }
}

#declare P_collar_wing17 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w17 }
}

#declare P_collar_wing18 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w18 }
}

#declare P_collar_wing19 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w19 }
}

#declare P_collar_wing20 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w20 }
}

#declare P_collar_wing21 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w21 }
}

#declare P_collar_wing22 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w22 }
}

#declare P_collar_wing23 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w23 }
}

#declare P_collar_wing24 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w24 }
}

#declare P_collar_wing25 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w25 }
}

#declare P_collar_wing26 =
union
{
  object { P_wing texture { T_collar_wing } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w26 }
}

#declare P_collar_com =
union
{
  object { P_collar texture { T_collar_com } no_shadow }
  object { P_com texture { T_collar_wing } no_shadow }
  object { P_com_border no_shadow }
}

#declare P_collar_tccs =
object
{
  P_collar
  texture { T_collar_tccs }
  no_shadow
}

#declare P_collar_ca =
object
{
  P_collar
  texture { T_collar_ca_ia_sgcom }
  no_shadow
}

#declare P_collar_ia = P_collar_ca
#declare P_collar_sgcom = P_collar_ca

#declare P_collar_cs =
object
{
  P_collar
  texture { T_collar_cs }
  no_shadow
}

#declare P_collar_fc =
object
{
  P_collar
  texture { T_collar_fc }
  no_shadow
}


// Default collar
#declare P_acollar =
object
{
  P_collar
  texture { pigment { color rgbt <0, 0, 0, 1> } }
  no_shadow
}

#if (!strcmp(category,"flag"))
  #if (!strcmp(position,"FC")) #declare P_acollar = P_collar_fc; #end
  #if (!strcmp(position,"XO")) #declare P_acollar = P_collar_cs; #end
  #if (!strcmp(position,"CS")) #declare P_acollar = P_collar_cs; #end
  #if (!strcmp(position,"SGCOM")) #declare P_acollar = P_collar_sgcom; #end
  #if (!strcmp(position,"CA")) #declare P_acollar = P_collar_ca; #end
  #if (!strcmp(position,"IA")) #declare P_acollar = P_collar_ia; #end
  #if (!strcmp(position,"TCCS")) #declare P_acollar = P_collar_tccs; #end
  #if (!strcmp(position,"COM")) #declare P_acollar = P_collar_com; #end
#end
#if (!strcmp(category,"line"))
  #if (!strcmp(wing,"Wing I")) #declare P_acollar = P_collar_wing01; #end
  #if (!strcmp(wing,"Wing II")) #declare P_acollar = P_collar_wing02; #end
  #if (!strcmp(wing,"Wing III")) #declare P_acollar = P_collar_wing03; #end
  #if (!strcmp(wing,"Wing IV")) #declare P_acollar = P_collar_wing04; #end
  #if (!strcmp(wing,"Wing V")) #declare P_acollar = P_collar_wing05; #end
  #if (!strcmp(wing,"Wing VI")) #declare P_acollar = P_collar_wing06; #end
  #if (!strcmp(wing,"Wing VII")) #declare P_acollar = P_collar_wing07; #end
  #if (!strcmp(wing,"Wing VIII")) #declare P_acollar = P_collar_wing08; #end
  #if (!strcmp(wing,"Wing IV")) #declare P_acollar = P_collar_wing09; #end
  #if (!strcmp(wing,"Wing X")) #declare P_acollar = P_collar_wing10; #end
  #if (!strcmp(wing,"Wing XI")) #declare P_acollar = P_collar_wing11; #end
  #if (!strcmp(wing,"Wing XII")) #declare P_acollar = P_collar_wing12; #end
  #if (!strcmp(wing,"Wing XIII")) #declare P_acollar = P_collar_wing13; #end
  #if (!strcmp(wing,"Wing XIV")) #declare P_acollar = P_collar_wing14; #end
  #if (!strcmp(wing,"Wing XV")) #declare P_acollar = P_collar_wing15; #end
  #if (!strcmp(wing,"Wing XVI")) #declare P_acollar = P_collar_wing16; #end
  #if (!strcmp(wing,"Wing XVII")) #declare P_acollar = P_collar_wing17; #end
  #if (!strcmp(wing,"Wing XVIII")) #declare P_acollar = P_collar_wing18; #end
  #if (!strcmp(wing,"Wing XIX")) #declare P_acollar = P_collar_wing19; #end
  #if (!strcmp(wing,"Wing XX")) #declare P_acollar = P_collar_wing20; #end
  #if (!strcmp(wing,"Wing XXI")) #declare P_acollar = P_collar_wing21; #end
  #if (!strcmp(wing,"Wing XXII")) #declare P_acollar = P_collar_wing22; #end
  #if (!strcmp(wing,"Wing XXIII")) #declare P_acollar = P_collar_wing23; #end
  #if (!strcmp(wing,"Wing XXIV")) #declare P_acollar = P_collar_wing24; #end
  #if (!strcmp(wing,"Wing XXV")) #declare P_acollar = P_collar_wing25; #end
  #if (!strcmp(wing,"Wing XXVI")) #declare P_acollar = P_collar_wing26; #end
  #if (!strcmp(squad,"Omega")) #declare P_acollar = P_collar_omega; #end
  #if (!strcmp(squad,"Praetorian")) #declare P_acollar = P_collar_prae; #end
#end