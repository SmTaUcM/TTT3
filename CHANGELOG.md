# TTT3 Changelog

## Description

TIE Corps Tailoring Tool 3 (TTT3) is the next generation uniform tool for the Emperor's Hammer 
and TIE Corps.  It supports greater integration with the Emperor's Hammer/TIE Corps web site and 
databases, and provides for several new options.

## Important Notes

After importing your profile via the Import tab, please verify the accuracy of all information
before rendering your uniform.

Report problems or concerns to the Internet Office at io@emperorshammer.org, or open an issue 
at https://github.com/emperorshammer/issues-incoming-queue.

## Changelog

## ------------------------------------------------------------------------------------------------##

## [v3.0.0] 2021-05-01

### Added
- At runtime, TTT3 will synchronize with the Emperor's Hammer/TIE Corps database to obtain current
  fleet structure information, unit patches, and unit-specific uniform parameters.  This data is then
  cached locally.
- Added neck ribbon display option.  Members with both the IC and GOE may elect to display both neck
  ribbons and GOE dagger, or only the IC neck ribbon along with the dagger to represent receipt of the
  GOE.
- Implemented the Legion of Skirmish (LoS) for display on the uniform.
- Implemented the Iron Star - Copper Wings (IS-CW) and Copper Ribbon (IS-CR).
- Implemented new TIE Corps awards: TIE Corps Commander's Unit Award (TUA) and TIE Corps Meritorious 
  Unit Award (MUA).
- Implemented new Emperor's Hammer award: Imperial Achievement Ribbon (IAR).
- Added ribbon for display of the Letter of Achievement (LoA).
- Added 'Weapons' tab to facilitate dress/duty uniform lightsaber options and blaster options for the 
  duty uniform.
- Added three additional lightsaber models.  Lightsabers may be displayed on both the duty and dress
  uniforms for members that have achieved the rank of Sith Knight in the Emperor's Hammer Dark
  Brotherhood.
- Added sidearm option for duty uniforms with support for left or right-handed carry of the DH-17 or
  SE-14r.
- Added viewer after successful uniform render, which allows saving the finished uniform to a
  user-specific location as well as the option to open a saved image in your native image viewer.
- Render options: Added option for transparent background.
- Importing of profiles can now be triggered with the 'Enter' key after entering a PIN on the 'Import' 
  tab.
- Medals and Ribbons have largely been removed from the TTT source code and can be added / removed and 
  edited at medals.ini & ribbons.ini for ease of use.  Instructions for use are included within these 
  files.

### Changed
- Update to new Iron Star Ribbon colours for Ribbon variety.
- Complete re-write using Python 3 and QT.
- Improved appearance of wing devices on ribbons (IS, DFC, etc.).
- Expanded Order of the Vanguard to a maximum of 39th echelon.  The base ribbon indicates 1 year of
  service, with a white pip representing an additional year, a gold pip representing 5 years,
  and a (new) blue pip 10 years.
- Only the member's highest Medal of Communication level is displayed.
- Wings for FCHG ranks updated to Flight Certification Wings; added additional 21st Echelon with
  updated 3D model.
- The legacy BGCOM position has been removed, and replaced with TIE Corps Command Staff (TCCS) 
  option.
- The Subgroup Commander (SGCOM) position has been renamed to Group Commanding Officer (GCO).
- Imperial Advisor (IA)/Command Attache (CA) positions support ranks up to Sector Admiral (SA).
- Increased maximum number of ribbons to 28.
- Render options: Render profiles save/load correctly.
- Rendering: native rendering format changed to PNG.
- Commodore (COM) position now allows for the ranks of Rear Admiral (RA) to Grand Admiral (GA).

### Fixed
- Display COM collars correctly.
- Display IA collars correctly.
- Display uniform trim colours correctly.
- Helmet faceplate renders correctly.

### Removed
- Support for POV-Ray v3.6. POV-Ray v3.7+ is now required.
- Due to lack of modern support for the legacy 3D assets, the live 3D preview option has not been
  re-implemented in TTT3.  An alternative preview system using POV-Ray (which also renders the final
  uniform) has been implemented.  While slightly less interactive, the preview render matches the final
  output more precisely and eliminates the need for legacy 3D models and duplicate uniform generation
  logic.
  
## ------------------------------------------------------------------------------------------------##
