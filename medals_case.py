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
        except Exception as e:
            handleException(e)
        #-------------------------------------------------------------------------------------------------------------------------------------------#

    def showPreviewDialog(self):
        '''Method to open the render preview / options GUI.'''

        self.previewLoaded = False
        # Load our GUI file 'data\uis\preview.ui'.
        self.preview = uic.loadUi(r"data\uis\preview.ui")

        # Set the correct window title.
        self.preview.setWindowTitle("TTT3 Rendering Options - Medals Case")

        # Show the preview GUI.
        self.preview.show()
        setPixelSizes(self.preview)
        self.preview.closeEvent = self.previewCloseEvent
        self.ttt3.gui.hide()
        self.preview.lbl_wait.setAttribute(Qt.WA_TranslucentBackground)
        self.preview.lbl_wait.setHidden(True)

        # Apply setttings.
        self.applyPreviewSettings()

        # Connections.
##        self.preview.btn_raytrace.clicked.connect(self.launchPOVRay)
##        self.preview.btn_preview.clicked.connect(self.renderPreview)
##        self.preview.btn_PaletteSpot.clicked.connect(self.btn_PaletteSpotFunc)
##        self.preview.btn_PaletteEnv.clicked.connect(self.btn_PaletteEnvFunc)
##        self.preview.btn_PaletteBack.clicked.connect(self.btn_PaletteBackFunc)
##        self.preview.btn_resetColours.clicked.connect(self.btn_previewResetColoursFunc)
##        self.preview.sb_Width.valueChanged.connect(self.sb_previewWidthFunc)
##        self.preview.btn_resetOptions.clicked.connect(self.btn_previewResetOptionsFunc)
##        self.preview.sb_Quality.valueChanged.connect(self.sb_previewQualityFunc)
##        self.preview.cb_Detail.currentIndexChanged.connect(self.cb_previewDetailFunc)
##        self.preview.cb_AA.stateChanged.connect(self.cb_previewAAFunc)
##        self.preview.cb_Shadowless.stateChanged.connect(self.cb_previewShadowlessFunc)
##        self.preview.cb_Mosaic.stateChanged.connect(self.cb_previewMosaicFunc)
##        self.preview.cb_TransparentBG.stateChanged.connect(self.cb_previewTransparentFunc)
##        self.preview.vs_CamX.valueChanged.connect(self.vs_previewCamXFunc)
##        self.preview.vs_CamY.valueChanged.connect(self.vs_previewCamYFunc)
##        self.preview.vs_CamZ.valueChanged.connect(self.vs_previewCamZFunc)
##        self.preview.vs_LookX.valueChanged.connect(self.vs_previewLookXFunc)
##        self.preview.vs_LookY.valueChanged.connect(self.vs_previewLookYFunc)
##        self.preview.vs_LookZ.valueChanged.connect(self.vs_previewLookZFunc)
##        self.preview.btn_resetCamera.clicked.connect(self.btn_previewResetCameraFunc)
##        self.preview.vs_LightX.valueChanged.connect(self.vs_previewLightXFunc)
##        self.preview.vs_LightY.valueChanged.connect(self.vs_previewLightYFunc)
##        self.preview.vs_LightZ.valueChanged.connect(self.vs_previewLightZFunc)
##        self.preview.btn_resetLight.clicked.connect(self.btn_previewResetLightFunc)
##        self.preview.btn_Reset.clicked.connect(self.btn_previewResetFunc)
##        self.preview.btn_Save.clicked.connect(self.btn_previewSaveFunc)
##        self.preview.btn_Load.clicked.connect(self.btn_previewLoadFunc)
##        self.preview.cb_PresetCam.currentIndexChanged.connect(self.cb_previewPresetCamFunc)
##        self.preview.cb_PresetLook.currentIndexChanged.connect(self.cb_previewPresetLookFunc)
##        self.preview.cb_PresetLight.currentIndexChanged.connect(self.cb_previewPresetLightFunc)
##        self.preview.lbl_CamX.mouseReleaseEvent = self.lbl_CamXFunc
##        self.preview.lbl_CamY.mouseReleaseEvent = self.lbl_CamYFunc
##        self.preview.lbl_CamZ.mouseReleaseEvent = self.lbl_CamZFunc
##        self.preview.lbl_LookX.mouseReleaseEvent = self.lbl_LookXFunc
##        self.preview.lbl_LookY.mouseReleaseEvent = self.lbl_LookYFunc
##        self.preview.lbl_LookZ.mouseReleaseEvent = self.lbl_LookZFunc
##        self.preview.lbl_LightX.mouseReleaseEvent = self.lbl_LightXFunc
##        self.preview.lbl_LightY.mouseReleaseEvent = self.lbl_LightYFunc
##        self.preview.lbl_LightZ.mouseReleaseEvent = self.lbl_LightZFunc
##        self.preview.cb_fastPreview.stateChanged.connect(self.fastPreviewFunc)
##
##        # Set widgets to auto update on their mouseReleaseEvent.
##        self.preview.cb_Refresh.stateChanged.connect(self.cb_previewRefreshFunc)
##
##        # Checkboxes.
##        for checkbox in [self.preview.cb_TransparentBG, self.preview.cb_Shadowless]:
##            checkbox.stateChanged.connect(self.previewAutoRefresh)
##
##        # Buttons.
##        for button in [self.preview.btn_resetCamera, self.preview.btn_resetLight]:
##            button.clicked.connect(self.previewAutoRefresh)
##
##        # Spinboxes.
##        for spinbox in [self.preview.sb_Quality]:
##            spinbox.valueChanged.connect(self.previewAutoRefresh)
##
##        # Sliders.
##        for slider in [self.preview.vs_CamX, self.preview.vs_CamY, self.preview.vs_CamZ,
##                       self.preview.vs_LookX, self.preview.vs_LookY, self.preview.vs_LookZ,
##                       self.preview.vs_LightX, self.preview.vs_LightY, self.preview.vs_LightZ]:
##            slider.mouseReleaseEvent = self.previewAutoRefresh
##
##        # ComboBoxes.
##        self.preview.cb_Detail.currentIndexChanged.connect(self.previewAutoRefresh)
##
##        # Get a preview uniform render.
##        self.renderPreview()
##        self.previewLoaded = True
        #-------------------------------------------------------------------------------------------------------------------------------------------#

    def previewCloseEvent(self, event):
        '''Method that overloads the self.output_gui close event and the application.'''

        self.ttt3.gui.show()
        self.preview.close()
        #-------------------------------------------------------------------------------------------------------------------------------------------#

    def applyPreviewSettings(self):
        '''Method to apply the currently loaded preview settings.'''

        pass
##        # Reset the last cut of the renderData to allow the uniform to be drawn.
##        self.lastRenderData = ()
##
##        if self.uniform != "helmet":
##            # Colours.
##            # Spotlight Colour.
##            self.colourSelected(self.spotColour, "spotColour", self.preview.lbl_PaletteSpot, self.preview.le_PaletteSpot)
##            # Environment Colour.
##            self.colourSelected(self.envColour, "envColour", self.preview.lbl_PaletteEnv, self.preview.le_PaletteEnv)
##            # Background Colour.
##            self.colourSelected(self.bgColour, "bgColour", self.preview.lbl_PaletteBack, self.preview.le_PaletteBack)
##            # POV-Ray Options.
##            # Resolution.
##            self.preview.sb_Width.setValue(self.width)
##            self.preview.le_Height.setText(str(self.height))
##            # Quality.
##            self.preview.sb_Quality.setValue(self.quality)
##            # Cloth.
##            self.preview.cb_Detail.setCurrentIndex(self.clothDetail)
##            # Checkboxes.
##            self.preview.cb_AA.setChecked(self.antiAliasing)
##            self.preview.cb_Shadowless.setChecked(self.shadowless)
##            self.preview.cb_Mosaic.setChecked(self.mosaicPreview)
##            if self.transparentBG == " +UA":
##                self.preview.cb_TransparentBG.setChecked(True)
##                self.cb_previewTransparentFunc(2)
##            else:
##                self.preview.cb_TransparentBG.setChecked(False)
##                self.cb_previewTransparentFunc(0)
##            # Slider Bars
##            self.preview.vs_CamX.setValue(self.camX)
##            self.preview.lbl_CamX.setText(self.convertIntToFloatStr(self.camX, 10))
##            self.preview.vs_CamY.setValue(self.camY)
##            self.preview.lbl_CamY.setText(self.convertIntToFloatStr(self.camY, 10))
##            self.preview.vs_CamZ.setValue(self.camZ)
##            self.preview.lbl_CamZ.setText(self.convertIntToFloatStr(self.camZ, 10))
##            self.preview.vs_LookX.setValue(self.lookX)
##            self.preview.lbl_LookX.setText(self.convertIntToFloatStr(self.lookX, 10))
##            self.preview.vs_LookY.setValue(self.lookY)
##            self.preview.lbl_LookY.setText(self.convertIntToFloatStr(self.lookY, 10))
##            self.preview.vs_LookZ.setValue(self.lookZ)
##            self.preview.lbl_LookZ.setText(self.convertIntToFloatStr(self.lookZ, 10))
##            self.preview.vs_LightX.setValue(self.lightX)
##            self.preview.lbl_LightX.setText(self.convertIntToFloatStr(self.lightX, 10))
##            self.preview.vs_LightY.setValue(self.lightY)
##            self.preview.lbl_LightY.setText(self.convertIntToFloatStr(self.lightY, 10))
##            self.preview.vs_LightZ.setValue(self.lightZ)
##            self.preview.lbl_LightZ.setText(self.convertIntToFloatStr(self.lightZ, 10))
##            self.preview.cb_fastPreview.setChecked(self.fastPreview)
##            # Combo Boxes
##            self.preview.cb_PresetCam.setCurrentIndex(self.cbCamIndex)
##            self.preview.cb_PresetLook.setCurrentIndex(self.cbLookIndex)
##            self.preview.cb_PresetLight.setCurrentIndex(self.cbLightIndex)
        #-------------------------------------------------------------------------------------------------------------------------------------------#
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