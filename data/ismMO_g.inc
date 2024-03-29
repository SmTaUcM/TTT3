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
    translate <50.4533,-145.351,150.246>
  }
  object
  {
    P_ism
    translate <50.4123,-141.78,116.2>
  }
}  

#declare P_ism_2_2 =
union
{ 
  object
  {
    P_ism_body
    translate <62.19475,-145.351,150.246>
  }
  object
  {
    P_ism
    translate <62.25,-141.78,116.25>
  }
}

#declare P_ism_3_3 =
union
{ 
  object
  {
    P_ism_body
    translate <73.9363,-145.351,150.246>
  }
  object
  {
    P_ism
    translate <74.15,-141.78,116.25>
  }
}   

#declare P_ism_4_4 =
union
{ 
  object
  {
    P_ism_body
    translate <85.67775,-145.351,150.253> 
  }
  object
  {
    P_ism
    translate <86.0,-141.78,116.25>
  }
}   

#declare P_ism_5_5 =
union
{ 
  object
  {
    P_ism_body
    translate <62.19475,-142.746,125.443> 
  }
  object
  {
    P_ism
    translate <62.25,-142.096,91.442>
  }
}   



          


