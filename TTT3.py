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
# External dependencies are commented. Imports with no comments are included with the regular Python installation.
# Alternatively run "TTT3\Useful Info\Dependency Installer.bat"
import logging
import resource
import sys
import os
import subprocess
import ctypes
import configparser
import psutil  # python -m pip install psutil
import time
import datetime
import winreg
from PyQt5 import uic  # python -m pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu, QColorDialog, QInputDialog  # python -m pip install pyqt5-tools
from PyQt5.QtGui import QPixmap, QColor, QFont, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QEvent, pyqtSignal, QSize, QRectF
from PIL import Image, ImageOps  # python -m pip install pillow
import cv2  # python -m pip install opencv-python
import numpy
import platform
import pickle
import urllib3  # python -m pip install urllib3
import json
import hashlib
import threading
import queue
import Slider
# python -m pip install pyinstaller - for compiler.
#----------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Classes.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#


class TTT3(QMainWindow):
    '''Main object class representing the TTT3 application.'''

    updateProgressBar = pyqtSignal(str, int)

    def __init__(self):
        '''Class constructor.'''

        try:
            # Version info.
            version = "3.0.1"
            devVersion = "Beta 2"
            date = "8 August 2021"
            self.saveFileVersion = 1  # Used for save file compatibility. Bump if any changes are made to self.btn_saveProfMethod()
            self.version = "{v} {a}".format(v=version, a=devVersion)

            # Initialise an instance of a QT Main Window and load our GUI file 'data\uis\ttt.ui'.
            QMainWindow.__init__(self)
            self.gui = uic.loadUi(r"data\uis\ttt.ui")
            self.gui.pb_update.hide()
            self.gui.lbl_update.hide()
            self.gui.show()
            setPixelSizes(self.gui)
            self.gui.closeEvent = self.closeEvent
            self.gui.keyPressEvent = self.keyPressEvent

            # Set the version number.
            self.gui.lblVersion.setText("<p align=\"center\">Version: {v} {a}&nbsp;&nbsp;&nbsp;Date: {d}</p>".format(v=version, a=devVersion, d=date))
            #self.gui.lblDate.setText("Date: " + date)

            # ---------- Initialise instance variables and connections. ----------

            # ----- Main Graphical User Interface. -----

            # Button Connections.
            self.gui.btn_dress.clicked.connect(self.btn_dressMethod)
            self.gui.btn_duty.clicked.connect(self.btn_dutyMethod)
            self.gui.btn_helmet.clicked.connect(self.btn_helmetMethod)
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

            # ----- 'Miscellaneous' Tab. -----
            # Set default Misc Options.
            # Detect and load in lighsaber styles.
            self.gui.cb_dressSaberStyles.hide()
            self.saberDict = {}
            self.loadLighsabers()
            self.cb_dressLightsaberFunc()
            self.cb_dutyLightsaberFunc()
            self.cb_dutyBlasterFunc()
            self.blasterDict = {}
            self.loadBlasters()
            self.gui.cb_dressLightsaber.setChecked(False)
            self.gui.rb_daggerLeft.setChecked(True)
            self.gui.cb_dutyLightsaber.setChecked(False)
            self.gui.rb_blasterLeft.setChecked(True)

            # Lightsaber options.
            self.gui.cb_dressLightsaber.stateChanged.connect(self.cb_dressLightsaberFunc)
            self.gui.cb_dutyLightsaber.stateChanged.connect(self.cb_dutyLightsaberFunc)
            self.gui.rb_dressSaberLeft.clicked.connect(self.saberDaggerDeconflict)
            self.gui.rb_dressSaberRight.clicked.connect(self.saberDaggerDeconflict)
            self.gui.cb_dressSaberStyles.currentIndexChanged.connect(self.lightsaberDressSelectedFunc)
            self.gui.cb_dutySaberStyles.currentIndexChanged.connect(self.lightsaberDutySelectedFunc)
            # GOE Options.
            self.gui.rb_daggerLeft.clicked.connect(self.daggerSaberDeconflict)
            self.gui.rb_daggerRight.clicked.connect(self.daggerSaberDeconflict)

            # Blaster options.
            self.gui.cb_dutyBlaster.stateChanged.connect(self.cb_dutyBlasterFunc)
            self.gui.rb_blasterLeft.clicked.connect(self.blasterSaberDeconflict)
            self.gui.rb_blasterRight.clicked.connect(self.blasterSaberDeconflict)
            self.gui.rb_dutySaberLeft.clicked.connect(self.saberBlasterDeconflict)
            self.gui.rb_dutySaberRight.clicked.connect(self.saberBlasterDeconflict)

            # ----- 'Import' Tab. -----
            self.gui.btn_browseRoster.clicked.connect(self.btn_browseRosterFunc)
            self.gui.btn_search.clicked.connect(self.btn_searchFunc)
            self.gui.btn_import.clicked.connect(self.btn_importFunc)
            self.gui.btn_remember.clicked.connect(self.btn_rememberFunc)
            self.gui.lw_presets.itemClicked.connect(self.lw_presetsFunc)
            self.gui.lw_presets.itemDoubleClicked.connect(self.btn_importFunc)
            self.gui.lw_presets.installEventFilter(self)

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
            self.callsign = "None"
            self.pin = None
            self.ship = ""
            self.wing = ""
            self.sqn = ""
            self.awards = {}
            self.eeCount = 0
            self.devModeCount = 0
            self.deconflictNeckRibbons = False
            self.spotColour = QColor(255, 255, 255)
            self.envColour = QColor(128, 118, 108)
            self.bgColour = QColor(0, 0, 0)
            self.transparentBG = ""
            self.width = 640
            self.height = 853
            self.quality = 9
            self.clothDetail = 0
            self.antiAliasing = True
            self.shadowless = False
            self.mosaicPreview = False
            self.camX = -2500
            self.camY = -13300
            self.camZ = 2100
            self.lookX = 0
            self.lookY = -128
            self.lookZ = 28
            self.lightX = 13000
            self.lightY = -15000
            self.lightZ = 13000
            self.helmColour = QColor(33, 33, 33)
            self.bgColourHelm = QColor(69, 79, 112)
            self.decColour = QColor(147, 147, 147)
            self.lightColour = QColor(255, 255, 255)
            self.transparentBGHelm = ""
            self.ambientHelm = 30
            self.specularHelm = 50
            self.roughHelm = 1
            self.reflectionHelm = 10
            self.camXHelm = 2170
            self.camYHelm = -6510
            self.camZHelm = 3146
            self.lookXHelm = -568
            self.lookYHelm = -445
            self.lookZHelm = 1052
            self.lightXHelm = 2244
            self.lightYHelm = -5089
            self.lightZHelm = 5282
            self.widthHelm = 640
            self.heightHelm = 548
            self.qualityHelm = 9
            self.antiAliasingHelm = True
            self.shadowlessHelm = False
            self.homoHelm = False
            self.mosaicPreviewHelm = False
            self.nameHelm = "EH TC"
            self.fontHelmQFront = QFont("impact")
            self.logo1TypeHelm = "Image - stencil mask"
            self.logo2TypeHelm = "Squadron Patch"
            self.logo1FilepathHelm = os.getcwd() + "\\data\\misc\\Helmet Stencils\\tclogo.gif"
            self.logo2FilepathHelm = ""

            # PovRay Template Constants.
            self.RANK_OFFSET_RIBBONS_00_TO_08 = ["-18.8939990997314,0.351000010967255,7.92899990081787",  # Rotate
                                                 "51.3199996948242,-131.973007202148,213.126998901367"]  # Translate

            self.RANK_OFFSET_RIBBONS_09_TO_12 = ["-18.8939990997314,0.351000010967255,7.92899990081787",
                                                 "51.1030006408691,-130.444000244141,217.598007202148"]

            self.RANK_OFFSET_RIBBONS_13_TO_16 = ["-20.8950004577637,0.25,7.64699983596802",
                                                 "50.8540000915527,-128.714996337891,222.033004760742"]

            self.RANK_OFFSET_RIBBONS_17_TO_20 = ["-23.7950000762939,0.264999985694885,7.68100023269653",
                                                 "50.5919990539551,-126.778999328613,226.337997436523"]

            self.RANK_OFFSET_RIBBONS_21_TO_28 = ["-25.6240005493164,0.264999985694885,7.68100023269653",
                                                 "50.326000213623,-124.832000732422,230.47900390625"]

            self.RANK_OFFSET_DUTY_LINE = ["-20.74,1.325,9.085",      # Rotate
                                          "69.846,-125.146,223.304"]  # Translate

            self.RANK_OFFSET_DUTY_FLAG = ["-20.74,1.325,9.085",
                                          "69.846,-124.146,223.304"]

            # ----- Configuration variables. -----
            self.config = None
            self.fleetConfig = None
            self.medalConfig = None
            self.ribbonConfig = None
            self.pinData = []

            # ----- GUI variables. -----
            self.subRibbonAwards = []
            self.cb_singleMedalConnected = False
            self.combo_topConnected = False
            self.rb_upgradeablesConnected = False
            self.imagePath = None
            self.launchingPOVRay = False
            self.previewLoaded = False

            # ----- Application logic. -----
            self.queue = queue.Queue()
            threading.Thread(target=self.taskQueuer, daemon=True).start()
            self.fastRendering = False  # Forces POV-Ray to render at a lower quality for quicker rendering during testing.
            self.continueRender = True
            self.uniform = None
            self.loadSettings()
            self.loadFleetData()
            self.lastRenderData = None
            self.updateProgressBar.connect(self.updaterSlot)
            self.update = threading.Thread(target=self.checkForUpdates)
            self.update.start()
            self.initialGUISetup()
            self.loadPinData()
            self.maxedRibbons = False
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def readmeLink(self, event):
        '''Method event for when 'TTT3readme.htm' is clicked on the 'Info' tab.'''

        subprocess.Popen("start TTT3_readme.htm", shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def ioLink(self, event):
        '''Method event for when 'Internet Office' is clicked on the 'Info' tab.'''

        subprocess.Popen("start https://ehnet.org/", shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def tcpmLink(self, event):
        '''Method event for when 'TIE Corps Pilot Manual' is clicked on the 'Info' tab.'''

        subprocess.Popen("start https://tc.emperorshammer.org/downloads/TCPM.pdf", shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def uniformsLink(self, event):
        '''Method event for when 'TIE Corps Personnel Uniforms' is clicked on the 'Info' tab.'''

        subprocess.Popen("start https://emperorshammer.org/uniforms.php", shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def pythonLink(self, event):
        '''Method event for when 'Python' is clicked on the 'Info' tab.'''

        subprocess.Popen("start https://www.python.org/about/", shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def qtLink(self, event):
        '''Method event for when 'QT' is clicked on the 'Info' tab.'''

        subprocess.Popen("start https://www.qt.io/", shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def povrayLink(self, event):
        '''Method event for when 'POV-Ray' is clicked on the 'Info' tab.'''

        subprocess.Popen("start http://www.povray.org/", shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def eeLink(self, event):
        '''Method event for ee.'''

        try:
            self.eeCount += 1
            if self.eeCount >= 3:
                self.gui.label_11.setText("PRAETORIAN MODE")
                self.gui.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

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
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def closeEvent(self, event):
        '''Method that overloads the self.gui close event and the application.'''

        logging.shutdown()
        if os.stat("TTT3 Crash.log").st_size == 0:
            os.remove("TTT3 Crash.log")
        sys.exit()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def outputCloseEvent(self, event):
        '''Method that overloads the self.output_gui close event and the application.'''

        self.preview.show()
        self.output_gui.close()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def previewCloseEvent(self, event):
        '''Method that overloads the self.output_gui close event and the application.'''

        self.gui.show()
        self.preview.close()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadFleetData(self):
        '''Method to read in the locally stored fleet data.'''

        # Load 'Wing and Squadron' tab items from 'settings\fleet.json'.
        try:
            with open("settings\\fleet.json", "r") as fleetConfigFile:
                fleetData = fleetConfigFile.read()
            self.fleetConfig = json.loads(fleetData)
            self.gui.cb_eliteSqn.setEnabled(False)

        except json.JSONDecodeError:
            pass  # Will cause update to trigger if fleet.json is corrupted.

        except FileNotFoundError:
            self.fleetConfig = json.loads('{"squadrons" : [{"name" : "NULL"}], "wings" : [{"name" : "NULL"}], "ships" : [{"nameShort" : "NULL"}]}')
            with open("settings\\fleet.json", "w") as fleetConfigFile:
                fleetConfigFile.write(json.dumps(self.fleetConfig))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def initialGUISetup(self):
        '''Method that sets the application's GUI for initial use.
           This mainly comprises of hiding the correct rank radio buttons.'''

        # Hide all ranks for initial use.
        for rank in self.rankRadioButtons:
            rank.hide()

        # Add the Ships to the Ships list view.
        try:
            for ship in self.fleetConfig.get("ships"):
                self.gui.lw_ship.addItem(ship.get("nameShort"))
        except AttributeError:
            time.sleep(2)  # Allow time for the checkUpdates thread to download a new fleet definition.
            for ship in self.fleetConfig.get("ships"):
                self.gui.lw_ship.addItem(ship.get("nameShort"))
        setLWPixelSizes(self.gui.lw_ship)

        # Load Medal and Ribbon data.
        self.loadMedals()
        self.loadRibbons()

        # Hide 'Medals, Ribbons and FCHG' items.
        self.gui.gb_medals.hide()
        self.hideMedalOptions()
        self.gui.cbFCHG.setCurrentIndex(0)

        self.gui.btn_helmet.setEnabled(True)

        # TODO Disabled Dress Lightsaber Customisation.
        self.gui.btn_dressSaberCustom.setEnabled(False)

        # TODO Disabled Duty Lightsaber Customisation.
        self.gui.btn_dutySaberCustom.setEnabled(False)

        # Hide the remember button.
        self.gui.btn_remember.hide()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def posRBLogic(self):
        '''Method that controls the Position Radio Button Logic - Showing or hiding the required rank options.'''

        try:
            # Reset the user's position value.
            self.enableWingAndSqnTab(False)
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
                        self.enableWingAndSqnTab(True)
                        break

                    # Flight Leader.
                    elif radioButton == self.gui.rb_pos_fl:
                        self.showRanks(LT, GN)
                        self.position = "FL"
                        self.enableWingAndSqnTab(True)
                        break

                    # Squadron Commander.
                    elif radioButton == self.gui.rb_pos_cmdr:
                        self.showRanks(CM, GN)
                        self.position = "CMDR"
                        self.enableWingAndSqnTab(True)
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
                        self.enableWingAndSqnTab(True)
                        break

                    # Commodore.
                    elif radioButton == self.gui.rb_pos_com:
                        self.showRanks(RA, GA)
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
                        self.enableWingAndSqnTab(True)
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
                for ship in self.fleetConfig.get("ships"):
                    self.gui.lw_ship.addItem(ship.get("nameShort"))
            setLWPixelSizes(self.gui.lw_ship)

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
# self.gui.cb_eliteSqn.setEnabled(boolEnabled)
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

            # Apply any previous Ship/Wing/Sqn options.
            if self.ship != "":
                for row in range(self.gui.lw_ship.count()):
                    self.gui.lw_ship.setCurrentRow(row)
                    if self.gui.lw_ship.currentItem().text() == self.ship:
                        break
                self.shipSelectionLogic(None)

            if self.wing != "":
                for row in range(self.gui.lw_wing.count()):
                    self.gui.lw_wing.setCurrentRow(row)
                    if self.gui.lw_wing.currentItem().text() == self.wing:
                        break
                self.wingSelectionLogic(None)

            if self.sqn != "":
                for row in range(self.gui.lw_squad.count()):
                    self.gui.lw_squad.setCurrentRow(row)
                    if self.gui.lw_squad.currentItem().text() == self.sqn:
                        break
                self.squadSelectionLogic(None)

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
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_dressMethod(self):
        '''Method that is triggered when the 'Dress Uniform' button is clicked.
           This method will check that the correct selections has been made within TTT3 such as Ship and Squadron and then
           directly call 'launchPOVRay' to open up PovRay and render the unirom.'''

        try:
            self.uniform = "dress"
            # Check to see if the user has made the correct selections for their position and rank.
            if self.position in ["FM", "FL", "CMDR", "WC"] and self.gui.cb_eliteSqn.isChecked() == False:
                if not self.ship or not self.wing:
                    msg = "Error: As a pilot you need to specify at least a ship and wing before a dress uniform can be created."
                    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                else:
                    self.showPreviewDialog()

            elif self.gui.cb_eliteSqn.isChecked() and not self.sqn:
                msg = "Error: As an elite pilot you need to specify a squadron before a dress uniform can be created."
                return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

            elif self.position in ["COM"]:
                if not self.ship:
                    msg = "Error: As a COM you need to specify a ship before a dress uniform can be created."
                    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                else:
                    self.showPreviewDialog()

            # Run PovRay to render a uniform.
            else:
                self.showPreviewDialog()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def showPreviewDialog(self):
        '''Method to open the render preview / options GUI.'''

        self.previewLoaded = False
        # Load our GUI file 'data\uis\preview.ui'.
        self.preview = uic.loadUi(r"data\uis\preview.ui")

        # Set the correct window title.
        self.preview.setWindowTitle("TTT3 Rendering Options - " + self.uniform.title() + " Uniform")

        # Show the preview GUI.
        self.preview.show()
        setPixelSizes(self.preview)
        self.preview.closeEvent = self.previewCloseEvent
        self.gui.hide()
        self.preview.lbl_wait.setAttribute(Qt.WA_TranslucentBackground)
        self.preview.lbl_wait.setHidden(True)

        # Apply setttings.
        self.applyPreviewSettings()

        # Connections.
        self.preview.btn_raytrace.clicked.connect(self.launchPOVRay)
        self.preview.btn_preview.clicked.connect(self.renderPreview)
        self.preview.btn_PaletteSpot.clicked.connect(self.btn_PaletteSpotFunc)
        self.preview.btn_PaletteEnv.clicked.connect(self.btn_PaletteEnvFunc)
        self.preview.btn_PaletteBack.clicked.connect(self.btn_PaletteBackFunc)
        self.preview.btn_resetColours.clicked.connect(self.btn_previewResetColoursFunc)
        self.preview.sb_Width.valueChanged.connect(self.sb_previewWidthFunc)
        self.preview.btn_resetOptions.clicked.connect(self.btn_previewResetOptionsFunc)
        self.preview.sb_Quality.valueChanged.connect(self.sb_previewQualityFunc)
        self.preview.cb_Detail.currentIndexChanged.connect(self.cb_previewDetailFunc)
        self.preview.cb_AA.stateChanged.connect(self.cb_previewAAFunc)
        self.preview.cb_Shadowless.stateChanged.connect(self.cb_previewShadowlessFunc)
        self.preview.cb_Mosaic.stateChanged.connect(self.cb_previewMosaicFunc)
        self.preview.cb_TransparentBG.stateChanged.connect(self.cb_previewTransparentFunc)
        self.preview.vs_CamX.valueChanged.connect(self.vs_previewCamXFunc)
        self.preview.vs_CamY.valueChanged.connect(self.vs_previewCamYFunc)
        self.preview.vs_CamZ.valueChanged.connect(self.vs_previewCamZFunc)
        self.preview.vs_LookX.valueChanged.connect(self.vs_previewLookXFunc)
        self.preview.vs_LookY.valueChanged.connect(self.vs_previewLookYFunc)
        self.preview.vs_LookZ.valueChanged.connect(self.vs_previewLookZFunc)
        self.preview.btn_resetCamera.clicked.connect(self.btn_previewResetCameraFunc)
        self.preview.vs_LightX.valueChanged.connect(self.vs_previewLightXFunc)
        self.preview.vs_LightY.valueChanged.connect(self.vs_previewLightYFunc)
        self.preview.vs_LightZ.valueChanged.connect(self.vs_previewLightZFunc)
        self.preview.btn_resetLight.clicked.connect(self.btn_previewResetLightFunc)
        self.preview.btn_Reset.clicked.connect(self.btn_previewResetFunc)
        self.preview.btn_Save.clicked.connect(self.btn_previewSaveFunc)
        self.preview.btn_Load.clicked.connect(self.btn_previewLoadFunc)
        self.preview.cb_PresetCam.currentIndexChanged.connect(self.cb_previewPresetCamFunc)
        self.preview.cb_PresetLook.currentIndexChanged.connect(self.cb_previewPresetLookFunc)
        self.preview.cb_PresetLight.currentIndexChanged.connect(self.cb_previewPresetLightFunc)
        self.preview.lbl_CamX.mouseReleaseEvent = self.lbl_CamXFunc
        self.preview.lbl_CamY.mouseReleaseEvent = self.lbl_CamYFunc
        self.preview.lbl_CamZ.mouseReleaseEvent = self.lbl_CamZFunc
        self.preview.lbl_LookX.mouseReleaseEvent = self.lbl_LookXFunc
        self.preview.lbl_LookY.mouseReleaseEvent = self.lbl_LookYFunc
        self.preview.lbl_LookZ.mouseReleaseEvent = self.lbl_LookZFunc
        self.preview.lbl_LightX.mouseReleaseEvent = self.lbl_LightXFunc
        self.preview.lbl_LightY.mouseReleaseEvent = self.lbl_LightYFunc
        self.preview.lbl_LightZ.mouseReleaseEvent = self.lbl_LightZFunc

        # Set widgets to auto update on their mouseReleaseEvent.
        self.preview.cb_Refresh.stateChanged.connect(self.cb_previewRefreshFunc)

        # Colours.
        for label in [self.preview.lbl_PaletteSpot, self.preview.lbl_PaletteEnv, self.preview.lbl_PaletteBack]:
            label.paintEvent = self.previewAutoRefresh

        # Checkboxes.
        for checkbox in [self.preview.cb_TransparentBG, self.preview.cb_Shadowless]:
            checkbox.stateChanged.connect(self.previewAutoRefresh)

        # Buttons.
        for button in [self.preview.btn_resetCamera, self.preview.btn_resetLight]:
            button.clicked.connect(self.previewAutoRefresh)

        # Spinboxes.
        for spinbox in [self.preview.sb_Quality]:
            spinbox.valueChanged.connect(self.previewAutoRefresh)

        # Sliders.
        for slider in [self.preview.vs_CamX, self.preview.vs_CamY, self.preview.vs_CamZ,
                       self.preview.vs_LookX, self.preview.vs_LookY, self.preview.vs_LookZ,
                       self.preview.vs_LightX, self.preview.vs_LightY, self.preview.vs_LightZ]:
            slider.mouseReleaseEvent = self.previewAutoRefresh

        # ComboBoxes.
        self.preview.cb_Detail.currentIndexChanged.connect(self.previewAutoRefresh)

        # Get a preview uniform render.
        self.renderPreview()
        self.previewLoaded = True
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def showPreviewHelmDialog(self):
        '''Method to open the render preview / options GUI.'''

        self.previewLoaded = False
        # Load our GUI file 'data\uis\preview.ui'.
        self.preview = uic.loadUi(r"data\uis\previewHelm.ui")

        # Show the preview GUI.
        self.preview.show()
        setPixelSizes(self.preview)
        self.preview.closeEvent = self.previewCloseEvent
        self.gui.hide()
        self.preview.lbl_wait.setAttribute(Qt.WA_TranslucentBackground)
        self.preview.lbl_wait.setHidden(True)

        # Apply setttings.
        self.applyPreviewSettings()

        # Connections.
        self.preview.btn_raytrace.clicked.connect(self.launchPOVRay)
        self.preview.btn_preview.clicked.connect(self.renderPreview)
        self.preview.btn_PaletteHelm.clicked.connect(self.btn_PaletteHelmFunc)
        self.preview.btn_PaletteBack.clicked.connect(self.btn_PaletteBackFunc)
        self.preview.btn_PaletteDec.clicked.connect(self.btn_PaletteHelmDecFunc)
        self.preview.btn_PaletteLight.clicked.connect(self.btn_PaletteHelmLightFunc)
        self.preview.cb_TransparentBG.stateChanged.connect(self.cb_previewTransparentFunc)
        self.preview.btn_resetColours.clicked.connect(self.btn_previewResetColoursFunc)
        self.preview.vs_Ambient.valueChanged.connect(self.vs_previewAmbientFunc)
        self.preview.vs_Specular.valueChanged.connect(self.vs_previewSpecularFunc)
        self.preview.vs_Roughness.valueChanged.connect(self.vs_previewRoughnessFunc)
        self.preview.vs_Reflection.valueChanged.connect(self.vs_previewReflectionFunc)
        self.preview.btn_resetSurfProps.clicked.connect(self.btn_previewResetSurfPropsFunc)
        self.preview.vs_CamX.valueChanged.connect(self.vs_previewCamXFunc)
        self.preview.vs_CamY.valueChanged.connect(self.vs_previewCamYFunc)
        self.preview.vs_CamZ.valueChanged.connect(self.vs_previewCamZFunc)
        self.preview.vs_LookX.valueChanged.connect(self.vs_previewLookXFunc)
        self.preview.vs_LookY.valueChanged.connect(self.vs_previewLookYFunc)
        self.preview.vs_LookZ.valueChanged.connect(self.vs_previewLookZFunc)
        self.preview.btn_resetCamera.clicked.connect(self.btn_previewResetCameraFunc)
        self.preview.vs_LightX.valueChanged.connect(self.vs_previewLightXFunc)
        self.preview.vs_LightY.valueChanged.connect(self.vs_previewLightYFunc)
        self.preview.vs_LightZ.valueChanged.connect(self.vs_previewLightZFunc)
        self.preview.btn_resetLight.clicked.connect(self.btn_previewResetLightFunc)
        self.preview.sb_Width.valueChanged.connect(self.sb_previewWidthFunc)
        self.preview.sb_Quality.valueChanged.connect(self.sb_previewQualityFunc)
        self.preview.cb_AA.stateChanged.connect(self.cb_previewAAFunc)
        self.preview.cb_Shadowless.stateChanged.connect(self.cb_previewShadowlessFunc)
        self.preview.cb_Homo.stateChanged.connect(self.cb_previewHomoFunc)
        self.preview.cb_Mosaic.stateChanged.connect(self.cb_previewMosaicFunc)
        self.preview.btn_resetOptions.clicked.connect(self.btn_previewResetOptionsFunc)
        self.preview.le_helmText.textChanged.connect(self.le_previewHelmTextFunc)
        self.preview.fcb_helmFont.currentFontChanged.connect(self.fcb_previewHelmFontFunc)
        self.preview.cb_hemlLogo1Type.currentIndexChanged.connect(self.cb_previewHemlLogo1TypeFunc)
        self.preview.cb_hemlLogo2Type.currentIndexChanged.connect(self.cb_previewHemlLogo2TypeFunc)
        self.preview.btn_helmLogo1Filepath.clicked.connect(lambda: self.getLogoFile(1))
        self.preview.btn_helmLogo2Filepath.clicked.connect(lambda: self.getLogoFile(2))
        self.preview.le_helmLogo1Filepath.textChanged.connect(lambda: self.le_previewHelmLogoXFilepathFunc(1))
        self.preview.le_helmLogo2Filepath.textChanged.connect(lambda: self.le_previewHelmLogoXFilepathFunc(2))
        self.preview.btn_resetDecorations.clicked.connect(self.btn_previewResetDecsFunc)
        self.preview.btn_Reset.clicked.connect(self.btn_previewResetFunc)
        self.preview.btn_Save.clicked.connect(self.btn_previewSaveFunc)
        self.preview.btn_Load.clicked.connect(self.btn_previewLoadFunc)
        self.preview.cb_PresetCam.currentIndexChanged.connect(self.cb_previewPresetCamHelmFunc)
        self.preview.cb_PresetLook.currentIndexChanged.connect(self.cb_previewPresetLookHelmFunc)
        self.preview.cb_PresetLight.currentIndexChanged.connect(self.cb_previewPresetLightHelmFunc)
        self.preview.lbl_CamX.mouseReleaseEvent = self.lbl_CamXHelmFunc
        self.preview.lbl_CamY.mouseReleaseEvent = self.lbl_CamYHelmFunc
        self.preview.lbl_CamZ.mouseReleaseEvent = self.lbl_CamZHelmFunc
        self.preview.lbl_LookX.mouseReleaseEvent = self.lbl_LookXHelmFunc
        self.preview.lbl_LookY.mouseReleaseEvent = self.lbl_LookYHelmFunc
        self.preview.lbl_LookZ.mouseReleaseEvent = self.lbl_LookZHelmFunc
        self.preview.lbl_LightX.mouseReleaseEvent = self.lbl_LightXHelmFunc
        self.preview.lbl_LightY.mouseReleaseEvent = self.lbl_LightYHelmFunc
        self.preview.lbl_LightZ.mouseReleaseEvent = self.lbl_LightZHelmFunc
        self.preview.lbl_Ambient.mouseReleaseEvent = self.lbl_AmbientFunc
        self.preview.lbl_Specular.mouseReleaseEvent = self.lbl_SpecularFunc
        self.preview.lbl_Roughness.mouseReleaseEvent = self.lbl_RoughnessFunc
        self.preview.lbl_Reflection.mouseReleaseEvent = self.lbl_ReflectionFunc

        # Set widgets to auto update on their mouseReleaseEvent.
        self.preview.cb_Refresh.stateChanged.connect(self.cb_previewRefreshFunc)

        # Colours.
        for label in [self.preview.lbl_PaletteHelm, self.preview.lbl_PaletteDec, self.preview.lbl_PaletteBack, self.preview.lbl_PaletteLight]:
            label.paintEvent = self.previewAutoRefresh

        # Checkboxes.
        for checkbox in [self.preview.cb_TransparentBG, self.preview.cb_Shadowless, self.preview.cb_Homo]:
            checkbox.stateChanged.connect(self.previewAutoRefresh)

        # Buttons.
        for button in [self.preview.btn_resetSurfProps, self.preview.btn_resetCamera, self.preview.btn_resetLight]:
            button.clicked.connect(self.previewAutoRefresh)

        # Spinboxes.
        for spinbox in [self.preview.sb_Quality]:
            spinbox.valueChanged.connect(self.previewAutoRefresh)

        # Sliders.
        for slider in [self.preview.vs_CamX, self.preview.vs_CamY, self.preview.vs_CamZ,
                       self.preview.vs_LookX, self.preview.vs_LookY, self.preview.vs_LookZ,
                       self.preview.vs_LightX, self.preview.vs_LightY, self.preview.vs_LightZ,
                       self.preview.vs_Ambient, self.preview.vs_Specular, self.preview.vs_Roughness, self.preview.vs_Reflection]:
            slider.mouseReleaseEvent = self.previewAutoRefresh

        # Decorations.
        self.preview.cb_hemlLogo1Type.currentIndexChanged.connect(self.previewAutoRefresh)
        self.preview.cb_hemlLogo2Type.currentIndexChanged.connect(self.previewAutoRefresh)
        self.preview.fcb_helmFont.currentTextChanged.connect(self.previewAutoRefresh)
        self.preview.le_helmLogo1Filepath.textChanged.connect(self.previewAutoRefresh)
        self.preview.le_helmLogo2Filepath.textChanged.connect(self.previewAutoRefresh)
        self.preview.le_helmText.editingFinished.connect(self.previewAutoRefresh)

        # Get a preview uniform render.
        self.renderPreview()
        self.previewLoaded = True
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def applyPreviewSettings(self):
        '''Method to apply the currently loaded preview settings.'''

        # Reset the last cut of the renderData to allow the uniform to be drawn.
        self.lastRenderData = ()

        if self.uniform != "helmet":
            # Colours.
            # Spotlight Colour.
            self.colourSelected(self.spotColour, "spotColour", self.preview.lbl_PaletteSpot, self.preview.le_PaletteSpot)
            # Environment Colour.
            self.colourSelected(self.envColour, "envColour", self.preview.lbl_PaletteEnv, self.preview.le_PaletteEnv)
            # Background Colour.
            self.colourSelected(self.bgColour, "bgColour", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
            # POV-Ray Options.
            # Resolution.
            self.preview.sb_Width.setValue(self.width)
            self.preview.le_Height.setText(str(self.height))
            # Quality.
            self.preview.sb_Quality.setValue(self.quality)
            # Cloth.
            self.preview.cb_Detail.setCurrentIndex(self.clothDetail)
            # Checkboxes.
            self.preview.cb_AA.setChecked(self.antiAliasing)
            self.preview.cb_Shadowless.setChecked(self.shadowless)
            self.preview.cb_Mosaic.setChecked(self.mosaicPreview)
            if self.transparentBG == " +UA":
                self.preview.cb_TransparentBG.setChecked(True)
                self.cb_previewTransparentFunc(2)
            else:
                self.preview.cb_TransparentBG.setChecked(False)
                self.cb_previewTransparentFunc(0)
            # Slider Bars
            self.preview.vs_CamX.setValue(self.camX)
            self.preview.lbl_CamX.setText(self.convertIntToFloatStr(self.camX, 10))
            self.preview.vs_CamY.setValue(self.camY)
            self.preview.lbl_CamY.setText(self.convertIntToFloatStr(self.camY, 10))
            self.preview.vs_CamZ.setValue(self.camZ)
            self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(self.camZ, 10))
            self.preview.vs_LookX.setValue(self.lookX)
            self.preview.lbl_LookX.setText(self.convertIntToFloatStr(self.lookX, 10))
            self.preview.vs_LookY.setValue(self.lookY)
            self.preview.lbl_LookY.setText(self.convertIntToFloatStr(self.lookY, 10))
            self.preview.vs_LookZ.setValue(self.lookZ)
            self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(self.lookZ, 10))
            self.preview.vs_LightX.setValue(self.lightX)
            self.preview.lbl_LightX.setText(self.convertIntToFloatStr(self.lightX, 10))
            self.preview.vs_LightY.setValue(self.lightY)
            self.preview.lbl_LightY.setText(self.convertIntToFloatStr(self.lightY, 10))
            self.preview.vs_LightZ.setValue(self.lightZ)
            self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(self.lightZ, 10))
        else:
            # Colours.
            # Helmet Colour.
            self.colourSelected(self.helmColour, "helmColour", self.preview.lbl_PaletteHelm, self.preview.le_PaletteHelm)
            # Decoration Colour.
            self.colourSelected(self.decColour, "decColour", self.preview.lbl_PaletteDec, self.preview.le_PaletteDec)
            # Background Colour.
            self.colourSelected(self.bgColourHelm, "bgColourHelm", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
            # Light Colour.
            self.colourSelected(self.lightColour, "lightColour", self.preview.lbl_PaletteLight, self.preview.le_PaletteLight)

            # POV-Ray Options.
            # Resolution.
            self.preview.sb_Width.setValue(self.widthHelm)
            self.preview.le_Height.setText(str(self.heightHelm))
            # Quality.
            self.preview.sb_Quality.setValue(self.qualityHelm)
            # Checkboxes.
            self.preview.cb_AA.setChecked(self.antiAliasingHelm)
            self.preview.cb_Shadowless.setChecked(self.shadowlessHelm)
            self.preview.cb_Homo.setChecked(self.homoHelm)
            self.preview.cb_Mosaic.setChecked(self.mosaicPreviewHelm)
            if self.transparentBGHelm == " +UA":
                self.preview.cb_TransparentBG.setChecked(True)
                self.cb_previewTransparentFunc(2)
            else:
                self.preview.cb_TransparentBG.setChecked(False)
                self.cb_previewTransparentFunc(0)
            # Slider Bars
            self.preview.vs_Ambient.setValue(self.ambientHelm)
            self.preview.lbl_Ambient.setText(self.convertIntToFloatStr(self.ambientHelm, 100))
            self.preview.vs_Specular.setValue(self.specularHelm)
            self.preview.lbl_Specular.setText(self.convertIntToFloatStr(self.specularHelm, 100))
            self.preview.vs_Roughness.setValue(self.roughHelm)
            self.preview.lbl_Roughness.setText(self.convertIntToFloatStr(self.roughHelm, 100))
            self.preview.vs_Reflection.setValue(self.reflectionHelm)
            self.preview.lbl_Reflection.setText(self.convertIntToFloatStr(self.reflectionHelm, 100))
            self.preview.vs_CamX.setValue(self.camXHelm)
            self.preview.lbl_CamX.setText(self.convertIntToFloatStr(self.camXHelm, 100))
            self.preview.vs_CamY.setValue(self.camYHelm)
            self.preview.lbl_CamY.setText(self.convertIntToFloatStr(self.camYHelm, 100))
            self.preview.vs_CamZ.setValue(self.camZHelm)
            self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(self.camZHelm, 100))
            self.preview.vs_LookX.setValue(self.lookXHelm)
            self.preview.lbl_LookX.setText(self.convertIntToFloatStr(self.lookXHelm, 100))
            self.preview.vs_LookY.setValue(self.lookYHelm)
            self.preview.lbl_LookY.setText(self.convertIntToFloatStr(self.lookYHelm, 100))
            self.preview.vs_LookZ.setValue(self.lookZHelm)
            self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(self.lookZHelm, 100))
            self.preview.vs_LightX.setValue(self.lightXHelm)
            self.preview.lbl_LightX.setText(self.convertIntToFloatStr(self.lightXHelm, 100))
            self.preview.vs_LightY.setValue(self.lightYHelm)
            self.preview.lbl_LightY.setText(self.convertIntToFloatStr(self.lightYHelm, 100))
            self.preview.vs_LightZ.setValue(self.lightZHelm)
            self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(self.lightZHelm, 100))

            # Decorations.
            # Helmet Text.
            if self.nameHelm == "EH TC":
                if self.callsign != "None":
                    self.nameHelm = self.callsign[:12].rstrip(" ")
            self.preview.le_helmText.setText(self.nameHelm)
            self.preview.fcb_helmFont.setCurrentFont(self.fontHelmQFront)

            # Logo options.
            widgets = [self.preview.cb_hemlLogo1Type, self.preview.cb_hemlLogo2Type]
            logo1Type = self.logo1TypeHelm  # Used to reset user options during the addition of combo box items.
            logo2Type = self.logo2TypeHelm

            self.loadingHelm = True
            for widget in widgets:
                widget.clear()
                if self.sqn == "":
                    widget.addItems(["Image - bg. transparent", "Image - stencil mask", "None"])
                else:
                    widget.addItems(["Squadron Patch", "Image - bg. transparent", "Image - stencil mask", "None"])
            self.loadingHelm = False

            self.logo1TypeHelm = logo1Type
            self.logo2TypeHelm = logo2Type
            logo1TypeInt = self.preview.cb_hemlLogo1Type.findText(self.logo1TypeHelm, Qt.MatchExactly | Qt.MatchCaseSensitive)
            logo2TypeInt = self.preview.cb_hemlLogo2Type.findText(self.logo2TypeHelm, Qt.MatchExactly | Qt.MatchCaseSensitive)
            self.preview.cb_hemlLogo1Type.setCurrentIndex(logo1TypeInt)
            self.preview.cb_hemlLogo2Type.setCurrentIndex(logo2TypeInt)

            if self.preview.cb_hemlLogo2Type.currentText() == "":  # If previous setting was 'Squadron Patch' (default) but it's not longer available.
                self.preview.cb_hemlLogo2Type.setCurrentIndex(1)
                self.logo2FilepathHelm = os.getcwd() + "\\data\\misc\\Helmet Stencils\\tiecorps_logo_new.png"

            self.preview.le_helmLogo1Filepath.setText(self.logo1FilepathHelm)
            self.preview.le_helmLogo2Filepath.setText(self.logo2FilepathHelm)
            self.cb_previewHemlLogo1TypeFunc()
            self.cb_previewHemlLogo2TypeFunc()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def renderPreview(self):
        '''Method for rendering a preview image.'''

        if self.getUniformData() != self.lastRenderData:
            if self.previewLoaded:
                self.preview.lbl_wait.setHidden(False)
            if self.uniform == "dress":
                self.createDressPov()
            elif self.uniform == "duty":
                self.createDutyPov()
            elif self.uniform == "helmet":
                self.createHelmetPov()
            self.queue.put(None)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def taskQueuer(self):
        '''Method used to queuing preview requests.'''

        while True:
            item = self.queue.get()
            if self.getUniformData() != self.lastRenderData:
                self.lastRenderData = self.getUniformData()
                self.launchPOVRay(preview=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_dutyMethod(self):
        '''Method that is triggered when the 'Duty Uniform' button is clicked.
           This method will check that the correct selections has been made within TTT3 such as Ship and Squadron and then
           directly call 'launchPOVRay' to open up PovRay and render the unirom.'''

        try:
            self.uniform = "duty"
            self.showPreviewDialog()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_helmetMethod(self):
        '''Method that is triggered when the 'Pilot's Helmet' button is clicked.
           This method will check that the correct selections has been made within TTT3 such as Ship and Squadron and then
           directly call 'launchPOVRay' to open up PovRay and render the unirom.'''

        try:
            self.uniform = "helmet"
            self.showPreviewHelmDialog()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def launchPOVRay(self, preview=False):
        '''Method that dynamically launches POV-Ray with the correct paths.
           The "uniform" argument takes "dress", "duty or "helmet" which is dependant on which button has been pressed.'''

        self.launchingPOVRay = True
        self.lastRenderData = self.getUniformData()
        self.preview.btn_raytrace.setEnabled(False)
        QApplication.processEvents()

        # Recreate our *.pov file for final rendering.
        if not preview:
            if self.uniform == "dress":
                self.createDressPov()

            elif self.uniform == "duty":
                self.createDutyPov()

            elif self.uniform == "helmet":
                self.createHelmetPov()

        if self.uniform == "dress":
            width = self.width
            height = self.height
            quality = self.quality

        elif self.uniform == "duty":
            width = self.width
            height = self.height
            quality = self.quality

        elif self.uniform == "helmet":
            width = self.widthHelm
            height = self.heightHelm
            quality = self.qualityHelm

        # Remove old uniform image files.
        try:
            os.remove("data\\%s.png" % self.uniform)
        except FileNotFoundError:
            pass

        # Set the correct paths based on where TTT3 is located and the TTT3.ini settings file.
        if not preview:
            if not self.fastRendering:
                # Normal mode.
                if self.uniform == "helmet":
                    template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\" +I&TYPE&.pov +W{width} +H{height} +Q{quality} +AM2 +A0.1 +F +GA +J1.0{trans} -D /EXIT'.format(
                        width=width, height=height, quality=quality, trans=self.transparentBGHelm)
                    if self.mosaicPreviewHelm:
                        template = template.replace("-D", "+SP64")
                    if not self.antiAliasingHelm:
                        template = template.replace("+AM2 +A0.1", "-A")
                else:
                    template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\" +I&TYPE&.pov +W{width} +H{height} +Q{quality} +AM2 +A0.1 +F +GA +J1.0{trans} -D /EXIT'.format(
                        width=width, height=height, quality=quality, trans=self.transparentBG)
                    if self.mosaicPreview:
                        template = template.replace("-D", "+SP64")
                    if not self.antiAliasing:
                        template = template.replace("+AM2 +A0.1", "-A")
            else:
                # Fast render mode.
                if self.uniform == "helmet":
                    template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\" +I&TYPE&.pov +W640 +H548 +Q6{trans} -D /EXIT'.format(trans=self.transparentBG)
                else:
                    template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\" +I&TYPE&.pov +W640 +H853 +Q6{trans} -D /EXIT'.format(
                        trans=self.transparentBGHelm)
        else:
            # Preview Mode.
            if self.uniform == "helmet":
                template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\" +I&TYPE&.pov +W390 +H334 +Q{quality}{trans} -A -D /EXIT'.format(
                    quality=quality, trans=self.transparentBGHelm)
            else:
                template = r'"&POVPATH&" /RENDER "&TTTPATH&\data\" +I&TYPE&.pov +W390 +H520 +Q{quality}{trans} -A -D /EXIT'.format(
                    quality=quality, trans=self.transparentBG)

        template = template.replace("&TTTPATH&", os.getcwd())

        # Apply the path depending on what the user has selected from within the Configuratrion window.
        if self.config.get("POV-Ray", "detection_mode") == "registry":
            regPath = self.getPathFromRegistry()
            if regPath != "POV-Ray Installation Not Found":
                template = template.replace("&POVPATH&", regPath)
            else:
                msg = "TTT3 cannot find valid installion of POV-Ray.\n\nPlease ensure that POV-Ray v3.7 or greater is installed. " \
                      + "The POV-Ray website can be found on the 'Info' tab." \
                      + "\n\nYou can also set the POV-Ray installtion path manually from the 'Configuration' menu."
                ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                self.launchingPOVRay = False
                return
        else:
            template = template.replace("&POVPATH&", self.config.get("POV-Ray", "user_specified_path"))

        template = template.replace("&TYPE&", self.uniform)

        # Launch POV-Ray
        if preview:
            SW_HIDE = 0
            info = subprocess.STARTUPINFO()
            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
            info.wShowWindow = SW_HIDE
            pov = subprocess.Popen(template, startupinfo=info)
        else:
            pov = subprocess.Popen(template)

        # Wait for POV-Ray to close.
        self.povrayMonitor(pov.pid)

        self.preview.btn_raytrace.setEnabled(True)
        if not preview:
            # Show the output GUI.
            self.showOutputDialog(self.uniform)
        else:
            self.showPreviewImage()
            self.queue.task_done()

        self.launchingPOVRay = False
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def showPreviewImage(self):
        '''Method to show a preview image in the preview GUI.'''

        # Determine the version of POV-Ray and it's associated file output type.
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

        self.imagePath = r"data\%s%s" % (self.uniform, ext)
        self.preview.lbl_preview.setPixmap(QPixmap(self.imagePath))
        self.preview.lbl_wait.setHidden(True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def showOutputDialog(self, uniform):
        '''Method to display the POV-Ray rendered image.'''

        # Determine the version of POV-Ray and it's associated file output type.
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
        if self.uniform == "helmet":
            helmetHeight = 548
            yOffset = 305
            self.output_gui.lbl_output.setMinimumHeight(helmetHeight)
            self.output_gui.lbl_output.setMaximumHeight(helmetHeight)
            self.output_gui.groupBox.setMinimumHeight(self.output_gui.groupBox.height() - yOffset)
            self.output_gui.groupBox.setMaximumHeight(self.output_gui.groupBox.height() - yOffset)
            self.output_gui.setMinimumHeight(self.output_gui.height() - yOffset)
            self.output_gui.setMaximumHeight(self.output_gui.height() - yOffset)
            for button in [self.output_gui.btn_saveAs, self.output_gui.btn_open, self.output_gui.btn_close]:
                pos = button.pos()
                pos.setY(pos.y() - yOffset)
                button.move(pos)
        self.output_gui.lbl_output.installEventFilter(self)
        self.resizeOutput()
        self.output_gui.show()
        setPixelSizes(self.output_gui)
        self.output_gui.btn_saveAs.clicked.connect(self.btn_saveAsFunc)
        self.output_gui.btn_open.clicked.connect(self.btn_openFunc)
        self.output_gui.btn_close.clicked.connect(self.outputCloseEvent)
        self.output_gui.closeEvent = self.outputCloseEvent
        self.preview.hide()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def resizeOutput(self):
        '''Method to resize the output window to match the user's height and width settings.'''

        if self.uniform != "helmet":
            height = self.height
            width = self.width
            baseHeight = 853
            baseWidth = 640
        else:
            height = self.heightHelm
            width = self.widthHelm
            baseHeight = 548
            baseWidth = 640

        # Determine if the user's selected width and height extend beyond their monitor's display output and display at max screen resolution if so.
        screenWidth, screenHeight = getScreenResolution()

        if height > screenHeight - 180:  # 180 pixels to account for groupbox and lower buttons.
            height = screenHeight - 180
            if self.uniform != "helmet":
                width = getX(height)
            else:
                width = getXHelm(height)

        elif width - 40 > screenWidth:  # 40 pixels to allow for groupbox and borders.
            width = screenWidth - 40
            if self.uniform != "helmet":
                height = getY(width)
            else:
                height = getYHelm(width)

        # Resize the output window, it's inner groupbox and the output image.
        xOffset = width - baseWidth
        yOffset = height - baseHeight

        # Image sizing.
        self.output_gui.lbl_output.setMinimumHeight(height)
        self.output_gui.lbl_output.setMaximumHeight(height)
        self.output_gui.lbl_output.setMinimumWidth(width)
        self.output_gui.lbl_output.setMaximumWidth(width)

        if xOffset < -240:  # Prevent the output window from going too small.
            xOffset = -240

        # Groupbox sizing.
        self.output_gui.groupBox.setMinimumHeight(self.output_gui.groupBox.height() + yOffset)
        self.output_gui.groupBox.setMaximumHeight(self.output_gui.groupBox.height() + yOffset)
        self.output_gui.groupBox.setMinimumWidth(self.output_gui.groupBox.width() + xOffset)
        self.output_gui.groupBox.setMaximumWidth(self.output_gui.groupBox.width() + xOffset)

        # Window sizing.
        self.output_gui.setMinimumHeight(self.output_gui.height() + yOffset)
        self.output_gui.setMaximumHeight(self.output_gui.height() + yOffset)
        self.output_gui.setMinimumWidth(self.output_gui.width() + xOffset)
        self.output_gui.setMaximumWidth(self.output_gui.width() + xOffset)

        # Center the image horizontally.
        pos = self.output_gui.lbl_output.pos()
        try:
            pos.setX(round((self.output_gui.groupBox.width() - self.output_gui.lbl_output.width()) / 2))
        except ZeroDivisionError:
            pass
        self.output_gui.lbl_output.move(pos)

        # Place the buttons in the correct place.
        for button in [self.output_gui.btn_saveAs, self.output_gui.btn_open, self.output_gui.btn_close]:
            pos = button.pos()
            try:
                pos.setX(pos.x() + round(xOffset / 2))
            except ZeroDivisionError:
                pass
            pos.setY(pos.y() + yOffset)
            button.move(pos)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_saveAsFunc(self):
        '''Method to Save As the rendered image file.'''

        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            if self.name != "Unknown":
                name = self.name
            else:
                name = "untitled"
            saveName, ext = QFileDialog.getSaveFileName(
                self, "Save Uniform As", os.getcwd() + "\\Data\\%s" %
                name + "_" + self.uniform.title(), "*.png;;*.jpg;;*.gif;;*.bmp", options=options)
            ext = ext.replace("*", "")
            if saveName:
                saveName = saveName.replace(r"/", "\\") + ext
                self.convertImage(self.imagePath, ext, saveName)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_openFunc(self):
        '''Method to open rendered image files once displayed and saved in the output window.'''

        subprocess.Popen(os.getcwd() + "\\data\\" + self.uniform + ".png", shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def povrayMonitor(self, pid):
        '''Monitors for POV-Ray running in the background and signals when it has closed.'''

        time.sleep(0.1)  # Allow some time for POV-Ray to open.
        povRunning = True

        while povRunning:
            povRunning = False

            if psutil.pid_exists(pid):
                povRunning = True
                time.sleep(0.1)  # Save some CPU cycles
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def convertImage(self, src, ext, dest):
        '''Converts a given .bpf file into .jpg, .gif, .png or .bmp'''

        if self.uniform == "helmet":
            width = self.widthHelm
            height = self.heightHelm
        else:
            width = self.width
            height = self.height

        img = Image.open(src)
        new_img = img.resize((width, height))
        newFilePath = dest.replace(ext, "") + ext
        if ext == ".jpg":
            ext = ".jpeg"
        try:
            new_img.save(newFilePath, ext.replace(".", ""))
        except PermissionError:
            msg = "Error: TTT3 does not have permission to save files to %s\n\nPlease try saving to a different location." % newFilePath
            return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
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
        self.config_gui.le_pilotAPI.setText(self.config.get("TCDB", "pinapi"))
        self.config_gui.le_fleetAPI.setText(self.config.get("TCDB", "fleetapi"))
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
            setPixelSizes(self.config_gui)

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
            self.config.set("TCDB", "pinapi", str(self.config_gui.le_pilotAPI.text()))
            self.config.set("TCDB", "fleetapi", str(self.config_gui.le_fleetAPI.text()))
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
                # Test to see if POV-Ray is in the registry.
                try:
                    winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\POV-Ray\\", 0, winreg.KEY_READ)
                except FileNotFoundError:
                    path = "POV-Ray Installation Not Found"
                    self.config.set("POV-Ray", "registry_detected_path", path)
                    self.saveSettings()
                    if not self.launchingPOVRay:
                        msg = "Cannot find valid installion of POV-Ray in the Windows Registry."
                        ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                    return path

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
                    try:
                        path = winreg.QueryValueEx(values, "Home")[0]
                        self.config.set("POV-Ray", "detection_mode", "fallback")
                    except FileNotFoundError:
                        path = "POV-Ray Installation Not Found"
                        self.config.set("POV-Ray", "registry_detected_path", path)
                        self.saveSettings()
                        if not self.launchingPOVRay:
                            msg = "Cannot find valid installion of POV-Ray in the Windows Registry."
                            ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                        return path

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
            ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

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
                if self.transparentBG == "":
                    povData.append(line.replace("&BGCOLOUR&", "#declare bg = <%s>;" % self.convertToPOVRGB(self.bgColour)))
                else:
                    povData.append(line.replace("&BGCOLOUR&", ""))

            # ----- Light. -----

            elif "&LIGHT&" in line:
                povData.append(
                    line.replace(
                        "&LIGHT&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.lightX, 10), self.convertIntToFloatStr(
                            self.lightY, 10), self.convertIntToFloatStr(
                            self.lightZ, 10))))

            elif "&SPOTLIGHTCOLOUR&" in line:
                povData.append(line.replace("&SPOTLIGHTCOLOUR&", self.convertToPOVRGB(self.spotColour)))

            elif "&ENVLIGHTCOLOUR&" in line:
                povData.append(line.replace("&ENVLIGHTCOLOUR&", self.convertToPOVRGB(self.envColour)))

            elif "&SHADOWLESS&" in line:
                if self.shadowless:
                    povData.append(line.replace("&SHADOWLESS&", "shadowless"))
                else:
                    povData.append(line.replace("&SHADOWLESS&", ""))

            # ----- Camera. -----

            elif "&CAMERA&" in line:
                povData.append(
                    line.replace(
                        "&CAMERA&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.camX, 10), self.convertIntToFloatStr(
                            self.camY, 10), self.convertIntToFloatStr(
                            self.camZ, 10))))

            elif "&TARGET&" in line:
                povData.append(
                    line.replace(
                        "&TARGET&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.lookX, 10), self.convertIntToFloatStr(
                            self.lookY, 10), self.convertIntToFloatStr(
                            self.lookZ, 10))))

            # ----- Basic Info. -----
            elif "&EE&" in line:
                if self.eeCount >= 3:
                    povData.append(line.replace("&EE&", "#declare prae = 1;"))
                    self.gui.label_11.setText("FA Turtle Jerrar,")
                    self.gui.label_11.setStyleSheet("")

            elif "&CLOTH&" in line:
                povData.append(line.replace("&CLOTH&", str(self.clothDetail)))

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
                    self.createMask()

            elif "&TRIMCOLOUR&" in line:

                if self.wing != "":
                    # Find the selected wing from fleetConfig.
                    for wing in self.fleetConfig.get("wings"):
                        if wing.get("name") == self.wing:
                            # Get the trim colouring.
                            trimColour = wing.get("uniformData").get("trimColor")
                            # Set the trim colouring.
                            if trimColour:
                                col0, col1 = trimColour.split(":")
                                trimLine = """#declare ttt_pcolour =
color_map
{
  [0.0 colour rgb %s]
  [1.0 colour rgb %s]
}
#declare ttt_wingcolour = color rgb %s;""" % (col0, col1, col0)

                                povData.append(line.replace("&TRIMCOLOUR&", trimLine))
                                break
                            else:
                                povData.append(line.replace("&TRIMCOLOUR&", ""))
                                break
                        else:
                            povData.append(line.replace("&TRIMCOLOUR&", ""))

                elif self.ship != "":
                    # Find the selected ship from fleetConfig.
                    for ship in self.fleetConfig.get("ships"):
                        if ship.get("nameShort") == self.ship:
                            # Get the trim colouring.
                            trimColour = ship.get("uniformData").get("trimColor")
                            # Set the trim colouring.
                            if trimColour:
                                trimLine = "#declare ttt_wingcolour = color rgb %s;" % (trimColour)
                                povData.append(line.replace("&TRIMCOLOUR&", trimLine))
                                break
                            else:
                                povData.append(line.replace("&TRIMCOLOUR&", ""))
                                break

                else:
                    povData.append(line.replace("&TRIMCOLOUR&", ""))

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
                    povData.append(line.replace("&FCHGINCLUDE&", '#include "wing_g.inc"'))

            elif "&SABERINCLUDE&" in line:
                if self.gui.cb_dressLightsaber.isChecked() and self.gui.cb_dressSaberStyles.currentText() != "":
                    include = '#include "%s"' % self.saberDict.get(self.gui.cb_dressSaberStyles.currentText())
                    povData.append(line.replace("&SABERINCLUDE&", include))

            elif "&MEDALSINCLUDE&" in line:
                for includeRef in self.buildMedalIncludes():
                    povData.append('#include "%s"\n' % includeRef)

            # ----- Scene. -----

            # Flight Certification Wings (formerly FCHG). -------------------------------
            elif "&FCHG&" in line:
                if "None" in self.gui.cbFCHG.currentText():
                    pass

                elif self.gui.cbFCHG.currentText().startswith("1st Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon1 }"))

                elif self.gui.cbFCHG.currentText().startswith("2nd Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon2 }"))

                elif self.gui.cbFCHG.currentText().startswith("3rd Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon3 }"))

                elif self.gui.cbFCHG.currentText().startswith("4th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon4 }"))

                elif self.gui.cbFCHG.currentText().startswith("5th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon5 }"))

                elif self.gui.cbFCHG.currentText().startswith("6th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon6 }"))

                elif self.gui.cbFCHG.currentText().startswith("7th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon7 }"))

                elif self.gui.cbFCHG.currentText().startswith("8th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon8 }"))

                elif self.gui.cbFCHG.currentText().startswith("9th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon9 }"))

                elif self.gui.cbFCHG.currentText().startswith("10th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon10 }"))

                elif self.gui.cbFCHG.currentText().startswith("11th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon11 }"))

                elif self.gui.cbFCHG.currentText().startswith("12th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon12 }"))

                elif self.gui.cbFCHG.currentText().startswith("13th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon13 }"))

                elif self.gui.cbFCHG.currentText().startswith("14th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon14 }"))

                elif self.gui.cbFCHG.currentText().startswith("15th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon15 }"))

                elif self.gui.cbFCHG.currentText().startswith("16th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon16 }"))

                elif self.gui.cbFCHG.currentText().startswith("17th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon17 }"))

                elif self.gui.cbFCHG.currentText().startswith("18th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon18 }"))

                elif self.gui.cbFCHG.currentText().startswith("19th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon19 }"))

                elif self.gui.cbFCHG.currentText().startswith("20th Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon20 }"))

                elif self.gui.cbFCHG.currentText().startswith("21st Echelon"):
                    povData.append(line.replace("&FCHG&", "object { echelon21 }"))

                else:
                    pass
                # ------------------------------------------------------------

            elif "&SABER&" in line:
                if self.gui.cb_dressLightsaber.isChecked() and self.gui.cb_dressSaberStyles.currentText() != "":
                    style = self.saberDict.get(self.gui.cb_dressSaberStyles.currentText()).replace("_g.inc", "")
                    if self.gui.rb_dressSaberLeft.isChecked():
                        side = "left"
                    else:
                        side = "right"
                    object = 'object { %s_%s }' % (style, side)
                    povData.append(line.replace("&SABER&", object))

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
        padding = (35 - len(posRankName)) * " "
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
                if self.transparentBG == "":
                    povData.append(line.replace("&BGCOLOUR&", "#declare bg = <%s>;" % self.convertToPOVRGB(self.bgColour)))
                else:
                    povData.append(line.replace("&BGCOLOUR&", ""))

            # ----- Light. -----

            elif "&LIGHT&" in line:
                povData.append(
                    line.replace(
                        "&LIGHT&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.lightX, 10), self.convertIntToFloatStr(
                            self.lightY, 10), self.convertIntToFloatStr(
                            self.lightZ, 10))))

            elif "&SPOTLIGHTCOLOUR&" in line:
                povData.append(line.replace("&SPOTLIGHTCOLOUR&", self.convertToPOVRGB(self.spotColour)))

            elif "&SHADOWLESS&" in line:
                if self.shadowless:
                    povData.append(line.replace("&SHADOWLESS&", "shadowless"))
                else:
                    povData.append(line.replace("&SHADOWLESS&", ""))

            elif "&ENVLIGHTCOLOUR&" in line:
                povData.append(line.replace("&ENVLIGHTCOLOUR&", self.convertToPOVRGB(self.envColour)))

            # ----- Camera. -----

            elif "&CAMERA&" in line:
                povData.append(
                    line.replace(
                        "&CAMERA&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.camX, 10), self.convertIntToFloatStr(
                            self.camY, 10), self.convertIntToFloatStr(
                            self.camZ, 10))))

            elif "&TARGET&" in line:
                povData.append(
                    line.replace(
                        "&TARGET&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.lookX, 10), self.convertIntToFloatStr(
                            self.lookY, 10), self.convertIntToFloatStr(
                            self.lookZ, 10))))

            # ----- Basic Info. -----
            elif "&CLOTH&" in line:
                povData.append(line.replace("&CLOTH&", str(self.clothDetail)))

            elif "&POSITION&" in line:
                if self.position == "TRN" or self.position == "LR" or self.position == "FR":
                    povData.append(line.replace("&POSITION&", ""))
                else:
                    povData.append(line.replace("&POSITION&", "object { P_%s }" % self.position))

            elif "&RANK&" in line:
                povData.append(line.replace("&RANK&", self.rank))

            elif "&RANKROTATE&" in line:
                if self.rank in ["CT", "SL", "LT", "LCM", "CM", "CPT", "MAJ", "LC", "COL", "GN"]:
                    povData.append(line.replace("&RANKROTATE&", self.RANK_OFFSET_DUTY_LINE[0]))
                else:
                    povData.append(line.replace("&RANKROTATE&", self.RANK_OFFSET_DUTY_FLAG[0]))

            elif "&RANKTRANSLATE&" in line:
                if self.rank in ["CT", "SL", "LT", "LCM", "CM", "CPT", "MAJ", "LC", "COL", "GN"]:
                    povData.append(line.replace("&RANKTRANSLATE&", self.RANK_OFFSET_DUTY_LINE[1]))
                else:
                    povData.append(line.replace("&RANKTRANSLATE&", self.RANK_OFFSET_DUTY_FLAG[1]))

            elif "&SABERINCLUDE&" in line:
                if self.gui.cb_dutyLightsaber.isChecked() and self.gui.cb_dutySaberStyles.currentText() != "":
                    include = '#include "%s"' % self.saberDict.get(self.gui.cb_dutySaberStyles.currentText())
                    povData.append(line.replace("&SABERINCLUDE&", include))

            elif "&SABER&" in line:
                if self.gui.cb_dutyLightsaber.isChecked() and self.gui.cb_dutySaberStyles.currentText() != "":
                    style = self.saberDict.get(self.gui.cb_dutySaberStyles.currentText()).replace("_g.inc", "")
                    if self.gui.rb_dutySaberLeft.isChecked():
                        side = "left"
                    else:
                        side = "right"
                    object = 'object { %s_%s }' % (style, side)
                    povData.append(line.replace("&SABER&", object))

            elif "&BLASTERINCLUDE&" in line:
                if self.gui.cb_dutyBlaster.isChecked() and self.gui.cb_dutyBlasterStyles.currentText() != "":
                    include = '#include "%s"' % self.blasterDict.get(self.gui.cb_dutyBlasterStyles.currentText())
                    povData.append(line.replace("&BLASTERINCLUDE&", include))

            elif "&BLASTER&" in line:
                if self.gui.cb_dutyBlaster.isChecked() and self.gui.cb_dutyBlasterStyles.currentText() != "":
                    style = self.blasterDict.get(self.gui.cb_dutyBlasterStyles.currentText()).replace("_g.inc", "")
                    if self.gui.rb_blasterLeft.isChecked():
                        side = "left"
                    else:
                        side = "right"
                    object = 'object { %s_%s }' % (style, side)
                    povData.append(line.replace("&BLASTER&", object))

            # ----- Non-Editable Data. -----
            else:
                povData.append(line)

        # Write the parsed data to '\data\dress.pov'.
        with open(r"data\duty.pov", "w") as povFile:
            povFile.writelines(povData)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def createHelmetPov(self):
        r'''Method that loads in '\data\helmet.tpt' parses in the correct uniform data and creates a new 'data\helmet.pov' file.'''

        # Create the Pilot Helmet nametag.
        self.createHelmetNameTag()

        # Read in the template data.
        with open(r"data\helmet.tpt", "r") as tptFile:
            template = tptFile.readlines()

        # Header text.
        position = ""
        if self.position == "NUL" or self.position is None or self.position == "LR" or self.position == "FR":
            position = "NIL/"
        else:
            position = self.position + "/"

        posName = position + self.name
        padding = (41 - len(posName)) * " "
        posName += padding

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d  %H:%M:%S")
        padding = (64 - len(timestamp)) * " "
        timestamp += padding

        version = self.version
        padding = (59 - len(version)) * " "
        version += padding

        header = """ ////////////////////////////////////////////////////////////////////
//                                                                 //
// EH/TIE Corps Helmet of {posName}//
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
""".format(posName=posName, version=version, timestamp=timestamp)

        povData = []

        for line in header:
            povData.append(line)

        # Parse the template data.
        for line in template:

            # ----- Global. -----
            if "&BGCOLOUR&" in line:
                if self.transparentBGHelm == "":
                    povData.append(line.replace("&BGCOLOUR&", "#declare bg = <%s>;" % self.convertToPOVRGB(self.bgColourHelm)))
                else:
                    povData.append(line.replace("&BGCOLOUR&", ""))

            # ----- Light. -----

            elif "&LIGHT&" in line:
                povData.append(
                    line.replace(
                        "&LIGHT&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.lightXHelm, 100), self.convertIntToFloatStr(
                            self.lightYHelm, 100), self.convertIntToFloatStr(
                            self.lightZHelm, 100))))

            elif "&SPOTLIGHTCOLOUR&" in line:
                povData.append(line.replace("&SPOTLIGHTCOLOUR&", self.convertToPOVRGB(self.lightColour)))

            elif "&SHADOWLESS&" in line:
                if self.shadowlessHelm:
                    povData.append(line.replace("&SHADOWLESS&", "shadowless"))
                else:
                    povData.append(line.replace("&SHADOWLESS&", ""))

            # ----- Camera. -----

            elif "&CAMERA&" in line:
                povData.append(
                    line.replace(
                        "&CAMERA&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.camXHelm, 100), self.convertIntToFloatStr(
                            self.camYHelm, 100), self.convertIntToFloatStr(
                            self.camZHelm, 100))))

            elif "&TARGET&" in line:
                povData.append(
                    line.replace(
                        "&TARGET&", "%s, %s, %s" %
                        (self.convertIntToFloatStr(
                            self.lookXHelm, 100), self.convertIntToFloatStr(
                            self.lookYHelm, 100), self.convertIntToFloatStr(
                            self.lookZHelm, 100))))

            # ----- Helmet Settings -----
            elif "&HELMCOLOUR&" in line:
                self.creatHelmetFaceColour(self.helmColour)
                povData.append(line.replace("&HELMCOLOUR&", "%s" % self.convertToPOVRGB(self.helmColour)))

            elif "&AMBIENT&" in line:
                povData.append(line.replace("&AMBIENT&", "%s" % self.convertIntToFloatStr(self.ambientHelm, 100)))

            elif "&SPECULAR&" in line:
                povData.append(line.replace("&SPECULAR&", "%s" % self.convertIntToFloatStr(self.specularHelm, 100)))

            elif "&ROUGHNESS&" in line:
                povData.append(line.replace("&ROUGHNESS&", "%s" % self.convertIntToFloatStr(self.roughHelm, 100)))

            elif "&REFLECTION&" in line:
                povData.append(line.replace("&REFLECTION&", "%s" % self.convertIntToFloatStr(self.reflectionHelm, 100)))

            elif "&POSRANKFILE&" in line:
                if self.position not in ["FM", "FL", "CMDR", "WC"] or self.rank not in ["SL", "LT", "LCM", "CM", "CPT", "MAJ", "LC", "COL", "GN"]:
                    povData.append(line.replace("&POSRANKFILE&", "NIL"))
                else:
                    fileName = self.position + "_" + self.rank
                    povData.append(line.replace("&POSRANKFILE&", fileName))

            elif "&DECOCOLOUR&" in line:
                povData.append(line.replace("&DECOCOLOUR&", "%s" % self.convertToPOVRGB(self.decColour)))

            elif "&LOGO1STENCIL&" in line:
                if self.logo1FilepathHelm != "" and self.preview.cb_hemlLogo1Type.currentText() != "Squadron Patch":

                    if self.logo1TypeHelm == "Image - stencil mask":
                        filePath = self.logo1FilepathHelm.replace("\\", "/")
                        ext = filePath.rsplit(".", 1)[1]
                        if ext == "jpg":
                            ext = "jpeg"
                        povData.append(line.replace("&LOGO1STENCIL&", r'%s "%s"' % (ext, filePath)))

                    elif self.logo1TypeHelm == "Image - bg. transparent":
                        self.createMask(self.logo1FilepathHelm)
                        filePath = self.logo1FilepathHelm.replace("\\", "/")
                        # Change file path to mask file.
                        filePath = filePath.rsplit('.', 1)[0] + "_mask.png"
                        povData.append(line.replace("&LOGO1STENCIL&", r'png "%s"' % (filePath)))

                    # None selected.
                    else:
                        povData.append(line.replace("&LOGO1STENCIL&", r'gif "helmet/fallback_mask.gif"'))

                elif self.logo1TypeHelm == "Squadron Patch":
                    self.createMask()
                    ext, filePath = self.findSquadPatch()
                    ext = ext.replace(".", "")
                    filePath = filePath.replace("data\\", "").replace("\\", "/")
                    filePath = filePath.rsplit(".", 1)[0] + "_mask.png"
                    povData.append(line.replace("&LOGO1STENCIL&", r'%s "%s"' % (ext, filePath)))

                # No image selected.
                else:
                    povData.append(line.replace("&LOGO1STENCIL&", r'gif "helmet/fallback_mask.gif"'))

            elif "&LOGO1PIGMENT&" in line:
                if self.logo1FilepathHelm != "" and self.preview.cb_hemlLogo1Type.currentText() != "Squadron Patch":

                    if self.logo1TypeHelm == "Image - stencil mask":
                        povData.append(line.replace("&LOGO1PIGMENT&", "rgb <%s>" % self.convertToPOVRGB(self.decColour)))

                    elif self.logo1TypeHelm == "Image - bg. transparent":
                        filePath = self.logo1FilepathHelm.replace("\\", "/")
                        ext = filePath.rsplit(".", 1)[1]
                        if ext == "jpg":
                            ext = "jpeg"
                        povData.append(line.replace("&LOGO1PIGMENT&", r'image_map { %s "%s" }' % (ext, filePath)))

                    # None selected.
                    else:
                        povData.append(
                            line.replace(
                                "&LOGO1PIGMENT&",
                                r'image_map { png "helmet/fallback.png" interpolate 2 }'))

                elif self.logo1TypeHelm == "Squadron Patch":
                    ext, filePath = self.findSquadPatch()
                    ext = ext.replace(".", "")
                    filePath = filePath.replace("data\\", "").replace("\\", "/")
                    povData.append(line.replace("&LOGO1PIGMENT&", r'image_map { %s "%s" }' % (ext, filePath)))

                # No image selected.
                else:
                    povData.append(
                        line.replace(
                            "&LOGO1PIGMENT&",
                            r'image_map { png "helmet/fallback.png" interpolate 2 }'))

            elif "&LOGO2STENCIL&" in line:
                if self.logo2FilepathHelm != "" and self.preview.cb_hemlLogo2Type.currentText() != "Squadron Patch":

                    if self.logo2TypeHelm == "Image - stencil mask":
                        filePath = self.logo2FilepathHelm.replace("\\", "/")
                        ext = filePath.rsplit(".", 1)[1]
                        if ext == "jpg":
                            ext = "jpeg"
                        povData.append(line.replace("&LOGO2STENCIL&", r'%s "%s"' % (ext, filePath)))

                    elif self.logo2TypeHelm == "Image - bg. transparent":
                        self.createMask(self.logo2FilepathHelm)
                        filePath = self.logo2FilepathHelm.replace("\\", "/")
                        # Change file path to mask file.
                        filePath = filePath.rsplit(".", 1)[0] + "_mask.png"
                        povData.append(line.replace("&LOGO2STENCIL&", r'png "%s"' % (filePath)))

                    # None selected.
                    else:
                        povData.append(line.replace("&LOGO2STENCIL&", r'gif "helmet/fallback_mask.gif"'))

                elif self.logo2TypeHelm == "Squadron Patch":
                    self.createMask()
                    ext, filePath = self.findSquadPatch()
                    ext = ext.replace(".", "")
                    filePath = filePath.replace("data\\", "").replace("\\", "/")
                    filePath = filePath.rsplit(".", 1)[0] + "_mask.png"
                    povData.append(line.replace("&LOGO2STENCIL&", r'%s "%s"' % (ext, filePath)))

                # No image selected.
                else:
                    povData.append(line.replace("&LOGO2STENCIL&", r'gif "helmet/fallback_mask.gif"'))

            elif "&LOGO2PIGMENT&" in line:
                if self.logo2FilepathHelm != "" and self.preview.cb_hemlLogo2Type.currentText() != "Squadron Patch":

                    if self.logo2TypeHelm == "Image - stencil mask":
                        povData.append(line.replace("&LOGO2PIGMENT&", "rgb <%s>" % self.convertToPOVRGB(self.decColour)))

                    elif self.logo2TypeHelm == "Image - bg. transparent":
                        filePath = self.logo2FilepathHelm.replace("\\", "/")
                        ext = filePath.rsplit(".", 1)[1]
                        if ext == "jpg":
                            ext = "jpeg"
                        povData.append(line.replace("&LOGO2PIGMENT&", r'image_map { %s "%s" }' % (ext, filePath)))

                    # None selected.
                    else:
                        povData.append(
                            line.replace(
                                "&LOGO2PIGMENT&",
                                r'image_map { png "helmet/fallback.png" interpolate 2 }'))

                elif self.logo2TypeHelm == "Squadron Patch":
                    ext, filePath = self.findSquadPatch()
                    ext = ext.replace(".", "")
                    filePath = filePath.replace("data\\", "").replace("\\", "/")
                    povData.append(line.replace("&LOGO2PIGMENT&", r'image_map { %s "%s" }' % (ext, filePath)))

                # No image selected.
                else:
                    povData.append(
                        line.replace(
                            "&LOGO2PIGMENT&",
                            r'image_map { png "helmet/fallback.png" interpolate 2 }'))

            elif "&HOMOGENOUS&" in line:
                if self.transparentBGHelm == "":
                    if not self.homoHelm:
                        povData.append(line.replace("&HOMOGENOUS&", "object{ P_plane }"))
                    else:
                        povData.append(line.replace("&HOMOGENOUS&", "object{ P_backdrop }"))
                else:
                    povData.append(line.replace("&HOMOGENOUS&", ""))

            # ----- Non-Editable Data. -----
            else:
                povData.append(line)

        # Write the parsed data to '\data\dress.pov'.
        with open(r"data\helmet.pov", "w") as povFile:
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
        elif ribbonCount > 20 and ribbonCount <= 28:
            return self.RANK_OFFSET_RIBBONS_21_TO_28[0]
        else:
            return self.RANK_OFFSET_RIBBONS_21_TO_28[0]
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
        elif ribbonCount > 20 and ribbonCount <= 28:
            return self.RANK_OFFSET_RIBBONS_21_TO_28[1]
        else:
            return self.RANK_OFFSET_RIBBONS_21_TO_28[1]
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
                    if award == "Medal of Communication (MoC)":
                        break  # Allows for counting of only a sinly MoC award.

            # Ranged and MultiRibbon type awards.
            elif self.awards.get(award)["type"] == "ranged" or self.awards.get(award)["type"] == "multiRibbon":
                if self.awards.get(award)["upgrades"][quantity] > 0:
                    for section in self.ribbonConfig.sections():
                        if self.ribbonConfig.get(section, "name") == award:
                            ribbonCount += 1
        return ribbonCount
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def findSquadPatch(self):
        '''Method that retrieves the squadron patch file for the user's selected squadron.'''

        for ext in [".png", ".jpg"]:
            extension = ext
            fileName = "data\\squads\\{squad}{extension}".format(squad=self.sqn, extension=ext)
            if os.path.isfile(fileName):
                break
        return ext, fileName
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def createMask(self, filepath=None):
        '''Method that will create a mask file for the desired image.'''

        if not filepath:
            extension, fileName = self.findSquadPatch()
        else:
            fileName = filepath
            extension = "." + fileName.rsplit(".", 1)[1]

        try:
            # Primary Mask Creation. Requires a transparent background.
            # Load image with alpha channel.
            img = cv2.imread(fileName, cv2.IMREAD_UNCHANGED)

            # Get mask from alpha channel.
            try:
                mask = img[:, :, 3]
            except TypeError:
                # Show error message.
                msg = "%s does not have a transparent background." % fileName.split("\\")[-1]
                return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

            # Save the mask.
            fileName = fileName.replace(extension, "_mask.png")
            cv2.imwrite(fileName, mask)

        # Bacground likely not transparent. Doesn't need a transparent background but does not work well with high color / shaded patches.
        except IndexError:
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
            fileName = fileName.replace(extension, "_mask.png")
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
                    # Get the ship's ID.
                    for ship in self.fleetConfig.get("ships"):
                        if ship.get("nameShort") == self.ship:
                            shipId = ship.get("id")

                    # Add wings that have the shipId as a parentId.
                    for wing in self.fleetConfig.get("wings"):
                        if wing.get("uniformData").get("parentId") == shipId:
                            self.gui.lw_wing.addItem(wing.get("name"))
                    setLWPixelSizes(self.gui.lw_wing)

                    # If only one Wing exists, select it by default.
                    if self.gui.lw_wing.count() == 1:
                        self.gui.lw_wing.setCurrentRow(0)

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
                    # Get the wing's ID.
                    for wing in self.fleetConfig.get("wings"):
                        if wing.get("name") == self.wing:
                            wingId = wing.get("id")

                    # Add squadrons that have the wingId as a parentId.
                    for squad in self.fleetConfig.get("squadrons"):
                        if squad.get("uniformData").get("parentId") == wingId:
                            self.gui.lw_squad.addItem(squad.get("name"))
                    setLWPixelSizes(self.gui.lw_squad)
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
                for ship in self.fleetConfig.get("ships"):
                    self.gui.lw_ship.addItem(ship.get("nameShort"))
                setLWPixelSizes(self.gui.lw_ship)

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
        setLWPixelSizes(self.gui.lw_medals)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadRibbons(self):
        '''Method that reads in data from 'settings\ribbons.ini' adds the ribbons to the 'Medals, Ribbons and FCHG' tab
           and then dynamically writes ribbons_g.inc ready for use.'''

        ribbons_g = """ ////////////////////////////////////////////////////
//                                                 //
//  TIE Corps Dress Uniform                        //
//  Service Award Ribbons                          //
//                                                 //
//  Settings in this file are generated by TTT     //
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

                # Create the required include declarations for 'ribbons_g.inc'
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
                if self.ribbonConfig.get(ribbon, "type") == "multiRibbon":
                    self.awards[name]["upgrades"] = [name, 0]
                else:
                    self.awards[name]["upgrades"] = []

                for option in self.ribbonConfig.options(ribbon):

                    # Store the ribbon data to the 'self.awards' dictionary.
                    if "type" not in option and "name" not in option.lower():
                        self.awards[name]["upgrades"].append([self.ribbonConfig.get(ribbon, option), 0])

                    # Create the required include declarations for 'ribbons_g.inc'
                    if option != "name" and option != "type":
                        # Add the ribbon to ribbons_g.inc
                        if "upgrade" in option:
                            ribbons_g += self.addToRibbonIncludes(self.getFilename(self.ribbonConfig.get(ribbon, option)))

        setLWPixelSizes(self.gui.lw_medals)

        with open("data\\ribbons_g.inc", "w") as ribbonFile:
            ribbonFile.write(ribbons_g)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def getFilename(self, award):
        '''Method that determines an award's filename from it's abbreviation.'''
        return award.replace("(s)", "").split("(")[1].replace(")", "").lower() + ".gif"
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def addToRibbonIncludes(self, filename):
        '''Method that creates the include data for a single ribbon. This include data goes on to build ribbons_g.inc'''

        ribbonName = filename.replace("-", "_").replace(".gif", "")

        includeTemplate = """#declare T_r_%s =
texture
{
  pigment { image_map { gif "ribbons/%s" } }
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
        self.gui.lbl_multi_left5.hide()
        self.gui.sb_multi_left1.hide()
        self.gui.sb_multi_left2.hide()
        self.gui.sb_multi_left3.hide()
        self.gui.sb_multi_left4.hide()
        self.gui.sb_multi_left5.hide()

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
        self.gui.lbl_multi_right5.hide()
        self.gui.sb_multi_right1.hide()
        self.gui.sb_multi_right2.hide()
        self.gui.sb_multi_right3.hide()
        self.gui.sb_multi_right4.hide()
        self.gui.sb_multi_right5.hide()

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
            self.gui.sb_multi_center2.setRange(0, 999)  # Resets the range if range ribbon/OV was selected.

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
            elif award.get("type") == "multi" or award.get("type") == "multiRibbon":
                self.gui.lbl_multi_center1.setText(award.get("upgrades")[name])
                self.gui.lbl_multi_center1.show()
                self.gui.sb_multi_center1.setValue(award.get("upgrades")[quantity])
                self.gui.sb_multi_center1.show()
                self.gui.sb_multi_center1.valueChanged.connect(self.sb_multi_center1Logic)

                # === Ribbons ===
                # ----- Upgradeable type ribbon awards. (MoI, MoC LoC, LoS, DFC)
            elif award.get("type") == "upgradeable":
                self.gui.cb_singleMedal.setText(item.text())

                for upgrade in award.get("upgrades"):
                    if upgrade[quantity] >= 1:
                        self.gui.cb_singleMedal.setChecked(True)
                        break
                    else:
                        self.gui.cb_singleMedal.setChecked(False)

                if not self.cb_singleMedalConnected:
                    self.gui.cb_singleMedal.stateChanged.connect(self.cb_singleMedalSelectionLogic)
                    self.cb_singleMedalConnected = True

                self.gui.cb_singleMedal.show()
                self.showUpgradeableRadioButtons()

                # ----- SubRibbons type ribbon awards. (MoS, MoT, IS, CoX)
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
                    spinBoxes = [
                        self.gui.sb_multi_left1,
                        self.gui.sb_multi_left2,
                        self.gui.sb_multi_left3,
                        self.gui.sb_multi_left4,
                        self.gui.sb_multi_left5,
                        self.gui.sb_multi_right1,
                        self.gui.sb_multi_right2,
                        self.gui.sb_multi_right3,
                        self.gui.sb_multi_right4,
                        self.gui.sb_multi_right5]
                    spinBoxes = spinBoxes[: subRibbonNum]
                    spinLabels = [
                        self.gui.lbl_multi_left1,
                        self.gui.lbl_multi_left2,
                        self.gui.lbl_multi_left3,
                        self.gui.lbl_multi_left4,
                        self.gui.lbl_multi_left5,
                        self.gui.lbl_multi_right1,
                        self.gui.lbl_multi_right2,
                        self.gui.lbl_multi_right3,
                        self.gui.lbl_multi_right4,
                        self.gui.lbl_multi_right5]
                    spinLabels = spinLabels[: subRibbonNum]
                    spinFunctions = [
                        self.sb_multi_left1Logic,
                        self.sb_multi_left2Logic,
                        self.sb_multi_left3Logic,
                        self.sb_multi_left4Logic,
                        self.sb_multi_left5Logic,
                        self.sb_multi_right1Logic,
                        self.sb_multi_right2Logic,
                        self.sb_multi_right3Logic,
                        self.sb_multi_right4Logic,
                        self.sb_multi_right5Logic]
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

    def checkRibbonCount(self):
        '''Method to ensure that the user has not selected more than the maxiumum number of allowed ribbons (24)'''

        maxRibbons = 28
        objectRefs = self.buildRibbonObjects()

        if len(objectRefs) > maxRibbons:
            self.continueRender = False
            # Show error message.
            self.gui.btn_dress.setEnabled(False)
            self.gui.btn_duty.setEnabled(False)
            if not self.maxedRibbons:
                self.maxedRibbons = True
                msg = "You have selected more than {0} ribbons. Unfortunately TTT3 cannot make a uniform with more than {0} ribbons at this time.\n\n Please select less ribbon awards.".format(
                    str(maxRibbons))
                return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

        else:
            self.maxedRibbons = False

            if self.rank:
                self.gui.btn_dress.setEnabled(True)
                self.gui.btn_duty.setEnabled(True)
            self.maxedRibbons = False
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
                        if upgrade[quantity] >= 1:
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

            # Check to see if the user has selected more than the maximum number of allowed ribbons.
            if award.get("type") != "single" and award.get("type") != "multi":
                self.checkRibbonCount()

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
                if upgrade[quantity] >= 1:
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

            # Check to see if the user has selected more than the maximum number of allowed ribbons.
            self.checkRibbonCount()

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def neckRibbonDeconfliction(self):
        '''Method for handling the display and selection logic for neck ribbon deconfliction.'''

        quantity = 1
        if self.awards.get("Imperial Cross (IC)")["upgrades"][quantity] >= 1 and \
                self.awards.get("Grand Order of the Emperor (GOE)")["upgrades"][quantity] >= 1:

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
                            objRef = self.awards.get(award)["objectRef%s" % obj]

                            # GOE left/right mounting.
                            if objRef == "dagger_left" and self.gui.rb_daggerRight.isChecked():
                                objRef = "dagger_right"

                            # Add the object to our dress.pov file.
                            medalObjects.append(objRef)
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

        # Special handling of awards for >24 ribbons. All ribbon awards are shifted downwards instead of moving the rank upward.
        if self.getRibbonAwardCount() > 24:
            yOffset = -2.5  # Move all ribbons down half a ribbons height.
        else:
            yOffset = 0  # Do not move ribbons up or down.

        for award in self.awards:
            # Upgradeable and SubRibbon type awards.
            if self.awards.get(award)["type"] == "upgradeable" or self.awards.get(award)["type"] == "subRibbons":

                if "Iron Star (IS)" == award or "Medal of Communication (MoC)" == award or \
                   "Medal of Scholarship (MoS)" == award:  # Reverse the ribbon list for certain medals.

                    upgrades = self.awards.get(award)["upgrades"][::-1]

                    if "Iron Star (IS)" == award:  # Re-Sorting of IS-XW and US-XR.
                        half1 = upgrades[0: 5]
                        half2 = upgrades[5:]
                        upgrades = half2 + half1

                    if "Medal of Communication (MoC)" == award:
                        highestMOC = ["name", 0]
                        for upgrade in upgrades[::-1]:
                            if upgrade[1] >= 1:
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
                        awardName = "T_r_" + self.getFilename(upgrade[name]).split(".")[0].lower().replace("-", "_")
                        ribbonObjects.append("P_r&NUM& translate <0,0,%s> texture { %s }" % (yOffset, awardName))

            # Ranged type awards.
            elif self.awards.get(award)["type"] == "ranged":
                if self.awards.get(award)["upgrades"][quantity] > 0:
                    for section in self.ribbonConfig.sections():
                        if self.ribbonConfig.get(section, "name") == award:
                            awardName = "T_r_" + self.ribbonConfig.get(section, "filename").split(".")[0].lower().replace("-", "_")
                            awardName = awardName.replace("&range&", str(self.awards.get(award)["upgrades"][quantity]))
                            ribbonObjects.append("P_r&NUM& translate <0,0,%s> texture { %s }" % (yOffset, awardName))

            # Multi type awards.
            elif self.awards.get(award)["type"] == "multiRibbon":
                if self.awards.get(award)["upgrades"][quantity] > 0:
                    awardName = "T_r_" + self.getFilename(award).split(".")[0].lower().replace("-", "_")
                    ribbonObjects.append("P_r&NUM& translate <0,0,%s> texture { %s }" % (yOffset, awardName))

        return self.ribbonNumberOrdering(ribbonObjects)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def ribbonNumberOrdering(self, ribbons):
        '''Method that arranged the awarded ribbons into the correct order.'''

        ribbonObjects = []
        fullRows = int(len(ribbons) / 4)
        bottomRowNumCount = len(ribbons) % 4
        ribbonCounter = 28 - (fullRows * 4)

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
                    ribbonCounter = 29
                elif bottomRowNumCount == 2:
                    ribbonCounter = 25
                elif bottomRowNumCount == 3:
                    ribbonCounter = 28

                for ribbon in ribbons[-bottomRowNumCount:]:
                    ribbonObjects.append(ribbon.replace("&NUM&", str(ribbonCounter)))
                    ribbonCounter += 1

        # Logic to add the bottom row of ribbons for less than 5 ribbons.
        else:
            if len(ribbons) == 1:
                for ribbon in ribbons:
                    ribbonCounter = 29

            elif len(ribbons) == 2:
                ribbonCounter = 25

            elif len(ribbons) == 3:
                ribbonCounter = 28

            elif len(ribbons) == 4:
                ribbonCounter = 24

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
        spinBoxes = [self.gui.sb_multi_left1, self.gui.sb_multi_left2, self.gui.sb_multi_left3, self.gui.sb_multi_left4, self.gui.sb_multi_left5,
                     self.gui.sb_multi_center1, self.gui.sb_multi_center2, self.gui.sb_multi_center3, self.gui.sb_multi_center4,
                     self.gui.sb_multi_right1, self.gui.sb_multi_right2, self.gui.sb_multi_right3, self.gui.sb_multi_right4, self.gui.sb_multi_right5]

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
            if award.get("type") == "multi" or award.get("type") == "multiRibbon":
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

            # Check to see if the user has selected more than the maximum number of allowed ribbons.
            if award.get("type") != "multi":
                self.checkRibbonCount()

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

    def sb_multi_left5Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(4, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right1Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(5, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right2Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(6, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right3Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(7, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right4Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(8, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_multi_right5Logic(self, value):
        '''Method for handling the Center Bottom spinbox logic.'''

        self.sb_masterLogic(9, value)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_browseRosterFunc(self, event):
        '''Method event for when the 'Browse Fleet Roster' button is clicked on the 'Import' tab.'''

        subprocess.Popen("start " + self.config.get("TCDB", "roster"), shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_searchFunc(self, event):
        '''Method event for when the 'Personnel Search' button is clicked on the 'Import' tab.'''

        subprocess.Popen("start " + self.config.get("TCDB", "search"), shell=True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_newProfMethod(self, event):
        '''Method event for when the 'New Profile' button is clicked.'''

        try:
            self.gui.lw_medals.setCurrentRow(0)  # Required to prevent bug of the user's last upgradeable type selection not showing.

            # PovRay Template variables.
            self.position = None
            self.rank = None
            self.name = "Unknown"
            self.callsign = "None"
            self.nameHelm = "EH TC"
            self.ship = ""
            self.wing = ""
            self.sqn = ""
            self.awards = {}
            self.deconflictNeckRibbons = False
            self.maxedRibbons = False

            # Configuration variables.
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
            # Set default Misc Tab Options.
            if event != "ImportProfile" and event != "OpenProfile":
                # Dress.
                self.gui.cb_dressLightsaber.setChecked(False)
                self.gui.cb_dressSaberStyles.setCurrentIndex(0)
                self.gui.rb_daggerLeft.setChecked(True)
                self.gui.rb_dressSaberRight.setChecked(True)
                # Duty.
                self.gui.cb_dutyLightsaber.setChecked(False)
                self.gui.cb_dutySaberStyles.setCurrentIndex(0)
                self.gui.rb_dutySaberRight.setChecked(True)
                self.gui.cb_dutyBlaster.setChecked(False)
                self.gui.cb_dutyBlasterStyles.setCurrentIndex(0)
                self.gui.rb_blasterLeft.setChecked(True)

            # Disable render buttons.
            self.gui.btn_dress.setEnabled(False)
            self.gui.btn_duty.setEnabled(False)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_openProfMethod(self, event):
        '''Method event for when the 'Open Profile' button is clicked.'''

        try:
            # Reset TTTs data.
            self.btn_newProfMethod("OpenProfile")

            # Load the saved data file.
            fileName = (self.loadUniformFileDialog())
            if fileName:

                with open(fileName, "rb") as dataFile:
                    try:
                        saveData = pickle.load(dataFile)
                    except pickle.UnpicklingError:
                        msg = "%s is not compatible with TTT3.\nPlease save a new profile." % fileName.split("\\")[-1]
                        return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

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
                            if self.position.lower() == radioButton.objectName().replace("rb_pos_", ""):
                                radioButton.setChecked(True)
                                break
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
                            if self.rank.lower() == radioButton.objectName().replace("rb_rank_", ""):
                                radioButton.setChecked(True)
                                break
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

                    # Miscellaneous Tab Options.
                    # Dress.
                    self.gui.cb_dressLightsaber.setChecked(saveData[10])
                    self.gui.cb_dressSaberStyles.setCurrentIndex(saveData[11])
                    if saveData[12]:
                        self.gui.rb_dressSaberRight.setChecked(True)
                    else:
                        self.gui.rb_dressSaberLeft.setChecked(True)
                    if saveData[13]:
                        self.gui.rb_daggerLeft.setChecked(True)
                    else:
                        self.gui.rb_daggerRight.setChecked(True)

                    # Duty.
                    # Lightsaber.
                    self.gui.cb_dutyLightsaber.setChecked(saveData[14])
                    self.gui.cb_dutySaberStyles.setCurrentIndex(saveData[15])
                    if saveData[16]:
                        self.gui.rb_dutySaberRight.setChecked(True)
                    else:
                        self.gui.rb_dutySaberLeft.setChecked(True)

                    # Blaster.
                    self.gui.cb_dutyBlaster.setChecked(saveData[17])
                    self.gui.cb_dutyBlasterStyles.setCurrentIndex(saveData[18])
                    if saveData[19]:
                        self.gui.rb_blasterLeft.setChecked(True)
                    else:
                        self.gui.rb_blasterRight.setChecked(True)

                    # Callsign.
                    self.callsign = saveData[20]

                else:
                    # Show error message.
                    msg = "%s is not compatible with this version of TTT3.\nPlease save a new profile." % fileName.split("\\")[-1]
                    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)

            # Check to see if the user has selected more than the maximum number of allowed ribbons.
            self.checkRibbonCount()

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_saveProfMethod(self, event):
        '''Method event for when the 'Save Profile' button is clicked.'''

        try:
            # Collect the data to be saved into a list.
            saveData = (self.saveFileVersion, self.position, self.rank, self.ship, self.wing, self.gui.cb_eliteSqn.isChecked(),
                        self.sqn, self.awards, self.deconflictNeckRibbons, self.gui.cbFCHG.currentText(), self.gui.cb_dressLightsaber.isChecked(),
                        self.gui.cb_dressSaberStyles.currentIndex(), self.gui.rb_dressSaberRight.isChecked(), self.gui.rb_daggerLeft.isChecked(),
                        self.gui.cb_dutyLightsaber.isChecked(), self.gui.cb_dutySaberStyles.currentIndex(), self.gui.rb_dutySaberRight.isChecked(),
                        self.gui.cb_dutyBlaster.isChecked(), self.gui.cb_dutyBlasterStyles.currentIndex(), self.gui.rb_blasterLeft.isChecked(),
                        self.callsign)

            # Save the data.
            fileName = self.saveUniformFileDialog()
            if fileName:
                with open(fileName, "wb") as saveFile:
                    pickle.dump(saveData, saveFile)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def saveUniformFileDialog(self):
        '''Method that opens a QT File Save dialog to save a uniform.'''

        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            if self.name != "Unknown":
                name = self.name
            else:
                name = "untitled"
            fileName, _ = QFileDialog.getSaveFileName(self, "Save uniform settings", os.getcwd() +
                                                      "\\settings\\%s.ttt" % name, "*.ttt", options=options)
            if fileName:
                if ".ttt" not in fileName:
                    fileName = fileName + ".ttt"
                return fileName

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

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

    def getRetrieveAPIData(self, url, pin):
        '''Method to retrieve TIE Corps Website API returned data and return it as a Python Dictionary.'''

        http = urllib3.PoolManager()
        response = http.request("GET", url + pin)
        data = json.loads(response.data)

        return data
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_importFunc(self):
        '''Method to parse the API data in the form of a Python Dictionary and apply those settings to TTT3.'''

        try:
            # Reset TTTs data.
            self.btn_newProfMethod("ImportProfile")

            # Write to information box.
            self.writeToImportTextBox("Importing uniform data...")

            # Read the data.
            try:
                apiData = self.getRetrieveAPIData(self.config.get("TCDB", "pinapi"), str(self.gui.sbPin.value()))

                if "error" not in apiData.keys():

                    # Name
                    self.name = apiData.get("name")

                    # Callsign
                    self.callsign = apiData.get("callsign")

                    # PIN
                    self.pin = apiData.get("PIN")

                    # Rank.
                    self.rank = apiData.get("rankAbbr")

                    # Position.
                    if apiData.get("position") == "":
                        if self.rank in ["CT", "SL", "LT", "LCM", "CM", "CPT", "MAJ", "LC", "COL", "GN"]:
                            self.position = "LR"
                        else:
                            self.position = "FR"
                    else:
                        self.position = apiData.get("TTT").get("position")

                    # Special handling of FC and XO positions.
                    idLine = apiData.get("IDLine")
                    pos = idLine.split("/")[0]
                    if pos == "FC" or pos == "XO":
                        self.position = pos

                    # Apply the Position setting to the GUI.
                    radioBtns = [self.gui.rb_pos_trn, self.gui.rb_pos_fm, self.gui.rb_pos_fl, self.gui.rb_pos_cmdr,
                                 self.gui.rb_pos_wc, self.gui.rb_pos_com, self.gui.rb_pos_tccs, self.gui.rb_pos_ia,
                                 self.gui.rb_pos_ca, self.gui.rb_pos_sgcom, self.gui.rb_pos_cs, self.gui.rb_pos_xo,
                                 self.gui.rb_pos_fc, self.gui.rb_pos_lr, self.gui.rb_pos_fr]

                    # Apply the Rank setting to the GUI.
                    if self.position:
                        for radioButton in radioBtns:
                            if self.position.lower() == radioButton.objectName().replace("rb_pos_", ""):
                                radioButton.setChecked(True)
                                break
                        self.posRBLogic()
                        self.rank = apiData.get("rankAbbr")  # Added again because self.posRBLogic() sets self.rank to None.

                    radioBtns = [self.gui.rb_rank_ct, self.gui.rb_rank_sl, self.gui.rb_rank_lt, self.gui.rb_rank_lcm,
                                 self.gui.rb_rank_cm, self.gui.rb_rank_cpt, self.gui.rb_rank_maj, self.gui.rb_rank_lc,
                                 self.gui.rb_rank_col, self.gui.rb_rank_gn, self.gui.rb_rank_ra, self.gui.rb_rank_va,
                                 self.gui.rb_rank_ad, self.gui.rb_rank_fa, self.gui.rb_rank_ha, self.gui.rb_rank_sa,
                                 self.gui.rb_rank_ga]

                    if self.rank:
                        for radioButton in radioBtns:
                            if self.rank.lower() == radioButton.objectName().replace("rb_rank_", ""):
                                radioButton.setChecked(True)
                                break
                        self.rankRBLogic()

                    # Ship
                    shipData = apiData.get("ship")
                    if shipData:
                        self.ship = shipData.get("nameShort")
                    else:
                        self.ship = ""

                    # Apply the Ship setting to the GUI.
                    if self.ship:
                        for row in range(self.gui.lw_ship.count()):
                            self.gui.lw_ship.setCurrentRow(row)
                            if self.gui.lw_ship.currentItem().text() == self.ship:
                                break
                        self.shipSelectionLogic(None)

                    # Wing.
                    wingData = apiData.get("wing")
                    if wingData:
                        self.wing = wingData.get("name")
                    else:
                        self.wing = ""

                    # Apply the Wing setting to the GUI.
                    if self.wing:
                        for row in range(self.gui.lw_wing.count()):
                            self.gui.lw_wing.setCurrentRow(row)
                            if self.gui.lw_wing.currentItem().text() == self.wing:
                                break
                        self.wingSelectionLogic(None)

                    # Squadron.
                    sqnData = apiData.get("squadron")
                    if sqnData:
                        self.sqn = sqnData.get("name")
                    else:
                        self.sqn = ""

                    # Apply the Sqn setting to the GUI.
                    if self.sqn:
                        for row in range(self.gui.lw_squad.count()):
                            self.gui.lw_squad.setCurrentRow(row)
                            if self.gui.lw_squad.currentItem().text() == self.sqn:
                                break
                        self.squadSelectionLogic(None)

                    # Medals & Ribbons.
                    apiMedalData = apiData.get("medals")
                    name = 0
                    quantity = 1

                    try:
                        for medal in apiMedalData.keys():
                            for award in self.awards:

                                try:
                                    awardShort = award.split("(")[1].replace(")", "")
                                except IndexError:
                                    awardShort = award
                                medalShort = medal.split("-")[0]

                                if medalShort == awardShort or ("CoX" == awardShort and "Co" in medalShort):

                                    # Single, Multi and Ranged type awards.
                                    if self.awards.get(award)["type"] == "single" or \
                                       self.awards.get(award)["type"] == "multi" or \
                                       self.awards.get(award)["type"] == "multiRibbon" or \
                                       self.awards.get(award)["type"] == "ranged":

                                        self.awards.get(award)["upgrades"][1] = apiMedalData.get(medal)

                                    # Upgradeable and SubRibbons type awards.
                                    elif self.awards.get(award)["type"] == "upgradeable" or \
                                            self.awards.get(award)["type"] == "subRibbons":

                                        for upgrade in self.awards.get(award)["upgrades"]:

                                            try:
                                                upgradeShort = upgrade[name].replace("(s)", "").split("(")[1].replace(")", "")
                                            except IndexError:
                                                upgradeShort = upgrade[name]

                                            if medal == upgradeShort:
                                                index = self.awards.get(award)["upgrades"].index(upgrade)
                                                self.awards.get(award)["upgrades"][index][quantity] = apiMedalData.get(medal)
                    except AttributeError:
                        pass  # User has no medals.

                    # Pilot Wings.
                    self.gui.cbFCHG.setCurrentIndex(apiData.get("TTT").get("pilotWings"))

                    # Write to information box.
                    msg = "Imported uniform data for {label}\nCallsign '{callsign}'\n{idLine}\n\nImport finished.".format(
                        label=apiData.get("label"), callsign=apiData.get("callsign"), idLine=apiData.get("IDLine"))
                    self.writeToImportTextBox(msg)

                    # PIN number saving.
                    self.checkForNewPIN()

                    # Check to see if the user has selected more than the maximum number of allowed ribbons.
                    self.checkRibbonCount()

                else:
                    self.writeToImportTextBox(apiData.get("error")["message"])

            except urllib3.exceptions.MaxRetryError:
                self.writeToImportTextBox("Error! No Internet Connection!")

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def writeToImportTextBox(self, message):
        '''Method that will display text in the 'Import' tab text box.'''

        # self.gui.textEdit.clear()
        self.gui.textEdit.append(message)
        QApplication.processEvents()  # Required to refresh the textbox widget.
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_rememberFunc(self):
        '''Method to remember imported PINS.'''

        try:
            pin = self.name + "#" + str(self.pin) + "\n"
            self.pinData.append(pin)
            self.savePinData()
            self.loadPinData()
            self.gui.btn_remember.hide()

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def savePinData(self):
        '''Method to save imported PINS.'''

        try:
            data = []
            for item in self.pinData:
                if item != "\n" and item != "":
                    data.append(item)

            with open("settings\\pins.dat", "w") as pinFile:
                pinFile.writelines(data)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadPinData(self):
        '''Method to load imported PINS.'''

        try:
            self.gui.lw_presets.clear()

            with open("settings\\pins.dat", "r") as pinFile:
                self.pinData = pinFile.readlines()

            for item in self.pinData:
                if item != "\n":
                    self.gui.lw_presets.addItem(item.split("#")[0])
            setLWPixelSizes(self.gui.lw_presets)

        except FileNotFoundError:
            pass  # No pin.dat file is saved.
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def checkForNewPIN(self):
        '''Method to check if a pin has already been saved..'''

        if self.pinData != []:
            nameFound = False

            for item in self.pinData:
                if self.name in item:
                    nameFound = True

            if not nameFound:
                self.gui.btn_remember.show()
            else:
                self.gui.btn_remember.hide()

        else:
            self.gui.btn_remember.show()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lw_presetsFunc(self):
        '''Method to remember imported PINS.'''

        try:
            for pin in self.pinData:
                if self.gui.lw_presets.currentItem().text() in pin:
                    self.gui.sbPin.setValue(int(pin.split("#")[1]))

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def eventFilter(self, source, event):
        '''Widget context menus.'''

        try:
            if (event.type() == QEvent.ContextMenu and source is self.gui.lw_presets):
                menu = QMenu()
                menu.addAction('delete      Del')
                if menu.exec_(event.globalPos()):
                    item = source.itemAt(event.pos())
                    try:
                        self.deletePreset(item.text())
                    except AttributeError:
                        pass  # User has not clicked on a name.
                return True

            elif (event.type() == QEvent.ContextMenu and source is self.output_gui.lbl_output):
                menu = QMenu()
                saveAs = menu.addAction("Save As")
                openImage = menu.addAction("Open Image")
                close = menu.addAction("Close")
                action = menu.exec_(event.globalPos())
                if action == saveAs:
                    self.btn_saveAsFunc()
                elif action == openImage:
                    self.btn_openFunc()
                elif action == close:
                    self.outputCloseEvent(None)
                return True
            return super(TTT3, self).eventFilter(source, event)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def deletePreset(self, name):
        '''Method to remove a reset stored PIN.'''

        for pin in self.pinData:
            if name in pin:
                self.pinData.pop(self.pinData.index(pin))
        self.savePinData()
        self.loadPinData()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def keyPressEvent(self, event):
        '''Method to detect keyboard input.'''

        try:
            if event.key() == Qt.Key_Escape:
                self.close()

            if event.key() == Qt.Key_Delete:
                if self.gui.tabWidget.tabText(self.gui.tabWidget.currentIndex()) == "Import":
                    try:
                        self.deletePreset(self.gui.lw_presets.currentItem().text())
                    except AttributeError:
                        pass  # User has not clicked on a name.

            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                if self.gui.tabWidget.tabText(self.gui.tabWidget.currentIndex()) == "Import":
                    self.btn_importFunc()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadLighsabers(self):
        '''Method to detect and load the number of lightsaber styles within the data folder.'''

        # Detect installed saber styles and add them to the GUI.
        for root, dirs, files in os.walk(os.getcwd() + "\\data\\", topdown=False):
            for name in files:
                if "saber" in name and "_g.inc" in name:
                    # Read in the name of the Lightsaber by locating it's '// DESCRIPTION' reference.
                    # If no '// DESCRIPTION' is provided. Use the filename instead.
                    with open(os.getcwd() + "\\data\\" + name, "r") as saberFile:
                        descriptionFound = False
                        for line in saberFile.readlines():
                            if "// DESCRIPTION" in line:
                                descriptionFound = True
                                break

                        # Add the saber to the GUI and store it's name and filepath into self.saberDict.
                        if descriptionFound:
                            style = line.replace("// DESCRIPTION ", "").replace("\n", "")
                            self.saberDict[style] = name
                        else:
                            style = name.replace("_g.inc", "")
                            self.saberDict[style] = name

                        self.gui.cb_dressSaberStyles.addItem(style)
                        self.gui.cb_dutySaberStyles.addItem(style)

        # Prepare the GUI for initial use.
        self.gui.rb_dressSaberRight.setChecked(True)
        self.gui.rb_dutySaberRight.setChecked(True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_dressLightsaberFunc(self):
        '''Method that triggers when the 'Use Lightsaber' checkbox is selected'''

        try:
            saberItems = [self.gui.cb_dressSaberStyles, self.gui.lbl_dressSaberSide, self.gui.rb_dressSaberLeft,
                          self.gui.rb_dressSaberRight, self.gui.btn_dressSaberCustom]

            for item in saberItems:
                if self.gui.cb_dressLightsaber.isChecked():
                    item.show()
                else:
                    item.hide()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_dutyLightsaberFunc(self):
        '''Method that triggers when the 'Use Lightsaber' checkbox is selected'''

        try:
            saberItems = [self.gui.cb_dutySaberStyles, self.gui.lbl_dutySaberSide, self.gui.rb_dutySaberLeft,
                          self.gui.rb_dutySaberRight, self.gui.btn_dutySaberCustom]

            for item in saberItems:
                if self.gui.cb_dutyLightsaber.isChecked():
                    item.show()
                else:
                    item.hide()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lightsaberDressSelectedFunc(self):
        '''Method that synchronises the duty saber with the dress saber when a lightsaber is selected from the dress combo box'''

        try:
            self.gui.cb_dutySaberStyles.currentIndexChanged.disconnect(self.lightsaberDutySelectedFunc)
            self.gui.cb_dutySaberStyles.setCurrentIndex(self.gui.cb_dressSaberStyles.currentIndex())
            self.gui.cb_dutySaberStyles.currentIndexChanged.connect(self.lightsaberDutySelectedFunc)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lightsaberDutySelectedFunc(self):
        '''Method that synchronises the dress saber with the duty saber when a lightsaber is selected from the duty combo box'''

        try:
            self.gui.cb_dressSaberStyles.currentIndexChanged.disconnect(self.lightsaberDressSelectedFunc)
            self.gui.cb_dressSaberStyles.setCurrentIndex(self.gui.cb_dutySaberStyles.currentIndex())
            self.gui.cb_dressSaberStyles.currentIndexChanged.connect(self.lightsaberDressSelectedFunc)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def saberDaggerDeconflict(self):
        '''Method to deconflict the lightsaber and dagger if a saber mounting option is selected.'''

        try:
            if self.gui.rb_dressSaberLeft.isChecked():
                self.gui.rb_dutySaberLeft.setChecked(True)
                self.gui.rb_daggerRight.setChecked(True)
                self.gui.rb_blasterRight.setChecked(True)
            else:
                self.gui.rb_dutySaberRight.setChecked(True)
                self.gui.rb_daggerLeft.setChecked(True)
                self.gui.rb_blasterLeft.setChecked(True)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def daggerSaberDeconflict(self):
        '''Method to deconflict the dagger and lightsaber if a dagger mounting option is selected.'''

        try:
            if self.gui.rb_daggerLeft.isChecked():
                self.gui.rb_blasterLeft.setChecked(True)
                self.gui.rb_dressSaberRight.setChecked(True)
                self.gui.rb_dutySaberRight.setChecked(True)
            else:
                self.gui.rb_blasterRight.setChecked(True)
                self.gui.rb_dressSaberLeft.setChecked(True)
                self.gui.rb_dutySaberLeft.setChecked(True)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadBlasters(self):
        '''Method to detect and load the number of blaster styles within the data folder.'''

        # Detect installed blaster styles and add them to the GUI.
        for root, dirs, files in os.walk(os.getcwd() + "\\data\\", topdown=False):
            for name in files:
                if "blaster" in name and "_g.inc" in name:
                    # Read in the name of the Blaster by locating it's '// DESCRIPTION' reference.
                    # If no '// DESCRIPTION' is provided. Use the filename instead.
                    with open(os.getcwd() + "\\data\\" + name, "r") as blasterFile:
                        descriptionFound = False
                        for line in blasterFile.readlines():
                            if "// DESCRIPTION" in line:
                                descriptionFound = True
                                break

                        # Add the blaster to the GUI and store it's name and filepath into self.blasterDict.
                        if descriptionFound:
                            style = line.replace("// DESCRIPTION ", "").replace("\n", "")
                            self.blasterDict[style] = name
                        else:
                            style = name.replace("_g.inc", "")
                            self.blasterDict[style] = name

                        self.gui.cb_dutyBlasterStyles.addItem(style)

        # Prepare the GUI for initial use.
        self.gui.rb_blasterLeft.setChecked(True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_dutyBlasterFunc(self):
        '''Method that triggers when the 'Use sidearm' checkbox is selected.'''

        try:
            blasterItems = [self.gui.cb_dutyBlasterStyles, self.gui.lbl_blasterSide, self.gui.rb_blasterLeft, self.gui.rb_blasterRight]

            for item in blasterItems:
                if self.gui.cb_dutyBlaster.isChecked():
                    item.show()
                else:
                    item.hide()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def blasterSaberDeconflict(self):
        '''Method to deconflict the blaster and lightsaber if a blaster mounting option is selected.'''

        try:
            if self.gui.rb_blasterLeft.isChecked():
                self.gui.rb_daggerLeft.setChecked(True)
                self.gui.rb_dutySaberRight.setChecked(True)
                self.gui.rb_dressSaberRight.setChecked(True)
            else:
                self.gui.rb_daggerRight.setChecked(True)
                self.gui.rb_dutySaberLeft.setChecked(True)
                self.gui.rb_dressSaberLeft.setChecked(True)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def saberBlasterDeconflict(self):
        '''Method to deconflict the lightsaber and blaster if a saber mounting option is selected.'''

        try:
            if self.gui.rb_dutySaberLeft.isChecked():
                self.gui.rb_dressSaberLeft.setChecked(True)
                self.gui.rb_blasterRight.setChecked(True)
                self.gui.rb_daggerRight.setChecked(True)
            else:
                self.gui.rb_dressSaberRight.setChecked(True)
                self.gui.rb_blasterLeft.setChecked(True)
                self.gui.rb_daggerLeft.setChecked(True)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def checkForUpdates(self):
        '''Method for checking for online updates for TTT.'''

        # Fleet data updates.
        try:
            self.updateMsg = ""
            apiFleetData = self.getRetrieveAPIData(self.config.get("TCDB", "fleetapi"), "")

            if "error" in apiFleetData.keys():
                self.updateProgressBar.emit("code400", 0)
                self.updateMsg += "Checking for updates failed.\nInvalid connection to emperorshammer.org or bad 'fleetapi' TTT3.ini setting.\n"
                self.updateProgressBar.emit("message", None)

            else:
                # Update the locally stored fleet.json file and load the downloaded settings.
                self.updateMsg += "Successful connection to emperorshammer.org...\n"
                if self.fleetConfig != apiFleetData:
                    with open(os.getcwd() + "\\settings\\fleet.json", "w") as fleetDataFile:
                        fleetDataFile.write(json.dumps(apiFleetData))
                    self.loadFleetData()
                    self.updateMsg += "New TIE Corps fleet structure successfully downloaded.\n"
                else:
                    self.updateMsg += "TIE Corps fleet structure already up to date.\n"

                # Squadron Patch checks.
                dbSqnList = []
                self.updateProgressBar.emit("init", len(self.fleetConfig.get("squadrons")))

                for squadron in self.fleetConfig.get("squadrons"):
                    dbSqnName = squadron.get("name")
                    dbSqnList.append(dbSqnName)
                    dbPatchURL = squadron.get("uniformData").get("patchURL")
                    dbPatchHash = squadron.get("uniformData").get("patchHash")
                    self.updateProgressBar.emit(dbSqnName, 0)

                    for root, dirs, files in os.walk(os.getcwd() + "\\data\\squads\\", topdown=False):

                        # Search for patch files that TTT3 doesn't currently have locally at all.
                        squadFound = False

                        for name in files:
                            # Filter for missing squadrons.
                            if dbSqnName in name:
                                squadFound = True

                                # Delete squad patch masks.
                                if "_mask" in name:
                                    os.remove(os.getcwd() + "\\data\\squads\\" + name)

                                else:
                                    # Check if exisiting files are up to date using MD5 hashes and if not download new versions.
                                    hash = getHash(os.getcwd() + "\\data\\squads\\" + name)
                                    if hash != dbPatchHash:
                                        self.updateProgressBar.emit("show", 0)
                                        self.downloadPatchFile(dbSqnName, dbPatchURL)
                                        self.updateMsg += "Downloaded updated squadron patch for %s squadron.\n" % dbSqnName
                                        break

                        # Download missing patches.
                        if not squadFound:
                            self.updateProgressBar.emit("show", 0)
                            self.downloadPatchFile(dbSqnName, dbPatchURL)
                            self.updateMsg += "Downloaded new squadron patch for %s squadron.\n" % dbSqnName

                # Remove redundant patch files that are no longer in use.
                for root, dirs, files in os.walk(os.getcwd() + "\\data\\squads\\", topdown=False):
                    for name in files:
                        sqnFound = False
                        for squadron in dbSqnList:
                            if squadron == name.split(".")[0]:
                                sqnFound = True
                        if not sqnFound:
                            os.remove(os.getcwd() + "\\data\\squads\\" + name)
                self.updateProgressBar.emit("complete", 0)
                self.updateProgressBar.emit("message", None)

        except urllib3.exceptions.MaxRetryError:
            self.updateProgressBar.emit("error", 0)
            self.updateMsg += "Checking for updates failed.\nNo internet connection.\n"
            self.updateProgressBar.emit("message", None)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def downloadPatchFile(self, name, url):
        '''Method for downloading squadron patches.'''

        try:
            # Remove duplicate file types.
            for ext in [".png", ".jpg", ".jpeg", ".gif", ".bmp"]:
                try:
                    os.remove(os.getcwd() + "\\data\\squads\\" + name + ext)
                except FileNotFoundError:
                    pass

            # Download new patch.
            http = urllib3.PoolManager()
            response = http.request("GET", url)

            # Detect the file extension.
            fileType = response.headers.get("Content-Type")
            if "png" in fileType:
                ext = ".png"
            elif "jpeg" in fileType:
                ext = ".jpg"
            elif "gif" in fileType:
                ext = ".gif"
            else:
                ext = ""

            # Save the new file.
            filePath = os.getcwd() + "\\data\\squads\\" + name.title() + ext

            with open(filePath, "wb") as imgFile:
                imgFile.write(response.data)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def updaterSlot(self, type, value):
        '''PyQt Slot for updating the progress bar from an external thread.'''

        try:
            if type == "init":
                self.gui.pb_update.setMaximum(value)

            elif type == "show":
                self.gui.pb_update.show()
                self.gui.lbl_update.show()

            elif type == "complete":
                self.gui.pb_update.hide()
                self.gui.lbl_update.hide()

            elif type == "error":
                self.gui.lbl_update.setText("Squadron Patch Update Error! No Internet Connection!")
                self.gui.pb_update.setStyleSheet(r"background-color: rgb(170, 0, 0);border-color: rgb(170, 0, 0);text-align: right;")
                self.gui.pb_update.show()
                self.gui.lbl_update.show()

            elif type == "code400":
                self.gui.lbl_update.setText("Squadron Patch Update Error! Invalid Fleet API setting!")
                self.gui.pb_update.setStyleSheet(r"background-color: rgb(170, 0, 0);border-color: rgb(170, 0, 0);text-align: right;")
                self.gui.pb_update.show()
                self.gui.lbl_update.show()

            elif type == "message":
                self.writeToImportTextBox(self.updateMsg)

            else:
                self.gui.lbl_update.setText("Downloading patch data for %s squadron..." % type)
                self.gui.pb_update.setValue(int(self.gui.pb_update.value()) + 1)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_PaletteSpotFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            self.openColourPicker(self.spotColour, "spotColour", self.preview.lbl_PaletteSpot, self.preview.le_PaletteSpot)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_PaletteEnvFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            self.openColourPicker(self.envColour, "envColour", self.preview.lbl_PaletteEnv, self.preview.le_PaletteEnv)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_PaletteBackFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            if self.uniform != "helmet":
                self.openColourPicker(self.bgColour, "bgColour", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
            else:
                self.openColourPicker(self.bgColourHelm, "bgColourHelm", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def openColourPicker(self, colourOption, optionStr, label, lineEdit):
        '''Method to open the QColorDialog.'''

        try:
            # Prevent auto-refresh from spamming changes to the render que when picking a colour.
            oldColourOption = colourOption
            oldRefreshSetting = self.preview.cb_Refresh.isChecked()
            self.preview.cb_Refresh.setChecked(False)

            # Open the colour picker.
            self.colourDlg = QColorDialog()
            self.colourDlg.setCurrentColor(colourOption)
            self.colourDlg.show()
            # Connections.
            self.colourDlg.accepted.connect(lambda: self.colourSelected(self.colourDlg.currentColor(), optionStr, label, lineEdit))
            self.colourDlg.rejected.connect(lambda: self.cancelColourPicker(oldColourOption, optionStr, label, lineEdit))
            self.colourDlg.finished.connect(lambda: self.closeColourPicker(oldRefreshSetting))
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def closeColourPicker(self, setting):
        '''Method for closing the colour picker.'''

        self.preview.cb_Refresh.setChecked(setting)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cancelColourPicker(self, oldColourOption, optionStr, label, lineEdit):
        '''Method for closing the colour picker.'''

        self.colourSelected(oldColourOption, optionStr, label, lineEdit)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def colourSelected(self, colour, optionStr, label, lineEdit):
        '''Method for handling colour selection from within the ColourPicker.'''

        # Set the class member.
        setattr(self, optionStr, colour)

        # Conver values.
        realRGB = getattr(self, optionStr).getRgb()
        hexRGB = "#%02x%02x%02x" % (realRGB[0], realRGB[1], realRGB[2])

        # Apply values to GUI.
        label.setStyleSheet("background-color: rgb(%s, %s, %s);" % (realRGB[0], realRGB[1], realRGB[2]))
        lineEdit.setText(hexRGB)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def convertToPOVRGB(self, colour):
        '''Method to convert a QColor RGB item into a POV-Ray RGB Item.'''

        colourPov = []
        for col in colour.getRgb()[:3]:
            colourPov.append(col / 255.0)
        colourPov = str(tuple(colourPov)).replace("(", "").replace(")", "")
        return colourPov
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewResetColoursFunc(self):
        '''Method for reseting the preview window colour options.'''

        try:
            if self.uniform != "helmet":
                self.spotColour = QColor(255, 255, 255)
                self.envColour = QColor(128, 118, 108)
                self.bgColour = QColor(0, 0, 0)
                # Spotlight Colour.
                self.colourSelected(self.spotColour, "spotColour", self.preview.lbl_PaletteSpot, self.preview.le_PaletteSpot)
                # Environment Colour.
                self.colourSelected(self.envColour, "envColour", self.preview.lbl_PaletteEnv, self.preview.le_PaletteEnv)
                # Background Colour.
                self.colourSelected(self.bgColour, "bgColour", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
                self.transparentBG = ""
                self.preview.cb_TransparentBG.setChecked(False)
            else:
                self.helmColour = QColor(33, 33, 33)
                self.bgColourHelm = QColor(69, 79, 112)
                self.decColour = QColor(147, 147, 147)
                self.lightColour = QColor(255, 255, 255)
                # Helmet Colour.
                self.colourSelected(self.helmColour, "helmColour", self.preview.lbl_PaletteHelm, self.preview.le_PaletteHelm)
                # Decoration Colour.
                self.colourSelected(self.decColour, "decColour", self.preview.lbl_PaletteDec, self.preview.le_PaletteDec)
                # Background Colour.
                self.colourSelected(self.bgColourHelm, "bgColourHelm", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
                # Light Colour.
                self.colourSelected(self.lightColour, "lightColour", self.preview.lbl_PaletteLight, self.preview.le_PaletteLight)
                self.transparentBGHelm = ""
                self.preview.cb_TransparentBG.setChecked(False)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_previewWidthFunc(self, value=None):
        '''Method for handling user input to the preview GUI width spin box.'''

        try:
            if self.uniform != "helmet":
                self.width = value
                self.height = getY(self.width)
                self.preview.le_Height.setText(str(self.height))
            else:
                self.widthHelm = value
                self.heightHelm = getYHelm(self.widthHelm)
                self.preview.le_Height.setText(str(self.heightHelm))
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewResetOptionsFunc(self):
        '''Method for reseting the preview window options.'''

        try:
            if self.uniform != "helmet":
                self.width = 640
                self.preview.sb_Width.setValue(self.width)
                self.sb_previewWidthFunc(self.width)
                self.quality = 9
                self.preview.sb_Quality.setValue(self.quality)
                self.clothDetail = 0
                self.preview.cb_Detail.setCurrentIndex(self.clothDetail)
                self.antiAliasing = True
                self.preview.cb_AA.setChecked(self.antiAliasing)
                self.shadowless = False
                self.preview.cb_Shadowless.setChecked(self.shadowless)
                self.mosaicPreview = False
                self.preview.cb_Mosaic.setChecked(self.mosaicPreview)
            else:
                self.widthHelm = 640
                self.preview.sb_Width.setValue(self.widthHelm)
                self.sb_previewWidthFunc(self.widthHelm)
                self.qualityHelm = 7
                self.preview.sb_Quality.setValue(self.qualityHelm)
                self.antiAliasingHelm = True
                self.preview.cb_AA.setChecked(self.antiAliasingHelm)
                self.shadowlessHelm = False
                self.preview.cb_Shadowless.setChecked(self.shadowlessHelm)
                self.homoHelm = False
                self.preview.cb_Homo.setChecked(self.homoHelm)
                self.mosaicPreviewHelm = False
                self.preview.cb_Mosaic.setChecked(self.mosaicPreviewHelm)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sb_previewQualityFunc(self, value):
        '''Method for applying the quality setting within the preview window.'''

        if self.uniform != "helmet":
            self.quality = value
        else:
            self.qualityHelm = value
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewDetailFunc(self, value):
        '''Method for applying the cloth detail setting within the preview window.'''

        self.clothDetail = value
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewAAFunc(self, value):
        '''Method for applying the anti aliasing setting within the preview window.'''

        if self.uniform != "helmet":
            if value == 2:
                self.antiAliasing = True
            else:
                self.antiAliasing = False
        else:
            if value == 2:
                self.antiAliasingHelm = True
            else:
                self.antiAliasingHelm = False
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewShadowlessFunc(self, value):
        '''Method for applying the shadowless setting within the preview window.'''

        if self.uniform != "helmet":
            if value == 2:
                self.shadowless = True
            else:
                self.shadowless = False
        else:
            if value == 2:
                self.shadowlessHelm = True
            else:
                self.shadowlessHelm = False
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewMosaicFunc(self, value):
        '''Method for applying the mosaic preview mode setting within the preview window.'''

        if self.uniform != "helmet":
            if value == 2:
                self.mosaicPreview = True
            else:
                self.mosaicPreview = False
        else:
            if value == 2:
                self.mosaicPreviewHelm = True
            else:
                self.mosaicPreviewHelm = False
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewHomoFunc(self, value):
        '''Method for applying the mosaic preview mode setting within the preview window.'''

        if value == 2:
            self.homoHelm = True
        else:
            self.homoHelm = False
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewTransparentFunc(self, value):
        '''Method for applying the transparent background setting setting within the preview window.'''

        try:
            bgWidgets = [self.preview.lbl_Back, self.preview.lbl_PaletteBack, self.preview.le_PaletteBack, self.preview.btn_PaletteBack]

            if value == 2:
                if self.uniform != "helmet":
                    self.transparentBG = " +UA"
                else:
                    self.transparentBGHelm = " +UA"
                    self.preview.lbl_PaletteBack.setStyleSheet("background-color: rgb(211, 211, 211);")
                    self.preview.cb_Homo.setEnabled(False)
                for widget in bgWidgets:
                    widget.setEnabled(False)

            else:
                if self.uniform != "helmet":
                    self.transparentBG = ""
                    self.colourSelected(self.bgColour, "bgColour", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
                else:
                    self.transparentBGHelm = ""
                    self.colourSelected(self.bgColourHelm, "bgColourHelm", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
                    self.preview.cb_Homo.setEnabled(True)
                for widget in bgWidgets:
                    widget.setEnabled(True)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewCamXFunc(self, value):
        '''Method for applying the camera angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.camX = value
            self.preview.lbl_CamX.setText(self.convertIntToFloatStr(value, 10))
        else:
            self.camXHelm = value
            self.preview.lbl_CamX.setText(self.convertIntToFloatStr(value, 100))

        self.preview.cb_PresetCam.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewCamYFunc(self, value):
        '''Method for applying the camera angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.camY = value
            self.preview.lbl_CamY.setText(self.convertIntToFloatStr(value, 10))
        else:
            self.camYHelm = value
            self.preview.lbl_CamY.setText(self.convertIntToFloatStr(value, 100))

        self.preview.cb_PresetCam.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewCamZFunc(self, value):
        '''Method for applying the camera angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.camZ = value
            self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(value, 10))
        else:
            self.camZHelm = value
            self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(value, 100))

        self.preview.cb_PresetCam.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewLookXFunc(self, value):
        '''Method for applying the look at angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.lookX = value
            self.preview.lbl_LookX.setText(self.convertIntToFloatStr(value, 10))
        else:
            self.lookXHelm = value
            self.preview.lbl_LookX.setText(self.convertIntToFloatStr(value, 100))

        self.preview.cb_PresetLook.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewLookYFunc(self, value):
        '''Method for applying the look at angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.lookY = value
            self.preview.lbl_LookY.setText(self.convertIntToFloatStr(value, 10))
        else:
            self.lookYHelm = value
            self.preview.lbl_LookY.setText(self.convertIntToFloatStr(value, 100))

        self.preview.cb_PresetLook.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewLookZFunc(self, value):
        '''Method for applying the look at angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.lookZ = value
            self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(value, 10))
        else:
            self.lookZHelm = value
            self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(value, 100))

        self.preview.cb_PresetLook.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewResetCameraFunc(self):
        '''Method for reseting the preview window camera.'''

        try:
            if self.uniform != "helmet":
                self.camX = -2500
                self.preview.vs_CamX.setValue(self.camX)
                self.preview.lbl_CamX.setText(self.convertIntToFloatStr(self.camX, 10))
                self.camY = -13300
                self.preview.vs_CamY.setValue(self.camY)
                self.preview.lbl_CamY.setText(self.convertIntToFloatStr(self.camY, 10))
                self.camZ = 2100
                self.preview.vs_CamZ.setValue(self.camZ)
                self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(self.camZ, 10))
                self.lookX = 0
                self.preview.vs_LookX.setValue(self.lookX)
                self.preview.lbl_LookX.setText(self.convertIntToFloatStr(self.lookX, 10))
                self.lookY = -128
                self.preview.vs_LookY.setValue(self.lookY)
                self.preview.lbl_LookY.setText(self.convertIntToFloatStr(self.lookY, 10))
                self.lookZ = 28
                self.preview.vs_LookZ.setValue(self.lookZ)
                self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(self.lookZ, 10))
            else:
                self.camXHelm = 2170
                self.preview.vs_CamX.setValue(self.camXHelm)
                self.preview.lbl_CamX.setText(self.convertIntToFloatStr(self.camXHelm, 100))
                self.camYHelm = -6510
                self.preview.vs_CamY.setValue(self.camYHelm)
                self.preview.lbl_CamY.setText(self.convertIntToFloatStr(self.camYHelm, 100))
                self.camZHelm = 3146
                self.preview.vs_CamZ.setValue(self.camZHelm)
                self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(self.camZHelm, 100))
                self.lookXHelm = -568
                self.preview.vs_LookX.setValue(self.lookXHelm)
                self.preview.lbl_LookX.setText(self.convertIntToFloatStr(self.lookXHelm, 100))
                self.lookYHelm = -445
                self.preview.vs_LookY.setValue(self.lookYHelm)
                self.preview.lbl_LookY.setText(self.convertIntToFloatStr(self.lookYHelm, 100))
                self.lookZHelm = 1052
                self.preview.vs_LookZ.setValue(self.lookZHelm)
                self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(self.lookZHelm, 100))

            self.preview.cb_PresetCam.setCurrentIndex(0)
            self.preview.cb_PresetLook.setCurrentIndex(0)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewLightXFunc(self, value):
        '''Method for applying the light angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.lightX = value
            self.preview.lbl_LightX.setText(self.convertIntToFloatStr(value, 10))
            self.preview.cb_PresetLight.setCurrentIndex(11)
        else:
            self.lightXHelm = value
            self.preview.lbl_LightX.setText(self.convertIntToFloatStr(value, 100))
            self.preview.cb_PresetLight.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewLightYFunc(self, value):
        '''Method for applying the light angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.lightY = value
            self.preview.lbl_LightY.setText(self.convertIntToFloatStr(value, 10))
            self.preview.cb_PresetLight.setCurrentIndex(11)
        else:
            self.lightYHelm = value
            self.preview.lbl_LightY.setText(self.convertIntToFloatStr(value, 100))
            self.preview.cb_PresetLight.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewLightZFunc(self, value):
        '''Method for applying the light angle setting within the preview window.'''

        if self.uniform != "helmet":
            self.lightZ = value
            self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(value, 10))
            self.preview.cb_PresetLight.setCurrentIndex(11)
        else:
            self.lightZHelm = value
            self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(value, 100))
            self.preview.cb_PresetLight.setCurrentIndex(10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewResetLightFunc(self):
        '''Method for reseting the preview window light source.'''

        try:
            if self.uniform != "helmet":
                self.lightX = 13000
                self.preview.vs_LightX.setValue(self.lightX)
                self.preview.lbl_LightX.setText(self.convertIntToFloatStr(self.lightX, 10))
                self.lightY = -15000
                self.preview.vs_LightY.setValue(self.lightY)
                self.preview.lbl_LightY.setText(self.convertIntToFloatStr(self.lightY, 10))
                self.lightZ = 13000
                self.preview.vs_LightZ.setValue(self.lightZ)
                self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(self.lightZ, 10))
            else:
                self.lightXHelm = 2244
                self.preview.vs_LightX.setValue(self.lightXHelm)
                self.preview.lbl_LightX.setText(self.convertIntToFloatStr(self.lightXHelm, 100))
                self.lightYHelm = -5089
                self.preview.vs_LightY.setValue(self.lightYHelm)
                self.preview.lbl_LightY.setText(self.convertIntToFloatStr(self.lightYHelm, 100))
                self.lightZHelm = 5282
                self.preview.vs_LightZ.setValue(self.lightZHelm)
                self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(self.lightZHelm, 100))

            self.preview.cb_PresetLight.setCurrentIndex(0)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewResetFunc(self):
        '''Method to reset all preview window options / profile.'''

        try:
            if self.uniform != "helmet":
                self.btn_previewResetColoursFunc()
                self.btn_previewResetCameraFunc()
                self.btn_previewResetOptionsFunc()
                self.btn_previewResetLightFunc()
                self.renderPreview()
            else:
                self.btn_previewResetColoursFunc()
                self.btn_previewResetSurfPropsFunc()
                self.btn_previewResetCameraFunc()
                self.btn_previewResetLightFunc()
                self.btn_previewResetDecsFunc()
                self.btn_previewResetOptionsFunc()
                self.renderPreview()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def getUniformData(self):
        '''Method that collects all of the user's selections and returns them as a tuple.'''

        if self.uniform != "helmet":
            # Collect the data to be saved into a list.
            saveData = (self.spotColour, self.envColour, self.bgColour, self.transparentBG, self.camX, self.camY, self.camZ,
                        self.lookX, self.lookY, self.lookZ, self.width, self.height, self.quality, self.clothDetail, self.antiAliasing,
                        self.shadowless, self.mosaicPreview, self.lightX, self.lightY, self.lightZ)

        else:
            saveData = (self.helmColour, self.decColour, self.bgColourHelm, self.lightColour, self.transparentBGHelm, self.ambientHelm,
                        self.specularHelm, self.roughHelm, self.reflectionHelm, self.camXHelm, self.camYHelm, self.camZHelm,
                        self.lookXHelm, self.lookYHelm, self.lookZHelm, self.lightXHelm, self.lightYHelm, self.lightZHelm,
                        self.fontHelmQFront.family(), self.nameHelm, self.logo1FilepathHelm, self.logo1TypeHelm,
                        self.logo2FilepathHelm, self.logo2TypeHelm, self.mosaicPreviewHelm, self.homoHelm, self.shadowlessHelm,
                        self.antiAliasingHelm, self.qualityHelm, self.widthHelm, self.heightHelm, self.rank, self.position, self.sqn)

        return saveData
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewSaveFunc(self):
        '''Method for when the preview 'Save' button is clicked.'''

        try:
            saveData = self.getUniformData()

            # Save the data.
            fileName = self.savePreviewFileDialog()
            if fileName:
                with open(fileName, "wb") as saveFile:
                    pickle.dump(saveData, saveFile)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def savePreviewFileDialog(self):
        '''Method that opens a QT File Save dialog to save a preview profile.'''

        try:
            if self.uniform != "helmet":
                ext = ".pro"
            else:
                ext = ".helm"

            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            if self.name != "Unknown":
                name = self.name + " " + self.uniform.title()
            else:
                name = "untitled " + self.uniform.title()
            fileName, _ = QFileDialog.getSaveFileName(self, "Save render settings", os.getcwd() +
                                                      "\\settings\\%s%s" % (name, ext), "*%s" % ext, options=options)
            if fileName:
                if ext not in fileName:
                    fileName = fileName + ext
                return fileName

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewLoadFunc(self):
        '''Method for when the preview 'Load' button is clicked.'''

        try:
            # Load the saved data file.
            fileName = (self.loadPreviewFileDialog())
            if fileName:

                with open(fileName, "rb") as dataFile:
                    saveData = pickle.load(dataFile)

                if self.uniform != "helmet":
                    # Apply the loaded settings.
                    self.spotColour = saveData[0]
                    self.envColour = saveData[1]
                    self.bgColour = saveData[2]
                    self.transparentBG = saveData[3]
                    self.camX = saveData[4]
                    self.camY = saveData[5]
                    self.camZ = saveData[6]
                    self.lookX = saveData[7]
                    self.lookY = saveData[8]
                    self.lookZ = saveData[9]
                    self.width = saveData[10]
                    self.height = saveData[11]
                    self.quality = saveData[12]
                    self.clothDetail = saveData[13]
                    self.antiAliasing = saveData[14]
                    self.shadowless = saveData[15]
                    self.mosaicPreview = saveData[16]
                    self.lightX = saveData[17]
                    self.lightY = saveData[18]
                    self.lightZ = saveData[19]

                else:
                    self.helmColour = saveData[0]
                    self.decColour = saveData[1]
                    self.bgColourHelm = saveData[2]
                    self.lightColour = saveData[3]
                    self.transparentBGHelm = saveData[4]
                    self.ambientHelm = saveData[5]
                    self.specularHelm = saveData[6]
                    self.roughHelm = saveData[7]
                    self.reflectionHelm = saveData[8]
                    self.camXHelm = saveData[9]
                    self.camYHelm = saveData[10]
                    self.camZHelm = saveData[11]
                    self.lookXHelm = saveData[12]
                    self.lookYHelm = saveData[13]
                    self.lookZHelm = saveData[14]
                    self.lightXHelm = saveData[15]
                    self.lightYHelm = saveData[16]
                    self.lightZHelm = saveData[17]
                    self.fontHelmQFront = QFont(saveData[18])
                    self.nameHelm = saveData[19]
                    self.logo1FilepathHelm = saveData[20]
                    self.logo1TypeHelm = saveData[21]
                    self.logo2FilepathHelm = saveData[22]
                    self.logo2TypeHelm = saveData[23]
                    self.mosaicPreviewHelm = saveData[24]
                    self.homoHelm = saveData[25]
                    self.shadowlessHelm = saveData[26]
                    self.antiAliasingHelm = saveData[27]
                    self.qualityHelm = saveData[28]
                    self.widthHelm = saveData[29]
                    self.heightHelm = saveData[30]
                    self.rank = saveData[31]
                    self.position = saveData[32]
                    self.sqn = saveData[33]

                oldRefreshSetting = self.preview.cb_Refresh.isChecked()
                # Turn off auto refresh to prevent applying the loaded settings to trigger multiple refreshes.
                self.preview.cb_Refresh.setChecked(False)
                self.applyPreviewSettings()
                self.preview.cb_Refresh.setChecked(oldRefreshSetting)
                self.renderPreview()
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def loadPreviewFileDialog(self):
        '''Method that opens a QT File Open dialog to save a profile.'''

        try:
            if self.uniform != "helmet":
                ext = ".pro"
            else:
                ext = ".helm"

            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self, "Load render settings", os.getcwd() + "\\settings\\", "*%s" % ext, options=options)
            if fileName:
                fileName = fileName.replace(r"/", "\\")
                return fileName

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def createHelmetNameTag(self):
        '''Method for creating nametag.png which is used to diasply the name on the pilot helmet.'''

        # Set the helmet's text.
        text = self.nameHelm

        # Local variables.
        width, height = 720, 264
        fontsize = 1  # Starting font size.

        # QT Method - Image creation.
        # Create the black image.
        self.image = QImage(QSize(width, height), QImage.Format_RGB32)
        self.painter = QPainter(self.image)
        self.painter.setBrush(QBrush(Qt.green))
        self.painter.fillRect(QRectF(0, 0, width, height), Qt.black)
        self.painter.setPen(QPen(Qt.white))
        self.painter.setFont(QFont(self.preview.fcb_helmFont.currentFont().family(), fontsize))

        # Determine the maximim width the text can be to fit in the image.
        try:
            factor = width / self.painter.fontMetrics().width(text)
            while factor > 1.06:
                fontsize += 1
                self.painter.setFont(QFont(self.preview.fcb_helmFont.currentFont().family(), fontsize))
                factor = width / self.painter.fontMetrics().width(text)
            maxWidthSize = fontsize
        except ZeroDivisionError:  # Some fonts don't return a width.
            maxWidthSize = 220

        # Determine the maximim height the text can be to fit in the image.
        fontsize = 1  # Reset to 1 for height calculation.
        self.painter.setFont(QFont(self.preview.fcb_helmFont.currentFont().family(), fontsize))
        factor = height / self.painter.fontMetrics().height()
        while factor > 1:
            fontsize += 1
            self.painter.setFont(QFont(self.preview.fcb_helmFont.currentFont().family(), fontsize))
            factor = height / self.painter.fontMetrics().height()
        maxHeightFontSize = fontsize

        # Determine which is the largest font size to use based on max height and max width.
        if maxWidthSize < maxHeightFontSize:
            fontsize = maxWidthSize
        else:
            fontsize = maxHeightFontSize
        self.painter.setFont(QFont(self.preview.fcb_helmFont.currentFont().family(), fontsize))

        # Draw the text and save the image.
        self.painter.drawText(self.image.rect(), Qt.AlignCenter | Qt.AlignVCenter, text)
        self.painter.end()
        self.image.save(os.getcwd() + "\\data\\helmet\\" + "nametag.png")
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_PaletteHelmFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            self.openColourPicker(self.helmColour, "helmColour", self.preview.lbl_PaletteHelm, self.preview.le_PaletteHelm)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def creatHelmetFaceColour(self, colour):
        r'''Method used to create "data\helmet\hemltex.bmp with the user's selected helmet colour.'''

        # creating an image object
        img = Image.open(os.getcwd() + "\\data\\helmet\\helmtex_m.gif")

        # image colorize function
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item == (255, 255, 255, 255):
                newData.append(colour.getRgb())
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(os.getcwd() + "\\data\\helmet\\helmtex.bmp", "BMP")
        self.creatHelmetFaceDetail(colour)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def creatHelmetFaceDetail(self, colour):
        r'''Method used to add helmtex_b.gif to "data\helmet\hemltex.bmp.'''

        # Convert helmtex_b.gif to a transparent background *.png.
        img = Image.open(os.getcwd() + "\\data\\helmet\\helmtex_b.gif")
        img = img.convert("RGBA")
        datas = img.getdata()

        # Make background transparent.
        colourRGB = colour.getRgb()
        newData = []
        for item in datas:
            if item == (0, 0, 0, 255):
                newData.append((255, 255, 255, 0))
            else:  # Reduce the base helmet colour by the shader colours to create shading.
                newData.append((colourRGB[0] - item[0], colourRGB[1] - item[1], colourRGB[2] - item[2], 255))
        img.putdata(newData)

        # Layer the transparent helmtex_b.png onto our coloured helmtex.bmp.
        img_w, img_h = img.size
        background = Image.open(os.getcwd() + "\\data\\helmet\\helmtex.bmp", 'r')
        bg_w, bg_h = background.size
        offset = (((bg_w - img_w) // 2) + 86, ((bg_h - img_h) // 2) - 38)
        background.paste(img, offset, mask=img)
        background.save(os.getcwd() + "\\data\\helmet\\helmtex.bmp")
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_PaletteHelmDecFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            self.openColourPicker(self.decColour, "decColour", self.preview.lbl_PaletteDec, self.preview.le_PaletteDec)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_PaletteHelmLightFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            self.openColourPicker(self.lightColour, "lightColour", self.preview.lbl_PaletteLight, self.preview.le_PaletteLight)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def convertIntToFloatStr(self, num, divisor):
        '''Method to convert a integer into a /10 float stgring for the slider values.'''

        return str(round(num / float(divisor), str(divisor).count("0")))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewAmbientFunc(self, value):
        '''Method for applying the light angle setting within the preview window.'''

        self.ambientHelm = value
        self.preview.lbl_Ambient.setText(self.convertIntToFloatStr(value, 100))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewSpecularFunc(self, value):
        '''Method for applying the light angle setting within the preview window.'''

        self.specularHelm = value
        self.preview.lbl_Specular.setText(self.convertIntToFloatStr(value, 100))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewRoughnessFunc(self, value):
        '''Method for applying the light angle setting within the preview window.'''

        self.roughHelm = value
        self.preview.lbl_Roughness.setText(self.convertIntToFloatStr(value, 100))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def vs_previewReflectionFunc(self, value):
        '''Method for applying the light angle setting within the preview window.'''

        self.reflectionHelm = value
        self.preview.lbl_Reflection.setText(self.convertIntToFloatStr(value, 100))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewResetSurfPropsFunc(self):
        '''Method for reseting the preview window light source.'''

        try:
            self.ambientHelm = 30
            self.preview.lbl_Ambient.setText(self.convertIntToFloatStr(self.ambientHelm, 100))
            self.preview.vs_Ambient.setValue(self.ambientHelm)
            self.specularHelm = 50
            self.preview.lbl_Specular.setText(self.convertIntToFloatStr(self.specularHelm, 100))
            self.preview.vs_Specular.setValue(self.specularHelm)
            self.roughHelm = 1
            self.preview.lbl_Roughness.setText(self.convertIntToFloatStr(self.roughHelm, 100))
            self.preview.vs_Roughness.setValue(self.roughHelm)
            self.reflectionHelm = 10
            self.preview.lbl_Reflection.setText(self.convertIntToFloatStr(self.reflectionHelm, 100))
            self.preview.vs_Reflection.setValue(self.reflectionHelm)
        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def le_previewHelmTextFunc(self, text):
        '''Method to handle text entry into the Helmet Text textbox.'''

        self.nameHelm = str(self.preview.le_helmText.text())
        self.preview.le_helmText.setText(self.nameHelm)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def fcb_previewHelmFontFunc(self, font):
        '''Method for handling helmet font selection'''

        self.fontHelmQFront = font
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def checkForAlpha(self, filepath):
        '''Method to check if an image has an alpha channel.'''

        # Load image.
        img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)

        # Check for alpha channel.
        try:
            mask = img[:, :, 3]  # Alpha is present
            return "True"
        except TypeError:
            return False
        except IndexError:
            return True
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewHemlLogo1TypeFunc(self):
        '''Method for handling Decoration Logo ComboBox actions.'''

        self.preview.le_helmLogo1Filepath.setEnabled(True)
        self.preview.btn_helmLogo1Filepath.setEnabled(True)

        if self.preview.cb_hemlLogo1Type.currentText() == "Squadron Patch":
            self.preview.le_helmLogo1Filepath.setEnabled(False)
            self.preview.btn_helmLogo1Filepath.setEnabled(False)

        elif self.preview.cb_hemlLogo1Type.currentText() == "Image - bg. transparent":
            if self.preview.le_helmLogo1Filepath.text() != "":
                if self.checkForAlpha(self.preview.le_helmLogo1Filepath.text()):
                    self.logo1TypeHelm = self.preview.cb_hemlLogo1Type.currentText()
                    return
                else:
                    self.logo1TypeHelm = self.preview.cb_hemlLogo1Type.currentText()
                    if not self.loadingHelm:
                        self.logo1FilepathHelm = ""
                        # Show error message.
##                        msg = "%s does not have a transparent background." % self.preview.le_helmLogo1Filepath.text().split("\\")[-1]
                        self.preview.le_helmLogo1Filepath.setText("")
##                        return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                        return

        elif self.preview.cb_hemlLogo1Type.currentText() == "None":
            self.preview.le_helmLogo1Filepath.setEnabled(False)
            self.preview.btn_helmLogo1Filepath.setEnabled(False)

        self.logo1TypeHelm = self.preview.cb_hemlLogo1Type.currentText()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewHemlLogo2TypeFunc(self):
        '''Method for handling Decoration Logo ComboBox actions.'''

        self.preview.le_helmLogo2Filepath.setEnabled(True)
        self.preview.btn_helmLogo2Filepath.setEnabled(True)

        if self.preview.cb_hemlLogo2Type.currentText() == "Squadron Patch":
            self.preview.le_helmLogo2Filepath.setEnabled(False)
            self.preview.btn_helmLogo2Filepath.setEnabled(False)

        elif self.preview.cb_hemlLogo2Type.currentText() == "Image - bg. transparent":
            if self.preview.le_helmLogo2Filepath.text() != "":
                if self.checkForAlpha(self.preview.le_helmLogo2Filepath.text()):
                    self.logo2TypeHelm = self.preview.cb_hemlLogo2Type.currentText()
                    return
                else:
                    self.logo2TypeHelm = self.preview.cb_hemlLogo2Type.currentText()
                    if not self.loadingHelm:
                        self.logo2FilepathHelm = ""
                        self.preview.le_helmLogo2Filepath.setText("")
                        return

        elif self.preview.cb_hemlLogo2Type.currentText() == "None":
            self.preview.le_helmLogo2Filepath.setEnabled(False)
            self.preview.btn_helmLogo2Filepath.setEnabled(False)

        self.logo2TypeHelm = self.preview.cb_hemlLogo2Type.currentText()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def getLogoFile(self, logoNum):
        '''Method that allows the user to select an image file from a file picker.'''

        try:
            # Specify the starting directory to open the file picker from.
            if logoNum == 1:
                if self.preview.cb_hemlLogo1Type.currentText() == "Image - bg. transparent":
                    path = os.getcwd() + "\\data\\misc\\Helmet Transparencies\\"
                elif self.preview.cb_hemlLogo1Type.currentText() == "Image - stencil mask":
                    path = os.getcwd() + "\\data\\misc\\Helmet Stencils\\"

            elif logoNum == 2:
                if self.preview.cb_hemlLogo2Type.currentText() == "Image - bg. transparent":
                    path = os.getcwd() + "\\data\\misc\\Helmet Transparencies\\"
                elif self.preview.cb_hemlLogo2Type.currentText() == "Image - stencil mask":
                    path = os.getcwd() + "\\data\\misc\\Helmet Stencils\\"

            # Open the file picker.
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(
                self, "Load texture for helmet logo", path, "All (*.gif *.jpg *.jpeg *.png *.bmp);;GIF Image (*.gif);; JPEG Image (*.jpg *.jpeg);; PNG Image (*.png);; Bitmap (*.bmp)", options=options)

            # Set the chosen file.
            if fileName:
                fileName = fileName.replace(r"/", "\\")

                if logoNum == 1:
                    if self.preview.cb_hemlLogo1Type.currentText() == "Image - bg. transparent":
                        if self.checkForAlpha(fileName):
                            self.createMask(fileName)
                            self.preview.le_helmLogo1Filepath.setText(fileName)
                        else:
                            self.preview.le_helmLogo1Filepath.setText("")
                            self.logo1FilepathHelm = ""
                            self.lastRenderData = self.getUniformData()
                            msg = "%s does not have a transparent background." % fileName.split("\\")[-1]
                            return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                    else:
                        self.preview.le_helmLogo1Filepath.setText(fileName)

                elif logoNum == 2:
                    self.logo2FilepathHelm = fileName
                    if self.preview.cb_hemlLogo2Type.currentText() == "Image - bg. transparent":
                        if self.checkForAlpha(fileName):
                            self.createMask(fileName)
                            self.preview.le_helmLogo2Filepath.setText(fileName)
                        else:
                            self.preview.le_helmLogo2Filepath.setText("")
                            self.logo2FilepathHelm = ""
                            self.lastRenderData = self.getUniformData()
                            msg = "%s does not have a transparent background." % fileName.split("\\")[-1]
                            return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
                    else:
                        self.preview.le_helmLogo2Filepath.setText(fileName)

        except Exception as e:
            handleException(e)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def le_previewHelmLogoXFilepathFunc(self, logoNum):
        '''Method to handle manual text entry of logo filepaths.'''

        if logoNum == 1:
            self.logo1FilepathHelm = self.preview.le_helmLogo1Filepath.text()
        elif logoNum == 2:
            self.logo2FilepathHelm = self.preview.le_helmLogo2Filepath.text()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_previewResetDecsFunc(self):
        '''Method for restting helmet decorations options.'''

        self.nameHelm = "EH TC"
        if self.callsign == "None":
            self.preview.le_helmText.setText(self.nameHelm)
        else:
            self.preview.le_helmText.setText(self.callsign)

        self.fontHelmQFront = QFont("impact")
        self.preview.fcb_helmFont.setCurrentFont(self.fontHelmQFront)

        self.logo1TypeHelm = "Image - stencil mask"
        self.logo1FilepathHelm = os.getcwd() + "\\data\\misc\\Helmet Stencils\\tclogo.gif"

        if self.sqn != "":
            self.logo2TypeHelm = "Squadron Patch"
            self.logo2FilepathHelm = ""
        else:
            self.logo2TypeHelm = "Image - stencil mask"
            self.logo2FilepathHelm = os.getcwd() + "\\data\\misc\\Helmet Stencils\\tiecorps_logo_new.png"

        logo1Type = self.preview.cb_hemlLogo1Type.findText(self.logo1TypeHelm, Qt.MatchExactly | Qt.MatchCaseSensitive)
        logo2Type = self.preview.cb_hemlLogo2Type.findText(self.logo2TypeHelm, Qt.MatchExactly | Qt.MatchCaseSensitive)
        self.preview.cb_hemlLogo1Type.setCurrentIndex(logo1Type)
        self.preview.cb_hemlLogo2Type.setCurrentIndex(logo2Type)
        if self.preview.cb_hemlLogo2Type.currentText() == "":
            self.preview.cb_hemlLogo2Type.setCurrentIndex(0)
        self.cb_previewHemlLogo1TypeFunc()
        self.cb_previewHemlLogo2TypeFunc()

        self.preview.le_helmLogo1Filepath.setText(self.logo1FilepathHelm)
        self.preview.le_helmLogo2Filepath.setText(self.logo2FilepathHelm)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewPresetCamFunc(self, intIndex):
        '''Method for preview camera presets.'''

        if intIndex == 0:
            self.camX = -2500
            self.camY = -13300
            self.camZ = 2100

        # Top Left.
        elif intIndex == 1:
            self.camX = -10000
            self.camY = -8000
            self.camZ = 8000

        # Top Centre.
        elif intIndex == 2:
            self.camX = 0
            self.camY = -11000
            self.camZ = 8000

        # Top Right.
        elif intIndex == 3:
            self.camX = 10000
            self.camY = -8000
            self.camZ = 8000

        # Middle Left.
        elif intIndex == 4:
            self.camX = -9000
            self.camY = -11000
            self.camZ = 0

        # Middle Centre.
        elif intIndex == 5:
            self.camX = 0
            self.camY = -13300
            self.camZ = 0

        # Middle Right.
        elif intIndex == 6:
            self.camX = 9000
            self.camY = -11000
            self.camZ = 0

        # Bottom Left.
        elif intIndex == 7:
            self.camX = -8000
            self.camY = -11000
            self.camZ = -8000

        # Bottom Centre.
        elif intIndex == 8:
            self.camX = 0
            self.camY = -12000
            self.camZ = -8000

        # Bottom Right.
        elif intIndex == 9:
            self.camX = 8000
            self.camY = -11000
            self.camZ = -8000

        if intIndex != 10:
            self.renderPreview()
            self.preview.vs_CamX.setValue(self.camX)
            self.preview.lbl_CamX.setText(self.convertIntToFloatStr(self.camX, 10))
            self.preview.vs_CamY.setValue(self.camY)
            self.preview.lbl_CamY.setText(self.convertIntToFloatStr(self.camY, 10))
            self.preview.vs_CamZ.setValue(self.camZ)
            self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(self.camZ, 10))
            self.preview.cb_PresetCam.currentIndexChanged.disconnect()
            self.preview.cb_PresetCam.setCurrentIndex(intIndex)
            self.preview.cb_PresetCam.currentIndexChanged.connect(self.cb_previewPresetCamFunc)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewPresetCamHelmFunc(self, intIndex):
        '''Method for preview camera presets.'''

        if intIndex == 0:
            self.camXHelm = 2170
            self.camYHelm = -6510
            self.camZHelm = 3146

        # Top Left.
        elif intIndex == 1:
            self.camXHelm = -5000
            self.camYHelm = -6510
            self.camZHelm = 5000

        # Top Centre.
        elif intIndex == 2:
            self.camXHelm = 0
            self.camYHelm = -7000
            self.camZHelm = 5000

        # Top Right.
        elif intIndex == 3:
            self.camXHelm = 5000
            self.camYHelm = -6510
            self.camZHelm = 5000

        # Middle Left.
        elif intIndex == 4:
            self.camXHelm = -5000
            self.camYHelm = -6510
            self.camZHelm = 1500

        # Middle Centre.
        elif intIndex == 5:
            self.camXHelm = 0
            self.camYHelm = -6510
            self.camZHelm = 1500

        # Middle Right.
        elif intIndex == 6:
            self.camXHelm = 5000
            self.camYHelm = -6510
            self.camZHelm = 1500

        # Bottom Left.
        elif intIndex == 7:
            self.camXHelm = -5000
            self.camYHelm = -6510
            self.camZHelm = -2000

        # Bottom Centre.
        elif intIndex == 8:
            self.camXHelm = 0
            self.camYHelm = -6510
            self.camZHelm = -2000

        # Bottom Right.
        elif intIndex == 9:
            self.camXHelm = 5000
            self.camYHelm = -6510
            self.camZHelm = -2000

        if intIndex != 10:
            self.renderPreview()
            self.preview.vs_CamX.setValue(self.camXHelm)
            self.preview.lbl_CamX.setText(self.convertIntToFloatStr(self.camXHelm, 100))
            self.preview.vs_CamY.setValue(self.camYHelm)
            self.preview.lbl_CamY.setText(self.convertIntToFloatStr(self.camYHelm, 100))
            self.preview.vs_CamZ.setValue(self.camZHelm)
            self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(self.camZHelm, 100))
            self.preview.cb_PresetCam.currentIndexChanged.disconnect()
            self.preview.cb_PresetCam.setCurrentIndex(intIndex)
            self.preview.cb_PresetCam.currentIndexChanged.connect(self.cb_previewPresetCamHelmFunc)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewPresetLookFunc(self, intIndex):
        '''Method for preview look presets.'''

        if intIndex == 0:
            self.lookX = 0
            self.lookY = -128
            self.lookZ = 28

        # Top Left.
        elif intIndex == 1:
            self.lookX = -2500
            self.lookY = -128
            self.lookZ = 2500

        # Top Centre.
        elif intIndex == 2:
            self.lookX = 0
            self.lookY = -128
            self.lookZ = 2500

        # Top Right.
        elif intIndex == 3:
            self.lookX = 2500
            self.lookY = -128
            self.lookZ = 2500

        # Middle Left.
        elif intIndex == 4:
            self.lookX = -2500
            self.lookY = -128
            self.lookZ = 0

        # Middle Centre.
        elif intIndex == 5:
            self.lookX = 0
            self.lookY = -128
            self.lookZ = 0

        # Middle Right.
        elif intIndex == 6:
            self.lookX = 2500
            self.lookY = -128
            self.lookZ = 0

        # Bottom Left.
        elif intIndex == 7:
            self.lookX = -2500
            self.lookY = -128
            self.lookZ = -2500

        # Bottom Centre.
        elif intIndex == 8:
            self.lookX = 0
            self.lookY = -128
            self.lookZ = -2500

        # Bottom Right.
        elif intIndex == 9:
            self.lookX = 2500
            self.lookY = -128
            self.lookZ = -2500

        if intIndex != 10:
            self.renderPreview()
            self.preview.vs_LookX.setValue(self.lookX)
            self.preview.lbl_LookX.setText(self.convertIntToFloatStr(self.lookX, 10))
            self.preview.vs_LookY.setValue(self.lookY)
            self.preview.lbl_LookY.setText(self.convertIntToFloatStr(self.lookY, 10))
            self.preview.vs_LookZ.setValue(self.lookZ)
            self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(self.lookZ, 10))
            self.preview.cb_PresetLook.currentIndexChanged.disconnect()
            self.preview.cb_PresetLook.setCurrentIndex(intIndex)
            self.preview.cb_PresetLook.currentIndexChanged.connect(self.cb_previewPresetLookFunc)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewPresetLookHelmFunc(self, intIndex):
        '''Method for preview look presets.'''

        if intIndex == 0:
            self.lookXHelm = -568
            self.lookYHelm = -445
            self.lookZHelm = 1052

        # Top Left.
        elif intIndex == 1:
            self.lookXHelm = -2500
            self.lookYHelm = -445
            self.lookZHelm = 2500

        # Top Centre.
        elif intIndex == 2:
            self.lookXHelm = 0
            self.lookYHelm = -445
            self.lookZHelm = 2500

        # Top Right.
        elif intIndex == 3:
            self.lookXHelm = 2500
            self.lookYHelm = -445
            self.lookZHelm = 2500

        # Middle Left.
        elif intIndex == 4:
            self.lookXHelm = -2500
            self.lookYHelm = -445
            self.lookZHelm = 0

        # Middle Centre.
        elif intIndex == 5:
            self.lookXHelm = 0
            self.lookYHelm = -445
            self.lookZHelm = 0

        # Middle Right.
        elif intIndex == 6:
            self.lookXHelm = 2500
            self.lookYHelm = -445
            self.lookZHelm = 0

        # Bottom Left.
        elif intIndex == 7:
            self.lookXHelm = -2500
            self.lookYHelm = -445
            self.lookZHelm = -2500

        # Bottom Centre.
        elif intIndex == 8:
            self.lookXHelm = 0
            self.lookYHelm = -445
            self.lookZHelm = -2500

        # Bottom Right.
        elif intIndex == 9:
            self.lookXHelm = 2500
            self.lookYHelm = -445
            self.lookZHelm = -2500

        if intIndex != 10:
            self.renderPreview()
            self.preview.vs_LookX.setValue(self.lookXHelm)
            self.preview.lbl_LookX.setText(self.convertIntToFloatStr(self.lookXHelm, 100))
            self.preview.vs_LookY.setValue(self.lookYHelm)
            self.preview.lbl_LookY.setText(self.convertIntToFloatStr(self.lookYHelm, 100))
            self.preview.vs_LookZ.setValue(self.lookZHelm)
            self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(self.lookZHelm, 100))
            self.preview.cb_PresetLook.currentIndexChanged.disconnect()
            self.preview.cb_PresetLook.setCurrentIndex(intIndex)
            self.preview.cb_PresetLook.currentIndexChanged.connect(self.cb_previewPresetLookHelmFunc)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewPresetLightFunc(self, intIndex):
        '''Method for preview light presets.'''

        if intIndex == 0:
            self.lightX = 13000
            self.lightY = -15000
            self.lightZ = 13000

        # Top Left.
        elif intIndex == 1:
            self.lightX = -10000
            self.lightY = -6474
            self.lightZ = 10000

        # Top Centre.
        elif intIndex == 2:
            self.lightX = 0
            self.lightY = -6474
            self.lightZ = 10000

        # Top Right.
        elif intIndex == 3:
            self.lightX = 10000
            self.lightY = -6474
            self.lightZ = 10000

        # Middle Left.
        elif intIndex == 4:
            self.lightX = -10000
            self.lightY = -6474
            self.lightZ = 0

        # Middle Centre.
        elif intIndex == 5:
            self.lightX = 0
            self.lightY = -6474
            self.lightZ = 0

        # Middle Right.
        elif intIndex == 6:
            self.lightX = 10000
            self.lightY = -6474
            self.lightZ = 0

        # Bottom Left.
        elif intIndex == 7:
            self.lightX = -10000
            self.lightY = -6474
            self.lightZ = -10000

        # Bottom Centre.
        elif intIndex == 8:
            self.lightX = 0
            self.lightY = -6474
            self.lightZ = -10000

        # Bottom Right.
        elif intIndex == 9:
            self.lightX = 10000
            self.lightY = -6474
            self.lightZ = -10000

        # TTT2 Default
        elif intIndex == 10:
            self.lightX = 15185
            self.lightY = -6474
            self.lightZ = -17501

        if intIndex != 11:
            self.renderPreview()
            self.preview.vs_LightX.setValue(self.lightX)
            self.preview.lbl_LightX.setText(self.convertIntToFloatStr(self.lightX, 10))
            self.preview.vs_LightY.setValue(self.lightY)
            self.preview.lbl_LightY.setText(self.convertIntToFloatStr(self.lightY, 10))
            self.preview.vs_LightZ.setValue(self.lightZ)
            self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(self.lightZ, 10))
            self.preview.cb_PresetLight.currentIndexChanged.disconnect()
            self.preview.cb_PresetLight.setCurrentIndex(intIndex)
            self.preview.cb_PresetLight.currentIndexChanged.connect(self.cb_previewPresetLightFunc)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_CamXFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_CamX, "Cam X", self.preview.lbl_CamX, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_CamYFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_CamY, "Cam Y", self.preview.lbl_CamY, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_CamZFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_CamZ, "Cam Z", self.preview.lbl_CamZ, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LookXFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LookX, "Look X", self.preview.lbl_LookX, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LookYFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LookY, "Look Y", self.preview.lbl_LookY, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LookZFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LookZ, "Look Z", self.preview.lbl_LookZ, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LightXFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LightX, "Light X", self.preview.lbl_LightX, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LightYFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LightY, "Light Y", self.preview.lbl_LightY, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LightZFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LightZ, "Light Z", self.preview.lbl_LightZ, -2000, 2000, 10)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_CamXHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_CamX, "Cam X", self.preview.lbl_CamX, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_CamYHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_CamY, "Cam Y", self.preview.lbl_CamY, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_CamZHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_CamZ, "Cam Z", self.preview.lbl_CamZ, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LookXHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LookX, "Look X", self.preview.lbl_LookX, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LookYHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LookY, "Look Y", self.preview.lbl_LookY, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LookZHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LookZ, "Look Z", self.preview.lbl_LookZ, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LightXHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LightX, "Light X", self.preview.lbl_LightX, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LightYHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LightY, "Light Y", self.preview.lbl_LightY, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_LightZHelmFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_LightZ, "Light Z", self.preview.lbl_LightZ, -100, 100, 100, 2)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_AmbientFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_Ambient, "Ambient", self.preview.lbl_Ambient, 0, 1, 100, 2, 0.01)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_SpecularFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_Specular, "Specular", self.preview.lbl_Specular, 0, 1, 100, 2, 0.01)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_RoughnessFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_Roughness, "Roughness", self.preview.lbl_Roughness, 0, 1, 100, 2, 0.01)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def lbl_ReflectionFunc(self, sender):
        '''Method that is triggered why a slider's label is clicked.'''

        self.sliderValueInput(self.preview.vs_Reflection, "Reflection", self.preview.lbl_Reflection, 0, 1, 100, 2, 0.01)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def sliderValueInput(self, slider, name, label, min, max, scale, decimals=1, step=1):
        '''Method directly asks the user for a slider input.'''

        value, ok = QInputDialog.getDouble(self, "%s Value" % name, slider.toolTip() + "\n\nEnter new value:", float(label.text()), min, max, decimals, Qt.WindowFlags(), step)
        if ok:
            slider.setValue(int(value * scale))
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewPresetLightHelmFunc(self, intIndex):
        '''Method for preview light presets.'''

        if intIndex == 0:
            self.lightXHelm = 2244
            self.lightYHelm = -5089
            self.lightZHelm = 5282

        # Top Left.
        elif intIndex == 1:
            self.lightXHelm = -5000
            self.lightYHelm = -5089
            self.lightZHelm = 5000

        # Top Centre.
        elif intIndex == 2:
            self.lightXHelm = 0
            self.lightYHelm = -5089
            self.lightZHelm = 5000

        # Top Right.
        elif intIndex == 3:
            self.lightXHelm = 5000
            self.lightYHelm = -5089
            self.lightZHelm = 5000

        # Middle Left.
        elif intIndex == 4:
            self.lightXHelm = -5000
            self.lightYHelm = -5089
            self.lightZHelm = 0

        # Middle Centre.
        elif intIndex == 5:
            self.lightXHelm = 0
            self.lightYHelm = -5089
            self.lightZHelm = 0

        # Middle Right.
        elif intIndex == 6:
            self.lightXHelm = 5000
            self.lightYHelm = -5089
            self.lightZHelm = 0

        # Bottom Left.
        elif intIndex == 7:
            self.lightXHelm = -5000
            self.lightYHelm = -5089
            self.lightZHelm = -5000

        # Bottom Centre.
        elif intIndex == 8:
            self.lightXHelm = 0
            self.lightYHelm = -5089
            self.lightZHelm = -5000

        # Bottom Right.
        elif intIndex == 9:
            self.lightXHelm = 5000
            self.lightYHelm = -5089
            self.lightZHelm = -5000

        if intIndex != 10:
            self.renderPreview()
            self.preview.vs_LightX.setValue(self.lightXHelm)
            self.preview.lbl_LightX.setText(self.convertIntToFloatStr(self.lightXHelm, 100))
            self.preview.vs_LightY.setValue(self.lightYHelm)
            self.preview.lbl_LightY.setText(self.convertIntToFloatStr(self.lightYHelm, 100))
            self.preview.vs_LightZ.setValue(self.lightZHelm)
            self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(self.lightZHelm, 100))
            self.preview.cb_PresetLight.currentIndexChanged.disconnect()
            self.preview.cb_PresetLight.setCurrentIndex(intIndex)
            self.preview.cb_PresetLight.currentIndexChanged.connect(self.cb_previewPresetLightHelmFunc)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def previewAutoRefresh(self, event=None):
        '''Method to handle auto refreshing of the preview windows.'''

        if self.preview.cb_Refresh.isChecked():
            self.renderPreview()
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def cb_previewRefreshFunc(self):
        '''Method to handle actions upon selection of the Auto-refresh checkbox.'''

        if self.preview.cb_Refresh.isChecked():
            self.preview.btn_preview.setEnabled(False)
            self.renderPreview()
        else:
            self.preview.btn_preview.setEnabled(True)
        #--------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Functions.                                                                    #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
def getYHelm(x):
    '''Function to return an aspect ratio locked value for any given x.'''

    return round(float(x) / 1.1678)
    #------------------------------------------------------------------------------------------------------------------------------------------------#


def getXHelm(y):
    '''Function to return an aspect ratio locked value for any given y.'''

    return round(float(y) * 1.1678)
    #------------------------------------------------------------------------------------------------------------------------------------------------#


def getY(x):
    '''Function to return an aspect ratio locked value for any given x.'''

    return round(float(x) / 0.7502)
    #------------------------------------------------------------------------------------------------------------------------------------------------#


def getX(y):
    '''Function to return an aspect ratio locked value for any given y.'''

    return round(float(y) * 0.7502)
    #------------------------------------------------------------------------------------------------------------------------------------------------#


def getHash(strSource):
    '''Method that calculates the MD5 hash for a given source file in string format.'''

    # Read in the source data.
    with open(strSource, "rb") as srcFile:
        data = srcFile.read()

    # Get MD5 has of source file and return it.
    return hashlib.md5(data).hexdigest()
    #------------------------------------------------------------------------------------------------------------------------------------------------#


def getScreenResolution():
    '''Method that returns the width and height of the user's monitor resolution.'''

    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    #------------------------------------------------------------------------------------------------------------------------------------------------#


def setPixelSizes(tgtGUI):
    '''Function that handles font scalling fron pointSize to pixelSize for a given GUI.
       pixelSize is used instead of the regular pointSize in order to scale text properly for high DPI monitor settings.'''

    for widget in vars(tgtGUI):
        try:
            font = vars(tgtGUI).get(widget).font()
            font.setPixelSize(font.pointSize() + 3)
            vars(tgtGUI).get(widget).setFont(font)
        except AttributeError:
            pass
    #------------------------------------------------------------------------------------------------------------------------------------------------#


def setLWPixelSizes(listWidget, pixelSize=13):
    '''Function that handles font scalling fron pointSize to pixelSize for a given QListWidget.
       pixelSize is used instead of the regular pointSize in order to scale text properly for high DPI monitor settings.'''

    for entry in range(listWidget.count()):
        font = listWidget.item(entry).font()
        font.setPixelSize(pixelSize)
        listWidget.item(entry).setFont(font)
    #------------------------------------------------------------------------------------------------------------------------------------------------#


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
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ttt3 = TTT3()
    sys.exit(app.exec_())
#----------------------------------------------------------------------------------------------------------------------------------------------------#
