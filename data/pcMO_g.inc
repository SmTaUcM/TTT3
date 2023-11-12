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
    translate <50.4533,-145.351,150.246>
  }
  object
  {
    P_pc
    translate <50.4123,-142.78,116.2>
  }
}  

#declare P_pc_2_1 =
union
{ 
  object
  {
    P_pc_body
    translate <38.71175,-145.351,150.246>
  }
  object
  {
    P_pc
    translate <38.55,-142.78,116.2>
  }
}

#declare P_pc_2_2 =
union
{ 
  object
  {
    P_pc_body
    translate <62.19475,-145.351,150.246> 
  }
  object
  {
    P_pc
    translate <62.25,-142.78,116.25>
  }
}

#declare P_pc_3_2 = P_pc_1_1;

#declare P_pc_3_3 =
union
{ 
  object
  {
    P_pc_body
    translate <73.9363,-145.351,150.246>
  }
  object
  {
    P_pc
    translate <74.15,-142.78,116.25>
  }
}   

#declare P_pc_4_3 = P_pc_2_2;

#declare P_pc_4_4 =
union
{ 
  object
  {
    P_pc_body
    translate <85.67775,-145.351,150.253> 
  }
  object
  {
    P_pc
    translate <85.89145,-142.78,116.25>
  }
}   

#declare P_pc_5_4 =
union
{ 
  object
  {
    P_pc_body
    translate <38.71175,-142.746,125.443> 
  }
  object
  {
    P_pc
    translate <38.75,-143.096,91.442>
  }
}   



          


