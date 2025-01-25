import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import os, sys

from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QToolBar, QMainWindow, QMenu
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

        # Create a central widget and layout
        self.central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(self.central_widget)  # Set it as the central widget
        self.layout = QGridLayout(self.central_widget)  # Create a layout for the central widget

        # Create widgets
        self.button = QPushButton('Plot Data', parent=self.central_widget)  # Create a button
        self.label = QLabel('Click the button to plot the data', parent=self.central_widget)  # Create a label

        # Create a menu bar
        menu_bar = self.menuBar()  # Create the menu bar
        file_menu = menu_bar.addMenu("File")  # Add "File" menu


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
        
        open_file_action.triggered.connect(self.get_file)  # Connect the action
        file_menu.addAction(open_file_action)  # Add the action to the "File" menu

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

        # Connect button to plotting function
        self.button.clicked.connect(
            lambda: self.plot_data(self.z_input.text(), self.y_input.text(), self.x_input.text(), self.title_input.text())
        )

        # Add widgets to the layout
        self.layout.addWidget(self.title_label, 0, 0)
        self.layout.addWidget(self.title_input, 0, 1)
        self.layout.addWidget(self.x_label, 1, 0)
        self.layout.addWidget(self.x_input, 1, 1)
        self.layout.addWidget(self.y_label, 2, 0)
        self.layout.addWidget(self.y_input, 2, 1)
        self.layout.addWidget(self.z_label, 3, 0)
        self.layout.addWidget(self.z_input, 3, 1)
        self.layout.addWidget(self.label, 4, 0)
        self.layout.addWidget(self.button, 4, 1)
        self.layout.addWidget(self.dialog_label, 5, 0, 1, 2)

    # This function pulls the file name
    def get_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            caption='Select File',
            filter='Excel Files (*.xlsx)',
            directory=os.getcwd()
        )
        if file_path:  # Check if the user selected a file
            file_name = os.path.basename(file_path)  # Extract only the filename
            self.dialog_label.setText(f"Selected File: {file_name}")  # Update label with filename
            print(file_path)  # Debugging output

    # This plots data pulled from file_handling; right now, it's random
    def plot_data(self, z_input, y_input, x_input, title_input):
        self.ax = plt.axes(projection='3d')  # Create an axis

        # Generate random data for demonstration purposes
        self.x_data = np.random.randint(0, 100, 500)
        self.y_data = np.random.randint(0, 100, 500)
        self.z_data = np.random.randint(0, 100, 500)

        self.ax.scatter(self.x_data, self.y_data, self.z_data, marker="v")  # Create a scatter plot

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
