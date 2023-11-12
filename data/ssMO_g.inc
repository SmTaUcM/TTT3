 ////////////////////////////////////////////////////
//                                                 //
//  Silver Star of the Empire                      //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "ss_o.inc";    


// RIBBON


#declare T_ss = 
texture
{
  pigment { image_map { gif "medals/ss.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer }    


// SS


#declare P_ss_body =
union
{
  object { P_cloth texture { T_ss } }
  object { P_bar texture { T_silver } }   
  #if (mab_ss = 1) object { P_mab01 } #end
  #if (mab_ss = 2) object { P_mab02 } #end
  #if (mab_ss = 3) object { P_mab03 } #end
  #if (mab_ss = 4) object { P_mab04 } #end
  #if (mab_ss >= 10) object { P_mab10 } #else
    #if (mab_ss >= 5) object { P_mab05 } #end
  #end
}
                 
                 
#declare P_ss_1_1 =
union
{
  object
  {
    P_ss_body
    translate <50.4533,-145.351,150.246>
  }
  object
  {
    P_ss
    translate <50.4123,-144.78,114.8>
  }
}  

#declare P_ss_2_1 =
union
{ 
  object
  {
    P_ss_body
    translate <38.71175,-145.351,150.253> 
  }
  object
  {
    P_ss
    translate <38.67075,-144.78,114.61>
  }
}

#declare P_ss_2_2 =
union
{ 
  object
  {
    P_ss_body
    translate <62.19475,-145.351,150.253> 
  }
  object
  {
    P_ss
    translate <62.15375,-144.78,114.61>
  }
}

#declare P_ss_3_1 =
union
{ 
  object
  {
    P_ss_body
    translate <26.9703,-145.351,150.246> 
  }
  object
  {
    P_ss
    translate <26.9293,-144.78,114.8>
  }
}   

#declare P_ss_3_2 = P_ss_1_1;

#declare P_ss_4_1 =
union
{ 
  object
  {
    P_ss_body
    translate <15.22875,-145.351,150.253> 
  }
  object
  {
    P_ss
    translate <15.18775,-144.78,114.61>
  }
}   

#declare P_ss_4_2 = P_ss_2_1;

#declare P_ss_5_2 = P_ss_3_2;



          


