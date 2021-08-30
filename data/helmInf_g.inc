 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Pilot Helmet                         //
//  Master include file                            //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


// BACKGROUND
#if (defined (bg))
  #declare P_backdrop = light_group
  {
    light_source
    {
      <1000,1000,1000>
      colour rgb <1,1,1>
    }
    sphere
    {
      <0,0,0>, 5000
      pigment { color rgb bg }    
      finish  { ambient 1 diffuse 1 emission 0}
      no_reflection
      no_shadow   
      inverse
    }  
 }

  #declare P_plane =
  plane
  {
   <0, 0, 1>, 0
    pigment { color rgb bg }    
    finish  { diffuse 1 }
    no_reflection
  }
#end

// TEXTURES

// mohawk
#declare T_mohawk = 
texture { T_posrank }

// helmet
#declare T_helmet = 
texture { T_helm }


// implogo
#declare T_implogo = 
texture { T_logo }

// jawlogo
#declare T_jawlogo = 
texture { T_logo2 }