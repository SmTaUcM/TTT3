'''#-------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        Slider.py
# Purpose:     Overloads the original QSlider class to allow direct jump to when clicking on a slider bar.
# Version:     v1.00
# Author:      Stuart Macintosh
#
# Created:     17/02/2021
#-------------------------------------------------------------------------------------------------------------------------------------------------#'''


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Imports.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
from PyQt5.QtWidgets import QSlider, QStyleOptionSlider, QStyle
from PyQt5.QtCore import Qt

#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Classes.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
class Slider(QSlider): # Bookmark.
    '''Class overloading the original QSlider class to alow direct go to clicking on the slider's bar.'''

    def mousePressEvent(self, event):
        '''Method to handle clicking on the slider.'''

        super(Slider, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.pos())
            self.setValue(val)
        #--------------------------------------------------------------------------------------------------------------------------------------------#

    def pixelPosToRangeValue(self, pos):
        '''Method for enabling the direct goto functionality.'''

        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        gr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)

        if self.orientation() == Qt.Horizontal:
            sliderLength = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLength + 1
        else:
            sliderLength = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLength + 1;
        pr = pos - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == Qt.Horizontal else pr.y()
        return QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin, sliderMax - sliderMin, opt.upsideDown)
        #--------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------------#
