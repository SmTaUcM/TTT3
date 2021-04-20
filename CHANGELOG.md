# TTT3

## Description

TIE Corps Tailoring Tool 3 (TTT3) represents a re-write of the TTT2 code.  It supports greater
integration with the Emperor's Hammer/TIE Corps web site and database, and provides for several
new options.

## Important Notes

After importing your profile via the Import tab, please verify the accuracy of all information.

Report problems or concerns to the Internet Office at io@emperorshammer.org, or open an issue 
at https://github.com/emperorshammer/issues-incoming-queue.

## Changelog

## [Unreleased-3.0.0] xxxx-xx-xx

### PENDING ###
CHANGED: - Updated shoulder marks for EH Command Staff positions.
ADDED: - Miscellaneous: Added sidearm option for duty uniforms with support for left or right handed carry.

### Added
- At runtime, TTT3 will synchronize with the Emperor's Hammer/TIE Corps database to obtain current
fleet structure information, unit patches, and unit-specific uniform colors.  This data is then
cached locally.
- Added neck ribbon display option.  Members with both the IC and GOE may elect to display both neck
ribbons and GOE dagger, or only the IC neck ribbon along with the dagger to represet receipt of the
GOE.
- Implemented the Legion of Skirmish for display on the uniform.
- Added new TIE Corps awards: TIE Corps Commander's Unit Award and TIE Corps Meritorious Unit Award.
- Added new Emperor's Hammer award: Imperial Achievement Ribbon.
- Added ribbon for display of the Letter of Achievement.
- Added three additional lightsaber models.  Lightsabers may be displayed on both the duty and dress
uniforms for members that have achieved the rank of Sith Knight in the Emperor's Hammer Dark
Brotherhood.
- Added viewer after successful uniform render, which allows saving the finished uniform to a
user-specific location.
- Implemented the Iron Star - Copper Wings and Copper Ribbon.
- Render options: Added option for transparent background.

### Changed
- Re-write using Python and QT.
- Improved appearance of wing devices on ribbons (IS, DFC, etc.).
- Expanded Order of the Vanguard to a maximum of 39th echelon.  The base ribbon indicates 1 year of
service, with a white pip representing an additional year, a gold pip representing 5 years,
and a (new) blue pip 10 years.
- Only the member's highest Medal of Communication level is displayed.
- Wings for FCHG ranks updated to Flight Certification Wings; added additional 21st Echelon with
updated 3D model.
- The legacy BGCOM position has been removed, and replaced with TIE Corps Command Staff (TCCS) 
option.
- Imperial Advisor/Command Attache positions support ranks up to Sector Admiral.
- Increased maximum number of ribbons to 24.
- Render options: Render profiles save/load correctly.
- Rendering: native rendering format changed to PNG.

### Fixed (since TTT2 UP1.09)
- Display COM collars correctly.
- Display IA collars correctly.

### Removed
- Due to lack of modern support for the legacy 3D assets, the live 3D preview option has not been
re-implemented in TTT3.  An alternative preview system using POV-Ray (which also renders the final
uniform) has been implemented.  While slightly less interactive, the preview render matches the final
output more precisely and eliminates the need for legacy 3D models and duplicate uniform generation
logic.