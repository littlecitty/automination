import sys
import subprocess
from PyQt5 import QtWidgets
from PyQt5 import uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("test1.ui", self)

        # Connect the "Enter" button to the function
        self.ipenter.clicked.connect(self.scan_ip)

    def scan_ip(self):
        ip = self.ip.text()  # Get the IP entered by the user
        if not ip:
            self.textBrowser.setPlainText("Please enter a valid IP address.")
            return
        
        try:
            # Run nmap
            nmap_process = subprocess.Popen(["nmap", "-sV", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            nmap_output, _ = nmap_process.communicate()

            # Run dirb
            dirb_process = subprocess.Popen(["dirb", f"http://{ip}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            dirb_output, _ = dirb_process.communicate()

            # Run nikto
            nikto_process = subprocess.Popen(["nikto", "-h", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            nikto_output, _ = nikto_process.communicate()

            # Combine all outputs
            combined_output = (
                "=== NMAP Output ===\n" + nmap_output.decode() +
                "\n\n=== DIRB Output ===\n" + dirb_output.decode() +
                "\n\n=== NIKTO Output ===\n" + nikto_output.decode()
            )

            # Display output in QTextBrowser
            self.textBrowser.setPlainText(combined_output)

        except Exception as e:
            self.textBrowser.setPlainText(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
