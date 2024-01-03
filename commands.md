## Start Here
### venv Installation with pip
```
PS> python -m venv venv
PS> source venv/bin/activate
(venv) PS> python -m pip install pyqt6
```
### Create a PyQt Application
```python
import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80) 
# .setGeometry defines the window’s size and screen position.
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
```

### Run you PyQt App
```commandline
$ python hello.py
```


## Some important components
- Widgets
  - Buttons - [QPushButton](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qpushbutton.html)
  - Labels 
  - Line edits - [QLineEdit](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qlineedit.html)
  - Combo boxes - [QComboBox](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qcombobox.html)
  - Radio buttons - [QRadioButton](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qradiobutton.html)
- Layout managers
  - [QHBoxLayout](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qhboxlayout.html) 
  - QVBoxLayout 
  - QGridLayout 
  - QFormLayout
- Dialogs
  - menu bar
  - toolbars
  - central widget
  - dock widgets
  - status bar
- Main windows
- Applications
- Event loops
- Signals and slots
  - **signal**: PyQt widgets act as event-catchers. This means that every widget can catch specific events, like mouse clicks, keypresses, and so on. In response to these events, a widget emits a signal, which is a kind of message that announces a change in its state.
  - **slots**: The signal on its own doesn’t perform any action. If you want a signal to trigger an action, then you need to connect it to a slot. This is the function or method that’ll perform an action whenever its associated signal is emitted. You can use any Python callable as a slot.
  - Connect signal and slot: `widget.signal.connect(slot_function)`
  - If need args pass in: 
    - ```python
      import sys
      from functools import partial
      button = QPushButton("Greet")
      button.clicked.connect(partial(greet, "World!"))```

  
## Reference
1. [Python and PyQt: Building a GUI Desktop Calculator](https://realpython.com/python-pyqt-gui-calculator/)
