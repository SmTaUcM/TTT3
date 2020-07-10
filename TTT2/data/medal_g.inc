 ////////////////////////////////////////////////////
//                                                 //
//  Ribbon and MABs needed for all medals          //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "medal_o.inc"; 


// MABs
                 

#declare P_mab01 = object { P_mab texture { T_bronze } }

#declare P_mab02 =
union
{
  object { P_mab texture { T_bronze } }
  object { P_mab texture { T_bronze } translate <0,0,4> }
}  

#declare P_mab03 =
union
{
  object { P_mab texture { T_bronze } }
  object { P_mab texture { T_bronze } translate <0,0,4> }
  object { P_mab texture { T_bronze } translate <0,0,8> }
}  

#declare P_mab04 =
union
{
  object { P_mab texture { T_bronze } }
  object { P_mab texture { T_bronze } translate <0,0,4> }
  object { P_mab texture { T_bronze } translate <0,0,8> }
  object { P_mab texture { T_bronze } translate <0,0,12> }
}  

#declare P_mab05 = object { P_mab texture { T_silver } }

#declare P_mab10 = object { P_mab texture { T_gold } }


