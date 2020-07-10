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
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def exit(self):
        '''Method that closes the application.'''

        sys.exit()
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
