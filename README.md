# pi-dev500/TkTerm
A simple xterm frame for tkinter with a few options like run and a bit hacky system for automatic resizing
made by pi-dev500
### Dependencies:
```
python3-tkinter
xterm
```
#### Debian dependencies installation:
```
sudo apt update
sudo apt upgrade
sudo apt install python3-tkinter xterm -y
```
### Use:
Just download this repo and run __init__.py (for simple terminal use):
```
git clone https://github.com/pi-dev500/TkTerm
cd TkTerm
python3 __init__.py
```
Or, if you want to integrate it in your project, please just clone my repo in your project's directory and import it with:
```
from TkTerm import *
```

Class parameters are the same as Frame(), with ```font``` and ```size``` parametters (by default Monospace 12) and additional methods ```.display_true(self)```, ```.display_false(self)``` and ```.run(self, command="bash")```

If using this in your application, please keep the readme in the TkTerm library directory or mention my project in your project's README.md
