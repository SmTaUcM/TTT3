 ////////////////////////////////////////////////////
//                                                 //
//  Gold Star of the Empire                        //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "gs_o.inc";    


// RIBBON


#declare T_gs = 
texture
{
  pigment { image_map { gif "medals/gs.gif" } }
  finish  { fin_T_uni } 
}
texture { T_unilayer }    


// GS


#declare P_gs_body =
union
{
  object { P_cloth texture { T_gs } }
  object { P_bar texture { T_gold } }   
  #if (mab_gs = 1) object { P_mab01 } #end
  #if (mab_gs = 2) object { P_mab02 } #end
  #if (mab_gs = 3) object { P_mab03 } #end
  #if (mab_gs = 4) object { P_mab04 } #end
  #if (mab_gs >= 10) object { P_mab10 } #else
    #if (mab_gs >= 5) object { P_mab05 } #end
  #end
}
                 
                 
#declare P_gs_1_1 =
union
{
  object
  {
    P_gs_body
    translate <51.211,-145.351,150.246>
  }
  union
  {
    object { P_gs_gold }
    object { P_gs_green }
    translate <51.17,-145.78,114.8>
  }
}  

#declare P_gs_2_1 =
union
{ 
  object
  {
    P_gs_body
    translate <39.41,-145.351,150.246>
  }
  union
  {
    object { P_gs_gold }
    object { P_gs_green }
    translate <39.35,-145.78,114.61>
  }
}

#declare P_gs_3_1 =
union
{ 
  object
  {
    P_gs_body
    translate <27.655,-145.351,150.246>
  }
  union
  {
    object { P_gs_gold }
    object { P_gs_green }
    translate <27.75,-145.78,114.8>
  }
}

#declare P_gs_4_1 =
union
{    
  object
  {
    P_gs_body
    translate <15.913,-145.351,150.253> 
  }
  union
  {
    object { P_gs_gold }
    object { P_gs_green }
    translate <15.95,-145.78,114.61>
  }
}

#declare P_gs_5_1 = P_gs_3_1;

          


