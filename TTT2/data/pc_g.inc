 ////////////////////////////////////////////////////
//                                                 //
//  Palpatine Crescent                             //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "pc_o.inc";    


// RIBBON


#declare T_pc = 
texture
{
  pigment { image_map { gif ".\medals\pc.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer }    


// PC


#declare P_pc_body =
union
{
  object { P_cloth texture { T_pc } }
  object { P_bar texture { T_copper } }   
  #if (mab_pc = 1) object { P_mab01 } #end
  #if (mab_pc = 2) object { P_mab02 } #end
  #if (mab_pc = 3) object { P_mab03 } #end
  #if (mab_pc = 4) object { P_mab04 } #end
  #if (mab_pc >= 10) object { P_mab10 } #else
    #if (mab_pc >= 5) object { P_mab05 } #end
  #end
}
                 
                 
#declare P_pc_1_1 =
union
{
  object
  {
    P_pc_body
    rotate <-6.909,1.128,7.168>
    translate <51.211,-141.995,150.247>
  }
  object
  {
    P_pc
    rotate <-0.909,1.128,5.168>
    translate <50.839,-144.4,116.5>
  }
}  

#declare P_pc_2_1 =
union
{ 
  object
  {
    P_pc_body
    rotate <-6.937,0.941,7.689>
    translate <39.41,-143.793,150.253>
  }
  object
  {
    P_pc
    rotate <-0.937,0.941,3.878>
    translate <39.3,-146,116.5>
  }
}

#declare P_pc_2_2 =
union
{ 
  object
  {
    P_pc_body
    rotate <-5.924,0.957,9.14>
    translate <62.893,-140.046,150.297>
  }
  object
  {
    P_pc
    rotate <0.076,0.957,5.14>
    translate <62.85,-141.7,116.55>
  }
}

#declare P_pc_3_2 = P_pc_1_1;

#declare P_pc_3_3 =
union
{ 
  object
  {
    P_pc_body
    rotate <-6.843,1.476,12.116>
    translate <74.576,-137.43,150.248> 
  }
  object
  {
    P_pc
    rotate <-0.843,1.476,12.116>
    translate <74.13,-139.617,116.441>
  }
}   

#declare P_pc_4_3 = P_pc_2_2;

#declare P_pc_4_4 =
union
{ 
  object
  {
    P_pc_body
    rotate <-5.81,1.501,14.439>
    translate <86.294,-134.413,150.292> 
  }
  object
  {
    P_pc
    rotate <0.19,1.501,14.439>
    translate <85.9,-136,116.43>
  }
}   

#declare P_pc_5_4 =
union
{ 
  object
  {
    P_pc_body
    rotate <-0.989,0.145,8.329>
    translate <39.381,-143.823,125.443> 
  }
  object
  {
    P_pc
    rotate <0.011,0.145,1.619>
    translate <39.5,-144.096,91.442>
  }
}   



          


