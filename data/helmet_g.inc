 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Pilot Helmet                         //
//  Master include file                            //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


// BACKGROUND

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
    finish  { ambient 1 diffuse 1}
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


// TEXTURES

// mohawk
#declare T_mohawk = 
texture { T_posrank }

// helmet
#declare T_helmet = 
texture // helmet
{
  pigment { pig_T_helmet }
  finish  { fin_T_helmet } 
}

// ears
#declare T_ears = 
texture
{
  pigment { color rgb <0.94, 0.93, 0.90> }
  finish 
  {
    ambient 0.30
    brilliance 3
    diffuse 0.4
    metallic
    specular 0.70
    roughness 1/60
    reflection 0.25
  }
}

// implogo
#declare T_implogo = 
texture { T_logo }

// jawlogo
#declare T_jawlogo = 
texture { T_logo2 }

// hoses
#declare T_hoses = 
texture // hoses
{
  pigment
  {
    color rgb <0.3, 0.3, 0.3>
  }

  finish
  {
    ambient 0.2
    diffuse 0.4
    phong 0.08
    phong_size 40.0
  }
}


