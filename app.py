import time
import os
from pathlib import Path

from PySide2 import QtWidgets, QtGui, QtCore

from utils import PathToDir, Data
from ui import main_window, browser, suffixes_window


class App(QtWidgets.QWidget, main_window.Ui_Form):

    def __init__(self):
        super(App, self).__init__()

        self.setupUi(self)
        self.le_show_dir_path.setText(PathToDir.read_path(self))
        self.setFixedSize(568, 350)
        self.setWindowIcon(QtGui.QIcon('FilesMAR.ico'))
        self.setWindowTitle("FilesMAR")
        self.setup_connections()
        self.manage_suffixes_win = SuffixesList()
        self.prg_manage = self.progressBar
        self.setup_css()

    def setup_connections(self):

        self.btn_request.clicked.connect(self.run_request_win)
        self.btn_choose_dir_path.clicked.connect(self.run_browser)
        self.btn_manage_suffixes.clicked.connect(self.run_suffixes_list_win)
        self.btn_start_manage.clicked.connect(self.start_manage)
        self.le_show_dir_path.returnPressed.connect(self.run_browser)

    def setup_css(self):
        self.setStyleSheet("color: #2C3E50;")
        self.le_show_dir_path.setStyleSheet("background-color: #E5E7E9")

    def start_manage(self):
        """Create dirs and move files """
        dir_path = Path(self.le_show_dir_path.text())
        data = Data()
        suffixes_dir = data.read_data()
        files = [f for f in dir_path.iterdir() if f.is_file()]
        if len(files) == 0:
            return False
        i = 0
        self.prg_manage.setRange(0, len(files))  # on set l'intervale de la progressbar
        for file in files:
            target_dir = dir_path / suffixes_dir.get(file.suffix, "Autres")
            target_dir.mkdir(exist_ok=True)
            # si le fichier existe déjà dans un fichier on retourne un erreur
            try:
                file.rename(target_dir / file.name)
            except FileExistsError:
                print(
                    f"le fichier '{file.name}' existe déjà dans le dossier {suffixes_dir.get(file.suffix, 'Autres')}.")

            i += 1
            self.prg_manage.setValue(i)  # on itère de 1 la valeur de i
            time.sleep(0.025)
        time.sleep(2)
        self.prg_manage.setValue(0)

    def run_suffixes_list_win(self):

        self.manage_suffixes_win.show()

    def run_browser(self):
        """Lance l'explorateur de fichier"""
        self.browser_win = FileBrowser()
        self.browser_win.show()

    def run_request_win(self):
        request_window = QtWidgets.QMessageBox()
        request_window.setWindowIcon(QtGui.QIcon('FilesMAR.ico'))
        request_window.setWindowTitle("Contact")
        request_window.setText("""Pour toutes demandes d'améliorations ou de corrections :\n\nar.magicsoft@gmail.com""")
        request_window.exec_()


class FileBrowser(QtWidgets.QMainWindow, browser.Ui_MainWindow):
    def __init__(self):
        self.load_path = PathToDir()
        super(FileBrowser, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('FilesMAR.ico'))
        self.setWindowTitle("Explorateur de Fichiers")
        self.resize(600, 300)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # Custom context menu for this widgets
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()

    def populate(self):
        """Widgets pour le treeview"""
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setSortingEnabled(True)  # trier les fichiers

    def context_menu(self):
        """affiche un menu avec le click droit de la souris"""
        menu = QtWidgets.QMenu()

        open = menu.addAction("Ouvrir")
        open.triggered.connect(self.open_file)  # Au click droit on se connect a la fonction open_file
        cursor = QtGui.QCursor()  # get position of cursor

        choose_dir_path = menu.addAction("Définir comme chemin d'accès")
        choose_dir_path.triggered.connect(self.get_path)

        menu.exec_(cursor.pos())

    def get_path(self):
        """Recup le path du tree widget et le set dans le line edit"""
        index = self.treeView.currentIndex()
        dir_path = self.model.filePath(index)
        self.load_path.write_path(dir_path)
        Win.le_show_dir_path.setText(PathToDir.read_path(self))  # Update le lineEdit avec le nouveau path
        self.close()  # Fermer la fenêtre après avoir choisi le Path

    def open_file(self):
        """On ouvre le fichier depuis le context menu"""
        index = self.treeView.currentIndex()  # on recup l'index selectioné
        file_path = self.model.filePath(index)  # on recup le path
        os.startfile(file_path)  # on lance le fichier
        print(file_path)


class SuffixesList(QtWidgets.QWidget, suffixes_window.Ui_Form):
    def __init__(self):
        super(SuffixesList, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('FilesMAR.ico'))
        self.setFixedSize(370, 620)
        self.setWindowTitle("Gestion des fichiers")
        self.le_suffix.setPlaceholderText("Exemple : .pdf")
        self.le_dir.setPlaceholderText("Exemple : Documents")
        self.connections()
        self.show_suffixes_list()
        self.setup_css()

    def connections(self):
        self.btn_add_values.clicked.connect(self.submit_suffixes_dir)
        self.btn_delete.clicked.connect(self.remove_suffix_from_list)
        self.lw_show_suffixes.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)  # selection Multiple
        self.le_suffix.returnPressed.connect(self.submit_suffixes_dir)
        self.le_dir.returnPressed.connect(self.submit_suffixes_dir)

    def submit_suffixes_dir(self):
        """Format and insert Values in Json file, change color of line edit if inputs it's wrongs"""
        suffixes_dict = Data().read_data()
        suffix = self.le_suffix.text()
        directory = self.le_dir.text()

        Validate = False

        if directory.startswith("."):  # enlève le point au debut du dossier
            directory = directory.replace(".", "")

        if suffix.startswith(".") and len(suffix) >= 3 and len(directory) >= 1:
            Validate = True
            self.update()

        elif len(suffix) >= 2 and len(directory) >= 1:
            suffix = '.' + suffix
            Validate = True

        elif not (len(suffix) >= 2 and len(directory) >= 1):
            self.le_suffix.setStyleSheet("background-color: rgba(227, 83, 70, 0.5);")
            self.le_dir.setStyleSheet("background-color: rgba(227, 83, 70, 0.5);")

        elif len(suffix) < 2:
            self.le_suffix.setStyleSheet("background-color: rgba(227, 83, 70, 0.5);")
            self.update()

        elif len(directory) < 1:
            self.le_dir.setStyleSheet("background-color: rgba(227, 83, 70, 0.5);")
            self.update()

        if Validate and not suffix in suffixes_dict:
            Data().add_suffix(suffix.lower(), directory.title())
            self.le_suffix.setText("")
            self.le_dir.setText("")
            self.lw_show_suffixes.addItem((f"{directory.title()}\t⬅\t{suffix}"))
            self.lw_show_suffixes.sortItems()
        elif suffix in suffixes_dict:
            #Supprimer le text et set le style par défaut
            self.le_suffix.clear()
            self.le_dir.clear()
            self.le_suffix.setStyleSheet("")
            self.le_dir.setStyleSheet("")
            self.update()

    def show_suffixes_list(self):
        """Return suffix list in lw 'DIR' '<=' 'SUFFIX' """
        suffixes_list = Data().read_data()
        for suffix in suffixes_list:
            self.lw_show_suffixes.addItem((f"{suffixes_list[suffix]}\t⬅\t{suffix}"))
        self.lw_show_suffixes.sortItems()

    def remove_suffix_from_list(self):
        """Remove suffix in Json file from list widget"""
        suffixes_list = Data().read_data()
        for selected_item in self.lw_show_suffixes.selectedItems():
            item_select = selected_item.text().split()  # transforme en string puis en liste pour recup le dernier mots
            Data().remove_data(
                item_select[-1])  # on retire le suffix du fichier Json , il correspond au dernier mot de la liste
            self.lw_show_suffixes.takeItem(self.lw_show_suffixes.row(
                selected_item))  # Retire les objets sélectionné, on récup le selected item l'objet sur le quel on couvle, takeItem retire l'item avec sont index

    def setup_css(self):
        self.setStyleSheet("color: #2C3E50;")



app = QtWidgets.QApplication([])
Win = App()
Win.show()
app.exec_()
