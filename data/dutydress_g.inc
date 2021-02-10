 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Duty and Dress Uniform               //
//  Shared include file                            //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


// BACKGROUND


#if (defined (bg))
  light_group
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
      finish  { ambient 1 diffuse 1 emission 0 }
      no_reflection
      no_shadow   
      inverse
    }  
  }
#end
   

// REFLECTION MAP


sphere
{
  <0,0,0>, 600
  pigment
  {
    image_map
    {
      jpeg "misc/refmap.jpg" 
      map_type 1
      interpolate 2
    }
  }
  finish  { ambient 1 diffuse 1 emission 0 }
  no_image
  no_shadow   
  inverse
  rotate <90,0,0>
}  


// UNIFORM

     
#if (cloth = 0)  
  #declare mipdist = vlength(locus-trace(P_uniform,locus,lookat-locus));
  #if (mipdist < 520)  
    #declare clothdetail = 3;
    #if (mipdist < 380)  
      #declare clothdetail = 2;
      #if (mipdist < 300)  
        #declare clothdetail = 1;
      #end
    #end
  #else #declare clothdetail = 4;
  #end
  #if (image_width >= 900)
    #declare clothdetail = max(1,(clothdetail - 1));
    #if (image_width >= 1100)
      #declare clothdetail = max(1,(clothdetail - 1));
      #if (image_width >= 1600)
        #declare clothdetail = max(1,(clothdetail - 1));
      #end
    #end
  #end
  #declare clothtex = concat(".\\misc\\cloth", str(clothdetail,0,0), ".jpg");
  #debug concat("Auto cloth detail: using ",clothtex,"\n") 
  //#debug concat("Distance camera - uniform: ", str(mipdist,6,1), "\n")
#else #declare clothtex = concat(".\\misc\\cloth", str(cloth,0,0), ".jpg"); 
#end
//#declare clothtex = ".\\misc\\cloth4.jpg"; 
                                            
#declare fin_T_uni = 
finish
{
  ambient 0.3
  diffuse 0.6 
  specular 0.02
  emission 0
}   

#declare norm_T_uni = 
normal
{
  bump_map
  {
    jpeg "misc/unibump.jpg"
    bump_size 1.4
  }
}


#declare T_unilayer = 
texture
{
  pigment
  {
    image_map
    {
      jpeg clothtex
      transmit all 0.7
    }
  }
  finish  { fin_T_uni } 
}    
                
                
// SEAMS


#declare T_seams = 
texture
{
  pigment
  {
    color rgbt <0, 0, 0, 0.9>
  }

  finish { fin_T_uni }
}


// BELT BUCKLE


#declare fin_T_metal = 
finish 
{            
  phong 1
  phong_size 250
  ambient 0.6
  specular 0.6 
  roughness 0.05 
  brilliance 5  
  emission 0  
  reflection
  
  {
    0.45
    metallic  
    exponent 0.75 
  }
}

#declare T_buckle = 
texture
{
  pigment
  {
    color rgb <0.45,0.45,0.5>
  }
  finish  { fin_T_metal } 
}


// BELT


#declare T_belt = 
texture
{
  pigment
  {
    color rgb <0.001, 0.001, 0.001>
  }
  finish
  {
    ambient 0.3
    diffuse 0.6
    specular 0.2
	emission 0
  }
}


// RANK


#declare fin_T_panel = 
finish 
{            
  phong 1
  phong_size 250
  reflection 0.2
  ambient rgb 0.3
  metallic
  specular 0.6
  emission 0
}

#declare T_panel = 
texture
{
  pigment
  {
    color rgb <0.35,0.35,0.4>
  }
  finish  { fin_T_panel } 
}

#declare fin_T_box = 
finish 
{            
  phong 0.1
  phong_size 160
  reflection 0.1
  ambient rgb 0.7
  specular 0.1
  diffuse 0.5
  emission 0
}

#declare T_rankblue = 
texture
{
  pigment
  {
    color rgb <0.05,0.17,0.445>
  }
  finish  { fin_T_box } 
}

#declare T_rankred = 
texture
{
  pigment
  {
    color rgb <0.387,0.066,0.03>
  }
  finish  { fin_T_box } 
}

#declare T_rankyellow = 
texture
{
  pigment
  {
    color rgb <0.56,0.29,0.09>
  }
  finish  { fin_T_box } 
}
