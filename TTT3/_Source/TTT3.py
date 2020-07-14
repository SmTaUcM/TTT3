'''#-------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        TIE Corps Tailoring Tool v3
# Purpose:     TTT is a tool to create Emperor's Hammer TIE Corps uniforms.
# Version:     v3.00
# Author:      S. Macintosh aka SkyShadow
#
# Created:     10/07/2020
# Copyright:   Emperor's Hammer
# Licence:     Open Source
#-------------------------------------------------------------------------------------------------------------------------------------------------#'''

#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Imports.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
import resource
import sys
import os
import ctypes
import ConfigParser
import psutil
import time
import datetime
from _winreg import *
from PyQt4 import QtGui, QtCore, uic
from PIL import Image



#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Classes.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
class NullDevice():
    '''A object class used to inhibit the SDTOUT/STDERR.'''

    def write(self, s):
        pass
    #------------------------------------------------------------------------------------------------------------------------------------------------#



class TTT3(QtGui.QMainWindow):
    '''Main object class representing the TTT3 application.'''

    def __init__(self):
        '''Class constructor.'''

        # Initialise an instance of a QT Main Window and load our GUI file 'data\uis\ttt.ui'.
        QtGui.QMainWindow.__init__(self)
        self.gui = uic.loadUi(r"data\uis\ttt.ui")
        self.gui.show()

        # ---------- Initialise instance variables. ----------
        # 'Info' Tab Hyperlinks.
        self.gui.lbl_readme.mouseReleaseEvent = self.readmeLink
        self.gui.lbl_email.mouseReleaseEvent = self.emailLink
        self.gui.lbl_tcpm.mouseReleaseEvent = self.tcpmLink
        self.gui.lbl_uniforms.mouseReleaseEvent = self.uniformsLink
        self.gui.lbl_pic_python.mouseReleaseEvent = self.pythonLink
        self.gui.lbl_python.mouseReleaseEvent = self.pythonLink
        self.gui.lbl_pic_qt.mouseReleaseEvent = self.qtLink
        self.gui.lbl_qt.mouseReleaseEvent = self.qtLink
        self.gui.lbl_pic_povray.mouseReleaseEvent = self.povrayLink
        self.gui.lbl_povray.mouseReleaseEvent = self.povrayLink

        # Button Connections.
        self.connect(self.gui.btn_dress, QtCore.SIGNAL("clicked()"), self.btn_dressMethod)
        self.connect(self.gui.btn_config, QtCore.SIGNAL("clicked()"), self.btn_configMethod)
        self.connect(self.gui.btn_exit, QtCore.SIGNAL("clicked()"), self.exit)

        # Radio Button Connections.
            # Positions.
        self.connect(self.gui.rb_pos_trn,    QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_fm,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_fl,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_cmdr,   QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_wc,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_com,    QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_bgcom,  QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_ia,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_ca,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_sgcom,  QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_cs,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_xo,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_fc,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_lr,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
        self.connect(self.gui.rb_pos_fr,     QtCore.SIGNAL("clicked()"), self.posRBLogic)
            # Ranks.
        self.connect(self.gui.rb_rank_ct,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_sl,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_lt,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_lcm,   QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_cm,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_cpt,   QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_maj,   QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_lc,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_col,   QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_gn,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_ra,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_va,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_ad,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_fa,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_ha,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_sa,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)
        self.connect(self.gui.rb_rank_ga,    QtCore.SIGNAL("clicked()"), self.rankRBLogic)

        # Radio Button lists.
        self.rankRadioButtons = [self.gui.rb_rank_ct, self.gui.rb_rank_sl, self.gui.rb_rank_lt, self.gui.rb_rank_lcm, self.gui.rb_rank_cm,
                                 self.gui.rb_rank_cpt, self.gui.rb_rank_maj, self.gui.rb_rank_lc, self.gui.rb_rank_col, self.gui.rb_rank_gn,
                                 self.gui.rb_rank_ra, self.gui.rb_rank_va, self.gui.rb_rank_ad, self.gui.rb_rank_fa, self.gui.rb_rank_ha,
                                 self.gui.rb_rank_sa, self.gui.rb_rank_ga]

        self.positionRadioButtons = [self.gui.rb_pos_trn, self.gui.rb_pos_fm, self.gui.rb_pos_fl, self.gui.rb_pos_cmdr, self.gui.rb_pos_wc,
                                     self.gui.rb_pos_com, self.gui.rb_pos_bgcom, self.gui.rb_pos_ia, self.gui.rb_pos_ca, self.gui.rb_pos_sgcom,
                                     self.gui.rb_pos_cs, self.gui.rb_pos_xo, self.gui.rb_pos_fc, self.gui.rb_pos_lr, self.gui.rb_pos_fr]

        # PovRay Template variables.
        self.position = None
        self.rank = None
        self.rankRotate = None
        self.rankTranslate = None
        self.name = "Unknown"
        self.ship = None
        self.wing = None
        self.sqn = None

        # PovRay Template Constants.
        self.RANK_04_SQUARES = ["-18.8939990997314,0.351000010967255,7.92899990081787", # Rotate
                                "51.3199996948242,-131.973007202148,213.126998901367"]  # Translate

        self.RANK_06_SQUARES = ["-18.8939990997314,0.351000010967255,7.92899990081787",
                                "51.1030006408691,-130.444000244141,217.598007202148"]

        self.RANK_08_SQUARES = ["-18.8939990997314,0.351000010967255,7.92899990081787",
                                "51.3199996948242,-131.973007202148,213.126998901367"]

        self.RANK_10_SQUARES = ["-18.8939990997314,0.351000010967255,7.92899990081787",
                                "51.3199996948242,-131.973007202148,213.126998901367"]

        self.RANK_12_SQUARES = ["-18.8939990997314,0.351000010967255,7.92899990081787",
                                "51.3199996948242,-131.973007202148,213.126998901367"]

        # Configuration variables.
        self.config = None

        # ---------- Application logic. ----------
        self.loadSettings()
        self.initialGUISetup()
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def readmeLink(self, event):
        '''Method event for when 'TTT3readme.htm' is clicked on the 'Info' tab.'''

        os.system("start TTT3_readme.htm")
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def emailLink(self, event):
        '''Method event for when 'SmTaUcM@Yahoo.co.uk' is clicked on the 'Info' tab.'''

        os.system("start mailto:SmTaUcM@Yahoo.co.uk")
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def tcpmLink(self, event):
        '''Method event for when 'TIE Corps Pilot Manual' is clicked on the 'Info' tab.'''

        os.system("start https://tc.emperorshammer.org/downloads/TCPM.pdf")
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def uniformsLink(self, event):
        '''Method event for when 'TIE Corps Personnel Uniforms' is clicked on the 'Info' tab.'''

        os.system("start https://tc.emperorshammer.org/uniforms.php")
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def pythonLink(self, event):
        '''Method event for when 'TIE Corps Personnel Uniforms' is clicked on the 'Info' tab.'''

        os.system("start https://www.python.org/about/")
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def qtLink(self, event):
        '''Method event for when 'TIE Corps Personnel Uniforms' is clicked on the 'Info' tab.'''

        os.system("start https://www.qt.io/")
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def povrayLink(self, event):
        '''Method event for when 'TIE Corps Personnel Uniforms' is clicked on the 'Info' tab.'''

        os.system("start http://www.povray.org/")
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def exit(self):
        '''Method that closes the application.'''

        sys.exit()
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def initialGUISetup(self):
        '''Method that sets the application's GUI for initial use.
           This mainly comprises of hiding the correct rank radio buttons.'''

        # Hide all ranks for initial use.
        for rank in self.rankRadioButtons:
            rank.hide()

        # ToDo Disabled Helmet & Profiles UTFN.
        self.gui.btn_helmet.setEnabled(False)

        self.gui.btn_newProf.setEnabled(False)
        self.gui.btn_openProf.setEnabled(False)
        self.gui.btn_saveProf.setEnabled(False)
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def posRBLogic(self):
        '''Method that controls the Position Radio Button Logic - Showing or hiding the required rank options.'''

        # Disable the Dress and Duty Uniform buttons.
        self.gui.btn_dress.setEnabled(False)
        self.gui.btn_duty.setEnabled(False)

        # Deselect any previous rank selection.
        for radioButton in self.rankRadioButtons:
            radioButton.setAutoExclusive(False)
            radioButton.setChecked(False)
            radioButton.setAutoExclusive(True)

        # Enable all options from the 'Wing and Squadron' Tab.
        self.enableWingAndSqnTab()

        # Initialise method constants.
        # Ranks:
            # Line Ranks.
        CT  = 0
        SL  = 1
        LT  = 2
        LCM = 3
        CM  = 4
        CPT = 5
        MAJ = 6
        LC  = 7
        COL = 8
        GN  = 9
            # Flag Ranks
        RA  = 10
        VA  = 11
        AD  = 12
        FA  = 13
        HA  = 14
        SA  = 15
        GA  = 16

        # Clean up the ranks group box.
        self.hideAllRanks()

        # Determine which position radio button has been selected.
        for radioButton in self.positionRadioButtons:
            if radioButton.isChecked():

                # Show the correct rank radio buttons for the selected position.
                # Trainee.
                if radioButton == self.gui.rb_pos_trn:
                    self.showRanks(CT, CT)
                    self.position = "TRN"
                    self.gui.rb_rank_ct.setChecked(True)
                    self.rankRBLogic()

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Flight Member.
                elif radioButton == self.gui.rb_pos_fm:
                    self.showRanks(SL, GN)
                    self.position = "FM"
                    break

                # Flight Leader.
                elif radioButton == self.gui.rb_pos_fl:
                    self.showRanks(LT, GN)
                    self.position = "FL"
                    break

                # Squadron Commander.
                elif radioButton == self.gui.rb_pos_cmdr:
                    self.showRanks(CM, GN)
                    self.position = "CMDR"
                    break

                # Wing Commander.
                elif radioButton == self.gui.rb_pos_wc:
                    self.showRanks(MAJ, GN)
                    self.position = "WC"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Commodore.
                elif radioButton == self.gui.rb_pos_com:
                    self.showRanks(RA, HA)
                    self.position = "COM"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Battlegroup Commander.
                elif radioButton == self.gui.rb_pos_bgcom:
                    self.showRanks(RA, HA)
                    self.position = "BGCOM"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Imperial Advisor.
                elif radioButton == self.gui.rb_pos_ia:
                    self.showRanks(RA, HA)
                    self.position = "IA"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Command Attache.
                elif radioButton == self.gui.rb_pos_ca:
                    self.showRanks(RA, HA)
                    self.position = "CA"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Sub-Group Commander.
                elif radioButton == self.gui.rb_pos_sgcom:
                    self.showRanks(RA, GA)
                    self.position = "SGCOM"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Command Staff.
                elif radioButton == self.gui.rb_pos_cs:
                    self.showRanks(RA, GA)
                    self.position = "CS"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Executive Officer.
                elif radioButton == self.gui.rb_pos_xo:
                    self.showRanks(RA, GA)
                    self.position = "XO"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Fleet Commander.
                elif radioButton == self.gui.rb_pos_fc:
                    self.showRanks(GA, GA)
                    self.position = "FC"
                    self.gui.rb_rank_ga.setChecked(True)
                    self.rankRBLogic()

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Line Ranks.
                elif radioButton == self.gui.rb_pos_lr:
                    self.showRanks(CT, GN)
                    self.position = "NUL"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break

                # Flag Ranks.
                elif radioButton == self.gui.rb_pos_fr:
                    self.showRanks(RA, GA)
                    self.position = "NUL"

                    # Set the options available to the user in the 'Wing and Squadron' tab.
                    self.gui.lw_ship.setEnabled(False)
                    self.gui.lw_wing.setEnabled(False)
                    self.gui.lw_squad.setEnabled(False)
                    self.gui.cb_eliteSqn.setEnabled(False)
                    break
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def enableWingAndSqnTab(self):
        '''Method that enables all options in the 'Wing and Squadron' tab.'''

        self.gui.lw_ship.setEnabled(True)
        self.gui.lw_wing.setEnabled(True)
        self.gui.lw_squad.setEnabled(True)
        self.gui.cb_eliteSqn.setEnabled(True)

        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def rankRBLogic(self):
        '''Method that controls the Rank Radio Button Logic - Showing the 'Dress and Duty Uniform' buttons.'''

        # Determine which rank radio button has been selected.
        for radioButton in self.rankRadioButtons:
            if radioButton.isChecked():

                # Set the correct rank for the selected rank.
                if radioButton == self.gui.rb_rank_ct:
                    self.rank = "CT"
                    self.rankRotate = self.RANK_04_SQUARES[0]
                    self.rankTranslate = self.RANK_04_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_sl:
                    self.rank = "SL"
                    self.rankRotate = self.RANK_04_SQUARES[0]
                    self.rankTranslate = self.RANK_04_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_lt:
                    self.rank = "LT"
                    break

                elif radioButton == self.gui.rb_rank_lcm:
                    self.rank = "LCM"
                    self.rankRotate = self.RANK_04_SQUARES[0]
                    self.rankTranslate = self.RANK_04_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_cm:
                    self.rank = "CM"
                    self.rankRotate = self.RANK_06_SQUARES[0]
                    self.rankTranslate = self.RANK_06_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_cpt:
                    self.rank = "CPT"
                    self.rankRotate = self.RANK_06_SQUARES[0]
                    self.rankTranslate = self.RANK_06_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_maj:
                    self.rank = "MAJ"
                    self.rankRotate = self.RANK_08_SQUARES[0]
                    self.rankTranslate = self.RANK_08_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_lc:
                    self.rank = "LC"
                    self.rankRotate = self.RANK_08_SQUARES[0]
                    self.rankTranslate = self.RANK_08_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_col:
                    self.rank = "COL"
                    self.rankRotate = self.RANK_08_SQUARES[0]
                    self.rankTranslate = self.RANK_08_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_gn:
                    self.rank = "GN"
                    self.rankRotate = self.RANK_08_SQUARES[0]
                    self.rankTranslate = self.RANK_08_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_ra:
                    self.rank = "RA"
                    self.rankRotate = self.RANK_10_SQUARES[0]
                    self.rankTranslate = self.RANK_10_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_va:
                    self.rank = "VA"
                    self.rankRotate = self.RANK_10_SQUARES[0]
                    self.rankTranslate = self.RANK_10_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_ad:
                    self.rank = "AD"
                    self.rankRotate = self.RANK_10_SQUARES[0]
                    self.rankTranslate = self.RANK_10_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_fa:
                    self.rank = "FA"
                    self.rankRotate = self.RANK_12_SQUARES[0]
                    self.rankTranslate = self.RANK_12_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_ha:
                    self.rank = "HA"
                    self.rankRotate = self.RANK_12_SQUARES[0]
                    self.rankTranslate = self.RANK_12_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_sa:
                    self.rank = "SA"
                    self.rankRotate = self.RANK_12_SQUARES[0]
                    self.rankTranslate = self.RANK_12_SQUARES[1]
                    break

                elif radioButton == self.gui.rb_rank_ga:
                    self.rank = "GA"
                    self.rankRotate = self.RANK_12_SQUARES[0]
                    self.rankTranslate = self.RANK_12_SQUARES[1]
                    break

        # Enable the Dress and Duty Uniform buttons.
        self.gui.btn_dress.setEnabled(True)
        # TODO Disabled Duty Uniform UTFN.
##        self.gui.btn_duty.setEnabled(True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def hideAllRanks(self):
        '''Method used to hide all rank radio buttons on the 'Position and Rank' tab.'''

        for rankRadioButton in self.rankRadioButtons:
            rankRadioButton.hide()

        self.rank = None
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def showRanks(self, rankMin, rankMax):
        '''Method used to show a range of ranks in the 'Position and Rank' tab.
           self.showRanks(int(rankMin), int(rankMax)) -> Rank Radio Buttons shown.'''

        for rankRadioButton in self.rankRadioButtons[rankMin : rankMax + 1]: # + 1 because Python doesn't include the last item when indexing.
            rankRadioButton.show()
        #----------------------------------------------------------------------------------------------------------------------------------------#


    def btn_dressMethod(self):
        '''Method that is triggered when the 'Dress Uniform' button is clicked.
           This method will check that the correct selections has been made within TTT3 such as Ship and Squadron and then
           directly call 'launchPOVRay' to open up PovRay and render the unirom.'''

        # Check to see if the user has made the correct selections for their position and rank.
        if self.position in ["FM", "FL", "CMDR", "WC"]:
            if not self.ship or not self.wing:
                msg = "Error: As a pilot you need to specify at least a ship and wing before a dress uniform can be created."
                return ctypes.windll.user32.MessageBoxA(0, msg, "TTT3", 0)

        elif self.position in ["COM"]:
            if not self.ship:
                msg = "Error: As a COM you need to specify a ship before a dress uniform can be created."
                return ctypes.windll.user32.MessageBoxA(0, msg, "TTT3", 0)

        # Run PovRay to render a uniform.
        else:
            self.createDressPov()
            self.launchPOVRay("dress")
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def launchPOVRay(self, uniform):
        '''Method that dynamically writes data\batch\povray.bat and invisible.vbs to silently loanch POV-Ray with the correct paths.
           The "uniform" agrument takes "dress", "duty or "helmet which is dependant on which button has been pressed."'''

        # Dynamically write the 'data\batch\povray.bat' file.
            # Set the correct paths based on where TTT3 is located and the TTT3.ini settings file.
        template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\&TYPE&.pov" +w640 +h853 +q9 /EXIT'
        template = template.replace("&TTTPATH&", os.getcwd())

        # Apply the path depending on what the user has selected from within the Configuratrion window.
        if self.config.get("POV", "mode") == "registry":
            template = template.replace("&POVPATH&", self.getPathFromRegistry())
        else:
            template = template.replace("&POVPATH&", self.config.get("POV", "path"))

        template = template.replace("&TYPE&", uniform)

            # Write the 'data\batch\povray.bat' file.
        with open(r"data\batch\povray.bat", "w") as dataFile:
            dataFile.write(template)

        # Dynamically write the 'data\batch\invisible.vbs' file.
            # Set the correct paths based on where TTT3 is located.
        template = [r'Set WshShell = CreateObject("WScript.Shell")' + "\n",
                     r'WshShell.Run chr(34) & "&PATH&\data\batch\povray.bat" & Chr(34), 0' + "\n",
                     r'Set WshShell = Nothing']
        output = []

        for line in template:
            if "&PATH&" in line:
                newLine = line.replace("&PATH&", os.getcwd())
                output.append(newLine)
            else:
                output.append(line)

            # Write the 'data\batch\invisible.vbs' file.
        with open(r"data\batch\invisible.vbs", "w") as dataFile:
            dataFile.writelines(output)

        # Launch POV-Ray using 'invisible.vbs' which then silently runs 'povray.bat' which then opens POV-Ray and auto renders the uniform.
        os.system(r"data\batch\invisible.vbs")

        # Wait for POV-Ray to close.
        self.povrayMonitor()

        # Open the newly generated uniform.png file.
        if self.config.get("POV", "mode") == "registry":
            if "3.6" in self.config.get("POV", "regpath"):
                self.convertImage(uniform)

        elif self.config.get("POV", "mode") == "specific":
            if "3.6" in self.config.get("POV", "path"):
                self.convertImage(uniform)

        os.system(r"data\{uniformType}.png".format(uniformType=uniform))
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def povrayMonitor(self):
        '''Monitors for povray running in the background and signals when it has closed.'''

        time.sleep(1) # Allow one second for POV-Ray to open.

        povRunning = True

        while povRunning:
            povRunning = False

            # Get a list of all running processes
            list = psutil.pids()

            # Go though list and check each processes executeable name for 'pvengine.exe'
            for i in range(0, len(list)):
                try:
                    p = psutil.Process(list[i])
                    if p.cmdline()[0].find("pvengine64.exe") != -1 or p.cmdline()[0].find("pvengine.exe") != -1:
                        povRunning = True
                        break;
                except:
                    pass
            time.sleep(1)
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def convertImage(self, uniform):
        '''Comnverts a given .bpf file into .jpg, .gif or .png'''

        path = r"data\%s"%uniform
        img = Image.open(path + ".bmp")
        new_img = img.resize( (640, 853) )
        new_img.save( path + ".png", 'png')
##        new_img.save( path + ".jpg", 'jpeg')
##        new_img.save( path + ".gif", 'gif')
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def loadSettings(self):
        '''Method that reads in 'settings\TT3.ini' and stores the data as a ConfigParser object.'''

        self.config = ConfigParser.ConfigParser()
        self.config.read("settings\TTT3.ini")
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def applySettings(self):
        '''Method that applies the settings to the 'Configuration' window.'''

        # ----- Mode. -----
        if self.config.get("POV", "mode") == "registry":
            self.config_gui.rb_reg.setChecked(True)

        elif self.config.get("POV", "mode") == "specific":
            self.config_gui.rb_specific.setChecked(True)

        else:
            msg = "Error: Invalid setting for 'mode' in TTT3.ini."
            return ctypes.windll.user32.MessageBoxA(0, msg, "TTT3", 0)

        # ----- All other values -----
        self.config_gui.lbl_regPath.setText(self.config.get("POV", "regpath"))
        self.config_gui.le_specPath.setText(self.config.get("POV", "path"))
        self.config_gui.le_backend.setText(self.config.get("TCDB", "xml"))
        self.config_gui.le_roster.setText(self.config.get("TCDB", "roster"))
        self.config_gui.le_search.setText(self.config.get("TCDB", "search"))
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def saveSettings(self):
        '''Method that saves the user's settings to 'settings\TT3.ini'.'''

        with open(r"settings\TTT3.ini", "w") as settingsFile:
            self.config.write(settingsFile)
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def btn_configMethod(self):
        '''Method that opens and handles control of the 'Configuration' window.'''

        # Load our GUI file 'data\uis\config.ui'.
        self.config_gui = uic.loadUi(r"data\uis\config.ui")
        self.config_gui.show()

        # GUI Connections.
        self.connect(self.config_gui.btn_config_close, QtCore.SIGNAL("clicked()"), self.config_gui.close)
        self.connect(self.config_gui.btn_config_ok, QtCore.SIGNAL("clicked()"), self.config_btn_ok_method)
        self.connect(self.config_gui.rb_reg, QtCore.SIGNAL("toggled(bool)"), self.config_rb_reg_logic)
        self.connect(self.config_gui.rb_specific, QtCore.SIGNAL("toggled(bool)"), self.config_rb_specific_logic)
        self.connect(self.config_gui.btn_config_browse, QtCore.SIGNAL("clicked()"), self.config_browse)

        # Set the values displayed to the values in our config / setting from 'settings\TTT3.ini'.
        self.applySettings()
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def config_rb_reg_logic(self, value=None):
        '''Method that controls what happens within the 'Configuration' window if a 'POV' radio button is clicked.'''

        # Enable the registry path options.
        self.config_gui.lbl_regPathTitle.setEnabled(True)
        self.config_gui.lbl_regPath.setEnabled(True)
        self.config_gui.lbl_regPath.setText(self.getPathFromRegistry())

        # Disable the specific path options.
        self.config_gui.le_specPath.setEnabled(False)
        self.config_gui.btn_config_browse.setEnabled(False)

        # Save our setting.
        self.config.set("POV", "mode", "registry")
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def config_rb_specific_logic(self, value=None):
        '''Method that controls what happens within the 'Configuration' window if a 'POV' radio button is clicked.'''

        # Enable the specific path options.
        self.config_gui.le_specPath.setEnabled(True)
        self.config_gui.btn_config_browse.setEnabled(True)

        # Disable the registry path options.
        self.config_gui.lbl_regPathTitle.setEnabled(False)
        self.config_gui.lbl_regPath.setEnabled(False)

        # Save our setting.
        self.config.set("POV", "mode", "specific")
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def config_btn_ok_method(self):
        '''Method that handles the functionality when the 'OK' button is pressed within  the 'Configuration' screen.'''

        # Test to ensure that the direct POV-Ray exceutable is present.
        if self.config.get("POV", "mode") == "specific":

            if not os.path.exists(self.config_gui.le_specPath.text()):
                msg = "Cannot find valid installion of POV-Ray at:\n\n%s"%str(self.config_gui.le_specPath.text())
                return ctypes.windll.user32.MessageBoxA(0, msg, "TTT3", 0)

            else:
                # Save the direct path.
                self.config.set("POV", "path", self.config_gui.le_specPath.text())

        else:
            # Seve the detected registry path.
            self.config.set("POV", "regpath", self.config_gui.lbl_regPath.text())

        # All other settings.
        self.config.set("TCDB", "xml", str(self.config_gui.le_backend.text()))
        self.config.set("TCDB", "roster", str(self.config_gui.le_roster.text()))
        self.config.set("TCDB", "search", str(self.config_gui.le_search.text()))



        # Save and close.
        self.saveSettings()
        self.config_gui.close()
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def getPathFromRegistry(self):
        '''Method to detect the installation path of POV-Ray from the Windows registry using the provided options..'''

        # Determin the highest version of POV-Ray from the version setting in 'TTT3.ini'.
        path = False
        version = float(self.config.get("POV", "version"))

        while not path:
            try:
                # Obtain the path to POV-Ray.
                aKey = "Software\\POV-Ray\\v" + str(version) + "\\Windows\\"
                values = OpenKey(HKEY_CURRENT_USER, aKey)
                path = QueryValueEx(values, "Home")[0]

            except WindowsError:
                version -= 0.1

                # Fall back to CurrentVerison if all else fails.
                if version < 3.6:
                    aKey = "Software\\POV-Ray\\CurrentVersion\\Windows\\"
                    values = OpenKey(HKEY_CURRENT_USER, aKey)
                    path = QueryValueEx(values, "Home")[0]

        # Add a backslash if required to the path.
        if path[-1] != "\\":
            path += "\\"

        # Detect weather the 32bit or 64bit version of POV-Ray is installed.
        if os.path.exists(path + "\\bin\\pvengine64.exe"):
            path += "bin\\pvengine64.exe"

        elif os.path.exists(path + "\\bin\\pvengine.exe"):
            path += "bin\\pvengine.exe"

        else:
            # Raise an error if we can't find POV-Ray in the Windows Registry.
            msg = "Cannot find valid installion of POV-Ray in the Windows Registry."
            return ctypes.windll.user32.MessageBoxA(0, msg, "TTT3", 0)

        # Save the detected path and return the value.
        self.config.set("POV", "regpath", path)
        self.saveSettings()
        return path
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def config_browse(self):
        '''Method that allows the user to select an executable file from a file picker.'''

        fileDialog = QtGui.QFileDialog()
        fileDialog.setFileMode(QtGui.QFileDialog.AnyFile)
        fileDialog.setDirectory(r"C:\Program Files\POV-Ray")
        fileDialog.setFilter("pvengine64.exe;;pvengine.exe")
        fileDialog.show()
        if fileDialog.exec_():
            target = fileDialog.selectedFiles()
            target = target[0].replace(r"/", "\\")
            self.config_gui.le_specPath.setText(target)
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def createDressPov(self):
        '''Method that loads in '\data\dress.tpt' parses in the correct uniform data and creates a new 'data\dress.pov' file.'''

        # Read in the template data.
        with open(r"data\dress.tpt", "r") as tptFile:
            template = tptFile.readlines()

        # Header text.
        position = ""
        if self.position == "NUL":
            position = "    "
        else:
            position = self.position + "/"

        posRankName = position + self.rank + " " + self.name
        padding = (37 - len(posRankName)) * " "
        posRankName += padding

        now = datetime.datetime.now()
        timestamp = now.strftime("%d/%m/%Y  %H:%M:%S")
        padding = (64 - len(timestamp)) * " "
        timestamp += padding

        header = """ ////////////////////////////////////////////////////////////////////
//                                                                 //
// TIE Corps Dress Uniform of {posRankName}//
//                                                                 //
// POV Scene file generated by TIECorps Tailoring Tool 3.00a1      //
// {timestamp}//
//                                                                 //
// Uniform created by LC Tempest, based on the model by            //
// Rapha?l de Bouchony a.k.a Tron (Imperial Officer, SciFi 3D)     //
//                                                                 //
// Geometry data POV export by 3DWin5 V 5.6                        //
// 3dto3d engine by tb-software.com (support@tb-software.com)      //
// Created by POV Export Plugin 1.2                                //
//                                                                 //
// http://www.emperorshammer.org/                                  //
// http://www.ehtiecorps.org/                                      //
// http://www.tb-software.com/                                     //
// http://www.povray.org/                                          //
// http://www.Tempest.net.tc/                                      //
//                                                                 //
////////////////////////////////////////////////////////////////////
""".format(posRankName=posRankName, timestamp=timestamp)

        povData = []

        for line in header:
            povData.append(line)

        # Parse the template data.
        for line in template:

            # ----- Global. -----
            if "&BGCOLOUR&" in line:
                povData.append(line.replace("&BGCOLOUR&", "0, 0, 0")) # TODO


            # ----- Light. -----

            elif "&LIGHT&" in line:
                povData.append(line.replace("&LIGHT&", "1518.5, -647.4, 1750.1")) # TODO

            elif "&SPOTLIGHTCOLOUR&" in line:
                povData.append(line.replace("&SPOTLIGHTCOLOUR&", "1, 1, 1")) # TODO

            elif "&SHADOWLESS&" in line:
                povData.append(line.replace("&SHADOWLESS&", "")) # TODO


            # ----- Camera. -----

            elif "&CAMERA&" in line:
                povData.append(line.replace("&CAMERA&", "-260.8, -1331.1, 209.0")) # TODO

            elif "&TARGET&" in line:
                povData.append(line.replace("&TARGET&", "0, -12.8, 2.8")) # TODO


            # ----- Basic Info. -----
            elif "&CLOTH&" in line:
                povData.append(line.replace("&CLOTH&", "0")) # TODO

            elif "&POSITION&" in line:
                if self.position == "TRN":
                    povData.append(line.replace("&POSITION&", "NUL"))
                else:
                    povData.append(line.replace("&POSITION&", self.position))

            elif "&RANK&" in line:
                povData.append(line.replace("&RANK&", self.rank))

            elif "&RANKROTATE&" in line:
                povData.append(line.replace("&RANKROTATE&", self.rankRotate)) # TODO

            elif "&RANKTRANSLATE&" in line:
                povData.append(line.replace("&RANKTRANSLATE&", self.rankTranslate)) # TODO


            # ----- Assignment. -----
            elif "&CATEGORY&" in line:
                povData.append(line.replace("&CATEGORY&", "line")) # TODO

            elif "&SHIP&" in line:
                povData.append(line.replace("&SHIP&", "ISD Hammer")) # TODO

            elif "&WING&" in line:
                povData.append(line.replace("&WING&", "Wing I")) # TODO

            elif "&SQUAD&" in line:
                povData.append(line.replace("&SQUAD&", "Epsilon")) # TODO

            elif "&TRIMCOLOUR&" in line:
                povData.append(line.replace("&TRIMCOLOUR&", "black")) # TODO


            # ----- Medals. -----
            elif "&MABGS&" in line:
                povData.append(line.replace("&MABGS&", "0")) # TODO

            elif "&MABSS&" in line:
                povData.append(line.replace("&MABSS&", "0")) # TODO

            elif "&MABBS&" in line:
                povData.append(line.replace("&MABBS&", "0")) # TODO

            elif "&MABPC&" in line:
                povData.append(line.replace("&MABPC&", "1")) # TODO

            elif "&MABISM&" in line:
                povData.append(line.replace("&MABISM&", "2")) # TODO


            # ----- Other. -----

            elif "&PADINCLUDE&" in line:
                povData.append(line.replace("&PADINCLUDE&", '#include "pad_g.inc"')) # TODO

            elif "&FCHGINCLUDE&" in line:
                povData.append(line.replace("&FCHGINCLUDE&", '#include "fchg_g.inc"')) # TODO

            elif "&SABERINCLUDE&" in line:
                povData.append(line.replace("&SABERINCLUDE&", "")) # TODO

            elif "&MOHINCLUDE&" in line:
                povData.append(line.replace("&MOHINCLUDE&", "")) # TODO

            elif "&OORINCLUDE&" in line:
                povData.append(line.replace("&OORINCLUDE&", "")) # TODO

            elif "&ICGOEINCLUDE&" in line:
                povData.append(line.replace("&ICGOEINCLUDE&", "")) # TODO

            elif "&MEDALSINCLUDE&" in line:

                medalsInclude = ['#include "medal_g.inc"', '#include "bs_g.inc"', '#include "pc_g.inc"', '#include "ism_g.inc"']

                for line in medalsInclude:
                    povData.append(line + "\n") # TODO


            # ----- Scene. -----

            elif "&FCHG&" in line:
                povData.append(line.replace("&FCHG&", "object { pldn }")) # TODO

            elif "&SABER&" in line:
                povData.append(line.replace("&SABER&", "")) # TODO

            elif "&GOEDAGGER&" in line:
                povData.append(line.replace("&GOEDAGGER&", "")) # TODO


            elif "&MEDALS&" in line:

                medals = ["object { P_bs_3_1 }", "object { P_pc_3_2 }", "object { P_ism_3_3 }"]

                for medal in medals:
                    povData.append(medal + "\n") # TODO


            elif "&RIBBONS&" in line:
                ribbons = ["object { P_r12 texture { T_r_is_gw } }", "object { P_r13 texture { T_r_is_sw } }",
                           "object { P_r14 texture { T_r_is_bw } }", "object { P_r15 texture { T_r_is_gr } }",
                           "object { P_r16 texture { T_r_is_sr } }", "object { P_r17 texture { T_r_is_br } }",
                           "object { P_r18 texture { T_r_loc } }", "object { P_r19 texture { T_r_los_cs } }",
                           "object { P_r24 texture { T_r_moc_boc } }", "object { P_r25 texture { T_r_cob } }",
                           "object { P_r26 texture { T_r_ov_19e } }"]

                for ribbon in ribbons:
                    povData.append(ribbon + "\n") # TODO


            # ----- Non-Editable Data. -----
            else:
                povData.append(line)

        # Write the parsed data to '\data\dress.pov'.
        with open(r"data\dress.pov", "w") as povFile:
            povFile.writelines(povData)
        #--------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------------#



#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Functions.                                                                    #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
# None.


#----------------------------------------------------------------------------------------------------------------------------------------------------#



#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Main Program.                                                                  #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    # TODO Disabled for development.
##    # Inhibit the STDOUT and STDERR so we don't get the annoying pop up window when we close the app.
##    sys.stdout = NullDevice()
##    sys.stderr = NullDevice()

    # Start the QT application.
    app = QtGui.QApplication(sys.argv)
    ttt3 = TTT3()
    sys.exit(app.exec_())
#----------------------------------------------------------------------------------------------------------------------------------------------------#
