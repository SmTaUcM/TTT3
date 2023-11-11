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
    translate <51.211,-145.351,150.246>
  }
  object
  {
    P_ss
    translate <51.17,-144.78,114.8>
  }
}  

#declare P_ss_2_1 =
union
{ 
  object
  {
    P_ss_body
    translate <39.41,-145.351,150.253> 
  }
  object
  {
    P_ss
    translate <39.35,-144.78,114.61>
  }
}

#declare P_ss_2_2 =
union
{ 
  object
  {
    P_ss_body
    translate <62.893,-145.351,150.253> 
  }
  object
  {
    P_ss
    translate <63.0,-144.78,114.61>
  }
}

#declare P_ss_3_1 =
union
{ 
  object
  {
    P_ss_body
    translate <27.655,-145.351,150.246> 
  }
  object
  {
    P_ss
    translate <27.75,-144.78,114.8>
  }
}   

#declare P_ss_3_2 = P_ss_1_1;

#declare P_ss_4_1 =
union
{ 
  object
  {
    P_ss_body
    translate <15.913,-145.351,150.253> 
  }
  object
  {
    P_ss
    translate <15.95,-144.78,114.61>
  }
}   

#declare P_ss_4_2 = P_ss_2_1;

#declare P_ss_5_2 = P_ss_3_2;



          


