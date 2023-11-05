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
  pigment { image_map { gif "medals/bs.gif" } }
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
    translate <51.211,-145.351,150.246>
  }
  object
  {
    P_bs
    translate <51.17,-144.351,114.8>
  }
}  

#declare P_bs_2_1 =
union
{ 
  object
  {
    P_bs_body
    translate <39.41,-146.746,150.253> 
  }
  object
  {
    P_bs
    translate <39.35,-145.78,114.61>
  }
}

#declare P_bs_2_2 =
union
{ 
  object
  {
    P_bs_body
    translate <62.893,-146.746,150.253> 
  }
  object
  {
    P_bs
    translate <63.0,-144.78,114.61>
  }
}

#declare P_bs_3_1 =
union
{ 
  object
  {
    P_bs_body
    translate <27.655,-145.351,150.246>
  }
  object
  {
    P_bs
    translate <27.75,-145.351,114.8>
  }
}   

#declare P_bs_3_2 = P_bs_1_1;

#declare P_bs_3_3 =
union
{ 
  object
  {
    P_bs_body
    translate <74.576,-145.351,150.246>
  }
  object
  {
    P_bs
    translate <74.75,-143.351,114.8>
  }
}   

#declare P_bs_4_2 = P_bs_2_1;

#declare P_bs_4_3 = P_bs_2_2;

#declare P_bs_5_3 = P_bs_3_3;



          


