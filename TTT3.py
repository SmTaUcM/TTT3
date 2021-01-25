# -*- coding: latin-1 -*-
'''#-------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        TIE Corps Tailoring Tool v3
# Purpose:     TTT is a tool to create Emperor's Hammer TIE Corps uniforms.
# Version:     v3.00
# Author:      Stuart Macintosh aka SkyShadow
#
# Created:     10/07/2020
# Copyright:   Emperor's Hammer
# Licence:     Open Source
#-------------------------------------------------------------------------------------------------------------------------------------------------#'''

#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Imports.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
# Developed using Python v3.8.7 32-bit.
# External dependancies are commented. Imports with no comments are included with the regular Python installation.
# Alternatively run "TTT3\Useful Info\Dependancy Installer.bat"
import logging
import resource
import sys
import os
import ctypes
import configparser
import psutil  # python -m pip install psutil
import time
import datetime
import winreg
from PyQt5 import uic  # python -m pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog  # python -m pip install pyqt5-tools
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image  # python -m pip install pillow
import cv2  # python -m pip install opencv-python
import numpy
import platform
import pickle
# python -m pip install pyinstaller - for compiler.

#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Classes.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#


class TTT3(QMainWindow):
    '''Main object class representing the TTT3 application.'''

    def __init__(self):
        '''Class constructor.'''

        try:
            # Version info.
            version = "3.00"
            devVersion = "Alpha 12"
            date = "23 January 2021"
            self.saveFileVersion = 1
            self.version = "{v} {a}".format(v=version, a=devVersion)

            # Initialise an instance of a QT Main Window and load our GUI file 'data\uis\ttt.ui'.
            QMainWindow.__init__(self)
            self.gui = uic.loadUi(r"data\uis\ttt.ui")
            self.gui.show()
            self.gui.closeEvent = self.closeEvent

            # Set the version number.
            self.gui.lblVersion.setText("Version: {v} {a}".format(v=version, a=devVersion))
            self.gui.lblDate.setText("Date:     " + date)

            # ---------- Initialise instance variables and connections. ----------

            # ----- Main Graphical User Interface. -----

            # Button Connections.
            self.gui.btn_dress.clicked.connect(self.btn_dressMethod)
            self.gui.btn_duty.clicked.connect(self.btn_dutyMethod)
            self.gui.btn_newProf.clicked.connect(self.btn_newProfMethod)
            self.gui.btn_openProf.clicked.connect(self.btn_openProfMethod)
            self.gui.btn_saveProf.clicked.connect(self.btn_saveProfMethod)
            self.gui.btn_config.clicked.connect(self.btn_configMethod)
            self.gui.btn_exit.clicked.connect(self.closeEvent)

            # ----- 'Position and Rank' Tab. -----

            # Radio Button Connections.

            # Positions.
            self.gui.rb_pos_trn.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_fm.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_fl.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_cmdr.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_wc.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_com.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_tccs.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_ia.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_ca.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_sgcom.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_cs.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_xo.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_fc.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_lr.clicked.connect(self.posRBLogic)
            self.gui.rb_pos_fr.clicked.connect(self.posRBLogic)

            # Ranks.
            self.gui.rb_rank_ct.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_sl.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_lt.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_lcm.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_cm.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_cpt.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_maj.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_lc.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_col.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_gn.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_ra.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_va.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_ad.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_fa.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_ha.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_sa.clicked.connect(self.rankRBLogic)
            self.gui.rb_rank_ga.clicked.connect(self.rankRBLogic)

            # Radio Button lists.
            self.rankRadioButtons = [self.gui.rb_rank_ct, self.gui.rb_rank_sl, self.gui.rb_rank_lt, self.gui.rb_rank_lcm, self.gui.rb_rank_cm,
                                     self.gui.rb_rank_cpt, self.gui.rb_rank_maj, self.gui.rb_rank_lc, self.gui.rb_rank_col, self.gui.rb_rank_gn,
                                     self.gui.rb_rank_ra, self.gui.rb_rank_va, self.gui.rb_rank_ad, self.gui.rb_rank_fa, self.gui.rb_rank_ha,
                                     self.gui.rb_rank_sa, self.gui.rb_rank_ga]

            self.positionRadioButtons = [self.gui.rb_pos_trn, self.gui.rb_pos_fm, self.gui.rb_pos_fl, self.gui.rb_pos_cmdr, self.gui.rb_pos_wc,
                                         self.gui.rb_pos_com, self.gui.rb_pos_tccs, self.gui.rb_pos_ia, self.gui.rb_pos_ca, self.gui.rb_pos_sgcom,
                                         self.gui.rb_pos_cs, self.gui.rb_pos_xo, self.gui.rb_pos_fc, self.gui.rb_pos_lr, self.gui.rb_pos_fr]

            # ----- 'Wing and Squadron' Tab. -----

            # List Widget Connections.
            self.gui.lw_ship.itemClicked.connect(self.shipSelectionLogic)
            self.gui.lw_wing.itemClicked.connect(self.wingSelectionLogic)
            self.gui.lw_squad.itemClicked.connect(self.squadSelectionLogic)
            # CheckBox.
            self.gui.cb_eliteSqn.stateChanged.connect(self.eliteSqnSelectionLogic)

            # ----- 'Medals, Ribbons and FCHG' Tab. -----

            # List Widget Connections.
            self.gui.lw_medals.currentItemChanged.connect(self.medalSelectionLogic)

            # ----- 'Import' Tab. -----
            self.gui.btn_browseRoster.clicked.connect(self.btn_browseRosterFunc)
            self.gui.btn_search.clicked.connect(self.btn_searchFunc)

            # ----- Info Tab. -----

            # 'Info' Tab Hyperlinks.
            self.gui.lbl_readme.mouseReleaseEvent = self.readmeLink
            self.gui.lbl_email.mouseReleaseEvent = self.ioLink
            self.gui.lbl_tcpm.mouseReleaseEvent = self.tcpmLink
            self.gui.lbl_uniforms.mouseReleaseEvent = self.uniformsLink
            self.gui.lbl_pic_python.mouseReleaseEvent = self.pythonLink
            self.gui.lbl_python.mouseReleaseEvent = self.pythonLink
            self.gui.lbl_pic_qt.mouseReleaseEvent = self.qtLink
            self.gui.lbl_qt.mouseReleaseEvent = self.qtLink
            self.gui.lbl_pic_povray.mouseReleaseEvent = self.povrayLink
            self.gui.lbl_povray.mouseReleaseEvent = self.povrayLink
            self.gui.lbl_pic_io.mouseReleaseEvent = self.ioLink
            self.gui.lbl_io.mouseReleaseEvent = self.ioLink
            self.gui.label_11.mouseReleaseEvent = self.eeLink
            self.gui.label_10.mouseReleaseEvent = self.devModeLink

            # ----- POV-Ray Variables. -----

            # PovRay Template variables.
            self.position = None
            self.rank = None
            self.name = "Unknown"
            self.ship = ""
            self.wing = ""
            self.sqn = ""
            self.awards = {}
            self.eeCount = 0
            self.devModeCount = 0
            self.deconflictNeckRibbons = False

            # PovRay Template Constants.
            self.RANK_OFFSET_RIBBONS_00_TO_08 = ["-18.8939990997314,0.351000010967255,7.92899990081787",  # Rotate
                                                 "51.3199996948242,-131.973007202148,213.126998901367"]  # Translate

            self.RANK_OFFSET_RIBBONS_09_TO_12 = ["-18.8939990997314,0.351000010967255,7.92899990081787",
                                                 "51.1030006408691,-130.444000244141,217.598007202148"]

            self.RANK_OFFSET_RIBBONS_13_TO_16 = ["-20.8950004577637,0.25,7.64699983596802",
                                                 "50.8540000915527,-128.714996337891,222.033004760742"]

            self.RANK_OFFSET_RIBBONS_17_TO_20 = ["-23.7950000762939,0.264999985694885,7.68100023269653",
                                                 "50.5919990539551,-126.778999328613,226.337997436523"]

            self.RANK_OFFSET_RIBBONS_21_TO_24 = ["-25.6240005493164,0.264999985694885,7.68100023269653",
                                                 "50.326000213623,-124.832000732422,230.47900390625"]

            # ----- Configuration variables. -----
            self.config = None
            self.fleetConfig = None
            self.medalConfig = None
            self.ribbonConfig = None

            # ----- GUI variables. -----
            self.subRibbonAwards = []
            self.cb_singleMedalConnected = False
            self.combo_topConnected = False
            self.rb_upgradeablesConnected = False
            self.imagePath = None

            # ----- Application logic. -----
            self.fastRendering = False  # Forces POV-Ray to render at a lower quality for quicker rendering during testing.
            self.continueRender = True
            self.loadSettings()
            self.initialGUISetup()
        except Exception as e:
            handleException(e)
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def readmeLink(self, event):
        '''Method event for when 'TTT3readme.htm' is clicked on the 'Info' tab.'''

        os.system("start TTT3_readme.htm")
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def ioLink(self, event):
        '''Method event for when 'Internet Office' is clicked on the 'Info' tab.'''

        os.system("start https://ehnet.org/")
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
        '''Method event for when 'Python' is clicked on the 'Info' tab.'''

        os.system("start https://www.python.org/about/")
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def qtLink(self, event):
        '''Method event for when 'QT' is clicked on the 'Info' tab.'''

        os.system("start https://www.qt.io/")
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def povrayLink(self, event):
        '''Method event for when 'POV-Ray' is clicked on the 'Info' tab.'''

        os.system("start http://www.povray.org/")
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def eeLink(self, event):
        '''Method event for ee.'''

        try:
            self.eeCount += 1
            if self.eeCount >= 3:
                self.gui.label_11.setText("PRAETORIAN MODE")
                self.gui.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        except Exception as e:
            handleException(e)
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def devModeLink(self, event):
        '''Method event for ee.'''

        try:
            self.devModeCount += 1
            if self.devModeCount >= 3:
                self.gui.label_10.setText("DEV MODE")
                self.gui.label_10.setStyleSheet("color: rgb(255, 0, 0);")
                self.fastRendering = True
        except Exception as e:
            handleException(e)
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def closeEvent(self, event):
        '''Method that overloads the self.gui close event and the application.'''

        logging.shutdown()
        if os.stat("TTT3 Crash.log").st_size == 0:
            os.remove("TTT3 Crash.log")
        sys.exit()
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def outputCloseEvent(self, event):
        '''Method that overloads the self.output_gui close event and the application.'''

        self.gui.setWindowFlags(self.gui.windowFlags() & ~Qt.WindowStaysOnBottomHint)
        self.gui.show()
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def initialGUISetup(self):
        '''Method that sets the application's GUI for initial use.
           This mainly comprises of hiding the correct rank radio buttons.'''

        # Hide all ranks for initial use.
        for rank in self.rankRadioButtons:
            rank.hide()

        # Load 'Wing and Squadron' tab items from 'settings\fleet.ini'.
        self.fleetConfig = configparser.ConfigParser()
        self.fleetConfig.read("settings\\fleet.ini")

        # Add the Ships to the Ships list view.
        for ship in self.fleetConfig.options("fleet"):
            if ship != "count":
                self.gui.lw_ship.addItem(self.fleetConfig.get("fleet", ship))

        # Load Medal and Ribbon data.
        self.loadMedals()
        self.loadRibbons()

        # Hide 'Medals, Ribbons and FCHG' items.
        self.gui.gb_medals.hide()
        self.hideMedalOptions()

        # TODO Disabled Helmet UTFN.
        self.gui.btn_helmet.setEnabled(False)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def posRBLogic(self):
        '''Method that controls the Position Radio Button Logic - Showing or hiding the required rank options.'''

        try:
            # Reset the user's position value.
            self.position = "NUL"

            # Disable the Dress and Duty Uniform buttons.
            self.gui.btn_dress.setEnabled(False)
            self.gui.btn_duty.setEnabled(False)

            # Deselect any previous rank selection.
            for radioButton in self.rankRadioButtons:
                radioButton.setAutoExclusive(False)
                radioButton.setChecked(False)
                radioButton.setAutoExclusive(True)

            # Initialise method constants.
            # Ranks:
                # Line Ranks.
            CT = 0
            SL = 1
            LT = 2
            LCM = 3
            CM = 4
            CPT = 5
            MAJ = 6
            LC = 7
            COL = 8
            GN = 9
            # Flag Ranks
            RA = 10
            VA = 11
            AD = 12
            FA = 13
            HA = 14
            SA = 15
            GA = 16

            # Enable all options from the 'Wing and Squadron' Tab.
            if self.gui.cb_eliteSqn.isChecked() == False:  # Stops the ship and wing tabs from repopulating if 'Elite Squadron' is checked.
                self.enableWingAndSqnTab(True)

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
                        self.enableWingAndSqnTab(False)
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
                        self.gui.cb_eliteSqn.setChecked(False)
                        self.gui.cb_eliteSqn.setEnabled(False)
                        self.gui.lw_squad.setEnabled(False)
                        self.gui.lw_squad.clear()
                        self.sqn = ""
                        break

                    # Commodore.
                    elif radioButton == self.gui.rb_pos_com:
                        self.showRanks(RA, HA)
                        self.position = "COM"

                        # Set the options available to the user in the 'Wing and Squadron' tab.
                        self.gui.cb_eliteSqn.setChecked(False)
                        self.gui.cb_eliteSqn.setEnabled(False)
                        self.gui.lw_wing.setEnabled(False)
                        self.gui.lw_wing.clear()
                        self.wing = ""
                        self.gui.lw_squad.setEnabled(False)
                        self.gui.lw_squad.clear()
                        self.sqn = ""
                        break

                    # TE Corps Command Staff.
                    elif radioButton == self.gui.rb_pos_tccs:
                        self.showRanks(RA, HA)
                        self.position = "TCCS"
                        self.enableWingAndSqnTab(False)
                        break

                    # Imperial Advisor.
                    elif radioButton == self.gui.rb_pos_ia:
                        self.showRanks(RA, SA)
                        self.position = "IA"
                        self.enableWingAndSqnTab(False)
                        break

                    # Command Attache.
                    elif radioButton == self.gui.rb_pos_ca:
                        self.showRanks(RA, SA)
                        self.position = "CA"
                        self.enableWingAndSqnTab(False)
                        break

                    # Sub-Group Commander.
                    elif radioButton == self.gui.rb_pos_sgcom:
                        self.showRanks(RA, GA)
                        self.position = "SGCOM"
                        self.enableWingAndSqnTab(False)
                        break

                    # Command Staff.
                    elif radioButton == self.gui.rb_pos_cs:
                        self.showRanks(RA, GA)
                        self.position = "CS"
                        self.enableWingAndSqnTab(False)
                        break

                    # Executive Officer.
                    elif radioButton == self.gui.rb_pos_xo:
                        self.showRanks(RA, GA)
                        self.position = "XO"
                        self.enableWingAndSqnTab(False)
                        break

                    # Fleet Commander.
                    elif radioButton == self.gui.rb_pos_fc:
                        self.showRanks(GA, GA)
                        self.position = "FC"
                        self.gui.rb_rank_ga.setChecked(True)
                        self.rankRBLogic()
                        self.enableWingAndSqnTab(False)
                        break

                    # Line Ranks.
                    elif radioButton == self.gui.rb_pos_lr:
                        self.showRanks(CT, GN)
                        self.position = "LR"
                        self.enableWingAndSqnTab(False)
                        break

                    # Flag Ranks.
                    elif radioButton == self.gui.rb_pos_fr:
                        self.showRanks(RA, GA)
                        self.position = "FR"
                        self.enableWingAndSqnTab(False)
                        break
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def enableWingAndSqnTab(self, boolEnabled):
        '''Method that enables all options in the 'Wing and Squadron' tab.'''

        if boolEnabled:
            # Add the Ships to the Ships list view.
            if self.gui.lw_ship.count() == 0:
                self.gui.lw_ship.clear()
                for ship in self.fleetConfig.options("fleet"):
                    if ship != "count":
                        self.gui.lw_ship.addItem(self.fleetConfig.get("fleet", ship))

            # Populate the 'Wing' List Widget with the Wings for the selected Ship.
            try:
                if self.gui.lw_wing.count() == 0:
                    # Populate the 'Wing' List Widget with the Wings for the selected Ship.
                    for wing in self.fleetConfig.options(str(self.gui.lw_ship.currentItem().text())):
                        self.gui.lw_wing.addItem(self.fleetConfig.get(str(self.gui.lw_ship.currentItem().text()), wing))
            except AttributeError:
                pass

            # Populate the 'Squadron' List Widget with the Squadrons for the selected Wing.
            try:
                if self.gui.lw_squad.count() == 0:
                    # Populate the 'Wing' List Widget with the Wings for the selected Ship.
                    for squadron in self.fleetConfig.options(str(self.gui.lw_wing.currentItem().text())):
                        self.gui.lw_squad.addItem(self.fleetConfig.get(str(self.gui.lw_wing.currentItem().text()), squadron))
            except AttributeError:
                pass

        else:
            self.gui.cb_eliteSqn.setChecked(False)
            self.gui.lw_ship.clear()
            self.ship = ""
            self.gui.lw_wing.clear()
            self.wing = ""
            self.gui.lw_squad.clear()
            self.sqn = ""

        self.gui.lw_ship.setEnabled(boolEnabled)
        self.gui.lw_wing.setEnabled(boolEnabled)
        self.gui.lw_squad.setEnabled(boolEnabled)
        self.gui.cb_eliteSqn.setEnabled(boolEnabled)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def rankRBLogic(self):
        '''Method that controls the Rank Radio Button Logic - Showing the 'Dress and Duty Uniform' buttons.'''

        try:
            # Determine which rank radio button has been selected.
            for radioButton in self.rankRadioButtons:
                if radioButton.isChecked():

                    # Set the correct rank for the selected rank.
                    if radioButton == self.gui.rb_rank_ct:
                        self.rank = "CT"
                        break

                    elif radioButton == self.gui.rb_rank_sl:
                        self.rank = "SL"
                        break

                    elif radioButton == self.gui.rb_rank_lt:
                        self.rank = "LT"
                        break

                    elif radioButton == self.gui.rb_rank_lcm:
                        self.rank = "LCM"
                        break

                    elif radioButton == self.gui.rb_rank_cm:
                        self.rank = "CM"
                        break

                    elif radioButton == self.gui.rb_rank_cpt:
                        self.rank = "CPT"
                        break

                    elif radioButton == self.gui.rb_rank_maj:
                        self.rank = "MAJ"
                        break

                    elif radioButton == self.gui.rb_rank_lc:
                        self.rank = "LC"
                        break

                    elif radioButton == self.gui.rb_rank_col:
                        self.rank = "COL"
                        break

                    elif radioButton == self.gui.rb_rank_gn:
                        self.rank = "GN"
                        break

                    elif radioButton == self.gui.rb_rank_ra:
                        self.rank = "RA"
                        break

                    elif radioButton == self.gui.rb_rank_va:
                        self.rank = "VA"
                        break

                    elif radioButton == self.gui.rb_rank_ad:
                        self.rank = "AD"
                        break

                    elif radioButton == self.gui.rb_rank_fa:
                        self.rank = "FA"
                        break

                    elif radioButton == self.gui.rb_rank_ha:
                        self.rank = "HA"
                        break

                    elif radioButton == self.gui.rb_rank_sa:
                        self.rank = "SA"
                        break

                    elif radioButton == self.gui.rb_rank_ga:
                        self.rank = "GA"
                        break

            # Enable the Dress and Duty Uniform buttons.
            self.gui.btn_dress.setEnabled(True)
            self.gui.btn_duty.setEnabled(True)
        except Exception as e:
            handleException(e)
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

        for rankRadioButton in self.rankRadioButtons[rankMin: rankMax + 1]:  # + 1 because Python doesn't include the last item when indexing.
            rankRadioButton.show()
        #----------------------------------------------------------------------------------------------------------------------------------------#

    def btn_dressMethod(self):
        '''Method that is triggered when the 'Dress Uniform' button is clicked.
           This method will check that the correct selections has been made within TTT3 such as Ship and Squadron and then
           directly call 'launchPOVRay' to open up PovRay and render the unirom.'''

        try:
            self.continueRender = True

            # Check to see if the user has made the correct selections for their position and rank.
            if self.position in ["FM", "FL", "CMDR", "WC"] and self.gui.cb_eliteSqn.isChecked() == False:
                if not self.ship or not self.wing:
                    msg = "Error: As a pilot you need to specify at least a ship and wing before a dress uniform can be created."
                    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                else:
                    self.createDressPov()
                    self.launchPOVRay("dress")

            elif self.gui.cb_eliteSqn.isChecked() and not self.sqn:
                msg = "Error: As an elite pilot you need to specify a squadron before a dress uniform can be created."
                return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

            elif self.position in ["COM"]:
                if not self.ship:
                    msg = "Error: As a COM you need to specify a ship before a dress uniform can be created."
                    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                else:
                    self.createDressPov()
                    self.launchPOVRay("dress")

            # Run PovRay to render a uniform.
            else:
                self.createDressPov()
                if self.continueRender:
                    self.launchPOVRay("dress")
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_dutyMethod(self):
        '''Method that is triggered when the 'Duty Uniform' button is clicked.
           This method will check that the correct selections has been made within TTT3 such as Ship and Squadron and then
           directly call 'launchPOVRay' to open up PovRay and render the unirom.'''

        try:
            self.createDutyPov()
            self.launchPOVRay("duty")
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def launchPOVRay(self, uniform):
        '''Method that dynamically writes data\batch\povray.bat and invisible.vbs to silently launch POV-Ray with the correct paths.
           data\batch\povray.bat and invisible.vbs are delete after POV-Ray is closed.
           The "uniform" agrument takes "dress", "duty or "helmet which is dependant on which button has been pressed."'''

        # Create the '..data\batch' directory if it doesn't already exist.
        try:
            os.mkdir("data\\batch")
        except WindowsError:
            pass  # Direcory already exists.

        # Dynamically write the 'data\batch\povray.bat' file.
            # Set the correct paths based on where TTT3 is located and the TTT3.ini settings file.
        if not self.fastRendering:
            template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\&TYPE&.pov" +W640 +H853 +Q9 +AM2 +A0.1 +D +F +GA +J1.0 -D /EXIT'
        else:
            template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\&TYPE&.pov" +W640 +H853 +Q6 -D /EXIT'
        template = template.replace("&TTTPATH&", os.getcwd())

        # Apply the path depending on what the user has selected from within the Configuratrion window.
        if self.config.get("POV-Ray", "detection_mode") == "registry":
            template = template.replace("&POVPATH&", self.getPathFromRegistry())
        else:
            template = template.replace("&POVPATH&", self.config.get("POV-Ray", "user_specified_path"))

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

        # Delete invisible.vbs and povray.bat.
        os.remove(r"data\batch\invisible.vbs")
        os.remove(r"data\batch\povray.bat")
        os.removedirs(r"data\batch")

        self.gui.setWindowFlags(self.gui.windowFlags() | Qt.WindowStaysOnBottomHint)
        self.gui.show()
        self.showOutputDialog(uniform)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def showOutputDialog(self, uniform):
        '''Method to display the POV-Ray rendered image.'''

        # Determin the version of POV-Ray and it's associated file output type.
        if self.config.get("POV-Ray", "detection_mode") == "registry":
            if "3.6" in self.config.get("POV-Ray", "registry_detected_path"):
                ext = ".bmp"
            else:
                ext = ".png"

        elif self.config.get("POV-Ray", "detection_mode") == "specific":
            if "3.6" in self.config.get("POV-Ray", "user_specified_path"):
                ext = ".bmp"
            else:
                ext = ".png"

        self.imagePath = r"data\%s%s" % (uniform, ext)

        # Load our GUI file 'data\uis\output.ui'
        self.output_gui = uic.loadUi(r"data\uis\output.ui")
        self.output_gui.lbl_output.setPixmap(QPixmap(self.imagePath))
        self.output_gui.show()
        self.output_gui.btn_upload.setEnabled(False)  # TODO Output upload diabled UTFN.
        self.output_gui.btn_saveAs.clicked.connect(self.btn_saveAsFunc)
        self.output_gui.closeEvent = self.outputCloseEvent
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_saveAsFunc(self):
        '''Method to Save As the rendered image file.'''

        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            saveName, ext = QFileDialog.getSaveFileName(self, "Save Uniform As", "C:\\users\\" +
                                                        os.getlogin() + "\\Pictures\\untitled", "*.png;;*.jpg;;*.gif;;*.bmp", options=options)
            ext = ext.replace("*", "")
            if saveName:
                saveName = saveName.replace(r"/", "\\") + ext
                self.convertImage(self.imagePath, ext, saveName)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def povrayMonitor(self):
        '''Monitors for POV-Ray running in the background and signals when it has closed.'''

        time.sleep(0.1)  # Allow some time for POV-Ray to open.
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
                        break
                except BaseException:
                    pass
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def convertImage(self, src, ext, dest):
        '''Converts a given .bpf file into .jpg, .gif, .png or .bmp'''

        img = Image.open(src)
        new_img = img.resize((640, 853))
        newFilePath = dest.split(".")[0] + ext
        if ext == ".jpg":
            ext = ".jpeg"
        new_img.save(newFilePath, ext.replace(".", ""))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadSettings(self):
        r'''Method that reads in 'settings\TT3.ini' and stores the data as a configparser object.'''

        self.config = configparser.ConfigParser()
        self.config.read(r"settings\TTT3.ini")
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def applySettings(self):
        '''Method that applies the settings to the 'Configuration' window.'''

        # ----- Mode. -----
        if self.config.get("POV-Ray", "detection_mode") == "registry":
            self.config_gui.rb_reg.setChecked(True)

        elif self.config.get("POV-Ray", "detection_mode") == "specific":
            self.config_gui.rb_specific.setChecked(True)

        else:
            msg = "Error: Invalid setting for 'mode' in TTT3.ini."
            return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

        # ----- All other values -----
        self.config_gui.lbl_regPath.setText(self.config.get("POV-Ray", "registry_detected_path"))
        self.config_gui.le_specPath.setText(self.config.get("POV-Ray", "user_specified_path"))
        self.config_gui.le_backend.setText(self.config.get("TCDB", "api"))
        self.config_gui.le_roster.setText(self.config.get("TCDB", "roster"))
        self.config_gui.le_search.setText(self.config.get("TCDB", "search"))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def saveSettings(self):
        r'''Method that saves the user's settings to 'settings\TT3.ini'.'''

        with open(r"settings\TTT3.ini", "w") as settingsFile:
            self.config.write(settingsFile)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_configMethod(self):
        '''Method that opens and handles control of the 'Configuration' window.'''

        try:
            # Load in the settings for TTT3.ini.
            self.loadSettings()

            # Load our GUI file 'data\uis\config.ui'.
            self.config_gui = uic.loadUi(r"data\uis\config.ui")
            self.config_gui.show()

            # GUI Connections.
            self.config_gui.btn_config_close.clicked.connect(self.config_gui.close)
            self.config_gui.btn_config_ok.clicked.connect(self.config_btn_ok_method)
            self.config_gui.rb_reg.toggled.connect(self.config_rb_reg_logic)
            self.config_gui.rb_specific.toggled.connect(self.config_rb_specific_logic)
            self.config_gui.btn_config_browse.clicked.connect(self.config_browse)

            # Set the values displayed to the values in our config / setting from 'settings\TTT3.ini'.
            self.applySettings()

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def config_rb_reg_logic(self, value=None):
        '''Method that controls what happens within the 'Configuration' window if a 'POV' radio button is clicked.'''

        try:
            # Enable the registry path options.
            self.config_gui.lbl_regPathTitle.setEnabled(True)
            self.config_gui.lbl_regPath.setEnabled(True)
            self.config_gui.lbl_regPath.setText(self.getPathFromRegistry())

            # Disable the specific path options.
            self.config_gui.le_specPath.setEnabled(False)
            self.config_gui.btn_config_browse.setEnabled(False)

            # Save our setting.
            self.config.set("POV-Ray", "detection_mode", "registry")
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def config_rb_specific_logic(self, value=None):
        '''Method that controls what happens within the 'Configuration' window if a 'POV' radio button is clicked.'''

        try:
            # Enable the specific path options.
            self.config_gui.le_specPath.setEnabled(True)
            self.config_gui.btn_config_browse.setEnabled(True)

            # Disable the registry path options.
            self.config_gui.lbl_regPathTitle.setEnabled(False)
            self.config_gui.lbl_regPath.setEnabled(False)

            # Save our setting.
            self.config.set("POV-Ray", "detection_mode", "specific")
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def config_btn_ok_method(self):
        '''Method that handles the functionality when the 'OK' button is pressed within  the 'Configuration' screen.'''

        try:
            # Test to ensure that the direct POV-Ray-Ray exceutable is present.
            if self.config.get("POV-Ray", "detection_mode") == "specific":

                if not os.path.exists(self.config_gui.le_specPath.text()):
                    msg = "Cannot find valid installion of POV-Ray-Ray at:\n\n%s" % str(self.config_gui.le_specPath.text())
                    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

                else:
                    # Save the direct path.
                    self.config.set("POV-Ray", "user_specified_path", self.config_gui.le_specPath.text())

            else:
                # Seve the detected registry path.
                self.config.set("POV-Ray", "registry_detected_path", self.config_gui.lbl_regPath.text())

            # All other settings.
            self.config.set("TCDB", "api", str(self.config_gui.le_backend.text()))
            self.config.set("TCDB", "roster", str(self.config_gui.le_roster.text()))
            self.config.set("TCDB", "search", str(self.config_gui.le_search.text()))

            # Save and close.
            self.saveSettings()
            self.config_gui.close()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def getPathFromRegistry(self):
        '''Method to detect the installation path of POV-Ray from the Windows registry using the provided options..'''

        # Determine the highest version of POV-Ray from the version setting in 'TTT3.ini'.
        path = False
        version = float(self.config.get("POV-Ray", "target_version"))

        while not path:
            try:
                # Obtain the path to POV-Ray.
                aKey = "Software\\POV-Ray\\v" + str(version) + "\\Windows\\"
                values = winreg.OpenKey(winreg.HKEY_CURRENT_USER, aKey, 0, winreg.KEY_READ)
                path = winreg.QueryValueEx(values, "Home")[0]

            except WindowsError:
                version -= 0.1
                version = round(version, 1)

                # Fall back to CurrentVerison if all else fails.
                if version < 3.6:
                    aKey = "Software\\POV-Ray\\CurrentVersion\\Windows\\"
                    values = winreg.OpenKey(winreg.HKEY_CURRENT_USER, aKey)
                    path = winreg.QueryValueEx(values, "Home")[0]
                    self.config.set("POV-Ray", "detection_mode", "fallback")

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
            return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

        # Save the detected path and return the value.
        self.config.set("POV-Ray", "registry_detected_path", path)
        self.saveSettings()
        return path
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def config_browse(self):
        '''Method that allows the user to select an executable file from a file picker.'''

        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self, "Browse for POV-Ray Installation", "C:\\",
                                                      "pvengine64.exe;;pvengine.exe", options=options)
            if fileName:
                fileName = fileName.replace(r"/", "\\")
                self.config_gui.le_specPath.setText(fileName)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def createDressPov(self):
        r'''Method that loads in '\data\dress.tpt' parses in the correct uniform data and creates a new 'data\dress.pov' file.'''

        quantity = 1

        # Read in the template data.
        with open(r"data\dress.tpt", "r") as tptFile:
            template = tptFile.readlines()

        # Header text.
        position = ""
        if self.position == "NUL" or self.position == "LR" or self.position == "FR":
            position = "    "
        else:
            position = self.position + "/"

        posRankName = position + self.rank + " " + self.name
        padding = (34 - len(posRankName)) * " "
        posRankName += padding

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d  %H:%M:%S")
        padding = (64 - len(timestamp)) * " "
        timestamp += padding

        version = self.version
        padding = (59 - len(version)) * " "
        version += padding

        header = """ ////////////////////////////////////////////////////////////////////
//                                                                 //
// EH/TIE Corps Dress Uniform of {posRankName}//
//                                                                 //
// POV Scene file generated by TIECorps Tailoring                  //
// Tool {version}//
//                                                                 //
// {timestamp}//
//                                                                 //
// Uniform created by LC Tempest, based on the model by            //
// Raphael de Bouchony a.k.a Tron (Imperial Officer, SciFi 3D)     //
//                                                                 //
// Geometry data POV export by 3DWin5 V 5.6                        //
// 3dto3d engine by tb-software.com (support@tb-software.com)      //
// Created by POV Export Plugin 1.2                                //
//                                                                 //
// https://www.emperorshammer.org/                                 //
// https://tc.emperorshammer.org/                                  //
// https://ehnet.org/                                              //
// http://www.povray.org/                                          //
//                                                                 //
////////////////////////////////////////////////////////////////////
""".format(posRankName=posRankName, version=version, timestamp=timestamp)

        povData = []

        for line in header:
            povData.append(line)

        # Parse the template data.
        for line in template:

            # ----- Global. -----
            if "&BGCOLOUR&" in line:
                povData.append(line.replace("&BGCOLOUR&", "0, 0, 0"))  # TODO createDressPov() BGCOLOUR

            # ----- Light. -----

            elif "&LIGHT&" in line:
                povData.append(line.replace("&LIGHT&", "1518.5, -647.4, 1750.1"))  # TODO createDressPov() OpenGL BGCOLOUR

            elif "&SPOTLIGHTCOLOUR&" in line:
                povData.append(line.replace("&SPOTLIGHTCOLOUR&", "1, 1, 1"))  # TODO createDressPov() OpenGL SPOTLIGHTCOLOUR

            elif "&SHADOWLESS&" in line:
                povData.append(line.replace("&SHADOWLESS&", ""))  # TODO createDressPov() OpenGL SHADOWLESS

            # ----- Camera. -----

            elif "&CAMERA&" in line:
                povData.append(line.replace("&CAMERA&", "-260.8, -1331.1, 209.0"))  # TODO createDressPov() OpenGL CAMERA

            elif "&TARGET&" in line:
                povData.append(line.replace("&TARGET&", "0, -12.8, 2.8"))  # TODO createDressPov() OpenGL TARGET

            # ----- Basic Info. -----
            elif "&EE&" in line:
                if self.eeCount >= 3:
                    povData.append(line.replace("&EE&", "#declare prae = 1;"))
                    self.eeCount = 0
                    self.gui.label_11.setText("AD Turtle Jerrar,")
                    self.gui.label_11.setStyleSheet("")
                else:
                    povData.append(line.replace("&EE&", ""))

            elif "&CLOTH&" in line:
                povData.append(line.replace("&CLOTH&", "0"))  # TODO createDressPov() OpenGL CLOTH

            elif "&POSITION&" in line:
                if self.position == "TRN" or self.position == "LR" or self.position == "FR":
                    povData.append(line.replace("&POSITION&", "NUL"))
                else:
                    povData.append(line.replace("&POSITION&", self.position))

            elif "&RANK&" in line:
                povData.append(line.replace("&RANK&", self.rank))

            elif "&RANKROTATE&" in line:
                povData.append(line.replace("&RANKROTATE&", self.getRankRotateOffset()))

            elif "&RANKTRANSLATE&" in line:
                povData.append(line.replace("&RANKTRANSLATE&", self.getRankTranslateOffset()))

            # ----- Assignment. -----
            elif "&CATEGORY&" in line:

                if self.position == "NUL" or self.position == "LR" or self.position == "FR":
                    povData.append(line.replace("&CATEGORY&", "reserve"))

                elif self.rank in ["CT", "SL", "LT", "LCM", "CM", "CPT", "MAJ", "LC", "COL", "GN"]:
                    povData.append(line.replace("&CATEGORY&", "line"))

                else:
                    povData.append(line.replace("&CATEGORY&", "flag"))

            elif "&SHIP&" in line:
                povData.append(line.replace("&SHIP&", self.ship))

            elif "&WING&" in line:
                povData.append(line.replace("&WING&", self.wing))

            elif "&SQUAD&" in line:
                povData.append(line.replace("&SQUAD&", self.sqn))

                # Create squadron patch mask.
                if self.sqn != "":
                    self.createPatchMask()

            elif "&TRIMCOLOUR&" in line:
                if self.gui.cb_eliteSqn.isChecked():
                    povData.append(line.replace("&TRIMCOLOUR&", "white"))

                elif self.position in ["COM", "TCCS", "IA", "CA", "SGCOM", "CS", "XO", "FC"]:
                    povData.append(line.replace("&TRIMCOLOUR&", "gold"))

                elif self.wing == "Wing I":
                    povData.append(line.replace("&TRIMCOLOUR&", "black"))

                elif self.wing == "Wing II":
                    povData.append(line.replace("&TRIMCOLOUR&", "red"))

                elif self.wing == "Wing X":
                    povData.append(line.replace("&TRIMCOLOUR&", "blue"))

                else:
                    povData.append(line.replace("&TRIMCOLOUR&", "black"))  # TODO Automate trim colouring so not hard coded.

            # ----- Medals. -----
            elif "&MABGS&" in line:
                num = self.awards.get("Gold Star of the Empire (GS)")["upgrades"][quantity]
                povData.append(line.replace("&MABGS&", str(int(num) - 1)))

            elif "&MABSS&" in line:
                num = self.awards.get("Silver Star of the Empire (SS)")["upgrades"][quantity]
                povData.append(line.replace("&MABSS&", str(int(num) - 1)))

            elif "&MABBS&" in line:
                num = self.awards.get("Bronze Star of the Empire (BS)")["upgrades"][quantity]
                povData.append(line.replace("&MABBS&", str(int(num) - 1)))

            elif "&MABPC&" in line:
                num = self.awards.get("Palpatine Cresent (PC)")["upgrades"][quantity]
                povData.append(line.replace("&MABPC&", str(int(num) - 1)))

            elif "&MABISM&" in line:
                num = self.awards.get("Imperial Security Medal (ISM)")["upgrades"][quantity]
                povData.append(line.replace("&MABISM&", str(int(num) - 1)))

            # ----- Other. -----

            elif "&PADINCLUDE&" in line:
                if self.position in ["CS", "XO", "FC"]:
                    povData.append(line.replace("&PADINCLUDE&", '#include "pad_braids_g.inc"'))

                elif self.position in ["IA", "CA", "SGCOM"]:
                    povData.append(line.replace("&PADINCLUDE&", '#include "pad_braid_g.inc"'))

                else:
                    povData.append(line.replace("&PADINCLUDE&", '#include "pad_g.inc"'))

            elif "&FCHGINCLUDE&" in line:
                if not self.gui.cbFCHG.currentText() == "None (0 Pts)":
                    povData.append(line.replace("&FCHGINCLUDE&", '#include "fchg_g.inc"'))
                else:
                    povData.append(line.replace("&FCHGINCLUDE&", ""))

            elif "&SABERINCLUDE&" in line:
                povData.append(line.replace("&SABERINCLUDE&", ""))  # TODO SABERINCLUDE

            elif "&MEDALSINCLUDE&" in line:
                for includeRef in self.buildMedalIncludes():
                    povData.append('#include "%s"\n' % includeRef)

            # ----- Scene. -----

            # Fleet Commander's Honour Guard. -------------------------------
            elif "&FCHG&" in line:
                if "None" in self.gui.cbFCHG.currentText():
                    pass

                elif "Grenadier" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { gren }"))

                elif "Lancer" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { lanc }"))

                elif "Hussar" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { huss }"))

                elif "Fusilier" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { fusl }"))

                elif "Dragoon" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { drag }"))

                elif "Cavalier" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { cavl }"))

                elif "Gallant" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { gall }"))

                elif "Knight" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { kngt }"))

                elif "Paladin" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { pldn }"))

                elif "Legionnaire" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { lgnr }"))

                elif "Aquilifer" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { aqfr }"))

                elif "Decurion" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { dcrn }"))

                elif "Tesserarius" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { tsrs }"))

                elif "Optio" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { opti }"))

                elif "Centurion" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { cntr }"))

                elif "Executor" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { excr }"))

                elif "Gladiator" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { gldr }"))

                elif "Archon" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { arcn }"))

                elif "Templar" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { tmpr }"))

                elif "Imperator" in self.gui.cbFCHG.currentText():
                    povData.append(line.replace("&FCHG&", "object { impr }"))

                else:
                    pass
                # ------------------------------------------------------------

            elif "&SABER&" in line:
                povData.append(line.replace("&SABER&", ""))  # TODO SABER

            elif "&PAD&" in line:
                if self.rank == "CT":
                    povData.append(line.replace("&PAD&", ""))
                else:
                    povData.append(line.replace("&PAD&", "object { P_pad }"))

            elif "&PADTRIM&" in line:
                if self.rank == "CT":
                    povData.append(line.replace("&PADTRIM&", "object { P_shoulder_right }"))
                else:
                    povData.append(line.replace("&PADTRIM&", "object { P_pad_left texture { T_pad_left } }  "))

            elif "&MEDALS&" in line:
                for objectRef in self.buildMedalObjects():
                    povData.append('object { %s }\n' % objectRef)

            elif "&RIBBONS&" in line:
                objectRefs = self.buildRibbonObjects()

                # Check to see if the user has selected 24 or less ribbons.
                if len(objectRefs) > 24:
                    self.continueRender = False
                    # Show error message.
                    msg = "You have selected more than 24 ribbons. Unfortunately TTT3 cannot make a uniform with more than 24 ribbons at this time.\n\n Please select less ribbon awards."
                    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

                else:
                    for objectRef in objectRefs:
                        povData.append('object { %s }\n' % objectRef)

            # ----- Non-Editable Data. -----
            else:
                povData.append(line)

        # Write the parsed data to '\data\dress.pov'.
        with open(r"data\dress.pov", "w") as povFile:
            povFile.writelines(povData)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def createDutyPov(self):
        r'''Method that loads in '\data\duty.tpt' parses in the correct uniform data and creates a new 'data\duty.pov' file.'''

        quantity = 1

        # Read in the template data.
        with open(r"data\duty.tpt", "r") as tptFile:
            template = tptFile.readlines()

        # Header text.
        position = ""
        if self.position == "NUL" or self.position == "LR" or self.position == "FR":
            position = "    "
        else:
            position = self.position + "/"

        posRankName = position + self.rank + " " + self.name
        padding = (34 - len(posRankName)) * " "
        posRankName += padding

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d  %H:%M:%S")
        padding = (64 - len(timestamp)) * " "
        timestamp += padding

        version = self.version
        padding = (59 - len(version)) * " "
        version += padding

        header = """ ////////////////////////////////////////////////////////////////////
//                                                                 //
// EH/TIE Corps Duty Uniform of {posRankName}//
//                                                                 //
// POV Scene file generated by TIECorps Tailoring                  //
// Tool {version}//
//                                                                 //
// {timestamp}//
//                                                                 //
// Uniform created by LC Tempest, based on the model by            //
// Raphael de Bouchony a.k.a Tron (Imperial Officer, SciFi 3D)     //
//                                                                 //
// Geometry data POV export by 3DWin5 V 5.6                        //
// 3dto3d engine by tb-software.com (support@tb-software.com)      //
// Created by POV Export Plugin 1.2                                //
//                                                                 //
// https://www.emperorshammer.org/                                 //
// https://tc.emperorshammer.org/                                  //
// https://ehnet.org/                                              //
// http://www.povray.org/                                          //
//                                                                 //
////////////////////////////////////////////////////////////////////
""".format(posRankName=posRankName, version=version, timestamp=timestamp)

        povData = []

        for line in header:
            povData.append(line)

        # Parse the template data.
        for line in template:

            # ----- Global. -----
            if "&BGCOLOUR&" in line:
                povData.append(line.replace("&BGCOLOUR&", "0, 0, 0"))  # TODO createDressPov() BGCOLOUR

            # ----- Light. -----

            elif "&LIGHT&" in line:
                povData.append(line.replace("&LIGHT&", "1518.5, -647.4, 1750.1"))  # TODO createDressPov() OpenGL BGCOLOUR

            elif "&SPOTLIGHTCOLOUR&" in line:
                povData.append(line.replace("&SPOTLIGHTCOLOUR&", "1, 1, 1"))  # TODO createDressPov() OpenGL SPOTLIGHTCOLOUR

            elif "&SHADOWLESS&" in line:
                povData.append(line.replace("&SHADOWLESS&", ""))  # TODO createDressPov() OpenGL SHADOWLESS

            elif "&ENVLIGHTCOLOUR&" in line:
                povData.append(line.replace("&ENVLIGHTCOLOUR&", "0.501, 0.462, 0.423"))  # TODO createDressPov() OpenGL ENVLIGHTCOLOUR

            # ----- Camera. -----

            elif "&CAMERA&" in line:
                povData.append(line.replace("&CAMERA&", "-260.8, -1331.1, 209.0"))  # TODO createDressPov() OpenGL CAMERA

            elif "&TARGET&" in line:
                povData.append(line.replace("&TARGET&", "0, -12.8, 2.8"))  # TODO createDressPov() OpenGL TARGET

            # ----- Basic Info. -----
            elif "&CLOTH&" in line:
                povData.append(line.replace("&CLOTH&", "0"))  # TODO createDressPov() OpenGL CLOTH

            elif "&POSITION&" in line:
                if self.position == "TRN" or self.position == "LR" or self.position == "FR":
                    povData.append(line.replace("&POSITION&", ""))
                else:
                    povData.append(line.replace("&POSITION&", "object { P_%s }" % self.position))

            elif "&RANK&" in line:
                povData.append(line.replace("&RANK&", self.rank))

            elif "&RANKROTATE&" in line:
                povData.append(line.replace("&RANKROTATE&", self.getRankRotateOffset()))

            elif "&RANKTRANSLATE&" in line:
                povData.append(line.replace("&RANKTRANSLATE&", self.getRankTranslateOffset()))

            # ----- Non-Editable Data. -----
            else:
                povData.append(line)

        # Write the parsed data to '\data\dress.pov'.
        with open(r"data\duty.pov", "w") as povFile:
            povFile.writelines(povData)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def getRankRotateOffset(self):
        '''Method that returns the correct rank rotate value for the user's medal and ribbon selections.'''

        ribbonCount = self.getRibbonAwardCount()

        if ribbonCount <= 8:
            return self.RANK_OFFSET_RIBBONS_00_TO_08[0]
        elif ribbonCount > 8 and ribbonCount <= 12:
            return self.RANK_OFFSET_RIBBONS_09_TO_12[0]
        elif ribbonCount > 12 and ribbonCount <= 16:
            return self.RANK_OFFSET_RIBBONS_13_TO_16[0]
        elif ribbonCount > 16 and ribbonCount <= 20:
            return self.RANK_OFFSET_RIBBONS_17_TO_20[0]
        elif ribbonCount > 20 and ribbonCount <= 24:
            return self.RANK_OFFSET_RIBBONS_21_TO_24[0]
        else:
            return self.RANK_OFFSET_RIBBONS_21_TO_24[0]
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def getRankTranslateOffset(self):
        '''Method that returns the correct rank rotate value for the user's medal and ribbon selections.'''

        ribbonCount = self.getRibbonAwardCount()

        if ribbonCount <= 8:
            return self.RANK_OFFSET_RIBBONS_00_TO_08[1]
        elif ribbonCount > 8 and ribbonCount <= 12:
            return self.RANK_OFFSET_RIBBONS_09_TO_12[1]
        elif ribbonCount > 12 and ribbonCount <= 16:
            return self.RANK_OFFSET_RIBBONS_13_TO_16[1]
        elif ribbonCount > 16 and ribbonCount <= 20:
            return self.RANK_OFFSET_RIBBONS_17_TO_20[1]
        elif ribbonCount > 20 and ribbonCount <= 24:
            return self.RANK_OFFSET_RIBBONS_21_TO_24[1]
        else:
            return self.RANK_OFFSET_RIBBONS_21_TO_24[1]
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def getRibbonAwardCount(self):
        '''Method that returns the number of indicidual ribbons that the user has selected.'''

        ribbonCount = 0
        name = 0
        quantity = 1

        for award in self.awards:
            # Upgradeable and SubRibbon type awards.
            if self.awards.get(award)["type"] == "upgradeable" or self.awards.get(award)["type"] == "subRibbons":
                for upgrade in self.awards.get(award)["upgrades"]:
                    if upgrade[quantity] != 0:
                        ribbonCount += 1

            # Ranged type awards.
            elif self.awards.get(award)["type"] == "ranged":
                if self.awards.get(award)["upgrades"][quantity] > 0:
                    for section in self.ribbonConfig.sections():
                        if self.ribbonConfig.get(section, "name") == award:
                            ribbonCount += 1

        return ribbonCount
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def createPatchMask(self):
        '''Method that will create a mask file for the desired squadron patch.'''

        fileName = "data\\squads\\{squad}.png".format(squad=self.sqn)

        try:
            # Primary Mask Creation. Requires a transparent background.
            # Load image with alpha channel.
            img = cv2.imread(fileName, cv2.IMREAD_UNCHANGED)
            # Get mask from alpha channel.
            mask = img[:, :, 3]
            # Save the mask.
            fileName = fileName.replace(".png", "_mask.png")
            cv2.imwrite(fileName, mask)

        except IndexError:  # Bacground likely not transparent. Doesn't need a transparent background but does not work well with high color / shaded patches.
            # Alternate Mask creation.
            image = cv2.imread(fileName)
            mask = numpy.ones(image.shape, dtype=numpy.uint8) * 255
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            for c in cnts:
                cv2.drawContours(mask, [c], -1, (0, 0, 0), cv2.FILLED)
            mask = cv2.bitwise_not(mask)
            # Save the mask.
            fileName = fileName.replace(".png", "_mask.png")
            cv2.imwrite(fileName, mask)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def shipSelectionLogic(self, value):
        '''Method that handles the actions once a ship is selected from the 'Ship' section in the 'Wing and Squadron' tab.'''

        try:
            # Clear the 'Wing' ListWidget.
            self.gui.lw_wing.clear()

            try:
                # Save the selected option.
                self.ship = self.gui.lw_ship.currentItem().text()

                if self.position not in ["TRN", "COM", "TCCS", "IA", "CA", "SGCOM", "CS",
                                         "XO", "FC"]:  # Stops Wings and Squadrons showing for COMs and above.

                    # Populate the 'Wing' List Widget with the Wings for the selected Ship.
                    for wing in self.fleetConfig.options(str(self.gui.lw_ship.currentItem().text())):
                        self.gui.lw_wing.addItem(self.fleetConfig.get(str(self.gui.lw_ship.currentItem().text()), wing))
                    self.wingSelectionLogic(None)

                else:
                    if self.position not in ["COM"]:  # Stops Ship List Widget from being cleared.
                        self.gui.lw_ship.clear()
                    self.gui.lw_wing.clear()

            except AttributeError:
                pass  # Prevents the application throwing an error when the 'Ship' List Widget is clears and tries to populate wings from a 'blank' ship.
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def wingSelectionLogic(self, value):
        '''Method that handles the actions once a Wing is selected from the 'Wing' section in the 'Wing and Squadron' tab.'''

        try:
            # Clear the 'Squadron' ListWidget.
            self.gui.lw_squad.clear()

            try:
                # Save the selected option.
                self.wing = self.gui.lw_wing.currentItem().text()

                if self.position not in ["WC"]:  # Stops Squadrons showing for WCs.

                    # Populate the 'Squadron' List Widget with the Squadrons for the selected Wing.
                    for squadron in self.fleetConfig.options(str(self.gui.lw_wing.currentItem().text())):
                        self.gui.lw_squad.addItem(self.fleetConfig.get(str(self.gui.lw_wing.currentItem().text()), squadron))

                else:
                    self.gui.lw_squad.clear()

            except AttributeError:
                pass  # Prevents the application throwing an error when the 'Wing' List Widget is clears and tries to populate squadrons from a 'blank' wing.
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def squadSelectionLogic(self, value):
        '''Method that handles the actions once a Wing is selected from the 'Wing' section in the 'Wing and Squadron' tab.'''

        try:
            # Save the selected option.
            self.sqn = self.gui.lw_squad.currentItem().text()

        except AttributeError:
            pass  # Prevents the application throwing an error when the 'Wing' List Widget clears and tries to populate squadrons from a 'blank' wing.
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def eliteSqnSelectionLogic(self, value):
        '''Method that handles the actions once the 'Elite Squadron' CheckBox is selected.

           0 = Unckecked, 2 = Checked.'''

        try:
            if value == 0:

                # Load and enable the Ship and Wing List Widgets.
                self.gui.lw_ship.setEnabled(True)
                self.gui.lw_wing.setEnabled(True)
                self.gui.lw_squad.clear()
                self.sqn = ""
                self.gui.lw_wing.clear()
                self.wing = ""
                self.gui.lw_ship.clear()
                self.ship = ""

                # Add the Ships to the Ships list view.
                for ship in self.fleetConfig.options("fleet"):
                    if ship != "count":
                        self.gui.lw_ship.addItem(self.fleetConfig.get("fleet", ship))

            elif value == 2:

                # Clear and disable the Ship and Wing List Widgets.
                self.gui.lw_squad.clear()
                self.gui.lw_ship.clear()
                self.gui.lw_ship.setEnabled(False)
                self.gui.lw_wing.clear()
                self.gui.lw_wing.setEnabled(False)

                # Remove any prior saved Ship or Wing.
                self.ship = ""
                self.wing = ""

                # Populate the 'Squadron' List Widget with the Squadrons for the selected Wing.
                for squadron in self.fleetConfig.options("elites"):
                    self.gui.lw_squad.addItem(self.fleetConfig.get("elites", squadron))
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadMedals(self):
        r'''Method that reads in data from 'settings\medals.ini' adds the medals to the 'Medals, Ribbons and FCHG' tab.'''

        # Read in the data from 'settings\medals.ini'.
        self.medalConfig = configparser.ConfigParser()
        self.medalConfig.read(r"settings\medals.ini")

        # Parse 'settings\medals.ini'.
        for medal in self.medalConfig.sections():

            name = self.medalConfig.get(medal, "name")

            # Store the medal in the 'self.awards' dictionary.
            self.awards[name] = {"type": self.medalConfig.get(medal, "type")}
            self.awards[name]["upgrades"] = [name, 0]
            self.awards[name]["includeFile"] = self.medalConfig.get(medal, "incFile")

            for obj in range(1, 101, 1):
                try:  # Add objects such as the Dagger for the GOE.
                    self.awards[name]["objectRef%s" % str(obj)] = self.medalConfig.get(medal, "objRef%s" % str(obj))
                except configparser.NoOptionError:
                    break  # No more objRefs found.

            # Add the medal name to the GUI.
            self.gui.lw_medals.addItem(self.medalConfig.get(medal, "name"))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadRibbons(self):
        '''Method that reads in data from 'settings\ribbons.ini' adds the ribbons to the 'Medals, Ribbons and FCHG' tab
           and then dynamically writes ribbons_g.inc ready for use.'''

        ribbons_g = """ ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Service Award Ribbons                          //
//                                                 //
//  Settings in this file are not affected by TTT  //
//                                                 //
////////////////////////////////////////////////////


#include "ribbons_o.inc";


// RIBBONS


"""
        # Read in the data from 'settings\ribbons.ini'.
        self.ribbonConfig = configparser.ConfigParser()
        self.ribbonConfig.read(r"settings\ribbons.ini")

        # Parse 'settings\ribbons.ini'.
        for ribbon in self.ribbonConfig.sections():

            name = self.ribbonConfig.get(ribbon, "name")

            # Add the ribbon name to the GUI.
            self.gui.lw_medals.addItem(name)

            # Store the ribbon in the 'self.awards' dictionary.
            self.awards[name] = {"type": self.ribbonConfig.get(ribbon, "type")}

            # Ranged ribbons like the OV.
            if self.ribbonConfig.get(ribbon, "type") == "ranged":

                # Create the required inclide declarations for 'ribbons_g.inc'
                rangeMin = int(self.ribbonConfig.get(ribbon, "rangeMin"))
                rangeMax = int(self.ribbonConfig.get(ribbon, "rangeMax"))

                for i in range(rangeMin, rangeMax + 1):  # + 1 as Python omits the last number in a range.

                    filename = self.ribbonConfig.get(ribbon, "filename").replace("&RANGE&", str(i))
                    ribbons_g += self.addToRibbonIncludes(filename)

                # Store the ribbon data to the 'self.awards' dictionary.
                self.awards[name]["upgrades"] = [self.ribbonConfig.get(ribbon, "incrementName"), 0]
                self.awards[name]["ranges"] = [rangeMin, rangeMax]

            # All other ribbons.
            else:
                self.awards[name]["upgrades"] = []

                for option in self.ribbonConfig.options(ribbon):

                    # Store the ribbon data to the 'self.awards' dictionary.
                    if "type" not in option and "name" not in option.lower():
                        self.awards[name]["upgrades"].append([self.ribbonConfig.get(ribbon, option), 0])

                    # Create the required include declarations for 'ribbons_g.inc'
                    if option != "name" and option != "type":
                        # Add the ribbon to ribbons_g.inc
                        if "filename" in option:
                            ribbons_g += self.addToRibbonIncludes(self.ribbonConfig.get(ribbon, option))

        with open("data\\ribbons_g.inc", "w") as ribbonFile:
            ribbonFile.write(ribbons_g)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def addToRibbonIncludes(self, filename):
        '''Method that creates the include data for a single ribbon. This include data goes on to build ribbons_g.inc'''

        ribbonName = filename.replace("-", "_").replace(".gif", "")

        includeTemplate = """#declare T_r_%s =
texture
{
  pigment { image_map { gif ".\\ribbons\\%s" } }
  finish  { fin_T_uni }
}
texture { T_unilayer scale 2}\n\n""" % (ribbonName, filename)

        return includeTemplate
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def hideMedalOptions(self):
        '''Method that hides all Medal Spin Boxes, checkboxes and Radio Buttons.'''

        # Single type awards.
        self.gui.cb_singleMedal.hide()
        self.gui.combo_top.hide()
        self.gui.lbl_top_free_text.hide()

        # Upgradeable type award.
        self.gui.rb_upgradeable_0.hide()
        self.gui.rb_upgradeable_1.hide()
        self.gui.rb_upgradeable_2.hide()
        self.gui.rb_upgradeable_3.hide()
        self.gui.rb_upgradeable_4.hide()
        self.gui.rb_upgradeable_5.hide()

        # Multi type award.
        self.gui.lbl_multi_left1.hide()
        self.gui.lbl_multi_left2.hide()
        self.gui.lbl_multi_left3.hide()
        self.gui.lbl_multi_left4.hide()
        self.gui.sb_multi_left1.hide()
        self.gui.sb_multi_left2.hide()
        self.gui.sb_multi_left3.hide()
        self.gui.sb_multi_left4.hide()

        self.gui.lbl_multi_center1.hide()
        self.gui.lbl_multi_center2.hide()
        self.gui.lbl_multi_center3.hide()
        self.gui.lbl_multi_center4.hide()
        self.gui.sb_multi_center1.hide()
        self.gui.sb_multi_center2.hide()
        self.gui.sb_multi_center3.hide()
        self.gui.sb_multi_center4.hide()

        self.gui.lbl_multi_right1.hide()
        self.gui.lbl_multi_right2.hide()
        self.gui.lbl_multi_right3.hide()
        self.gui.lbl_multi_right4.hide()
        self.gui.sb_multi_right1.hide()
        self.gui.sb_multi_right2.hide()
        self.gui.sb_multi_right3.hide()
        self.gui.sb_multi_right4.hide()

        # Ranged type award.
        self.gui.lbl_ranged.hide()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def medalSelectionLogic(self, item):
        '''Method that handles the actions once a medal is selected from the 'Medals, Ribbons and FCHG tab.'''

        try:
            # Reset the 'Medals, Ribbons and FCHG tab..
            if self.cb_singleMedalConnected:
                self.gui.cb_singleMedal.stateChanged.disconnect()
                self.cb_singleMedalConnected = False

            self.hideMedalOptions()
            self.disconnectAllMedalWidgets()
            self.gui.sb_multi_center2.setRange(0, 99)  # Resets the range if range ribbon/OV was selected.

            name = 0
            quantity = 1

            # Show the Medals GroupBox and set it's title the the selected medal.
            self.gui.gb_medals.show()
            self.gui.gb_medals.setTitle(item.text().split(" (")[0])

            # Show the correct GUI elements for the given medal.
            award = self.awards.get(str(item.text()))  # Str type conversion as you cannot reference a dict with a QString.

            # === Medals ===
            # ----- Single type medal awards. (MOH, IC, OoR, GOE)
            if award.get("type") == "single":
                self.gui.cb_singleMedal.setText(award.get("upgrades")[name])

                if award.get("upgrades")[quantity] == 0:
                    self.gui.cb_singleMedal.setChecked(False)
                else:
                    self.gui.cb_singleMedal.setChecked(True)

                if not self.cb_singleMedalConnected:
                    self.gui.cb_singleMedal.stateChanged.connect(self.cb_singleMedalSelectionLogic)
                    self.cb_singleMedalConnected = True

                self.gui.cb_singleMedal.show()
                self.neckRibbonDeconfliction()

                # ----- Multi type medal awards. (GS, SS, BS, PC, ISM)
            elif award.get("type") == "multi":
                self.gui.lbl_multi_center1.setText(award.get("upgrades")[name])
                self.gui.lbl_multi_center1.show()
                self.gui.sb_multi_center1.setValue(award.get("upgrades")[quantity])
                self.gui.sb_multi_center1.show()
                self.gui.sb_multi_center1.valueChanged.connect(self.sb_multi_center1Logic)

                # === Ribbons ===
                # ----- Upgradeable type ribbon awards. (MoI, LoC, LoS, DFC)
            elif award.get("type") == "upgradeable":
                self.gui.cb_singleMedal.setText(item.text())

                for upgrade in award.get("upgrades"):
                    if upgrade[quantity] == 1:
                        self.gui.cb_singleMedal.setChecked(True)
                        break
                    else:
                        self.gui.cb_singleMedal.setChecked(False)

                if not self.cb_singleMedalConnected:
                    self.gui.cb_singleMedal.stateChanged.connect(self.cb_singleMedalSelectionLogic)
                    self.cb_singleMedalConnected = True

                self.gui.cb_singleMedal.show()
                self.showUpgradeableRadioButtons()

                # ----- SubRibbons type ribbon awards. (MoS, MoT, IS, MoC, CoX)
            elif award.get("type") == "subRibbons":
                # Determine the number of subRibbons the award has for SpinBox assignment.
                subRibbonNum = len(award.get("upgrades"))
                upgrades = award.get("upgrades")

                if subRibbonNum <= 4:
                    spinBoxes = [self.gui.sb_multi_center1, self.gui.sb_multi_center2, self.gui.sb_multi_center3, self.gui.sb_multi_center4]
                    spinBoxes = spinBoxes[: subRibbonNum]
                    spinLabels = [self.gui.lbl_multi_center1, self.gui.lbl_multi_center2, self.gui.lbl_multi_center3, self.gui.lbl_multi_center4]
                    spinLabels = spinLabels[: subRibbonNum]
                    spinFunctions = [self.sb_multi_center1Logic, self.sb_multi_center2Logic, self.sb_multi_center3Logic, self.sb_multi_center4Logic]
                    spinFunctions = spinFunctions[: subRibbonNum]
                else:
                    spinBoxes = [self.gui.sb_multi_left1, self.gui.sb_multi_left2, self.gui.sb_multi_left3, self.gui.sb_multi_left4,
                                 self.gui.sb_multi_right1, self.gui.sb_multi_right2, self.gui.sb_multi_right3, self.gui.sb_multi_right4]
                    spinBoxes = spinBoxes[: subRibbonNum]
                    spinLabels = [self.gui.lbl_multi_left1, self.gui.lbl_multi_left2, self.gui.lbl_multi_left3, self.gui.lbl_multi_left4,
                                  self.gui.lbl_multi_right1, self.gui.lbl_multi_right2, self.gui.lbl_multi_right3, self.gui.lbl_multi_right4]
                    spinLabels = spinLabels[: subRibbonNum]
                    spinFunctions = [self.sb_multi_left1Logic, self.sb_multi_left2Logic, self.sb_multi_left3Logic, self.sb_multi_left4Logic,
                                     self.sb_multi_right1Logic, self.sb_multi_right2Logic, self.sb_multi_right3Logic, self.sb_multi_right4Logic]
                    spinFunctions = spinFunctions[: subRibbonNum]

                # Show the required spinboxes.
                self.subRibbonAwards = []
                for subRibbon in range(0, subRibbonNum):
                    spinBoxes[subRibbon].setValue(upgrades[subRibbon][quantity])
                    spinBoxes[subRibbon].show()
                    spinBoxes[subRibbon].valueChanged.connect(spinFunctions[subRibbon])
                    spinLabels[subRibbon].setText(upgrades[subRibbon][name])
                    spinLabels[subRibbon].show()
                    self.subRibbonAwards.append([self.gui.lw_medals.currentItem().text(), upgrades[subRibbon][name], spinBoxes[subRibbon]])

                # ----- Ranged type ribbon awards. (OV)
            elif award.get("type") == "ranged":
                self.gui.cb_singleMedal.setText(item.text())

                # Specify the award data for the spinbox.
                self.subRibbonAwards = []
                self.subRibbonAwards.append(self.gui.lw_medals.currentItem().text())
                self.subRibbonAwards.append(self.gui.sb_multi_center2)

                # Set the checkbox state.
                if award.get("upgrades")[quantity] > 0:
                    self.gui.cb_singleMedal.setChecked(True)
                    self.cb_singleMedalSelectionLogic()
                else:
                    self.gui.cb_singleMedal.setChecked(False)

                # Connect the checkbox.
                if not self.cb_singleMedalConnected:
                    self.gui.cb_singleMedal.stateChanged.connect(self.cb_singleMedalSelectionLogic)
                    self.cb_singleMedalConnected = True

                self.gui.cb_singleMedal.show()

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_singleMedalSelectionLogic(self):
        '''Method that handles the actions once a medal is selected in the 'Medals, Ribbons and FCHG tab.'''

        try:
            # Str type conversion as you cannot reference a dict with a QString.
            award = self.awards.get(str(self.gui.lw_medals.currentItem().text()))
            name = 0
            quantity = 1

            # === Medals ===
            # ----- Single type medal awards. (MOH, IC, OoR, GOE)
            if award.get("type") == "single":

                if self.gui.cb_singleMedal.isChecked():
                    self.awards.get(str(self.gui.cb_singleMedal.text()))["upgrades"][quantity] = 1
                else:
                    self.awards.get(str(self.gui.cb_singleMedal.text()))["upgrades"][quantity] = 0

                # IC & GOE Deconfliction.
                self.neckRibbonDeconfliction()

            # === Ribbons ===
                # ----- Upgradeable type ribbon awards. (MoI)
            elif award.get("type") == "upgradeable":

                widgets = [self.gui.rb_upgradeable_0, self.gui.rb_upgradeable_1, self.gui.rb_upgradeable_2,
                           self.gui.rb_upgradeable_3, self.gui.rb_upgradeable_4, self.gui.rb_upgradeable_5]

                if self.gui.cb_singleMedal.isChecked():

                    # Set the initial selection.
                    self.gui.rb_upgradeable_0.setChecked(True)
                    selectionMade = False

                    for upgrade in award.get("upgrades"):
                        if upgrade[quantity] == 1:
                            selectionMade = True

                    if not selectionMade:
                        award.get("upgrades")[0][quantity] = 1
                    self.showUpgradeableRadioButtons()

                else:
                    # Reset the user selections.
                    for upgrade in award.get("upgrades"):
                        upgrade[quantity] = 0

                    # Reset the selection.
                    self.gui.rb_upgradeable_0.setChecked(True)

                    # Hide and disconnect the radio buttons.
                    for widget in widgets:
                        widget.hide()
                        # Disconnect the radio buttons.
                        if self.rb_upgradeablesConnected:
                            try:
                                widget.clicked.disconnect()
                            except TypeError:
                                pass  # Prevents a crash when trying to disconnect a widget that isn't connected to aything.
                    self.rb_upgradeablesConnected = False

                # ----- Ranged type ribbon awards. (OV)
            elif award.get("type") == "ranged":

                if self.gui.cb_singleMedal.isChecked():

                    # Setup and display the ribbon's spinbox and label.
                    rangeMin = int(award.get("ranges")[0])
                    rangeMax = int(award.get("ranges")[1])
                    self.gui.sb_multi_center2.setRange(rangeMin, rangeMax)
                    self.gui.sb_multi_center2.setValue(award.get("upgrades")[quantity])
                    self.gui.sb_multi_center2.show()
                    self.gui.sb_multi_center2.valueChanged.connect(self.sb_multi_center2Logic)
                    self.gui.lbl_ranged.setText(award.get("upgrades")[name] + ":")
                    self.gui.lbl_ranged.show()
                    self.sb_multi_center2Logic(self.gui.sb_multi_center2.value())

                else:
                    self.gui.sb_multi_center2.hide()
                    self.gui.lbl_ranged.hide()
                    award.get("upgrades")[quantity] = 0

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def showUpgradeableRadioButtons(self):
        '''Method that shows the Upgradeable ribbon type radio buttonsd'''

        # Show the required Radio Buttons.
        if self.gui.cb_singleMedal.isChecked():

            # Str type conversion as you cannot reference a dict with a QString.
            award = self.awards.get(str(self.gui.lw_medals.currentItem().text()))
            name = 0
            quantity = 1
            widgets = [self.gui.rb_upgradeable_0, self.gui.rb_upgradeable_1, self.gui.rb_upgradeable_2,
                       self.gui.rb_upgradeable_3, self.gui.rb_upgradeable_4, self.gui.rb_upgradeable_5]
            upgradeCount = 0

            for upgrade in award.get("upgrades"):
                widgets[upgradeCount].setText(upgrade[name])

                # Connect the radio buttons.
                if not self.rb_upgradeablesConnected:
                    widgets[upgradeCount].clicked.connect(self.rb_upgradableSelectionLogic)

                # Set the the correct radio button to checked as per the user's selection.
                if upgrade[quantity] == 1:
                    widgets[upgradeCount].setChecked(True)

                widgets[upgradeCount].show()
                upgradeCount += 1
            self.rb_upgradeablesConnected = True
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def rb_upgradableSelectionLogic(self):
        '''Method to control the logic upon upgradeable ribbon type award selection.'''

        try:
            # Str type conversion as you cannot reference a dict with a QString.
            award = self.awards.get(str(self.gui.lw_medals.currentItem().text()))
            name = 0
            quantity = 1
            widgets = [self.gui.rb_upgradeable_0, self.gui.rb_upgradeable_1, self.gui.rb_upgradeable_2,
                       self.gui.rb_upgradeable_3, self.gui.rb_upgradeable_4, self.gui.rb_upgradeable_5]
            widgetCount = 0

            for widget in widgets:
                if widget.isChecked():
                    break
                widgetCount += 1

            # Store the user selection.
            for upgrade in award.get("upgrades"):
                upgrade[quantity] = 0
            award.get("upgrades")[widgetCount][quantity] = 1
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def neckRibbonDeconfliction(self):
        '''Method for handling the display and selection logic for neck ribbon deconfliction.'''

        quantity = 1
        if self.awards.get("Imperial Cross (IC)")["upgrades"][quantity] == 1 and \
                self.awards.get("Grand Order of the Emperor (GOE)")["upgrades"][quantity] == 1:

            if self.gui.lw_medals.currentItem().text() == "Grand Order of the Emperor (GOE)" or \
               self.gui.lw_medals.currentItem().text() == "Imperial Cross (IC)":

                # Text Label.
                self.gui.lbl_top_free_text.setText("Neck ribbon to display:")
                self.gui.lbl_top_free_text.show()
                # Combobox.
                if not self.combo_topConnected:
                    self.gui.combo_top.clear()
                    self.gui.combo_top.addItem("Both IC and GOE Ribbons")
                    self.gui.combo_top.addItem("Imperial Cross (IC) Only")
                self.gui.combo_top.show()

                # Apply the current setting.
                if self.deconflictNeckRibbons:
                    self.gui.combo_top.setCurrentIndex(1)
                else:
                    self.gui.combo_top.setCurrentIndex(0)

                # Connection.
                if not self.combo_topConnected:
                    self.gui.combo_top.currentTextChanged.connect(self.combo_neckRibbonDeconflictLogic)
                    self.combo_topConnected = True

        else:
            # Disconnection.
            self.disconnectAllMedalWidgets()

            # Text Label.
            self.gui.lbl_top_free_text.setText("==NUL====NUL====NUL====NUL==")
            self.gui.lbl_top_free_text.hide()

            # Comobox.
            self.gui.combo_top.clear()
            self.gui.combo_top.hide()

            # Set deconfliction back to False.
            self.deconflictNeckRibbons = False
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def combo_neckRibbonDeconflictLogic(self):
        '''Method that stores the user's preference to deconflicting the IC and GOE neck ribbons.'''

        try:
            if "Both" in str(self.gui.combo_top.currentText()):
                self.deconflictNeckRibbons = False
            else:
                self.deconflictNeckRibbons = True
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def buildMedalIncludes(self):
        '''Method that gathers all of the include files required for the user's medal selections..'''

        quantity = 1
        medalIncludes = []

        for award in self.awards:
            # Single type awards.
            if self.awards.get(award)["type"] == "single" or self.awards.get(award)["type"] == "multi":
                if self.awards.get(award)["upgrades"][quantity] >= 1:

                    # Add the medal_g.inc file.
                    if "medal_g.inc" not in medalIncludes:
                        medalIncludes.append("medal_g.inc")

                    # Add the selected medal's .inc file.
                    incFile = self.awards.get(award)["includeFile"]
                    if incFile == "goe_g.inc" or incFile == "ic_g.inc":
                        medalIncludes.insert(0, incFile)  # Must be first for all other medals to render properly.
                    else:
                        medalIncludes.append(self.awards.get(award)["includeFile"])

        # Special handling of IC and GOE combination.
        if "ic_g.inc" in medalIncludes and "goe_g.inc" in medalIncludes and not self.deconflictNeckRibbons:
            medalIncludes.remove("ic_g.inc")
            medalIncludes.remove("goe_g.inc")
            medalIncludes.insert(0, "ic_goe_g.inc")  # Must be first for all other medals to render properly.

        return medalIncludes
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def buildMedalObjects(self):
        '''Method that gathers all of the object references required for the user's medal selections.'''

        medalObjects = []

        for award in self.awards:
            # Single and Multi type awards.
            if self.awards.get(award)["type"] == "single" or self.awards.get(award)["type"] == "multi":
                if self.awards.get(award)["upgrades"][1] >= 1:
                    # Get all award objRefs.
                    for obj in range(1, 101, 1):
                        try:  # Filtering for medals that do not contain objRefs.
                            medalObjects.append(self.awards.get(award)["objectRef%s" % obj])
                        except KeyError:
                            break

        # Special handling of IC and GOE combination.
        if self.deconflictNeckRibbons:
            medalObjects.remove("P_goe")

        return self.determineMultiMedalOrders(medalObjects)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def determineMultiMedalOrders(self, medalObjecRefs):
        '''Used to determine the ordering for the GS to ISM medals and then upate their objRefs.'''

        multiMedalsFound = []
        modifiedObjectRefs = []
        posNumCounter = 1

        # Find and count multi type medals.
        for ref in medalObjecRefs:
            for medal in self.medalConfig.sections():
                if self.medalConfig.get(medal, "type") == "multi":
                    for num in range(1, 101, 1):
                        try:
                            if self.medalConfig.get(medal, "objRef%s" % num) == ref:
                                multiMedalsFound.append(ref)
                        except configparser.NoOptionError:
                            break

        # Modify the objRef with the correct numbering.
        for ref in medalObjecRefs:
            if ref in multiMedalsFound:
                modifiedObjectRefs.append(ref + "_{totNum}_{posNum}".format(totNum=(len(multiMedalsFound)), posNum=posNumCounter))
                posNumCounter += 1
            else:
                modifiedObjectRefs.append(ref)

        return modifiedObjectRefs
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def buildRibbonObjects(self):
        '''Method that gathers all of the object references required for the user's ribbon selections.'''

        ribbonObjects = []
        name = 0
        quantity = 1

        for award in self.awards:
            # Upgradeable and SubRibbon type awards.
            if self.awards.get(award)["type"] == "upgradeable" or self.awards.get(award)["type"] == "subRibbons":

                if "Iron Star (IS)" == award or "Medal of Communication (MoC)" == award or \
                   "Medal of Scholarship (MoS)" == award:  # Reverse the ribbon list for certain medals.

                    upgrades = self.awards.get(award)["upgrades"][::-1]

                    if "Iron Star (IS)" == award:  # Re-Sorting of IS-XW and US-XR.
                        half1 = upgrades[0: 4]
                        half2 = upgrades[4:]
                        upgrades = half2 + half1

                    if "Medal of Communication (MoC)" == award:
                        highestMOC = ["name", 0]
                        for upgrade in upgrades[::-1]:
                            if upgrade[1] >= highestMOC[1]:
                                highestMOC = upgrade
                        upgrades = [highestMOC]

                else:
                    upgrades = self.awards.get(award)["upgrades"]

                if "Medal of Tactics (MoT)" == award:  # Special sorting correction for MoT.
                    blue = [upgrades[0]]
                    green = [upgrades[1]]
                    red = [upgrades[2]]
                    upgrades = blue + red + green

                for upgrade in upgrades:  # Medals that don't require reversing.
                    if upgrade[quantity] != 0:
                        for section in self.ribbonConfig.sections():
                            for option in self.ribbonConfig.options(section):
                                if self.ribbonConfig.get(section, option) == upgrade[name] and self.ribbonConfig.get(section, "name") == award:
                                    awardName = "T_r_" + self.ribbonConfig.get(section, option + "filename").split(".")[0].lower().replace("-", "_")
                        ribbonObjects.append("P_r&NUM& texture { %s }" % awardName)

            # Ranged type awards.
            elif self.awards.get(award)["type"] == "ranged":
                if self.awards.get(award)["upgrades"][quantity] > 0:
                    for section in self.ribbonConfig.sections():
                        if self.ribbonConfig.get(section, "name") == award:
                            awardName = "T_r_" + self.ribbonConfig.get(section, "filename").split(".")[0].lower().replace("-", "_")
                            awardName = awardName.replace("&range&", str(self.awards.get(award)["upgrades"][quantity]))
                            ribbonObjects.append("P_r&NUM& texture { %s }" % awardName)

        return self.ribbonNumberOrdering(ribbonObjects)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def ribbonNumberOrdering(self, ribbons):
        '''Method that arranged the awarded ribbons into the correct order.'''

        ribbonObjects = []
        fullRows = int(len(ribbons) / 4)
        bottomRowNumCount = len(ribbons) % 4
        ribbonCounter = 24 - (fullRows * 4)

        # Logic for complete ribbon rows of 4 for more than 4 ribbons.
        if len(ribbons) > 4:
            if bottomRowNumCount == 0:
                for ribbon in ribbons:
                    ribbonObjects.append(ribbon.replace("&NUM&", str(ribbonCounter)))
                    ribbonCounter += 1
            else:
                ribbonCounter -= 4  # To account for the bottom row.
                for ribbon in ribbons[: - bottomRowNumCount]:
                    ribbonObjects.append(ribbon.replace("&NUM&", str(ribbonCounter)))
                    ribbonCounter += 1

            # Logic to add the bottom row of ribbons for more than 4 ribbons.
            if bottomRowNumCount != 0:
                if bottomRowNumCount == 1:
                    ribbonCounter = 25
                elif bottomRowNumCount == 2:
                    ribbonCounter = 21
                elif bottomRowNumCount == 3:
                    ribbonCounter = 24

                for ribbon in ribbons[-bottomRowNumCount:]:
                    ribbonObjects.append(ribbon.replace("&NUM&", str(ribbonCounter)))
                    ribbonCounter += 1

        # Logic to add the bottom row of ribbons for less than 5 ribbons.
        else:
            if len(ribbons) == 1:
                for ribbon in ribbons:
                    ribbonCounter = 25

            elif len(ribbons) == 2:
                ribbonCounter = 21

            elif len(ribbons) == 3:
                ribbonCounter = 24

            elif len(ribbons) == 4:
                ribbonCounter = 20

            for ribbon in ribbons:
                ribbonObjects.append(ribbon.replace("&NUM&", str(ribbonCounter)))
                ribbonCounter += 1

        return ribbonObjects
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def disconnectAllMedalWidgets(self):
        '''Method for disconnecting all medal widgets.'''

        # Combo Top.
        if self.combo_topConnected:
            self.gui.combo_top.disconnect()
            self.combo_topConnected = False

        # SpinBoxes.
        spinBoxes = [self.gui.sb_multi_left1, self.gui.sb_multi_left2, self.gui.sb_multi_left3, self.gui.sb_multi_left4,
                     self.gui.sb_multi_center1, self.gui.sb_multi_center2, self.gui.sb_multi_center3, self.gui.sb_multi_center4,
                     self.gui.sb_multi_right1, self.gui.sb_multi_right2, self.gui.sb_multi_right3, self.gui.sb_multi_right4]

        for spinBox in spinBoxes:
            try:
                spinBox.valueChanged.disconnect()
            except TypeError:
                pass  # Prevents a crash if the spinBox isn't currently connected.
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_masterLogic(self, sender, value):
        '''Method for handling the all spinbox logic.'''

        try:
            # Str type conversion as you cannot reference a dict with a QString.
            award = self.awards.get(str(self.gui.lw_medals.currentItem().text()))
            name = 0
            quantity = 1

            # ----- Multi type medal awards. (GS, SS, BS, PC, ISM)
            if award.get("type") == "multi":
                self.awards.get(str(self.gui.lw_medals.currentItem().text()))["upgrades"][quantity] = value

            # ----- SubRibbons type ribbon awards. (MoS, MoT, IS, MoC, CoX)
            elif award.get("type") == "subRibbons":
                awardName = self.subRibbonAwards[sender][0]
                subRibbonName = self.subRibbonAwards[sender][1]
                spinBox = self.subRibbonAwards[sender][2]

                for upgrade in self.awards.get(awardName)["upgrades"]:
                    if upgrade[name] == subRibbonName:
                        self.awards.get(awardName)["upgrades"][sender][1] = spinBox.value()

            # ----- Ranged type ribbon awards. (OV)
            elif award.get("type") == "ranged":
                awardName = self.subRibbonAwards[0]
                spinBox = self.subRibbonAwards[1]
                self.awards.get(awardName)["upgrades"][quantity] = spinBox.value()

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_center1Logic(self, value):
        '''Method for handling the Center Top spinbox logic.'''

        self.sb_masterLogic(0, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_center2Logic(self, value):
        '''Method for handling the Center Top Middle spinbox logic.'''

        self.sb_masterLogic(1, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_center3Logic(self, value):
        '''Method for handling the Center Bottom Middle spinbox logic.'''

        self.sb_masterLogic(2, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_center4Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(3, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_left1Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(0, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_left2Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(1, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_left3Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(2, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_left4Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(3, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right1Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(4, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right2Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(5, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right3Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(6, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right4Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(7, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_browseRosterFunc(self, event):
        '''Method event for when the 'Browse Fleet Roster' button is clicked on the 'Import' tab.'''

        os.system("start " + self.config.get("TCDB", "roster"))
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_searchFunc(self, event):
        '''Method event for when the 'Personnel Search' button is clicked on the 'Import' tab.'''

        os.system("start " + self.config.get("TCDB", "search"))
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_newProfMethod(self, event):
        '''Method event for when the 'New Profile' button is clicked.'''

        try:
            self.gui.lw_medals.setCurrentRow(0)  # Required to prevent bug of the user's last upgradeable type selection not showing.

            # PovRay Template variables.
            self.position = None
            self.rank = None
            self.name = "Unknown"
            self.ship = ""
            self.wing = ""
            self.sqn = ""
            self.awards = {}
            self.deconflictNeckRibbons = False

            # Configuration variables.
            self.fleetConfig = None
            self.medalConfig = None
            self.ribbonConfig = None

            # GUI variables.
            self.subRibbonAwards = []
            self.cb_singleMedalConnected = False
            self.combo_topConnected = False
            self.rb_upgradeablesConnected = False

            # Application logic.
            self.continueRender = True
            self.gui.lw_medals.currentItemChanged.disconnect(self.medalSelectionLogic)
            self.gui.lw_medals.clear()
            self.initialGUISetup()
            self.gui.lw_medals.currentItemChanged.connect(self.medalSelectionLogic)

            # GUI Cleanup.
            # Position Radio Buttons.
            self.gui.rb_pos_trn.setChecked(True)
            self.gui.rb_pos_trn.setAutoExclusive(False)
            self.gui.rb_pos_trn.setChecked(False)
            self.gui.rb_pos_trn.setAutoExclusive(True)
            # Ship, Wing and Squadron ListWidgets.
            self.enableWingAndSqnTab(False)

            # Disable render buttons.
            self.gui.btn_dress.setEnabled(False)
            self.gui.btn_duty.setEnabled(False)

        except Exception as e:
            handleException(e)
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_openProfMethod(self, event):
        '''Method event for when the 'Open Profile' button is clicked.'''

        try:
            # Load the saved data file.
            fileName = (self.loadUniformFileDialog())
            if fileName:

                with open(fileName, "rb") as dataFile:
                    saveData = pickle.load(dataFile)

                if saveData[0] == self.saveFileVersion:
                    # Apply the saved settings.

                    # Position.
                    self.position = saveData[1]
                    radioBtns = [self.gui.rb_pos_trn, self.gui.rb_pos_fm, self.gui.rb_pos_fl, self.gui.rb_pos_cmdr,
                                 self.gui.rb_pos_wc, self.gui.rb_pos_com, self.gui.rb_pos_tccs, self.gui.rb_pos_ia,
                                 self.gui.rb_pos_ca, self.gui.rb_pos_sgcom, self.gui.rb_pos_cs, self.gui.rb_pos_xo,
                                 self.gui.rb_pos_fc, self.gui.rb_pos_lr, self.gui.rb_pos_fr]

                    if self.position:
                        for radioButton in radioBtns:
                            if self.position.lower() in radioButton.objectName():
                                radioButton.setChecked(True)
                        self.posRBLogic()

                        # Ranks
                    self.rank = saveData[2]
                    radioBtns = [self.gui.rb_rank_ct, self.gui.rb_rank_sl, self.gui.rb_rank_lt, self.gui.rb_rank_lcm,
                                 self.gui.rb_rank_cm, self.gui.rb_rank_cpt, self.gui.rb_rank_maj, self.gui.rb_rank_lc,
                                 self.gui.rb_rank_col, self.gui.rb_rank_gn, self.gui.rb_rank_ra, self.gui.rb_rank_va,
                                 self.gui.rb_rank_ad, self.gui.rb_rank_fa, self.gui.rb_rank_ha, self.gui.rb_rank_sa,
                                 self.gui.rb_rank_ga]

                    if self.rank:
                        for radioButton in radioBtns:
                            if self.rank.lower() in radioButton.objectName():
                                radioButton.setChecked(True)
                        self.rankRBLogic()

                        # Ship.
                    self.ship = saveData[3]
                    if self.ship:
                        for row in range(self.gui.lw_ship.count()):
                            self.gui.lw_ship.setCurrentRow(row)
                            if self.gui.lw_ship.currentItem().text() == self.ship:
                                break
                        self.shipSelectionLogic(None)

                        # Wing.
                    self.wing = saveData[4]
                    if self.wing:
                        for row in range(self.gui.lw_wing.count()):
                            self.gui.lw_wing.setCurrentRow(row)
                            if self.gui.lw_wing.currentItem().text() == self.wing:
                                break
                        self.wingSelectionLogic(None)

                        # Squadron.
                    self.gui.cb_eliteSqn.setChecked(saveData[5])
                    self.sqn = saveData[6]
                    if self.sqn:
                        for row in range(self.gui.lw_squad.count()):
                            self.gui.lw_squad.setCurrentRow(row)
                            if self.gui.lw_squad.currentItem().text() == self.sqn:
                                break
                        self.squadSelectionLogic(None)

                        # Medals & Awards.
                    self.awards = saveData[7]
                    self.deconflictNeckRibbons = saveData[8]
                    if self.gui.lw_medals.currentItem():
                        self.medalSelectionLogic(self.gui.lw_medals.currentItem())

                        # FCHG.
                    self.gui.cbFCHG.setCurrentText(saveData[9])

                else:
                    # Show error message.
                    msg = "%s is not compatible with this version of TTT3.\nPlease save a new profile." % fileName.split("\\")[-1]
                    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

        except Exception as e:
            handleException(e)
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_saveProfMethod(self, event):
        '''Method event for when the 'Save Profile' button is clicked.'''

        try:
            # Collect the data to be saved into a list.
            saveData = (self.saveFileVersion, self.position, self.rank, self.ship, self.wing, self.gui.cb_eliteSqn.isChecked(),
                        self.sqn, self.awards, self.deconflictNeckRibbons, self.gui.cbFCHG.currentText())

            # Save the data.
            fileName = self.saveUniformFileDialog()
            if fileName:
                with open(fileName, "wb") as saveFile:
                    pickle.dump(saveData, saveFile)

        except Exception as e:
            handleException(e)
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def saveUniformFileDialog(self):
        '''Method that opens a QT File Save dialog to save a uniform.'''

        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self, "Save uniform settings", os.getcwd() +
                                                      "\\settings\\untitled.ttt", "*.ttt", options=options)
            if fileName:
                if ".ttt" not in fileName:
                    fileName = fileName + ".ttt"
                return fileName

        except Exception as e:
            handleException(e)
    #------------------------------------------------------------------------------------------------------------------------------------------------#

    def loadUniformFileDialog(self):
        '''Method that opens a QT File Open dialog to save a uniform.'''

        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self, "Load uniform settings", os.getcwd() + "\\settings\\", "*.ttt", options=options)
            if fileName:
                fileName = fileName.replace(r"/", "\\")
                return fileName

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Functions.                                                                    #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
def handleException(exception):
    '''Function that will log all python exceptions to TTT3 Crash.log.'''

    # Capture the error and log to "TTT3 Crash.log"
    logging.error("\n\n-----Crash Information:-----")
    logging.error(exception, exc_info=True)

    # Log System Info.
    logging.error("\n\n-----System Information:-----")
    try:
        os.environ["PROGRAMFILES(X86)"]
        bits = " 64"
    except BaseException:
        bits = " 32"
    logging.error("Windows Version: " + platform.platform() + bits + "-bit.")
    logging.error("Processor: " + platform.processor())
    logging.error("Python Version: " + sys.version)

    # Log TTT3 settings and selections.
    logging.error("\n\n-----TTT3 Settings:-----")

    # TTT3.ini logging.
    with open(os.getcwd() + "\\settings\\TTT3.ini", "r") as f:
        settings = f.read()

        # Medal selections.
    selectedAwards = []
    for award in ttt3.awards:

        if ttt3.awards.get(award)["type"] == "single" or ttt3.awards.get(award)["type"] == "ranged" or ttt3.awards.get(award)["type"] == "multi":
            if ttt3.awards.get(award)["upgrades"][1] != 0:
                selectedAwards.append(award)

        elif ttt3.awards.get(award)["type"] == "upgradeable":
            for upgrade in ttt3.awards.get(award)["upgrades"]:
                if upgrade[1] != 0:
                    selectedAwards.append(award + " : " + str(upgrade[0]))

        else:
            for upgrades in ttt3.awards.get(award)["upgrades"]:
                if upgrades[-1] != 0:
                    selectedAwards.append(award + " " + str(upgrades))

        # Current medal selection.
    try:
        currentSelection = ttt3.gui.lw_medals.currentItem().text()
    except AttributeError:
        currentSelection = "None"

        # Uniform selections.
    logging.error("\n" + settings + "\nPosition : " + str(ttt3.position) + "\nRank : " + str(ttt3.rank) + "\nShip : " + str(ttt3.ship) +
                  "\nWing : " + str(ttt3.wing) + "\nSquadron : " + str(ttt3.sqn) + "\nAwards :" + str(selectedAwards) +
                  "\nCurrent Medal Selection: " + str(currentSelection))

    # Show error message.
    msg = r"Error: Uh-Oh! TTT3 has encountered an error. Please submit 'TTT3\TTT3 Crash.log' to the Internet Office."
    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
    #------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Main Program.                                                                  #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":

    # Error logging.
    logging.basicConfig(filename="TTT3 Crash.log", filemode="a", level=logging.ERROR)

    # Start the QT application.
    app = QApplication(sys.argv)
    ttt3 = TTT3()
    sys.exit(app.exec_())
#----------------------------------------------------------------------------------------------------------------------------------------------------#
