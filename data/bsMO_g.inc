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
    translate <50.4533,-145.351,150.246>
  }
  object
  {
    P_bs
    translate <50.4123,-143.78,114.8>
  }
}  

#declare P_bs_2_1 =
union
{ 
  object
  {
    P_bs_body
    translate <38.71175,-145.351,150.253> 
  }
  object
  {
    P_bs
    translate <38.67075,-143.78,114.61>
  }
}

#declare P_bs_2_2 =
union
{ 
  object
  {
    P_bs_body
    translate <62.19475,-145.351,150.253> 
  }
  object
  {
    P_bs
    translate <62.15375,-143.78,114.61>
  }
}

#declare P_bs_3_1 =
union
{ 
  object
  {
    P_bs_body
    translate <26.9703,-145.351,150.246>
  }
  object
  {
    P_bs
    translate <26.9293,-143.78,114.8>
  }
}   

#declare P_bs_3_2 = P_bs_1_1;

#declare P_bs_3_3 =
union
{ 
  object
  {
    P_bs_body
    translate <73.9363,-145.351,150.246>
  }
  object
  {
    P_bs
    translate <73.9773,-143.78,114.8>
  }
}   

#declare P_bs_4_2 = P_bs_2_1;

#declare P_bs_4_3 = P_bs_2_2;

#declare P_bs_5_3 = P_bs_3_3;



          


