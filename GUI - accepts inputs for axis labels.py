import numpy as np #generates data
import  matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit



def GUI():
    app = QApplication([]) # holds the event loop basically the heart of the GUI
    window = QWidget()

    layout = QGridLayout(window) #Vertical Box layout where the window is the parent
    button = QPushButton('Plot Data', parent=window) #this makes a button   
    label = QLabel('Click the button to plot the data', parent=window) #this makes a label


    #This makes Textboxes for the user to input the labels for the X, Y, and Z axis
    x_label = QLabel('X-axis Label', window) 
    x_input = QLineEdit(window) 

    y_label = QLabel('Y-axis Label', window)
    y_input = QLineEdit(window) 

    z_label = QLabel('Z-axis Label', window)
    z_input = QLineEdit(window) 
    

    #this connects the button to the function that will plot the data
    button.clicked.connect(
        lambda: plot_data(z_input.text(), y_input.text(), x_input.text()) #Lambda is a way to pass in arguments to a function
        
        ) 

    ##this adds the button to the layout along with other set up things to make sure that widgets and things acutally apper.
    layout.addWidget(button, 4,6) #Spwans in the button - at grid position 0,1
    layout.addWidget(label, 4, 5) #Spawns in the label - at grid postion 0,0

    #this is for adding the textboxes to accpet input along with thier labels
    layout.addWidget(x_label, 1, 0)
    layout.addWidget(x_input, 1, 1)

    layout.addWidget(y_label, 2, 0)
    layout.addWidget(y_input, 2, 1)

    layout.addWidget(z_label, 3, 0)
    layout.addWidget(z_input, 3, 1)



    window.setLayout(layout) #Spawns in the layout with the label
    window.setWindowTitle('3D Graph Generator') #Sets title in the window   
    window.setGeometry(100, 100, 400, 200) # Sets the size of the window

    


    window.show()#Shows the window
    app.exec()#Runs the app
    return z_input.text(), y_input.text(), x_input.text()



def plot_data(z_input, y_input, x_input): 
    ax = plt.axes(projection='3d') # this makes an axis
    ##ax.scatter(1, 2, 3) #this makes a single point at the coordinates (1,2,3)

    x_data = np.random.randint(0, 100, 500)
    y_data = np.random.randint(0, 100, 500)
    z_data = np.random.randint(0, 100, 500)

    ax.scatter(x_data, y_data, z_data, marker="v") #this makes a scatter plot of the data

    ##this is the labels for the axis
    ax.set_title('Random Data')
    ax.set_xlabel(x_input if x_input else 'X-axis')
    ax.set_ylabel(y_input if y_input else 'Y-axis')
    ax.set_zlabel(z_input if z_input else 'Z-axis')

    plt.show() #this shows the plot

GUI()