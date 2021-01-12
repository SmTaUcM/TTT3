 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Collar layouts                                 //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////

    
// COLLAR PATCH


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

#declare T_collar_bgcom = 
texture
{
  material_map
  {
    gif ".\collars\BGCOM.gif"
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
          gif ".\collars\BGCOM.gif"
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
  object { P_wing texture { T_collargray } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w01 }
}

#declare P_collar_wing02 =
union
{
  object { P_wing texture { T_collardred } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w02 }
}

#declare P_collar_wing06 =
union
{
  object { P_wing texture { T_collarred } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w06 }
}

#declare P_collar_wing10 =
union
{
  object { P_wing texture { T_collardblue } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w10 }
}

#declare P_collar_wing19 =
union
{
  object { P_wing texture { T_collarpurple } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w19 }
}

#declare P_collar_wing21 =
union
{
  object { P_wing texture { T_collargreen } no_shadow }
  object { P_wing_border no_shadow }
  object { P_w21 }
}

#declare P_collar_sovcom =
union
{
  object { P_collar texture { T_collar_com } no_shadow }
  object { P_com texture { T_collarred } no_shadow }
  object { P_com_border no_shadow }
}

#declare P_collar_hammcom =
union
{
  object { P_collar texture { T_collar_com } no_shadow }
  object { P_com texture { T_collargray } no_shadow }
  object { P_com_border no_shadow }
}

#declare P_collar_warrcom =
union
{
  object { P_collar texture { T_collar_com } no_shadow }
  object { P_com texture { T_collardred } no_shadow }
  object { P_com_border no_shadow }
}

#declare P_collar_chalcom =
union
{
  object { P_collar texture { T_collar_com } no_shadow }
  object { P_com texture { T_collarblue } no_shadow }
  object { P_com_border no_shadow }
}

#declare P_collar_subcom =
union
{
  object { P_collar texture { T_collar_com } no_shadow }
  object { P_com texture { T_collarpurple } no_shadow }
  object { P_com_border no_shadow }
}

#declare P_collar_redcom =
union
{
  object { P_collar texture { T_collar_com } no_shadow }
  object { P_com texture { T_collargreen } no_shadow }
  object { P_com_border no_shadow }
}
  
#declare P_collar_bgcom =
object
{
  P_collar
  texture { T_collar_bgcom }
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
  #if (!strcmp(position,"BGCOM")) #declare P_acollar = P_collar_bgcom; #end
  #if (!strcmp(position,"COM")) 
    #if (!strcmp(ship,"SSSD Sovereign")) #declare P_acollar = P_collar_sovcom; #end 
    #if (!strcmp(ship,"ISD Hammer")) #declare P_acollar = P_collar_hammcom; #end 
    #if (!strcmp(ship,"ISD Warrior")) #declare P_acollar = P_collar_warrcom; #end 
    #if (!strcmp(ship,"ISD Challenge")) #declare P_acollar = P_collar_chalcom; #end   
    #if (!strcmp(ship,"ISD Subjugator")) #declare P_acollar = P_collar_subcom; #end   
    #if (!strcmp(ship,"MC80B Redemption")) #declare P_acollar = P_collar_redcom; #end   
  #end
#end
#if (!strcmp(category,"line")) 
  #if (!strcmp(wing,"Wing I")) #declare P_acollar = P_collar_wing01; #end
  #if (!strcmp(wing,"Wing II")) #declare P_acollar = P_collar_wing02; #end
  #if (!strcmp(wing,"Wing VI")) #declare P_acollar = P_collar_wing06; #end
  #if (!strcmp(wing,"Wing X")) #declare P_acollar = P_collar_wing10; #end
  #if (!strcmp(wing,"Wing XIX")) #declare P_acollar = P_collar_wing19; #end
  #if (!strcmp(wing,"Wing XXI")) #declare P_acollar = P_collar_wing21; #end
  #if (!strcmp(squad,"Omega")) #declare P_acollar = P_collar_omega; #end
  #if (!strcmp(squad,"Praetorian")) #declare P_acollar = P_collar_prae; #end
#end