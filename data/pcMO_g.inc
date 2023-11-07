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
  pigment { image_map { gif "medals/pc.gif" } }
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
    translate <51.211,-145.351,150.246>
  }
  object
  {
    P_pc
    translate <51.17,-145.351,116.2>
  }
}  

#declare P_pc_2_1 =
union
{ 
  object
  {
    P_pc_body
    translate <39.41,-145.351,150.246>
  }
  object
  {
    P_pc
    translate <39.4,-145.351,116.2>
  }
}

#declare P_pc_2_2 =
union
{ 
  object
  {
    P_pc_body
    translate <62.893,-145.351,150.246> 
  }
  object
  {
    P_pc
    translate <62.95,-143.78,116.25>
  }
}

#declare P_pc_3_2 = P_pc_1_1;

#declare P_pc_3_3 =
union
{ 
  object
  {
    P_pc_body
    translate <74.576,-145.351,150.246>
  }
  object
  {
    P_pc
    translate <74.75,-143.351,114.8>
  }
}   

#declare P_pc_4_3 = P_pc_2_2;

#declare P_pc_4_4 =
union
{ 
  object
  {
    P_pc_body
    translate <86.294,-146.746,150.253> 
  }
  object
  {
    P_pc
    translate <86.8,-142.78,116.25>
  }
}   

#declare P_pc_5_4 =
union
{ 
  object
  {
    P_pc_body
    translate <39.381,-142.823,125.443> 
  }
  object
  {
    P_pc
    translate <39.4,-143.096,91.442>
  }
}   



          


