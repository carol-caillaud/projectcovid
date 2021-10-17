import numpy as np
import matplotlib.pyplot as plt

# create a subplot with 2 rows and 1 columns
fig, ax = plt.subplots(2,1)
fig = plt.figure() # create the canvas for plotting
ax1 = plt.subplot(2,1,1) 
# (2,1,1) indicates total number of rows, columns, and figure number respectively
ax2 = plt.subplot(2,1,2)