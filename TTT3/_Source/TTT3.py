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
from _winreg import *
from PyQt4 import QtGui, QtCore, uic



#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Classes.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
class NullDevice():
    '''A object class used to inhibit the SDTOUT/STDERR.'''

    def write(self, s):
        pass
    #------------------------------------------------------------------------------------------------------------------------------------------------#


class TTT3(QtGui.QMainWindow):
    '''Main object class represting the TTT3 application.'''

    def __init__(self):
        '''Class constructor.'''

        # Initialise an instance of a QT Main Window and load our GUI file ttt.ui.
        QtGui.QMainWindow.__init__(self)
        self.gui = uic.loadUi(r"data\uis\ttt.ui")
        self.gui.show()

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

        # Initialise instance variables.
        self.rankRadioButtons = [self.gui.rb_rank_ct, self.gui.rb_rank_sl, self.gui.rb_rank_lt, self.gui.rb_rank_lcm, self.gui.rb_rank_cm,
                                 self.gui.rb_rank_cpt, self.gui.rb_rank_maj, self.gui.rb_rank_lc, self.gui.rb_rank_col, self.gui.rb_rank_gn,
                                 self.gui.rb_rank_ra, self.gui.rb_rank_va, self.gui.rb_rank_ad, self.gui.rb_rank_fa, self.gui.rb_rank_ha,
                                 self.gui.rb_rank_sa, self.gui.rb_rank_ga]

        self.positionRadioButtons = [self.gui.rb_pos_trn, self.gui.rb_pos_fm, self.gui.rb_pos_fl, self.gui.rb_pos_cmdr, self.gui.rb_pos_wc,
                                     self.gui.rb_pos_com, self.gui.rb_pos_bgcom, self.gui.rb_pos_ia, self.gui.rb_pos_ca, self.gui.rb_pos_sgcom,
                                     self.gui.rb_pos_cs, self.gui.rb_pos_xo, self.gui.rb_pos_fc, self.gui.rb_pos_lr, self.gui.rb_pos_fr]

        # Initialise PovRay Template variables.
        self.position = None
        self.rank = None
        self.ship = None
        self.wing = None
        self.sqn = None

        # Application logic.
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

        # ToDo Disabled Helmet UTFN.
        self.gui.btn_helmet.setEnabled(False)
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def posRBLogic(self):
        '''Method that controls the Position Radio Button Logic - Showing or hiding the required rank options'''

        # Disnable the Dress and Duty Uniform buttons.
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
                if radioButton == self.gui.rb_pos_trn:
                    self.showRanks(CT, CT)
                    self.position = "TRN"
                    break

                elif radioButton == self.gui.rb_pos_fm:
                    self.showRanks(SL, GN)
                    self.position = "FM"
                    break

                elif radioButton == self.gui.rb_pos_fl:
                    self.showRanks(LT, GN)
                    self.position = "FL"
                    break

                elif radioButton == self.gui.rb_pos_cmdr:
                    self.showRanks(CM, GN)
                    self.position = "CMDR"
                    break

                elif radioButton == self.gui.rb_pos_wc:
                    self.showRanks(MAJ, GN)
                    self.position = "WC"
                    break

                elif radioButton == self.gui.rb_pos_com:
                    self.showRanks(RA, HA)
                    self.position = "COM"
                    break

                elif radioButton == self.gui.rb_pos_bgcom:
                    self.showRanks(RA, HA)
                    self.position = "BGCOM"
                    break

                elif radioButton == self.gui.rb_pos_ia:
                    self.showRanks(RA, HA)
                    self.position = "IA"
                    break

                elif radioButton == self.gui.rb_pos_ca:
                    self.showRanks(RA, HA)
                    self.position = "CA"
                    break

                elif radioButton == self.gui.rb_pos_sgcom:
                    self.showRanks(RA, GA)
                    self.position = "SGCOM"
                    break

                elif radioButton == self.gui.rb_pos_cs:
                    self.showRanks(RA, GA)
                    self.position = "CS"
                    break

                elif radioButton == self.gui.rb_pos_xo:
                    self.showRanks(RA, GA)
                    self.position = "XO"
                    break

                elif radioButton == self.gui.rb_pos_fc:
                    self.showRanks(GA, GA)
                    self.position = "FC"
                    self.gui.rb_rank_ga.setChecked(True)
                    self.rankRBLogic()
                    break

                elif radioButton == self.gui.rb_pos_lr:
                    self.showRanks(CT, GN)
                    self.position = "NUL"
                    break

                elif radioButton == self.gui.rb_pos_fr:
                    self.showRanks(RA, GA)
                    self.position = "NUL"
                    break
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def rankRBLogic(self):
        '''Method that controls the Rank Radio Button Logic - Showing the 'Dress and Duty Uniform' buttons.'''

        # Determine which rank radio button has been selected.
        for radioButton in self.rankRadioButtons:
            if radioButton.isChecked():

                # Set the correct rank for the selected rank.
                if radioButton == self.gui.rb_rank_ct:
                    self.rank = "CT"
                    break
                # ToDo Finish!

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
           This method will check that the correct selectiosn have been made within TTT3 which as Ship and Squadron and then
           directly call up PovRay to render the unirom.'''

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
            # ToDo Dynamic PovRay .bat
        else:

            # ToDo Move to Config.
            # Detect the installation path of POV-Ray from the Windows registry.
            try:
                aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
                aKey = r"Software\POV-Ray\CurrentVersion\Windows"
                values = OpenKey(aReg, aKey)
                path = QueryValueEx(values, "Home")[0]

            except WindowsError:
                msg = "Cannot find valid installion of POV-Ray."
                return ctypes.windll.user32.MessageBoxA(0, msg, "TTT3", 0)
                path = "NULL"

            # Dynamically write the data\povray.bat file.
            template = r'&PATH&&ADD& /RENDER "&APPPATH&\data\&TYPE&.pov" +w640 +h853 +q9 /EXIT'
            template = template.replace("&APPPATH&", os.getcwd())
            template = template.replace("&PATH&", path)
            template = template.replace("&ADD&", r"bin\pvengine64.exe")
            template = template.replace("&TYPE&", "dress")
            print template
            with open(r"data\batch\povray.bat", "w") as dataFile:
                dataFile.write(template)

            # Dynamically write the data\invisible.vbs file.
            input = []
            output = []
            with open(r"data\batch\invisible.vbs", "r") as dataFile:
                input = dataFile.readlines()
                for line in input:
                    if "&PATH&" in line:
                        newLine = line.replace("&PATH&", os.getcwd())
                        output.append(newLine)
                    else:
                        output.append(line)

            with open(r"data\batch\invisible.vbs", "w") as dataFile:
                dataFile.writelines(output)

            os.system(r"data\batch\invisible.vbs")

            with open(r"data\batch\invisible.vbs", "w") as dataFile:
                dataFile.writelines(input)
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def btn_configMethod(self):
        '''Method that opens and handles control of the 'Configuration' window.'''

        self.config_gui = uic.loadUi(r"data\uis\config.ui")
        self.config_gui.show()
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
