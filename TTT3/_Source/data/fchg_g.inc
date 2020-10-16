 ////////////////////////////////////////////////////
//                                                 //
//  Fleet Commander's Honor Guard (FCHG) insignia  //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


// RIBBONS


#declare T_gren = 
texture
{
  pigment { image_map { gif ".\fchg\01_gren.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}
          
#declare T_lanc = 
texture
{
  pigment { image_map { gif ".\fchg\02_lanc.gif" } }
  finish  { fin_T_uni } 
}

texture { T_unilayer scale 2}

#declare T_huss = 
texture
{
  pigment { image_map { gif ".\fchg\03_huss.gif" } }
  finish  { fin_T_uni } 
}                                          
texture { T_unilayer scale 2}   

#declare T_fusl = 
texture
{
  pigment { image_map { gif ".\fchg\04_fusl.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_drag = 
texture
{
  pigment { image_map { gif ".\fchg\05_drag.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_cavl = 
texture
{
  pigment { image_map { gif ".\fchg\06_cavl.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_gall = 
texture
{
  pigment { image_map { gif ".\fchg\07_gall.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_kngt = 
texture
{
  pigment { image_map { gif ".\fchg\08_kngt.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_pldn = 
texture
{
  pigment { image_map { gif ".\fchg\09_pldn.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_lgnr = 
texture
{
  pigment { image_map { gif ".\fchg\10_lgnr.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}
                 
#declare T_aqfr = 
texture
{
  pigment { image_map { gif ".\fchg\11_aqfr.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_dcrn = 
texture
{
  pigment { image_map { gif ".\fchg\12_dcrn.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_tsrs = 
texture
{
  pigment { image_map { gif ".\fchg\13_tsrs.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_opti = 
texture
{
  pigment { image_map { gif ".\fchg\14_opti.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_cntr = 
texture
{
  pigment { image_map { gif ".\fchg\15_cntr.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_excr = 
texture
{
  pigment { image_map { gif ".\fchg\16_excr.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_gldr = 
texture
{
  pigment { image_map { gif ".\fchg\17_gldr.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_arcn = 
texture
{
  pigment { image_map { gif ".\fchg\18_arcn.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_tmpr = 
texture
{
  pigment { image_map { gif ".\fchg\19_tmpr.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}

#declare T_impr = 
texture
{
  pigment { image_map { gif ".\fchg\20_impr.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 2}
            

// OBJECTS

                 
#include "fchg_o.inc";


#declare gren =
union
{
  object { P_base }
  object { P_bronze1 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_gren } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare lanc =
union
{
  object { P_base }
  object { P_bronze2 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_lanc } translate <0,1.6,0> }  
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare huss =
union
{
  object { P_base }
  object { P_bronze3 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_huss } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare fusl =
union
{
  object { P_base }
  object { P_bronze4 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_fusl } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare drag =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_drag } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare cavl =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver1 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_cavl } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare gall =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver2 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_gall } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare kngt =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver3 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_kngt } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare pldn =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver4 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_pldn } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare lgnr =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver5 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_lgnr } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare aqfr =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_aqfr } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare dcrn =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold1 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_dcrn } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare tsrs =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold2 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_tsrs } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare opti =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold3 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_opti } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare cntr =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold4 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_cntr } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare excr =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold5 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_excr } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare gldr =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_gldr } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare arcn =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_laurel texture { T_bronze } }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_arcn } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare tmpr =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_laurel texture { T_silver } }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_tmpr } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare impr =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_laurel texture { T_gold } }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_impr } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}
