 ////////////////////////////////////////////////////
//                                                 //
//  Imperial Security Medal                        //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "ism_o.inc";    


// RIBBON


#declare T_ism = 
texture
{
  pigment { image_map { gif "medals/ism.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer }    


// ISM


#declare P_ism_body =
union
{
  object { P_cloth texture { T_ism } }
  object { P_bar texture { T_silver } }   
  #if (mab_ism = 1) object { P_mab01 } #end
  #if (mab_ism = 2) object { P_mab02 } #end
  #if (mab_ism = 3) object { P_mab03 } #end
  #if (mab_ism = 4) object { P_mab04 } #end
  #if (mab_ism >= 10) object { P_mab10 } #else
    #if (mab_ism >= 5) object { P_mab05 } #end
  #end
}
                 
                 
#declare P_ism_1_1 =
union
{
  object
  {
    P_ism_body
    rotate <-6.909,1.128,7.168>
    translate <51.211,-141.995,150.247>
  }
  object
  {
    P_ism
    rotate <-0.909,1.128,5.168>
    translate <50.839,-144.4,116.5>
  }
}  

#declare P_ism_2_2 =
union
{ 
  object
  {
    P_ism_body
    rotate <-5.924,0.957,9.14>
    translate <62.893,-140.046,150.297>
  }
  object
  {
    P_ism
    rotate <0.076,0.957,5.14>
    translate <62.85,-141.7,116.55>
  }
}

#declare P_ism_3_3 =
union
{ 
  object
  {
    P_ism_body
    rotate <-6.843,1.476,12.116>
    translate <74.576,-137.43,150.248> 
  }
  object
  {
    P_ism
    rotate <-0.843,1.476,12.116>
    translate <74.13,-139.617,116.441>
  }
}   

#declare P_ism_4_4 =
union
{ 
  object
  {
    P_ism_body
    rotate <-5.81,1.501,14.439>
    translate <86.294,-134.413,150.292> 
  }
  object
  {
    P_ism
    rotate <0.19,1.501,14.439>
    translate <85.9,-136,116.43>
  }
}   

#declare P_ism_5_5 =
union
{ 
  object
  {
    P_ism_body
    rotate <-0.983,0.186,11.696>
    translate <62.829,-140.079,125.443> 
  }
  object
  {
    P_ism
    rotate <-0.048,-0.105,7.406>
    translate <62.8,-139.909,91.442>
  }
}   



          


