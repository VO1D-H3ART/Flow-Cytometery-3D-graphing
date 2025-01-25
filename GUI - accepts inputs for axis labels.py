import numpy as np #generates data
import  matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import os

from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QFileDialog

#This is the main class that will hold the GUI
#A class is a way to group functions and variables together
# def __init__ is a special function that is called when the class is created. It is needed everytime you make a class for it is called a constructor
    # Its a setup function that runs as soon as the app starts up
    # you can set up intial states with __init__ without it we would have to call a setup function everytime we wanted to use the class which is annoying
    # self is the first parameter in __init__ and is a reference to the specfic object being created from the class and it is always the first parameter for __inti__
        #this means that every variable must be prefaced with self. to be used in the class these are called instance variables
            #local variables only work within the function they are created in therefore they do not have the self. prefix
    #super().__init__ is a way to call the parent class of the class that is being created 





class Main_GUI:
    # This function Hold the GUI
    def __init__(self):
        self.window = QWidget()

        self.layout = QGridLayout(self.window) #Vertical Box layout where the window is the parent
        self.button = QPushButton('Plot Data', parent=self.window) #this makes a button   
        self.label = QLabel('Click the button to plot the data', parent=self.window) #this makes a label


        #This makes Textboxes for the user to input the labels for the X, Y, and Z axis
        self.title_label = QLabel('Graph Title', self.window)
        self.title_input = QLineEdit(self.window)
        
        self.x_label = QLabel('X-axis Label', self.window) 
        self.x_input = QLineEdit(self.window) 

        self.y_label = QLabel('Y-axis Label', self.window)
        self.y_input = QLineEdit(self.window) 

        self.z_label = QLabel('Z-axis Label', self.window)
        self.z_input = QLineEdit(self.window) 

        self.select_button = QPushButton('Select File', self.window)
        self.select_button.clicked.connect(self.get_file)
        self.dialog_label = QLabel("No File selected", self.window)


        #this connects the button to the function that will plot the data
        self.button.clicked.connect(
            lambda: self.plot_data(self.z_input.text(), self.y_input.text(), self.x_input.text(), self.title_input.text()) #this is a lambda function that calls the plot_data function with the text from the textboxes) 
        )

        ##this adds the button to the layout along with other set up things to make sure that widgets and things acutally apper.
        self.layout.addWidget(self.button, 4,6) #Spwans in the button - at grid position 0,1
        self.layout.addWidget(self.label, 4, 5) #Spawns in the label - at grid postion 0,0

        #this is for adding the textboxes to accpet input along with thier labels

        self.layout.addWidget(self.title_label, 0, 0)
        self.layout.addWidget(self.title_input, 0, 1)

        self.layout.addWidget(self.x_label, 1, 0)
        self.layout.addWidget(self.x_input, 1, 1)

        self.layout.addWidget(self.y_label, 2, 0)
        self.layout.addWidget(self.y_input, 2, 1)

        self.layout.addWidget(self.z_label, 3, 0)   
        self.layout.addWidget(self.z_input, 3, 1)   

        self.layout.addWidget(self.select_button, 5, 0) 
        self.layout.addWidget(self.dialog_label, 5, 1)  


        self.window.show() #this shows the window BRO THIS IS FOR YOU. YEA YOU ALI GODDAMN IT YOU IDIOT HOW DID YOU FORGET THIS!!! YOU TOOK A WHOLE   H O U R   TO FIX THIS!!!!
    
    #This function pulls the file name 
    def get_file(self):
        file_path, _ = QFileDialog.getOpenFileName(  # Extract the first element (file path) this is due to using the underscore
        caption='Select File',
        filter='Excel Files (*.xlsx)',
        directory=os.getcwd()
    )
        if file_path:  # Check if the user selected a file
            file_name = os.path.basename(file_path)  # Extract only the filename
            self.dialog_label.setText(f"Selected File: {file_name}")  # Update label with filename
            print(file_path)  # Debugging output

    #This is suppose to handle the .xlsx file and append them to the dataframe
    def file_handling(self):
        pass
        
    #this plots data pulled from file_handling right now it's random
    def plot_data(self, z_input, y_input, x_input, title_input):
        self.ax = plt.axes(projection='3d') # this makes an axis

        self.x_data = np.random.randint(0, 100, 500)
        self.y_data = np.random.randint(0, 100, 500)
        self.z_data = np.random.randint(0, 100, 500)

        self.ax.scatter(self.x_data, self.y_data, self.z_data, marker="v") #this makes a scatter plot of the data

        ##this is the labels for the axis
        self.ax.set_title(title_input if title_input else '3D Graph')
        self.ax.set_xlabel(x_input if x_input else 'X-axis')
        self.ax.set_ylabel(y_input if y_input else 'Y-axis')
        self.ax.set_zlabel(z_input if z_input else 'Z-axis')

        plt.show() #this shows the plot

if __name__ == '__main__':
    app = QApplication([]) #this makes the app
    gui = Main_GUI()
    app.exec() #this runs the app




