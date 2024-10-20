import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileDialog
from PySide6.QtCore import QDir
from assets.ui import Ui_UI

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_UI()
        self.ui.setupUi(self)

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(QDir.currentPath()))

        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.Directory)
        self.dialog.setOption(QFileDialog.ShowDirsOnly, True)

        self.ui.open.clicked.connect(self.show_open_dialog)
        self.ui.save.clicked.connect(self.save_main)

        self.show_open_dialog()

    def show_open_dialog(self):
        if self.dialog.exec():
            selected_folder = self.dialog.selectedFiles()[0]
            self.ui.treeView.setRootIndex(self.model.index(self.dialog.selectedFiles()[0]))
            print("Selected folder:", selected_folder)

    def save_main(self):
        with open(self.dialog.selectedFiles()[0] + "/main.py", "w") as file:
            file.write(self.ui.textEdit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())