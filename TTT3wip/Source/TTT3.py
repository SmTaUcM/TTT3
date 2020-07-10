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
        self.gui = uic.loadUi('ttt.ui')
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
        self.connect(self.gui.btn_exit, QtCore.SIGNAL("clicked()"), self.exit)

        # Radio Button Connections.
            # Positions.
        self.connect(self.gui.rb_pos_trn,    QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_fm,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_fl,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_cmdr,   QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_wc,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_com,    QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_bgcom,  QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_ia,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_ca,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_sgcom,  QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_cs,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_xo,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_fc,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_lr,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)
        self.connect(self.gui.rb_pos_fr,     QtCore.SIGNAL("clicked()"), self.posRankRBLogic)

        # Initialise instance variables.
        self.rankRadioButtons = [self.gui.rb_rank_ct, self.gui.rb_rank_sl, self.gui.rb_rank_lt, self.gui.rb_rank_lcm, self.gui.rb_rank_cm,
                                 self.gui.rb_rank_cpt, self.gui.rb_rank_maj, self.gui.rb_rank_lc, self.gui.rb_rank_col, self.gui.rb_rank_gn,
                                 self.gui.rb_rank_ra, self.gui.rb_rank_va, self.gui.rb_rank_ad, self.gui.rb_rank_fa, self.gui.rb_rank_ha,
                                 self.gui.rb_rank_sa, self.gui.rb_rank_ga]

        self.positionRadioButtons = [self.gui.rb_pos_trn, self.gui.rb_pos_fm, self.gui.rb_pos_fl, self.gui.rb_pos_cmdr, self.gui.rb_pos_wc,
                                     self.gui.rb_pos_com, self.gui.rb_pos_bgcom, self.gui.rb_pos_ia, self.gui.rb_pos_ca, self.gui.rb_pos_sgcom,
                                     self.gui.rb_pos_cs, self.gui.rb_pos_xo, self.gui.rb_pos_fc, self.gui.rb_pos_lr, self.gui.rb_pos_fr]

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
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def posRankRBLogic(self):
        '''Method that controls the Position / Rank Radio Button Logic - Showing or hiding the required rank options'''

        # Ranks: 0=CT, 1=SL, 2=LT, 3=LCM, 4=CM, 5=CPT, 6=MAJ, 7=LC, 8=COL, 9=GN, 10=RA, 11=VA, 12=AD, 13=FA, 14=HA, 15=SA, 16=GA

        # Clean up the ranks group box.
        self.hideAllRanks()

        # Determine which position radio button has been selected.
        for radioButton in self.positionRadioButtons:
            if radioButton.isChecked():

                if radioButton == self.gui.rb_pos_trn:
                    self.showRanks(0, 1)
                    break

                elif radioButton == self.gui.rb_pos_fm:
                    self.showRanks(1, 10)
                    break

                elif radioButton == self.gui.rb_pos_fl:
                    self.showRanks(2, 10)
                    break

                elif radioButton == self.gui.rb_pos_cmdr:
                    self.showRanks(4, 10)
                    break

                elif radioButton == self.gui.rb_pos_wc:
                    self.showRanks(6, 10)
                    break

                elif radioButton == self.gui.rb_pos_com:
                    self.showRanks(10, 15)
                    break

                elif radioButton == self.gui.rb_pos_bgcom:
                    self.showRanks(10, 15)
                    break

                elif radioButton == self.gui.rb_pos_ia:
                    self.showRanks(10, 15)
                    break

                elif radioButton == self.gui.rb_pos_ca:
                    self.showRanks(10, 15)
                    break

                elif radioButton == self.gui.rb_pos_sgcom:
                    self.showRanks(10, 17)
                    break

                elif radioButton == self.gui.rb_pos_cs:
                    self.showRanks(10, 17)
                    break

                elif radioButton == self.gui.rb_pos_xo:
                    self.showRanks(10, 17)
                    break

                elif radioButton == self.gui.rb_pos_fc:
                    self.showRanks(16, 17)
                    self.gui.rb_rank_ga.setChecked(True)
                    break

                elif radioButton == self.gui.rb_pos_lr:
                    self.showRanks(0, 10)
                    break

                elif radioButton == self.gui.rb_pos_fr:
                    self.showRanks(10, 17)
                    break
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def hideAllRanks(self):
        '''Method that is used to hide all rank radio buttons on the Position and Rank tab.'''

        for rankRadioButton in self.rankRadioButtons:
            rankRadioButton.hide()
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def showRanks(self, rankRangeMin, rankRangeMax):
        '''Method used to show a range of ranks in the Position and Rank tab.
           self.showRanks(int(rankRangeMin), int(rankRangeMax)) -> Rank Radio Buttons shown.'''

        for rankRadioButton in self.rankRadioButtons[rankRangeMin : rankRangeMax]:
            rankRadioButton.show()
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
    # Inhibit the STDOUT and STDERR so we don't get the annoying pop up window when we close the app.
    sys.stdout = NullDevice()
    sys.stderr = NullDevice()

    # Start the QT application.
    app = QtGui.QApplication(sys.argv)
    ttt3 = TTT3()
    sys.exit(app.exec_())
#----------------------------------------------------------------------------------------------------------------------------------------------------#
