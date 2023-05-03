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
 *   (Recommend removing addToRibbonIncludes (TTT3.py line 3260))
 *
 ************************************************************************
 *
 * The current (v3.0.3) method of instantiating ribbons is as such:
 * 
 * object { P_v1 translate <0,0,v2> texture { T_r_v3 } }
 *
 *   with
 * 
 * v1 : int    : Ribbon slot number
 *                 TTT3.py's &NUM&
 * v2 : string : Offset to account for rank plaque
 *                 TTT3.py's yOffset
 * v3 : string : Award name
 *                 TTT3.py's awardName, without the preceding "T_r_".
 *
 * Which needs to be converted into the following:
 * 
 * object { P_ribbon_v3 transform device_trans_v1 translate <0,0,v2> }
 * 
 * Thus, recommend changing TTT3.py lines 874, 887, 894, and 900 to the 
 *   following:
 * 
 * ribbonObjects.append("P_ribbon_%s transform device_trans_&NUM& 
 *   translate <0,0,yOffset>" % (awardName, yOffset))
 *
 * Based on the current methods of creating the dress.pov, no additional
 * changes should be necessary to TTT3.py
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


#declare T_diamond =
texture
{
  pigment { color rgb <0.58, 0.58, 0.58> }
  finish  { fin_T_metal }
}

#declare T_red =
texture
{
  pigment { color rgb <0.5,0.25,0.25> }
  finish { fin_T_dullmetal }
}

#declare T_green =
texture
{
  pigment { color rgb <0.25,0.5,0.25> }
  finish { fin_T_dullmetal }
}

#declare T_blue =
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
union
{
  object { P_single_ribbon texture { T_r_iar } }
}

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
union
{
  object { P_single_ribbon texture { T_r_moi } }
}

#declare P_ribbon_moi_bc =
union
{
  object { P_single_ribbon texture { T_r_moi } }
  object { P_cross_ribbon_device texture { T_blue } }
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
  object { P_cross_ribbon_device texture { T_green } }
}

#declare P_ribbon_moi_dc =
union
{
  object { P_single_ribbon texture { T_r_moi } }
  object { P_cross_ribbon_device texture { T_diamond } }
}

// MEDAL OF SCHOLARSHIP

#declare P_ribbon_mos =
union
{
  object { P_single_ribbon texture { T_r_mos } }
}

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
   object { P_oak_cluster_ribbon_device texture { T_diamond } }
}

// TIE CORPS COMMANDER'S UNIT AWARD

#declare P_ribbon_tua =
union
{
  object { P_single_ribbon texture { T_r_tua } }
}

#declare P_ribbon_tua_b =
union
{
  object { P_single_ribbon texture { T_r_tua } }
  object { P_wings_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_tua_s =
union
{
  object { P_single_ribbon texture { T_r_tua } }
  object { P_wings_ribbon_device texture { T_silver } }
}

#declare P_ribbon_tua_g =
union
{
  object { P_single_ribbon texture { T_r_tua } }
  object { P_wings_ribbon_device texture { T_gold } }
}

// TIE CORPS MERITORIOUS UNIT AWARD

#declare P_ribbon_mua =
union
{
  object { P_single_ribbon texture { T_r_mua } }
}

#declare P_ribbon_mua_b =
union
{
  object { P_single_ribbon texture { T_r_mua } }
  object { P_wings_ribbon_device texture { T_bronze } }
}

#declare P_ribbon_mua_s =
union
{
  object { P_single_ribbon texture { T_r_mua } }
  object { P_wings_ribbon_device texture { T_silver } }
}

#declare P_ribbon_mua_g =
union
{
  object { P_single_ribbon texture { T_r_mua } }
  object { P_wings_ribbon_device texture { T_gold } }
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
union
{
  object { P_single_ribbon texture { T_r_loc } }
}

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
  object { P_scimitar_ribbon_device texture { T_green } }
}

#declare P_ribbon_loc_ts =
union
{
  object { P_single_ribbon texture { T_r_loc } }
  object { P_scimitar_ribbon_device texture { T_blue } }
}

#declare P_ribbon_loc_rs =
union
{
  object { P_single_ribbon texture { T_r_loc } }
   object { P_scimitar_ribbon_device texture { T_red } }
}

#declare P_ribbon_loc_ps =
union
{
  object { P_single_ribbon texture { T_r_loc } }
  object { P_scimitar_ribbon_device texture { T_platinum } }
}

// LEGION OF SKIRMISH

#declare P_ribbon_los =
union
{
  object { P_single_ribbon texture { T_r_los } }
}

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
  object { P_scimitar_ribbon_device texture { T_green } }
}

#declare P_ribbon_los_ts =
union
{
  object { P_single_ribbon texture { T_r_los } }
  object { P_scimitar_ribbon_device texture { T_blue } }
}

#declare P_ribbon_los_rs =
union
{
  object { P_single_ribbon texture { T_r_los } }
  object { P_scimitar_ribbon_device texture { T_red } }
}

#declare P_ribbon_los_ps =
union
{
  object { P_single_ribbon texture { T_r_los } }
  object { P_scimitar_ribbon_device texture { T_platinum } }
}

// DISTINGUISHED FLYING CROSS

#declare P_ribbon_dfc =
union
{
  object { P_single_ribbon texture { T_r_dfc } }
}

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
union
{
  object { P_single_ribbon texture { T_r_ora } }
}

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
union
{
  object { P_single_ribbon texture { T_r_loa } }
}

// ORDER OF THE VANGUARD

#declare P_ribbon_ov_1e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
}

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
  object { P_echelon_ribbon_device texture { T_blue } translate <0,0,0> }
}

#declare P_ribbon_ov_12e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
}

#declare P_ribbon_ov_13e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
}

#declare P_ribbon_ov_14e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_15e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
} 
 

#declare P_ribbon_ov_16e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <1.385,0,0> }
}

#declare P_ribbon_ov_17e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
} 
 
#declare P_ribbon_ov_18e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_19e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_20e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-6.885,0,0> } 
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
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <1.385,0,0> }
}

#declare P_ribbon_ov_22e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
}

#declare P_ribbon_ov_23e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_24e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_25e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}

#declare P_ribbon_ov_26e =
union
{ 
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <2.75,0,0> }
}

#declare P_ribbon_ov_27e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_28e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_29e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}
 
#declare P_ribbon_ov_30e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-8.25,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
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
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <2.75,0,0> }
}

#declare P_ribbon_ov_32e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
}

#declare P_ribbon_ov_33e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_34e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}

#declare P_ribbon_ov_35e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-8.25,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <8.25,0,0> }
}

#declare P_ribbon_ov_36e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <4.135,0,0> }
}

#declare P_ribbon_ov_37e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <0,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <2.75,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <5.5,0,0> }
}

#declare P_ribbon_ov_38e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-6.885,0,0> } 
  object { P_echelon_ribbon_device texture { T_blue } translate <-4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_gold } translate <1.385,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <4.135,0,0> }
  object { P_echelon_ribbon_device texture { T_platinum } translate <6.885,0,0> }
}

#declare P_ribbon_ov_39e =
union
{
  object { P_single_ribbon texture { T_r_oov } }
  object { P_echelon_ribbon_device texture { T_blue } translate <-8.25,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-5.5,0,0> }
  object { P_echelon_ribbon_device texture { T_blue } translate <-2.75,0,0> }
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
    rotate <-11.9, 0, 6.18>
    translate <16.5048, -138.079, 205.658>
} 

#declare device_trans_1 =
transform
{
    rotate <-11.15, 0, 7.09>
    translate <39.1371, -135.535, 205.658>
} 

#declare device_trans_2 =
transform
{
    rotate <-10.8, 0, 9.55>
    translate <61.7695, -132.244, 205.658>
} 

#declare device_trans_3 =
transform
{
    rotate <-10.4, 0, 13.3>
    translate <84.4018, -127.661, 205.658>
} 

// ROW 2

#declare device_trans_4 =
transform
{
    rotate <-11.8, 0, 6.18>
    translate <16.6633, -139.167, 200.323>
} 

#declare device_trans_5 =
transform
{
    rotate <-11.03, 0, 7.09>
    translate <39.2957, -136.623, 200.323>
}  

#declare device_trans_6 =
transform
{
    rotate <-10.7, 0, 9.55>
    translate <61.928, -133.332, 200.323>
} 

#declare device_trans_7 =
transform
{
    rotate <-10.5, 0, 13.3>
    translate <84.5604, -128.75, 200.323>
}  

// ROW 3

#declare device_trans_8 =
transform
{
    rotate <-11.7, 0, 6.18>
    translate <16.8186, -140.253, 194.994>
}  

#declare device_trans_9 =
transform
{
    rotate <-11.0, 0, 7.09>
    translate <39.4509, -137.65, 194.994>
}  

#declare device_trans_10 =
transform
{
    rotate <-10.5, 0, 9.55>
    translate <62.0833, -134.336, 194.994>
} 

#declare device_trans_11 =
transform
{
    rotate <-10.6, 0, 13.3>
    translate <84.7156, -129.758, 194.994>
} 

// ROW 4

#declare device_trans_12 =
transform
{
    rotate <-11.6, 0, 6.18>
    translate <16.9739, -141.339, 189.665>
} 

#declare device_trans_13 =
transform
{
    rotate <-10.84, 0, 7.09>
    translate <39.6062, -138.676, 189.665>
} 

#declare device_trans_14 =
transform
{
    rotate <-10.6, 0, 9.55>
    translate <62.2385, -135.332, 189.665>
} 

#declare device_trans_15 =
transform
{
    rotate <-10.6, 0, 13.3>
    translate <84.8709, -130.76, 189.665>
} 

// ROW 5

#declare device_trans_16 =
transform
{
    rotate <-11.3, 0, 6.18>
    translate <17.1291, -142.425, 184.335>
} 

#declare device_trans_17 =
transform
{
    rotate <-10.93, 0, 7.09>
    translate <39.7615, -139.703, 184.335>
} 

#declare device_trans_18 =
transform
{
    rotate <-9.7, 0, 9.55>
    translate <62.3938, -136.329, 184.335>
} 

#declare device_trans_19 =
transform
{
    rotate <-5.63, 0, 14.4>
    translate <85.0261, -131.514, 184.335>
} 

// ROW 6

#declare device_trans_20 =
transform
{
    rotate <-7.87, 0, 6.49>
    translate <17.2844, -143.483, 179.006>
}  

#declare device_trans_21 =
transform
{
    rotate <-6.77, 0, 7.78>
    translate <39.9167, -140.629, 179.006>
} 

#declare device_trans_22 =
transform
{
    rotate <-4.83, 0, 10.48>
    translate <62.5491, -136.98, 179.006>
} 

#declare device_trans_23 =
transform
{
    rotate <-4.6, 0, 14.4>
    translate <85.1814, -131.986, 179.006>
} 

// ROW 7

#declare device_trans_24 =
transform
{
    rotate <-4.83, 0, 6.53>
    translate <17.4396, -143.919, 173.677>
} 

#declare device_trans_28 =
transform
{
    rotate <-4.6, 0, 7.24>
    translate <28.7558, -142.488, 173.677>
} 

#declare device_trans_25 =
transform
{
    rotate <-4.36, 0, 7.9>
    translate <40.072, -141.036, 173.677>
} 

#declare device_trans_29 =
transform
{
    rotate <-4.36, 0, 8.26>
    translate <51.3881, -139.361, 173.677>
} 

#declare device_trans_26 =
transform
{
    rotate <-4.24, 0, 10.52>
    translate <62.7043, -137.36, 173.677>
}  

#declare device_trans_30 =
transform
{
    rotate <-4.28, 0, 12.5>
    translate <74.0205, -135.171, 173.677>
} 

#declare device_trans_27 =
transform
{
    rotate <-4.71, 0, 14.4>
    translate <85.3367, -132.403, 173.677>
} 