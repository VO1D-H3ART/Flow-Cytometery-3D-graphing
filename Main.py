import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import os, sys, openpyxl

from flowio import FlowData

from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QToolBar, QMainWindow, QMenu, QDialog
from PyQt6.QtGui import QAction

# This is the main class that will hold the GUI
# A class is a way to group functions and variables together
# def __init__ is a special function that is called when the class is created. It is needed everytime you make a class for it is called a constructor
    # Its a setup function that runs as soon as the app starts up
    # you can set up intial states with __init__ without it we would have to call a setup function everytime we wanted to use the class which is annoying
    # self is the first parameter in __init__ and is a reference to the specfic object being created from the class and it is always the first parameter for __inti__
        # this means that every variable must be prefaced with self. to be used in the class these are called instance variables
            # local variables only work within the function they are created in therefore they do not have the self. prefix
    # super().__init__ is a way to call the parent class of the class that is being created

class Main_GUI(QMainWindow):
    # This function Hold the GUI
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3D Graph Generator')  # Set the title of the main window
        self.setFixedSize(500,500)

        # Create a central widget and layout
        self.central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(self.central_widget)  # Set it as the central widget
        self.layout = QGridLayout(self.central_widget)  # Create a layout for the central widget

        # Create buttons
        self.plot_button = QPushButton('Plot Data', parent=self.central_widget)  # Create a button with the text "Plot Data"
        # Connect button to plotting function
        self.plot_button.clicked.connect(lambda: self.plot_data(self.z_input.text(), self.y_input.text(), self.x_input.text(), self.title_input.text()))
        
        self.generate_button = QPushButton('Generate 3D Points', parent=self.central_widget)# Create a button with the text "Generate 3D Points"
        self.generate_button.clicked.connect(self.pull_data)# Connect button to read the excel file and to make the 3D points

        

        # Create a menu bar
        menu_bar = self.menuBar()  # Create the menu bar
        file_menu = menu_bar.addMenu("File")  # Add "File" menu
        help_menu = menu_bar.addMenu("Help")  # Add "Help" menu


        #Sytlesheet
        menu_bar.setStyleSheet("""
        QMenu::item {
            text-align: left;
            padding: 8px 16px;
        }
        Qmenu{
            margin: 1px;
    }
        """)         

        # Create an "Open File" action
        open_file_action = QAction("Open File", self)
        open_file_action.setStatusTip("Open an Excel file")

        # Create a "Help" action
        open_help_action = QAction("Help", self)
        open_help_action.setStatusTip("Open the help menu") 
        
        open_file_action.triggered.connect(self.get_file)  # Connect the action
        file_menu.addAction(open_file_action)  # Add the action to the "File" menu

        open_help_action.triggered.connect(self.help)  # Connect the action
        help_menu.addAction(open_help_action)  # Add the action to the "Help" menu


        # Create input fields for graph labels
        self.title_label = QLabel('Graph Title', self.central_widget)
        self.title_input = QLineEdit(self.central_widget)

        self.x_label = QLabel('X-axis Label', self.central_widget)
        self.x_input = QLineEdit(self.central_widget)
        
        self.y_label = QLabel('Y-axis Label', self.central_widget)
        self.y_input = QLineEdit(self.central_widget)
        
        self.z_label = QLabel('Z-axis Label', self.central_widget)
        self.z_input = QLineEdit(self.central_widget)
        
        self.dialog_label = QLabel("No File selected", self.central_widget)


        # Add widgets to the layout
        self.layout.addWidget(self.title_label, 0, 0)
        self.layout.addWidget(self.title_input, 0, 1)
        self.layout.addWidget(self.x_label, 1, 0)
        self.layout.addWidget(self.x_input, 1, 1)
        self.layout.addWidget(self.y_label, 2, 0)
        self.layout.addWidget(self.y_input, 2, 1)
        self.layout.addWidget(self.z_label, 3, 0)
        self.layout.addWidget(self.z_input, 3, 1)
        self.layout.addWidget(self.plot_button, 6, 6)
        self.layout.addWidget(self.generate_button, 6, 5)
        self.layout.addWidget(self.dialog_label, 5, 0, 1, 2)



    # This function pulls the file name
    def get_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            caption='Select File',
            filter='Flow Cytometry Standard Files (*.fcs)',
            directory=os.getcwd()
        )
        if self.file_path:  # Check if the user selected a file
            file_name = os.path.basename(self.file_path)  # Extract only the filename
            self.dialog_label.setText(f"Selected File: {file_name}")  # Update label with filename
            print(f"Full file path: {self.file_path}")  # Debugging output
            

    def help(self):
        print("Help Menu")
        help_dialog = QDialog(self)
        help_dialog.setWindowTitle("Help Window")
        help_dialog.setFixedSize(400, 200)

        help_dialog_label = QLabel("- The help button actually works this time around")
        help_dialog_label_axis = QLabel("- Axis textboxes is  you get to input the names of your axis that will \n be projected onto the graph \n \n- Column Name textboxes are going to store the names of colmun in \n the program and used to find the data in the excel sheet you provide")
        

        help_dialog_layout = QGridLayout()

        help_dialog_layout.addWidget(help_dialog_label, 0, 0) #Row 0, Column 0
        help_dialog_layout.addWidget(help_dialog_label_axis, 1,0) # Row 1, Column 0
    
        help_dialog.setLayout(help_dialog_layout)
        help_dialog.exec()


    def pull_data(self):
        with open(self.file_path, 'rb') as f:
            flow_data = FlowData(f)

            print(flow_data.channels)
            print(f"Looking for {self.x_input.text()}, {self.y_input.text()}, {self.z_input.text()}")

            # Extract matching keys
            pre_x_channel_key = [key for key, value in flow_data.channels.items() if value.get('PnN', '').strip() == self.x_input.text().strip()]
            pre_y_channel_key = [key for key, value in flow_data.channels.items() if value.get('PnN', '').strip() == self.y_input.text().strip()]
            pre_z_channel_key = [key for key, value in flow_data.channels.items() if value.get('PnN', '').strip() == self.z_input.text().strip()]


        # Convert keys to integers
            x_channel_key = int(pre_x_channel_key[0])
            y_channel_key = int(pre_y_channel_key[0])
            z_channel_key = int(pre_z_channel_key[0])

            # Reshape the flat 1D array into a 2D array
            num_channels = len(flow_data.channels)  # Number of columns
            num_events = len(flow_data.events) // num_channels  # Number of rows
            events_array = np.array(flow_data.events).reshape((num_events, num_channels))

            # Extract data
            x_data = events_array[:, x_channel_key].astype(float)
            y_data = events_array[:, y_channel_key].astype(float)
            z_data = events_array[:, z_channel_key].astype(float)

            # Combine into one array
            self.datapoints = np.column_stack((x_data, y_data, z_data))

            print(f"All Data Points:\n{self.datapoints}\nEnd of data points")




    # This plots data pulled from pull_data 
    def plot_data(self, z_input, y_input, x_input, title_input):
        self.ax = plt.axes(projection='3d')  # Create an axis

        self.ax.scatter( self.datapoints[:,0],  #Pulls X values out of the comlumn stack
                        self.datapoints[:,1],   #Pulls Y values out of the comlumn stack
                        self.datapoints[:,2]    #Pulls Z values out of the comlumn stack
        )

        # Set labels and title
        self.ax.set_title(title_input if title_input else '3D Graph')
        self.ax.set_xlabel(x_input if x_input else 'X-axis')
        self.ax.set_ylabel(y_input if y_input else 'Y-axis')
        self.ax.set_zlabel(z_input if z_input else 'Z-axis')

        plt.show()  # Show the plot



if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    gui = Main_GUI()  # Instantiate the main GUI
    gui.show()  # Show the main GUI
    app.exec()  # Run the application
