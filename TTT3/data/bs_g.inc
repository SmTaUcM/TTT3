 ////////////////////////////////////////////////////
//                                                 //
//  Bronze Star of the Empire                      //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "bs_o.inc";    


// RIBBON


#declare T_bs = 
texture
{
  pigment { image_map { gif ".\medals\bs.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer }    


// BS


#declare P_bs_body =
union
{
  object { P_cloth texture { T_bs } }
  object { P_bar texture { T_bronze } }   
  #if (mab_bs = 1) object { P_mab01 } #end
  #if (mab_bs = 2) object { P_mab02 } #end
  #if (mab_bs = 3) object { P_mab03 } #end
  #if (mab_bs = 4) object { P_mab04 } #end
  #if (mab_bs >= 10) object { P_mab10 } #else
    #if (mab_bs >= 5) object { P_mab05 } #end
  #end
}
                 
                 
#declare P_bs_1_1 =
union
{
  object
  {
    P_bs_body
    rotate <-6.909,1.128,7.168>
    translate <51.211,-141.995,150.247>
  }
  object
  {
    P_bs
    rotate <-0.909,1.128,5.168>
    translate <50.9,-144.5,114.9>
  }
}  

#declare P_bs_2_1 =
union
{ 
  object
  {
    P_bs_body
    rotate <-6.937,0.941,7.689>
    translate <39.41,-143.793,150.253>
  }
  object
  {
    P_bs
    rotate <-0.937,0.941,3.878>
    translate <39.205,-146.2,114.725>
  }
}

#declare P_bs_2_2 =
union
{ 
  object
  {
    P_bs_body
    rotate <-5.924,0.957,9.14>
    translate <62.893,-140.046,150.297>
  }
  object
  {
    P_bs
    rotate <0.076,0.957,5.14>
    translate <62.65,-141.776,114.75>
  }
}

#declare P_bs_3_1 =
union
{ 
  object
  {
    P_bs_body
    rotate <-6.954,0.805,6.569>
    translate <27.655,-145.351,150.246> 
  }
  object
  {
    P_bs
    rotate <-0.954,0.805,1.569>
    translate <27.55,-147.9,114.8>
  }
}   

#declare P_bs_3_2 = P_bs_1_1;

#declare P_bs_3_3 =
union
{ 
  object
  {
    P_bs_body
    rotate <-6.843,1.476,12.116>
    translate <74.576,-137.43,150.248> 
  }
  object
  {
    P_bs
    rotate <-0.843,1.476,12.116>
    translate <74.13,-139.617,114.65>
  }
}   

#declare P_bs_4_2 = P_bs_2_1;

#declare P_bs_4_3 = P_bs_2_2;

#declare P_bs_5_3 = P_bs_3_3;



          


