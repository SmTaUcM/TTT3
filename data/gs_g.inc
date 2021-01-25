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
  pigment { image_map { gif ".\medals\gs.gif" } }
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
    rotate <-6.909,1.128,7.168>
    translate <51.211,-141.995,150.247>
  }
  union
  {
    object { P_gs_gold }
    object { P_gs_green }
    rotate <-0.909,1.128,5.168>
    translate <50.9,-144.5,114.9>
  }
}  

#declare P_gs_2_1 =
union
{ 
  object
  {
    P_gs_body
    rotate <-6.937,0.941,7.689>
    translate <39.41,-143.793,150.253>
  }
  union
  {
    object { P_gs_gold }
    object { P_gs_green }
    rotate <-0.937,0.941,3.878>
    translate <39.205,-146.2,114.725>
  }
}

#declare P_gs_3_1 =
union
{ 
  object
  {
    P_gs_body
    rotate <-6.954,0.805,6.569>
    translate <27.655,-145.351,150.246>
  }
  union
  {
    object { P_gs_gold }
    object { P_gs_green }
    rotate <-0.954,0.805,1.569>
    translate <27.55,-147.9,114.8>
  }
}

#declare P_gs_4_1 =
union
{    
  object
  {
    P_gs_body
    rotate <-6.941,0.91,7.429>
    translate <15.913,-146.746,150.253> 
  }
  union
  {
    object { P_gs_gold }
    object { P_gs_green }
    rotate <-0.941,0.91,-4.308>
    translate <15.81,-148.78,114.61>
  }
}

#declare P_gs_5_1 = P_gs_3_1;

          


