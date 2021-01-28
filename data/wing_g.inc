/////////////////////////////////////////////////////
//                                                 //
//  Flight Certification Wing insignia             //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
/////////////////////////////////////////////////////


// RIBBONS

#declare T_echelon1 =
texture
{
  pigment { image_map { gif ".\wings\01.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon2 =
texture
{
  pigment { image_map { gif ".\wings\02.gif" } }
  finish  { fin_T_uni }
}

texture { T_unilayer scale 2}

#declare T_echelon3 =
texture
{
  pigment { image_map { gif ".\wings\03.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon4 =
texture
{
  pigment { image_map { gif ".\wings\04.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon5 =
texture
{
  pigment { image_map { gif ".\wings\05.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon6 =
texture
{
  pigment { image_map { gif ".\wings\06.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon7 =
texture
{
  pigment { image_map { gif ".\wings\07.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon8 =
texture
{
  pigment { image_map { gif ".\wings\08.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon9 =
texture
{
  pigment { image_map { gif ".\wings\09.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon10 =
texture
{
  pigment { image_map { gif ".\wings\10.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon11 =
texture
{
  pigment { image_map { gif ".\wings\11.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon12 =
texture
{
  pigment { image_map { gif ".\wings\12.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon13 =
texture
{
  pigment { image_map { gif ".\wings\13.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon14 =
texture
{
  pigment { image_map { gif ".\wings\14.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon15 =
texture
{
  pigment { image_map { gif ".\wings\15.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon16 =
texture
{
  pigment { image_map { gif ".\wings\16.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon17 =
texture
{
  pigment { image_map { gif ".\wings\17.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon18 =
texture
{
  pigment { image_map { gif ".\wings\18.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon19 =
texture
{
  pigment { image_map { gif ".\wings\19.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon20 =
texture
{
  pigment { image_map { gif ".\wings\20.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}

#declare T_echelon21 =
texture
{
  pigment { image_map { gif ".\wings\21.gif" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}


// OBJECTS

#include "wing_o.inc";

#declare echelon1 =
union
{
  object { P_base }
  object { P_bronze1 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_echelon1 } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon2 =
union
{
  object { P_base }
  object { P_bronze2 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_echelon2 } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon3 =
union
{
  object { P_base }
  object { P_bronze3 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_echelon3 } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon4 =
union
{
  object { P_base }
  object { P_bronze4 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_echelon4 } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon5 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_crest texture { T_bronze } translate <0,1.6,0> }
  object { P_ribbon texture { T_echelon5 } translate <0,1.6,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon6 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver1 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_echelon6 } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon7 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver2 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_echelon7 } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon8 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver3 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_echelon8 } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon9 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver4 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_echelon9 } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon10 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver5 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_echelon10 } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon11 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_crest texture { T_silver } translate <0,0.8,0> }
  object { P_ribbon texture { T_echelon11 } translate <0,0.8,0> }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon12 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold1 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon12 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon13 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold2 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon13 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon14 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold3 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon14 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon15 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold4 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon15 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon16 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold5 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon16 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon17 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon17 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon18 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_laurel texture { T_bronze } }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon18 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon19 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_laurel texture { T_silver } }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon19 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon20 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_laurel texture { T_gold } }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon20 } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}

#declare echelon21 =
union
{
  object { P_base }
  object { P_bronze5 }
  object { P_silver6 }
  object { P_gold6 }
  object { P_laurel texture { T_gold } }
  object { P_crest texture { T_gold } }
  object { P_ribbon texture { T_echelon21 } }
  object { P_star texture { T_gold } }
  rotate <-16.477,-1.157,-7.125>
  translate <-52.385,-133.375,216.306>
}
