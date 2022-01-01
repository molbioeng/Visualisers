# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 11:02:45 2022

@author: FM

Plot interaction - right clicking the plot to display Raman spectra,
and indicators for what pixel is currently being selected.
"""


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import mat73

class PlotInteract:
    def __init__(self, ax, data):
        self.ax = ax
        self.data = data
        self.text = ax.text(0.7, 0.95, '', transform=ax.transAxes, color = 'w')
        self.square = Rectangle((0,0), 1,1, fill = None, color='r')
        ax.add_patch(self.square)
        self.creating_background = False
        self.press = None

    def connect(self):
        """Connect to all the events we need"""
        self.ciddraw = self.ax.figure.canvas.mpl_connect('draw_event', self.on_draw)
        self.cidpress = self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidmotion = self.ax.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
        
    def on_draw(self, event):
        """Create background image of data when initially plotted. 
        This is for efficiency so the image doesn't need to be replotted every time the cursor moves..."""
        if self.creating_background: return #discard calls triggered from within this function
        self.creating_background = True
        self.text.set_visible(False)
        self.square.set_visible(False)
        self.ax.figure.canvas.draw()
        self.background = self.ax.figure.canvas.copy_from_bbox(self.ax.bbox)
        self.text.set_visible(True)
        self.square.set_visible(True)
        self.creating_background = False
        
    def on_press(self, event):
        """Plot the associated Raman spectra when a pixel is right-clicked"""
        if event.inaxes!=self.ax.axes: return #Return if plot not clicked
        if str(event.button)!='MouseButton.RIGHT': return #Ensure right click to open new plot
        fig2, ax2 = plt.subplots()
        plt.plot(self.data[int(round(event.ydata))][int(round(event.xdata))][:]) #Double check why this is flipped
        plt.title('Raman Spectra at pixel (%i, %i)' % (int(round(event.xdata)), int(round(event.ydata))))
        plt.show()

    def on_motion(self, event):
        """Move the square indicating selected pixel"""
        if event.inaxes != self.ax.axes: return
        x, y = int(round(event.xdata)), int(round(event.ydata))
        # update the line positions
        self.text.set_text('x=%i, y=%i' % (x, y))
        self.square.set_xy([x-0.5,y-0.5])
        
        #Updating the display
        self.ax.figure.canvas.restore_region(self.background)
        self.ax.draw_artist(self.text)
        self.ax.draw_artist(self.square)
        self.ax.figure.canvas.blit(self.ax.bbox)

