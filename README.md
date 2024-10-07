# Church Songbook and Bible Display Application

## Introduction
This application, **Church Songbook and Bible Display**, is designed to manage and display hymn numbers and Bible portions during church services. It's tailored for use in churches, particularly to be displayed on large screens or TVs for congregational viewing. The user can enter hymn numbers, select from predefined categories such as "H (കീ):" and "L (ഗീ):", and add Bible portions. The app displays the selected items in fullscreen mode, making it easy to toggle between hymn displays and Bible verses with a simple mouse click.

This application is recommended for churches, especially those with large screens or TV displays powered by a Raspberry Pi or similar devices, providing an organized and clean way to show worship content to the congregation.

## Installation

### Dependencies
Before using the application, ensure you have the following installed:

1. **Python 3.x** – This application is written in Python, so make sure you have Python installed.
2. **PyQt5** – This application uses PyQt5 for its graphical interface. You can install it using:
   ```bash
   pip install pyqt5
   ```

### Recommended Setup for Church TV Displays
- For best results, this application is designed to be run on a TV connected to a Raspberry Pi or any other device that supports Python and PyQt5.
- Fullscreen display is optimized for larger screens with clear, bold fonts for easy visibility by the congregation.
  
## Usage Instructions

1. **Start the application** by running the Python script:
   ```bash
   python church_display_app.py
   ```
   
2. **Input Hymn Numbers**: Use the dropdown menus to select hymn categories such as "H (കീ)" or "L (ഗീ)", and enter the hymn numbers in the corresponding fields.

3. **Input Bible Portions**: Use the Bible portion input fields to select a Bible book from the dropdown menu and input a chapter and verse.

4. **Fullscreen Mode**: Once all input fields are filled, click the "Go Fullscreen" button to display the selected hymns or Bible portions on a connected TV or large screen.

5. **Toggle Between Hymns and Bible Display**: In fullscreen mode, left-clicking the mouse toggles between hymn display and Bible portion display.

6. **Exit Fullscreen**: Right-click or press the "Escape" key to exit fullscreen mode.
