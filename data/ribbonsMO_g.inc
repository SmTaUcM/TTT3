/************************************************************************
 *                     RIBBON DEVICE DOCUMENTATION
 *                         RA/LC Robert Hogan
 * Last Revised : 14 March 2023
 ************************************************************************
 *
 * NOTE: The data contained in ribbons_g.inc should NOT be modified.  
 *   This contains texture definitions, transformations, and object 
 *   declarations which are essential for the ribbon devices to work 
 *   correctly.
 *
 ************************************************************************
 *
 * For creating new ribbon textures, the following conventions are used:
 * 
 * #declare T_r_v1 =
 * texture
 * {
 *   pigment { image_map { gif "ribbons/v2.gif" } }
 *   finish  { fin_T_uni }
 * }
 * texture { T_unilayer scale 2}
 * 
 *   with
 * 
 * v1 : string : Base award name (such as "moi", not "moi_gc")
 * v2 : string : Ribbon file name as type .gif
 * 
 * For creating new ribbon objects, the following conventions are used:
 * 
 * #declare P_ribbon_mot_gh =
 * union
 * {
 *   object { P_single_ribbon texture { T_r_v1 } }
 *   object { P_v2_ribbon_device texture { T_v3 } v4 }
 * }
 * 
 *   with
 * 
 * v1 : string : Specific award name (such as "is_cr", "coe", "mot_bh")
 * v2 : string : Ribbon device name (such as "cross", "oak_cluster")
 * v3 : string : Device texture (such as "platinum", "gold", "blue")
 * v4 : string : A transformation object for the device, formatted as:
 *                 "translate <x,0,0>", with x being the translation.
 *                   Note a positive x moves the device to the camera's 
 *                     right / negative x to the camera's left.
 * 
 ************************************************************************/

///////////////////////////
//  TEXTURE INFORMATION  //
///////////////////////////


#declare T_platinum =
texture
{
  pigment { color rgb <0.7,0.7,0.7> }
  finish  { fin_T_metal }
}


#include "ribbons_o.inc"
#include "ribbon_devices_o.inc"
#include "medal_o.inc"


#declare T_diamond_rib =
texture
{
  pigment { color rgb <0.58, 0.58, 0.58> }
  finish  { fin_T_metal }
}

#declare T_red_rib =
texture
{
  pigment { color rgb <0.5,0.25,0.25> }
  finish { fin_T_dullmetal }
}

#declare T_green_rib =
texture
{
  pigment { color rgb <0.25,0.5,0.25> }
  finish { fin_T_dullmetal }
}

#declare T_blue_rib =
texture
{
  pigment { color rgb <0.25,0.25,0.5> }
  finish { fin_T_dullmetal }
}        

#declare T_r_cox =
texture
{
  pigment { image_map { gif "ribbons/cox.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_dfc =
texture
{
  pigment { image_map { gif "ribbons/dfc.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_iar =
texture
{
  pigment { image_map { gif "ribbons/iar.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_is_r =
texture
{
  pigment { image_map { gif "ribbons/is-r.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_is_w =
texture
{
  pigment { image_map { gif "ribbons/is-w.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_loa =
texture
{
  pigment { image_map { gif "ribbons/loa.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_loc =
texture
{
  pigment { image_map { gif "ribbons/loc.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_los =
texture
{
  pigment { image_map { gif "ribbons/los.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_moc =
texture
{
  pigment { image_map { gif "ribbons/moc.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_moi =
texture
{
  pigment { image_map { gif "ribbons/moi.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_mos =
texture
{
  pigment { image_map { gif "ribbons/mos.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_mot =
texture
{
  pigment { image_map { gif "ribbons/mot.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_mua =
texture
{
  pigment { image_map { gif "ribbons/mua.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_oov =
texture
{
  pigment { image_map { gif "ribbons/oov.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_ora =
texture
{
  pigment { image_map { gif "ribbons/ora.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_r_tua =
texture
{
  pigment { image_map { gif "ribbons/tua.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}


//////////////////////////
//  DEVICE ADJUSTMENTS  //
//////////////////////////

#declare P_oak_leaf_ribbon_device =
object { P_oak_leaf_device scale <0.9,0.9,0.9> rotate <0,180,0> translate <0,-2.5,0.2> }

#declare P_hammer_ribbon_device =
object { P_hammer_device rotate <0,180,0> translate <0,-2.5,0> }

#declare P_cross_ribbon_device =
object { P_cross_device rotate <0,180,0> translate <0,-2.5,0.2> }

#declare P_oak_cluster_ribbon_device =
object { P_oak_cluster_device scale <0.9,0.9,0.9> rotate <0,180,0> translate <0,-2.5,0> }

#declare P_wings_ribbon_device =
object { P_wings_device scale <0.9,0.9,0.9> rotate <0,180,0> translate <0,-2.5,0> }

#declare P_mab_ribbon_device =
object { P_mab scale <0.9,0.9,0.9> translate <0,-1.2,9.3> }

#declare P_scimitar_ribbon_device =
object { P_scimitar_device scale <-0.9,0.9,0.9> rotate <0,180,0> translate <0,-2.5,0> }

#declare P_cob_ribbon_device =
object { P_cob_device scale <0.9,0.9,0.9> rotate <0,180,0> translate <0,-2.5,0> }

#declare P_coe_ribbon_device = 
object { P_coe_device scale <0.9,0.9,0.9> rotate <0,180,0> translate <0,-2.5,0> }

#declare P_col_ribbon_device =
object { P_col_device scale <0.9,0.9,0.9> rotate <0,180,0> translate <0,-2.5,0> }

#declare P_cos_ribbon_device =
object { P_cos_device scale <0.9,0.9,0.9> rotate <0,180,0> translate <0,-2.5,0> }

#declare P_echelon_ribbon_device =
object { P_echelon_device scale <0.75,0.75,0.75> rotate <0,180,0> translate <0,-2.5,0> }


//////////////////////////
//  RIBBON DEFINITIONS  //
//////////////////////////

// IMPERIAL ACHIEVEMENT RIBBON

#declare P_ribbon_iar = 
object { P_single_ribbon texture { T_r_iar } }

#declare P_ribbon_iar_bl =
union
{
  object { P_single_ribbon texture { T_r_iar } }
  object { P_oak_leaf_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_iar_sl =
union
{
  object { P_single_ribbon texture { T_r_iar } }
  object { P_oak_leaf_ribbon_device texture { T_silver } }
}

#declare P_ribbon_iar_gl =
union
{
  object { P_single_ribbon texture { T_r_iar } }
  object { P_oak_leaf_ribbon_device texture { T_gold } }
}

// MEDAL OF TACTICS

#declare P_ribbon_mot_bh =
union
{
  object { P_single_ribbon texture { T_r_mot } }
  object { P_hammer_ribbon_device texture { T_platinum } translate <-7.7,0,0> }
}

#declare P_ribbon_mot_gh =
union
{
  object { P_single_ribbon texture { T_r_mot } }
  object { P_hammer_ribbon_device texture { T_platinum } translate <7.7,0,0> }
}

#declare P_ribbon_mot_rh =
union
{
  object { P_single_ribbon texture { T_r_mot } }
  object { P_hammer_ribbon_device texture { T_platinum } translate <0,0,0> }
}

// MEDAL OF INSTRUCTION

#declare P_ribbon_moi =
object { P_single_ribbon texture { T_r_moi } }


#declare P_ribbon_moi_bc =
union
{
  object { P_single_ribbon texture { T_r_moi } }
  object { P_cross_ribbon_device texture { T_blue_rib } }
}

#declare P_ribbon_moi_gc =
union
{
  object { P_single_ribbon texture { T_r_moi } }
  object { P_cross_ribbon_device texture { T_gold } }
}

#declare P_ribbon_moi_pc =
union
{
  object { P_single_ribbon texture { T_r_moi } }
  object { P_cross_ribbon_device texture { T_platinum } }
}

#declare P_ribbon_moi_ec =
union
{
  object { P_single_ribbon texture { T_r_moi } }
  object { P_cross_ribbon_device texture { T_green_rib } }
}

#declare P_ribbon_moi_dc =
union
{
  object { P_single_ribbon texture { T_r_moi } }
  object { P_cross_ribbon_device texture { T_diamond_rib } }
}

// MEDAL OF SCHOLARSHIP

#declare P_ribbon_mos =
object { P_single_ribbon texture { T_r_mos } }


#declare P_ribbon_mos_boc =
union
{
  object { P_single_ribbon texture { T_r_mos } }
  object { P_oak_cluster_ribbon_device texture { T_bronze } }
}
                     
#declare P_ribbon_mos_soc =
union
{
  object { P_single_ribbon texture { T_r_mos } }
  object { P_oak_cluster_ribbon_device texture { T_silver } }
}

#declare P_ribbon_mos_goc =
union
{
  object { P_single_ribbon texture { T_r_mos } }
  object { P_oak_cluster_ribbon_device texture { T_gold } }
}

// MEDAL OF COMMUNICATION

#declare P_ribbon_moc_boc =
union
{
  object { P_single_ribbon texture { T_r_moc } }
  object { P_oak_cluster_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_moc_soc =
union
{
  object { P_single_ribbon texture { T_r_moc } }
  object { P_oak_cluster_ribbon_device texture { T_silver } }
}

#declare P_ribbon_moc_goc =
union
{
  object { P_single_ribbon texture { T_r_moc } }
  object { P_oak_cluster_ribbon_device texture { T_gold } }
}

#declare P_ribbon_moc_poc =
union
{
  object { P_single_ribbon texture { T_r_moc } }
   object { P_oak_cluster_ribbon_device texture { T_platinum } }
}

#declare P_ribbon_moc_doc =
union
{
  object { P_single_ribbon texture { T_r_moc } }
   object { P_oak_cluster_ribbon_device texture { T_diamond_rib } }
}

// TIE CORPS COMMANDER'S UNIT AWARD

#declare P_ribbon_tua =
object { P_single_ribbon texture { T_r_tua } }

#declare P_ribbon_tua_bw =
union
{
  object { P_single_ribbon texture { T_r_tua } }
  object { P_wings_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_tua_sw =
union
{
  object { P_single_ribbon texture { T_r_tua } }
  object { P_wings_ribbon_device texture { T_silver } }
}

#declare P_ribbon_tua_gw =
union
{
  object { P_single_ribbon texture { T_r_tua } }
  object { P_wings_ribbon_device texture { T_gold } }
}

#declare P_ribbon_tua_pw =
union
{
  object { P_single_ribbon texture { T_r_tua } }
  object { P_wings_ribbon_device texture { T_platinum } }
}

// TIE CORPS MERITORIOUS UNIT AWARD

#declare P_ribbon_mua =
object { P_single_ribbon texture { T_r_mua } }

#declare P_ribbon_mua_bw =
union
{
  object { P_single_ribbon texture { T_r_mua } }
  object { P_wings_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_mua_sw =
union
{
  object { P_single_ribbon texture { T_r_mua } }
  object { P_wings_ribbon_device texture { T_silver } }
}

#declare P_ribbon_mua_gw =
union
{
  object { P_single_ribbon texture { T_r_mua } }
  object { P_wings_ribbon_device texture { T_gold } }
}

#declare P_ribbon_mua_pw =
union
{
  object { P_single_ribbon texture { T_r_mua } }
  object { P_wings_ribbon_device texture { T_platinum } }
}

// IRON STAR WITH WINGS

#declare P_ribbon_is_cw =
union
{
  object { P_single_ribbon texture { T_r_is_w } }
  object { P_wings_ribbon_device texture { T_copper } }
}

#declare P_ribbon_is_bw =
union
{
  object { P_single_ribbon texture { T_r_is_w } }
  object { P_wings_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_is_sw =
union
{
  object { P_single_ribbon texture { T_r_is_w } }
  object { P_wings_ribbon_device texture { T_silver } }
}

#declare P_ribbon_is_gw =
union
{
  object { P_single_ribbon texture { T_r_is_w } }
  object { P_wings_ribbon_device texture { T_gold } }
}

#declare P_ribbon_is_pw =
union
{
  object { P_single_ribbon texture { T_r_is_w } }
  object { P_wings_ribbon_device texture { T_platinum } }
}

// IRON STAR WITH RIBBON

#declare P_ribbon_is_cr =
union
{
  object { P_single_ribbon texture { T_r_is_r } }
  object { P_mab_ribbon_device texture { T_copper } }
}

#declare P_ribbon_is_br =
union
{
  object { P_single_ribbon texture { T_r_is_r } }
  object { P_mab_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_is_sr =
union
{
  object { P_single_ribbon texture { T_r_is_r } }
  object { P_mab_ribbon_device texture { T_silver } }
}

#declare P_ribbon_is_gr =
union
{
  object { P_single_ribbon texture { T_r_is_r } }
  object { P_mab_ribbon_device texture { T_gold } }
}

#declare P_ribbon_is_pr =
union
{
  object { P_single_ribbon texture { T_r_is_r } }
  object { P_mab_ribbon_device texture { T_platinum } }
}

// LEGION OF COMBAT

#declare P_ribbon_loc =
object { P_single_ribbon texture { T_r_loc } }

#declare P_ribbon_loc_cs =
union
{
  object { P_single_ribbon texture { T_r_loc } }
  object { P_scimitar_ribbon_device texture { T_copper } }
}

#declare P_ribbon_loc_is =
union
{
  object { P_single_ribbon texture { T_r_loc } }
  object { P_scimitar_ribbon_device texture { T_green_rib } }
}

#declare P_ribbon_loc_ts =
union
{
  object { P_single_ribbon texture { T_r_loc } }
  object { P_scimitar_ribbon_device texture { T_blue_rib } }
}

#declare P_ribbon_loc_rs =
union
{
  object { P_single_ribbon texture { T_r_loc } }
   object { P_scimitar_ribbon_device texture { T_red_rib } }
}

#declare P_ribbon_loc_ps =
union
{
  object { P_single_ribbon texture { T_r_loc } }
  object { P_scimitar_ribbon_device texture { T_platinum } }
}

// LEGION OF SKIRMISH

#declare P_ribbon_los =
object { P_single_ribbon texture { T_r_los } }

#declare P_ribbon_los_cs =
union
{
  object { P_single_ribbon texture { T_r_los } }
  object { P_scimitar_ribbon_device texture { T_copper } }
}

#declare P_ribbon_los_is =
union
{
  object { P_single_ribbon texture { T_r_los } }
  object { P_scimitar_ribbon_device texture { T_green_rib } }
}

#declare P_ribbon_los_ts =
union
{
  object { P_single_ribbon texture { T_r_los } }
  object { P_scimitar_ribbon_device texture { T_blue_rib } }
}

#declare P_ribbon_los_rs =
union
{
  object { P_single_ribbon texture { T_r_los } }
  object { P_scimitar_ribbon_device texture { T_red_rib } }
}

#declare P_ribbon_los_ps =
union
{
  object { P_single_ribbon texture { T_r_los } }
  object { P_scimitar_ribbon_device texture { T_platinum } }
}

// DISTINGUISHED FLYING CROSS

#declare P_ribbon_dfc =
object { P_single_ribbon texture { T_r_dfc } }

#declare P_ribbon_dfc_bw =
union                                                                          
{
  object { P_single_ribbon texture { T_r_dfc } }
  object { P_wings_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_dfc_sw =
union
{
  object { P_single_ribbon texture { T_r_dfc } }
  object { P_wings_ribbon_device texture { T_silver } }
}

#declare P_ribbon_dfc_gw =
union
{
  object { P_single_ribbon texture { T_r_dfc } }
  object { P_wings_ribbon_device texture { T_gold } }
}

// OPERATIONAL READINESS AWARD

#declare P_ribbon_ora =
object { P_single_ribbon texture { T_r_ora } }

#declare P_ribbon_ora_1c =
union
{
  object { P_single_ribbon texture { T_r_ora } }
  object { P_oak_cluster_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_ora_2c =
union
{
  object { P_single_ribbon texture { T_r_ora } }
  object { P_oak_cluster_ribbon_device texture { T_silver } }
}

#declare P_ribbon_ora_3c =
union
{
  object { P_single_ribbon texture { T_r_ora } }
  object { P_oak_cluster_ribbon_device texture { T_gold } }
}

#declare P_ribbon_ora_4c =
union
{
  object { P_single_ribbon texture { T_r_ora } }
  object { P_oak_cluster_ribbon_device texture { T_platinum }  }
}

#declare P_ribbon_ora_5c =
union
{
  object { P_single_ribbon texture { T_r_ora } }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <-2.5,0,0> }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <2.5,0,0> }
}

#declare P_ribbon_ora_6c =
union
{
  object { P_single_ribbon texture { T_r_ora } }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <-5,0,0> }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <5,0,0> }
}

#declare P_ribbon_ora_7c =
union
{
  object { P_single_ribbon texture { T_r_ora } }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <-7.5,-2.5,0> }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <-2.5,-2.5,0> }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <2.5,-2.5,0> }
  object { P_oak_cluster_ribbon_device texture { T_platinum } translate <7.5,-2.5,0> }
}

// COMMENDATIONS

#declare P_ribbon_cos =
union
{
  object { P_single_ribbon texture { T_r_cox } }
  object { P_cos_ribbon_device }
}

#declare P_ribbon_coe =
union
{
  object { P_single_ribbon texture { T_r_cox } }
  object { P_coe_ribbon_device }
  
}

#declare P_ribbon_col =
union
{
  object { P_single_ribbon texture { T_r_cox } }
  object { P_col_ribbon_device }
}

#declare P_ribbon_cob =
union
{
  object { P_single_ribbon texture { T_r_cox } }
  object { P_cob_ribbon_device }
}

// LETTER OF ACHIEVEMENT

#declare P_ribbon_loa =
object { P_single_ribbon texture { T_r_loa } }

// ORDER OF THE VANGUARD

#declare P_ribbon_ov_1e =
object { P_single_ribbon texture { T_r_oov } }

#declare P_ribbon_ov_2e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
}

#declare P_ribbon_ov_3e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
}

#declare P_ribbon_ov_4e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
}

#declare P_ribbon_ov_5e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_6e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_gold } translate <0,0,0> }
}

#declare P_ribbon_ov_7e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_gold } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
}

#declare P_ribbon_ov_8e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_gold } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
}

#declare P_ribbon_ov_9e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_gold } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_10e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_gold } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}


#declare P_ribbon_ov_11e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <0,0,0> }
}

#declare P_ribbon_ov_12e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
}

#declare P_ribbon_ov_13e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
}

#declare P_ribbon_ov_14e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_15e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
} 
 

#declare P_ribbon_ov_16e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <1.385,0,0> }
}

#declare P_ribbon_ov_17e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
} 
 
#declare P_ribbon_ov_18e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_19e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_20e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_gold } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}

#declare P_ribbon_ov_21e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <1.385,0,0> }
}

#declare P_ribbon_ov_22e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
}

#declare P_ribbon_ov_23e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_24e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_25e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}

#declare P_ribbon_ov_26e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <2.75,0,0> }
}

#declare P_ribbon_ov_27e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_28e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_29e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}
 
#declare P_ribbon_ov_30e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-8.25,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <8.25,0,0> }
}

#declare P_ribbon_ov_31e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <2.75,0,0> }
}

#declare P_ribbon_ov_32e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_33e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_34e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}

#declare P_ribbon_ov_35e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-8.25,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <8.25,0,0> }
}

#declare P_ribbon_ov_36e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <4.135,0,0> }
}

#declare P_ribbon_ov_37e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_38e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}

#declare P_ribbon_ov_39e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-8.25,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue_rib } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <8.25,0,0> }
}

//////////////////////////////
//  RIBBON TRANSFORMATIONS  //
//////////////////////////////

// ROW 1

#declare device_trans_0 =
transform
{
    translate <16.5048, -145.351, 205.658>
} 

#declare device_trans_1 =
transform
{
    translate <39.1371, -145.351, 205.658>
} 

#declare device_trans_2 =
transform
{
    translate <61.7695, -145.351, 205.658>
} 

#declare device_trans_3 =
transform
{
    translate <84.4018, -145.351, 205.658>
} 

// ROW 2

#declare device_trans_4 =
transform
{
    translate <16.5048, -145.351, 200.323>
} 

#declare device_trans_5 =
transform
{
    translate <39.1371, -145.351, 200.323>
}  

#declare device_trans_6 =
transform
{
    translate <61.7695, -145.351, 200.323>
} 

#declare device_trans_7 =
transform
{
    translate <84.4018, -145.351, 200.323>
}  

// ROW 3

#declare device_trans_8 =
transform
{
    translate <16.5048, -145.351, 194.994>
}  

#declare device_trans_9 =
transform
{
    translate <39.1371, -145.351, 194.994>
}  

#declare device_trans_10 =
transform
{
    translate <61.7695, -145.351, 194.994>
} 

#declare device_trans_11 =
transform
{
    translate <84.4018, -145.351, 194.994>
} 

// ROW 4

#declare device_trans_12 =
transform
{
    translate <16.5048, -145.351, 189.665>
} 

#declare device_trans_13 =
transform
{
    translate <39.1371, -145.351, 189.665>
} 

#declare device_trans_14 =
transform
{
    translate <61.7695, -145.351, 189.665>
} 

#declare device_trans_15 =
transform
{
    translate <84.4018, -145.351, 189.665>
} 

// ROW 5

#declare device_trans_16 =
transform
{
    translate <16.5048, -145.351, 184.335>
} 

#declare device_trans_17 =
transform
{
    translate <39.1371, -145.351, 184.335>
} 

#declare device_trans_18 =
transform
{
    translate <61.7695, -145.351, 184.335>
} 

#declare device_trans_19 =
transform
{
    translate <84.4018, -145.351, 184.335>
} 

// ROW 6

#declare device_trans_20 =
transform
{
    translate <16.5048, -145.351, 179.006>
}  

#declare device_trans_21 =
transform
{
    translate <39.1371, -145.351, 179.006>
} 

#declare device_trans_22 =
transform
{
    translate <61.7695, -145.351, 179.006>
} 

#declare device_trans_23 =
transform
{
    translate <84.4018, -145.351, 179.006>
} 

// ROW 7

#declare device_trans_24 =
transform
{
    translate <16.5048, -145.351, 173.677>
} 

#declare device_trans_25 =
transform
{
    translate <39.1371, -145.351, 173.677>
} 

#declare device_trans_26 =
transform
{
    translate <61.7695, -145.351, 173.677>
}

#declare device_trans_27 =
transform
{
    translate <84.4018, -145.351, 173.677>
}

#declare device_trans_28 =
transform
{
    translate <28.7558, -145.351, 173.677>
} 

#declare device_trans_29 =
transform
{
    translate <51.3881, -145.351, 173.677>
}   

#declare device_trans_30 =
transform
{
    translate <74.0205, -145.351, 173.677>
}  