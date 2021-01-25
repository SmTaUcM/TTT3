 ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Duty Uniform                         //
//  Master include file                            //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////

#include "dutydress_g.inc"

 
// UNIFORM
     
     
#declare norm_T_uni = 
normal
{
  bump_map
  {
    jpeg ".\misc\unibump.jpg"
    #if (strcmp (rank, "GA")) bump_size 1.4
    #else bump_size 1
    #end
  }
}

#declare T_uniform = 
texture
{
  pigment
  {
    #if (defined (prae)) color rgb <0.03, 0.03, 0.03>
    #elseif (!strcmp (rank, "GA")) color rgb 1
    #else color rgb <0.08, 0.08, 0.08>
    #end
  }
  finish  { fin_T_uni } 
  normal  { norm_T_uni } 
}
texture { T_unilayer scale .05 }
       
       
// BUTTONS


#declare T_buttons = 
texture
{
  pigment
  {
	#if (defined (prae)) color rgb <0.6, 0.6, 0.6>
  #else color rgb <0.84,0.62,0.33>
	#end
  }
  finish  { fin_T_metal } 
}


// POSITION 


#declare fin_T_cuffs = 
finish
{            
  ambient rgb 0.3
  diffuse 0.55
  specular 0.3
  roughness 0.2
  reflection 0.1
}
 
#declare norm_T_cuffs = 
normal
{
  bump_map
  {
    gif concat(".\\cuff stripes\\pos", position, ".gif")
    bump_size 2
  }
}
  
#declare T_cuffs = 
texture
{
  material_map
  {
    gif concat(".\\cuff stripes\\pos", position, "2.gif")
    interpolate 2 
    texture 
    { //index 0
      pigment { color rgbt <0, 0, 0, 1> }
      finish  { ambient 1 }  
    }
    texture
    { //index 1
      pigment
      {
        waves
        frequency 32
        color_map
        {
          [0.0 color rgb <0.96,0.7,0.256>]
          [1.0 color rgb <0.7,0.4,0.234>]
        }
      }
      finish { fin_T_cuffs }
      normal { norm_T_cuffs }
    }
  }  
scale <1.1,1,1>   
}  


// TRIMS


#declare fin_T_trim = 
finish
{            
  ambient rgb 0.6
  diffuse 0.5
  specular 0.12
  roughness 0.2  
  reflection 0.1
}
                          
#declare norm_T_trim =
normal
{
  waves
  frequency 9
  bump_size 1.2
}

#declare colour_gold =
color_map
{
  [0.0 colour rgb <1,0.71,0.25>]
  [1.0 colour rgb <0.75,0.4,0.19>]
} 

#declare colour_red =
color_map
{
  [0.0 colour rgb <0.52,0,0>]
  [1.0 colour rgb <0.45,0.01,0.01>]
} 

#declare colour_blue =
color_map
{
  [0.0 colour rgb <0,0.05,0.25>]
  [1.0 colour rgb <0,0.1,0.4>]
} 

#declare colour_purple =
color_map
{
  [0.0 colour rgb <0.15,0,0.35>]
  [1.0 colour rgb <0.25,0,0.45>]
} 

#declare colour_green =
color_map
{
  [0.0 colour rgb <0.05,0.2,0.05>]
  [1.0 colour rgb <0.1,0.3,0.1>]
} 

#declare colour_black =
color_map
{
  [0.0 colour rgb <0.02, 0.02, 0.02>]
  [1.0 colour rgb <0.04, 0.04, 0.04>]
} 

#declare colour_white =
color_map
{
  [0.0 colour rgb <0.6625, 0.6625, 0.6625>]
  [1.0 colour rgb <0.8, 0.8, 0.8>]
}

#declare colour_gray =
color_map
{
  [0.0 colour rgb <0.16, 0.2, 0.2>]
  [1.0 colour rgb <0.36, 0.4, 0.4>]
}

#declare colour_dred =
color_map
{
  [0.0 colour rgb <0.25, 0.0, 0.0>]
  [1.0 colour rgb <0.15, 0.0, 0.0>]
}

#declare colour_dblue =
color_map
{
  [0.0 colour rgb <0,0.09,0.6>]
  [1.0 colour rgb <0,0.09,0.6>]
}
  
#declare pcolour = colour_black;
#if (!strcmp(wing,"Wing I")) #declare pcolour = colour_gray; #end
#if (!strcmp(wing,"Wing II")) #declare pcolour = colour_dred; #end
#if (!strcmp(wing,"Wing VI")) #declare pcolour = colour_red; #end
#if (!strcmp(wing,"Wing X")) #declare pcolour = colour_dblue; #end
#if (!strcmp(wing,"Wing XIX")) #declare pcolour = colour_purple; #end
#if (!strcmp(wing,"Wing XXI")) #declare pcolour = colour_green; #end
#if (!strcmp(category,"flag")) #declare pcolour = colour_gold; #end
#if (!strcmp(squad,"Praetorian")) #declare pcolour = colour_white; #end
#if (!strcmp(squad,"Omega")) #declare pcolour = colour_white; #end
#if (defined (prae)) #declare pcolour = colour_white; #end

#declare T_trim_gold = 
texture
{
  pigment
  {
    waves
    frequency 9
    colour_map { colour_gold } 
  }  
  finish { fin_T_trim }
  normal { norm_T_trim }
}  
texture { T_unilayer scale 80}

#declare T_trim = 
texture
{
  pigment
  {
    waves
    frequency 5
    colour_map { pcolour } 
  }  
  finish { fin_T_trim }
  normal { norm_T_trim }
}  
texture { T_unilayer scale 80}
        

// SHOULDER PAD EMBROIDERMENT


#declare T_pad = 
texture
{
  material_map
  {
    gif ".\misc\ehtc.gif"
    once
    texture 
    { //index 0
      pigment { color rgbt <0, 0, 0, 1> }
      finish  { ambient 1 }  
    }
    texture
    { //index 1
      pigment
      {
        waves
        frequency 12
		    #if (defined (prae)) 
        color_map
        {
          [0.0 colour rgb <0.6625, 0.6625, 0.6625>]
          [1.0 colour rgb <0.8, 0.8, 0.8>]
        } 
		    #else 
		    color_map
			  {
          [0.0 colour rgb <1,0.71,0.25>]
          [1.0 colour rgb <0.75,0.4,0.19>]
        }
		    #end
      }  
      finish { fin_T_trim }
    }
  }  
}  

#declare T_pad_left = texture { T_pad translate <0.03,0.075,0> }
#declare T_pad_right = texture { T_pad translate <0.03,0.035,0> }


// SQUAD PATCH


#declare T_patchlayer1 = 
texture
{
  pigment
  {       
    #if ((file_exists(concat(".\\squads\\", squad, ".png"))) | (file_exists(concat(".\\squads\\", squad, ".png"))))
      #if (file_exists(concat(".\\squads\\", squad, ".bmp")))
        image_map
        {
          sys concat(".\\squads\\", squad, ".bmp")
          interpolate 2
          once
        }
      #end
      #if (file_exists(concat(".\\squads\\", squad, ".png")))
        image_map
        {
          png concat(".\\squads\\", squad, ".png")
          interpolate 2
          once
        }
      #end
    #else color rgbt <0, 0, 0, 1>
    #end
  }
  finish  { fin_T_uni } 
}

#declare T_patchlayer2 = 
texture
{
  pigment
  {
    image_map
    {
      jpeg clothtex
      transmit all 0.85
    }
  }
  scale .45
  finish  { fin_T_uni } 
}    

#declare T_patchcombo = 
texture { T_patchlayer1 }
texture { T_patchlayer2 }

#declare T_patch = 
texture
{
  #if (file_exists(concat(".\\squads\\", squad, "_mask.png")))
  material_map
  {
    png concat(".\\squads\\", squad, "_mask.png")
    once
    texture 
    { //index 0
      pigment { color rgbt <0, 0, 0, 1> }
      finish  { ambient 1 }
    }
    texture 
    { //index 1  
      T_patchcombo
    }
  }     
  #else pigment { color rgbt <0, 0, 0, 1> } // finish { fin_T_uni }
  #end
}

 
// METALS
  
  
#declare fin_T_dullmetal = 
finish 
{            
  reflection 0.2
  ambient 0.3
  metallic
  specular 0.5
}

#declare T_bronze = 
texture
{
  pigment { color rgb <0.35,0.2,0> }
  finish  { fin_T_metal } 
}

#declare T_silver = 
texture
{
  pigment { color rgb <0.4,0.4,0.42> }
  finish  { fin_T_metal } 
}

#declare T_gold = 
texture
{
  pigment { color rgb <0.80,0.57,0.28> }
  finish  { fin_T_metal } 
}

#declare T_metal = 
texture
{
  pigment { color rgb <0.25,0.25,0.27> }
  finish  { fin_T_metal } 
}

#declare T_copper = 
texture
{
  pigment { color rgb <0.56,0.43,0.32> }
  finish  { fin_T_dullmetal } 
}

#declare T_red =
texture
{
  pigment { color rgb <0.25,0,0> }
  finish { fin_T_dullmetal }
}

#declare T_green =
texture
{
  pigment { color rgb <0,0.15,0> }
  finish { fin_T_dullmetal }
}

#declare T_blue =
texture
{
  pigment { color rgb <0.1,0.117,0.348> }
  finish { fin_T_dullmetal }
}


#declare T_dullmetal = 
texture
{
  pigment { color rgb <0.5,0.5,0.52> }
  finish  { fin_T_dullmetal } 
}

#declare T_white =
texture
{
  pigment { color rgb <0.7,0.7,0.7> }
  finish { fin_T_dullmetal }
}

                      
// PLASTIC
                      
                      
#declare fin_T_plastic = 
finish 
{               
  diffuse 0.8
  reflection 0.05
  ambient 0.3
  specular 0.05
  roughness 0.6
}              

#declare T_black =
texture
{
  pigment { color rgb <0.02,0.02,0.02> }
  finish { fin_T_plastic }
}

#declare T_grey = 
texture
{
  pigment { color rgb <0.4,0.4,0.42> }
  finish  { fin_T_plastic } 
}



// MEDALS


#declare T_goe_cloth =
texture
{
  pigment
  {
    image_map
    {
      gif ".\medals\goe.gif"
    }
  }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 1.5 }  

#declare T_ic_cloth =
texture
{
  pigment
  {
    image_map
    {
      gif ".\medals\ic.gif"
    }
  }
  finish  { fin_T_uni } 
}
texture { T_unilayer scale 1.5 }

#declare T_goe_rings = T_silver;
#declare T_ic_rings = T_gold;     


