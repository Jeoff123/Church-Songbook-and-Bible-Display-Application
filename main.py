from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import math

class ChurchDisplayApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("St.James CSI Church Display Control")
        self.setGeometry(100, 100, 600, 600)

        # Main layout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Title label
        title_label = QtWidgets.QLabel("Church Display Control Center", self)
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setFont(QtGui.QFont('Arial', 24))
        self.layout.addWidget(title_label)

        # Input frame for song types and numbers
        self.input_frame = QtWidgets.QWidget(self)
        self.input_layout = QtWidgets.QGridLayout(self.input_frame)
        self.input_frame.setStyleSheet("background-color: #f2f2f2; padding: 20px; border-radius: 15px;")

        self.song_type_list = []
        self.song_number_list = []

        # Create input fields for 6 song numbers
        for i in range(6):
            # Dropdown for "H" and "L"
            song_type = QtWidgets.QComboBox(self)
            song_type.addItems(["H (കീ):", "L (ഗീ):", "Convention:", "Special:", "Other"])
            song_type.setFont(QtGui.QFont('Arial', 18))
            song_type.setStyleSheet(self.combo_style())
            self.song_type_list.append(song_type)
            self.input_layout.addWidget(song_type, i, 0)

            # Input field for song number
            song_number = QtWidgets.QLineEdit(self)
            song_number.setFont(QtGui.QFont('Arial', 18))
            song_number.setAlignment(QtCore.Qt.AlignCenter)
            song_number.setStyleSheet("QLineEdit { border: 2px solid #ccc; padding: 5px; }")
            self.song_number_list.append(song_number)
            self.input_layout.addWidget(song_number, i, 1)

        # Bible portions input
        self.bible_layout = QtWidgets.QVBoxLayout()
        self.bible_inputs = []

        # Bible book names organized by sections
        self.bible_books = {
            "Old Testament": [
                "ഉല്പത്തി", "പുറപ്പാടു്", "ലേവ്യപുസ്തകം", "സംഖ്യാപുസ്തകം",
                "ആവർത്തനം", "യോശുവ", "ന്യായാധിപന്മാർ", "രൂത്ത്", "ശമൂവേൽ-1",
                "ശമൂവേൽ -2", "രാജാക്കന്മാർ 1", "രാജാക്കന്മാർ 2", "ദിനവൃത്താന്തം 1",
                "ദിനവൃത്താന്തം 2", "എസ്രാ", "നെഹെമ്യാവു", "എസ്ഥേർ", "ഇയ്യോബ്",
                "സങ്കീർത്തനങ്ങൾ", "സദൃശ്യവാക്യങ്ങൾ", "സഭാപ്രസംഗി", "ഉത്തമ ഗീതം",
                "യെശയ്യാ", "യിരേമ്യാവു", "വിലാപങ്ങൾ", "യേഹേസ്കേൽ", "ദാനീയേൽ",
                "ഹോശേയ", "യോവേൽ", "ആമോസ്", "ഓബ്ദ്യാവു", "യോനാ", "മീഖാ",
                "നഹൂം", "ഹബക്കൂക്‍", "സെഫന്യാവു", "ഹഗ്ഗായി", "സെഖർയ്യാവു",
                "മലാഖി"
            ],
            "New Testament": [
                "അപ്പൊ. പ്രവൃത്തി", "റോമർ", "കൊരിന്ത്യർ 1", "കൊരിന്ത്യർ 2",
                "ഗലാത്യർ", "എഫെസ്യർ", "ഫിലിപ്പിയർ", "കൊലൊസ്സ്യർ",
                "തെസ്സലൊനീക്യർ 1", "തെസ്സലൊനീക്യർ 2", "തിമൊഥെയൊസ് 1",
                "തിമൊഥെയൊസ് 2", "തീത്തൊസ്", "ഫിലേമോൻ", "എബ്രായർ",
                "യാക്കോബ്", "പത്രൊസ് 1", "പത്രൊസ് 2", "യോഹന്നാൻ 1",
                "യോഹന്നാൻ 2", "യോഹന്നാൻ 3", "യൂദാ", "വെളിപ്പാടു"
            ],
            "Gospels": [
                "മത്തായി", "മർക്കൊസ്", "ലൂക്കോസ്", "യോഹന്നാൻ"
            ],
            "Psalms": [
                "സങ്കീർത്തനങ്ങൾ"
            ]
        }

        # Create input boxes for Bible portions
        self.create_bible_input("Old Testament", 0)
        self.create_bible_input("New Testament", 1)
        self.create_bible_input("Gospels", 2)
        self.create_bible_input("Psalms", 3)

        # Add input frames to main layout
        self.layout.addWidget(self.input_frame)
        self.layout.addLayout(self.bible_layout)

        # Fullscreen button
        self.fullscreen_button = QtWidgets.QPushButton("Go Fullscreen", self)
        self.fullscreen_button.setFont(QtGui.QFont('Arial', 20))
        self.fullscreen_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 10px;")
        self.fullscreen_button.clicked.connect(self.show_fullscreen)
        self.layout.addWidget(self.fullscreen_button)

        # Set the layout
        self.setLayout(self.layout)

    def combo_style(self):
        return """
            QComboBox {
                font-size: 18px;
                padding: 5px;
                background-color: white;
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::item {
                background-color: white;
                color: black;
            }
            QComboBox::item:selected {
                background-color: #4CAF50;  /* Highlight color */
                color: white;
            }
        """

    def create_bible_input(self, section, index):
        # Dropdown for the specific section
        bible_book_combo = QtWidgets.QComboBox(self)
        bible_book_combo.addItems(self.bible_books[section])
        bible_book_combo.setFont(QtGui.QFont('Arial', 18))
        bible_book_combo.setStyleSheet(self.combo_style())
        self.bible_layout.addWidget(bible_book_combo)

        # Input field for Bible portion
        bible_portion_input = QtWidgets.QLineEdit(self)
        bible_portion_input.setFont(QtGui.QFont('Arial', 18))
        bible_portion_input.setPlaceholderText("Enter Chapter:Verse (e.g., 20:1-32)")
        bible_portion_input.setStyleSheet("QLineEdit { border: 2px solid #ccc; padding: 5px; }")
        self.bible_layout.addWidget(bible_portion_input)

        # Store the combo and input field for later access
        self.bible_inputs.append((bible_book_combo, bible_portion_input))

    def show_fullscreen(self):
        # Collect song type and number, filtering out empty entries
        display_items = []
        for song_type, song_number in zip(self.song_type_list, self.song_number_list):
            song_num = song_number.text().strip()
            if song_num:  # No validation, just add the input as is
                display_items.append(f"{song_type.currentText()} {song_num}")

        # Collect Bible portions
        bible_items = []
        for dropdown, bible_input in self.bible_inputs:
            bible_portion = bible_input.text().strip()
            bible_items.append(f"{dropdown.currentText()}: {bible_portion}")  # Just show the input

        if not display_items and not bible_items:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter at least one song number or Bible portion.")
            return

        # Create a new fullscreen window
        self.fullscreen_window = FullscreenWindow(display_items, bible_items)
        self.fullscreen_window.showFullScreen()

class FullscreenWindow(QtWidgets.QWidget):
    def __init__(self, display_items, bible_items):
        super().__init__()
        self.setWindowTitle("Full Screen Display")
        self.setStyleSheet("background-color: black; color: white;")
        self.display_items = display_items
        self.bible_items = bible_items
        self.showing_bible = False  # To toggle between song and bible display

        # Set up the layout for fullscreen display
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(50, 50, 50, 50)  # Add some padding

        # Update display with the first page
        self.update_display()

    def update_display(self):
        self.clear_layout()

        items = self.bible_items if self.showing_bible else self.display_items

        # Add items line by line
        for item in items:
            label = QtWidgets.QLabel(item)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setFont(QtGui.QFont('Arial', 60, QtGui.QFont.Bold))
            self.layout.addWidget(label)

    def clear_layout(self):
        # Clear the current layout
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if not self.showing_bible:
                # Switch to Bible items
                self.showing_bible = True
            else:
                # Switch back to song items
                self.showing_bible = False
            self.update_display()
        elif event.button() == QtCore.Qt.RightButton:
            # Right click - exit fullscreen
            self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            # Escape key - exit fullscreen
            self.close()
        else:
            # Ignore all other key presses
            pass

# Main function to run the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Set the application's style
    app.setStyleSheet("""
        QWidget {
            background-color: #f5f5f5;
        }
        QPushButton {
            padding: 10px;
        }
        QLabel {
            padding: 10px;
        }
    """)

    window = ChurchDisplayApp()
    window.show()
    sys.exit(app.exec_())
