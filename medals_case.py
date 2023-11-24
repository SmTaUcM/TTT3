'''#------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        medals_case.py
# Purpose:     Class module for TTT3 medals case.
# Version:     v1.00
# Author:      Stuart Macintosh
#
# Created:     23/11/2023
#-------------------------------------------------------------------------------------------------------------------------------------------------#'''


#---------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Imports.                                                                     #
#---------------------------------------------------------------------------------------------------------------------------------------------------#
import logging
import os
import sys
import ctypes
import platform
from PyQt5 import uic  # python -m pip install pyqt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
# --------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Classes.                                                                     #
#---------------------------------------------------------------------------------------------------------------------------------------------------#
class MedalsCase(object): # Bookmark.
    '''Class module for TTT3 medals case.'''

    def __init__(self, TTT3Object):
        '''Method to handle clicking on the slider.'''

        try:
            self.ttt3 = TTT3Object
            self.spotColour = QColor(255, 255, 255)
            self.envColour = QColor(128, 118, 108)
            self.bgColour = QColor(0, 0, 0)
            self.width = 640 #TODO width
            self.height = 853 #TODO height
            self.camXDefault = -2500
            self.camYDefault = -13300
            self.camZDefault = 2100
            self.camX = self.camXDefault
            self.camY = self.camYDefault
            self.camZ = self.camZDefault
            self.cbCamIndex = 0
            self.lookXDefault = 0
            self.lookYDefault = -128
            self.lookZDefault = 28
            self.lookX = self.lookXDefault
            self.lookY = self.lookYDefault
            self.lookZ = self.lookZDefault
            self.cbLookIndex = 0
            self.lightX = 13000
            self.lightY = -15000
            self.lightZ = 13000
            self.cbLightIndex = 0
        except Exception as e:
            handleException(e)
        #-------------------------------------------------------------------------------------------------------------------------------------------#

    def showPreviewDialog(self):
        '''Method to open the render preview / options GUI.'''

        self.ttt3.uniform = "medalsCase"
        self.ttt3.previewLoaded = False
        self.ttt3.preview = uic.loadUi(r"data\uis\preview.ui")
        self.ttt3.preview.setWindowTitle("TTT3 Rendering Options - Medals Case")
        self.ttt3.preview.show()
        setPixelSizes(self.ttt3.preview)
        self.ttt3.preview.closeEvent = self.previewCloseEvent
        self.ttt3.gui.hide()
        self.ttt3.preview.lbl_wait.setAttribute(Qt.WA_TranslucentBackground)
        self.ttt3.preview.lbl_wait.setHidden(True)
        self.applyPreviewSettings()

        # Connections.
        self.ttt3.uniform = "dress" # TODO remove me
        self.ttt3.preview.btn_raytrace.clicked.connect(self.ttt3.launchPOVRay)
        self.ttt3.preview.btn_preview.clicked.connect(self.ttt3.renderPreview)
        self.ttt3.preview.btn_PaletteSpot.clicked.connect(self.btn_PaletteSpotFunc)
        self.ttt3.preview.btn_PaletteEnv.clicked.connect(self.btn_PaletteEnvFunc)
        self.ttt3.preview.btn_PaletteBack.clicked.connect(self.btn_PaletteBackFunc)
        self.ttt3.preview.btn_resetColours.clicked.connect(self.ttt3.btn_previewResetColoursFunc)
        self.ttt3.preview.sb_Width.valueChanged.connect(self.ttt3.sb_previewWidthFunc)
        self.ttt3.preview.btn_resetOptions.clicked.connect(self.ttt3.btn_previewResetOptionsFunc)
        self.ttt3.preview.sb_Quality.valueChanged.connect(self.ttt3.sb_previewQualityFunc)
        self.ttt3.preview.cb_Detail.currentIndexChanged.connect(self.ttt3.cb_previewDetailFunc)
        self.ttt3.preview.cb_AA.stateChanged.connect(self.ttt3.cb_previewAAFunc)
        self.ttt3.preview.cb_Shadowless.stateChanged.connect(self.ttt3.cb_previewShadowlessFunc)
        self.ttt3.preview.cb_Mosaic.stateChanged.connect(self.ttt3.cb_previewMosaicFunc)
        self.ttt3.preview.cb_TransparentBG.stateChanged.connect(self.ttt3.cb_previewTransparentFunc)
        self.ttt3.preview.vs_CamX.valueChanged.connect(self.ttt3.vs_previewCamXFunc)
        self.ttt3.preview.vs_CamY.valueChanged.connect(self.ttt3.vs_previewCamYFunc)
        self.ttt3.preview.vs_CamZ.valueChanged.connect(self.ttt3.vs_previewCamZFunc)
        self.ttt3.preview.vs_LookX.valueChanged.connect(self.ttt3.vs_previewLookXFunc)
        self.ttt3.preview.vs_LookY.valueChanged.connect(self.ttt3.vs_previewLookYFunc)
        self.ttt3.preview.vs_LookZ.valueChanged.connect(self.ttt3.vs_previewLookZFunc)
        self.ttt3.preview.btn_resetCamera.clicked.connect(self.ttt3.btn_previewResetCameraFunc)
        self.ttt3.preview.vs_LightX.valueChanged.connect(self.ttt3.vs_previewLightXFunc)
        self.ttt3.preview.vs_LightY.valueChanged.connect(self.ttt3.vs_previewLightYFunc)
        self.ttt3.preview.vs_LightZ.valueChanged.connect(self.ttt3.vs_previewLightZFunc)
        self.ttt3.preview.btn_resetLight.clicked.connect(self.ttt3.btn_previewResetLightFunc)
        self.ttt3.preview.btn_Reset.clicked.connect(self.ttt3.btn_previewResetFunc)
        self.ttt3.preview.btn_Save.clicked.connect(self.ttt3.btn_previewSaveFunc)
        self.ttt3.preview.btn_Load.clicked.connect(self.ttt3.btn_previewLoadFunc)
        self.ttt3.preview.cb_PresetCam.currentIndexChanged.connect(self.ttt3.cb_previewPresetCamFunc)
        self.ttt3.preview.cb_PresetLook.currentIndexChanged.connect(self.ttt3.cb_previewPresetLookFunc)
        self.ttt3.preview.cb_PresetLight.currentIndexChanged.connect(self.ttt3.cb_previewPresetLightFunc)
        self.ttt3.preview.lbl_CamX.mouseReleaseEvent = self.ttt3.lbl_CamXFunc
        self.ttt3.preview.lbl_CamY.mouseReleaseEvent = self.ttt3.lbl_CamYFunc
        self.ttt3.preview.lbl_CamZ.mouseReleaseEvent = self.ttt3.lbl_CamZFunc
        self.ttt3.preview.lbl_LookX.mouseReleaseEvent = self.ttt3.lbl_LookXFunc
        self.ttt3.preview.lbl_LookY.mouseReleaseEvent = self.ttt3.lbl_LookYFunc
        self.ttt3.preview.lbl_LookZ.mouseReleaseEvent = self.ttt3.lbl_LookZFunc
        self.ttt3.preview.lbl_LightX.mouseReleaseEvent = self.ttt3.lbl_LightXFunc
        self.ttt3.preview.lbl_LightY.mouseReleaseEvent = self.ttt3.lbl_LightYFunc
        self.ttt3.preview.lbl_LightZ.mouseReleaseEvent = self.ttt3.lbl_LightZFunc
        self.ttt3.preview.cb_fastPreview.stateChanged.connect(self.ttt3.fastPreviewFunc)

        # Set widgets to auto update on their mouseReleaseEvent.
        self.ttt3.preview.cb_Refresh.stateChanged.connect(self.ttt3.cb_previewRefreshFunc)

        # Checkboxes.
        for checkbox in [self.ttt3.preview.cb_TransparentBG, self.ttt3.preview.cb_Shadowless]:
            checkbox.stateChanged.connect(self.ttt3.previewAutoRefresh)

        # Buttons.
        for button in [self.ttt3.preview.btn_resetCamera, self.ttt3.preview.btn_resetLight]:
            button.clicked.connect(self.ttt3.previewAutoRefresh)

        # Spinboxes.
        for spinbox in [self.ttt3.preview.sb_Quality]:
            spinbox.valueChanged.connect(self.ttt3.previewAutoRefresh)

        # Sliders.
        for slider in [self.ttt3.preview.vs_CamX, self.ttt3.preview.vs_CamY, self.ttt3.preview.vs_CamZ,
                       self.ttt3.preview.vs_LookX, self.ttt3.preview.vs_LookY, self.ttt3.preview.vs_LookZ,
                       self.ttt3.preview.vs_LightX, self.ttt3.preview.vs_LightY, self.ttt3.preview.vs_LightZ]:
            slider.mouseReleaseEvent = self.ttt3.previewAutoRefresh

        # ComboBoxes.
        self.ttt3.preview.cb_Detail.currentIndexChanged.connect(self.ttt3.previewAutoRefresh)

        # Get a preview uniform render.
        self.ttt3.renderPreview()
        self.ttt3.previewLoaded = True
        #-------------------------------------------------------------------------------------------------------------------------------------------#

    def previewCloseEvent(self, event):
        '''Method that overloads the self.output_gui close event and the application.'''

        self.ttt3.gui.show()
        self.ttt3.preview.close()
        #-------------------------------------------------------------------------------------------------------------------------------------------#

    def applyPreviewSettings(self):
        '''Method to apply the currently loaded preview settings.'''

        # Reset the last cut of the renderData to allow the uniform to be drawn.
        self.ttt3.lastRenderData = ()

        # POV-Ray Options.

        # Checkboxes.
        self.ttt3.preview.cb_AA.setChecked(self.ttt3.antiAliasing)
        self.ttt3.preview.cb_Shadowless.setChecked(self.ttt3.shadowless)
        self.ttt3.preview.cb_Mosaic.setChecked(self.ttt3.mosaicPreview)
        if self.ttt3.transparentBG == " +UA":
            self.ttt3.preview.cb_TransparentBG.setChecked(True)
            self.ttt3.cb_previewTransparentFunc(2)
        else:
            self.ttt3.preview.cb_TransparentBG.setChecked(False)
            self.ttt3.cb_previewTransparentFunc(0)

        # Colours.
        # Spotlight Colour.
        self.ttt3.colourSelected(self, self.spotColour, "spotColour", self.ttt3.preview.lbl_PaletteSpot, self.ttt3.preview.le_PaletteSpot)
        # Environment Colour.
        self.ttt3.colourSelected(self, self.envColour, "envColour", self.ttt3.preview.lbl_PaletteEnv, self.ttt3.preview.le_PaletteEnv)
        # Background Colour.
        self.ttt3.colourSelected(self, self.bgColour, "bgColour", self.ttt3.preview.lbl_PaletteBack, self.ttt3.preview.le_PaletteBack)

        # Resolution.
        self.ttt3.preview.sb_Width.setValue(self.width)
        self.ttt3.preview.le_Height.setText(str(self.height))
        # Quality.
        self.ttt3.preview.sb_Quality.setValue(self.ttt3.quality)
        # Cloth.
        self.ttt3.preview.cb_Detail.setCurrentIndex(self.ttt3.clothDetail)
        # Slider Bars
        self.ttt3.preview.vs_CamX.setValue(self.camX)
        self.ttt3.preview.lbl_CamX.setText(self.ttt3.convertIntToFloatStr(self.camX, 10))
        self.ttt3.preview.vs_CamY.setValue(self.camY)
        self.ttt3.preview.lbl_CamY.setText(self.ttt3.convertIntToFloatStr(self.camY, 10))
        self.ttt3.preview.vs_CamZ.setValue(self.camZ)
        self.ttt3.preview.lbl_CamZ.setText(self.ttt3.convertIntToFloatStr(self.camZ, 10))
        self.ttt3.preview.vs_LookX.setValue(self.lookX)
        self.ttt3.preview.lbl_LookX.setText(self.ttt3.convertIntToFloatStr(self.lookX, 10))
        self.ttt3.preview.vs_LookY.setValue(self.lookY)
        self.ttt3.preview.lbl_LookY.setText(self.ttt3.convertIntToFloatStr(self.lookY, 10))
        self.ttt3.preview.vs_LookZ.setValue(self.lookZ)
        self.ttt3.preview.lbl_LookZ.setText(self.ttt3.convertIntToFloatStr(self.lookZ, 10))
        self.ttt3.preview.vs_LightX.setValue(self.lightX)
        self.ttt3.preview.lbl_LightX.setText(self.ttt3.convertIntToFloatStr(self.lightX, 10))
        self.ttt3.preview.vs_LightY.setValue(self.lightY)
        self.ttt3.preview.lbl_LightY.setText(self.ttt3.convertIntToFloatStr(self.lightY, 10))
        self.ttt3.preview.vs_LightZ.setValue(self.lightZ)
        self.ttt3.preview.lbl_LightZ.setText(self.ttt3.convertIntToFloatStr(self.lightZ, 10))
        self.ttt3.preview.cb_fastPreview.setChecked(self.ttt3.fastPreview)
        # Combo Boxes
        self.ttt3.preview.cb_PresetCam.setCurrentIndex(self.cbCamIndex)
        self.ttt3.preview.cb_PresetLook.setCurrentIndex(self.cbLookIndex)
        self.ttt3.preview.cb_PresetLight.setCurrentIndex(self.cbLightIndex)
        #-------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_PaletteSpotFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            self.ttt3.openColourPicker(self, self.spotColour, "spotColour", self.ttt3.preview.lbl_PaletteSpot, self.ttt3.preview.le_PaletteSpot)
        except Exception as e:
            handleException(e)
        # --------------------------------------------------------------------------------------------------------------------------------------------#

    def btn_PaletteEnvFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            self.ttt3.openColourPicker(self, self.envColour, "envColour", self.ttt3.preview.lbl_PaletteEnv, self.ttt3.preview.le_PaletteEnv)
        except Exception as e:
            handleException(e)
        # --------------------------------------------------------------------------------------------------------------------------------------------#


    def btn_PaletteBackFunc(self):
        '''Method for opening a colour palette dialog.'''

        try:
            self.ttt3.openColourPicker(self, self.bgColour, "bgColour", self.ttt3.preview.lbl_PaletteBack, self.ttt3.preview.le_PaletteBack)
        except Exception as e:
            handleException(e)
        # --------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------#


# --------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Functions.                                                                   #
# --------------------------------------------------------------------------------------------------------------------------------------------------#
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
    # ----------------------------------------------------------------------------------------------------------------------------------------------#

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

    # Show error message.
    msg = r"Error: Uh-Oh! TTT3 has encountered an error. Please submit 'TTT3\TTT3 Crash.log' to the Internet Office."
    return ctypes.windll.user32.MessageBoxA(0, msg.encode('ascii'), "TTT3".encode('ascii'), 0)
    # ----------------------------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------------------------------#


# --------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Main Program.                                                                 #
# --------------------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    print("ERROR! This Python module cannot be ran standalone and must be ran using TTT3.py")
# --------------------------------------------------------------------------------------------------------------------------------------------------#