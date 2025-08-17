import sys
import resources
from PyQt5.QtWidgets import QApplication
print(" app started ")
from path_manager import path_manager
from grui.main_window import MainApp

def main():

    # create qt aspp 
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # create main window
    print(" main window loaded ")
    main_window = MainApp()
    main_window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
