Python asteroids tutorial by boot.dev.
Added some stuff including:
1. Items that you can collect (1 as of now)
2. Score and timer
3. Pause with ESC
4. Sprites
5. Variety of asteroids
And more!

**Steps to run it:**  
Requisites:  
Python 13.2.5 or later, check version with:  
```Python --version```  
Install the requirements with:  
```Pip install requirements.txt```  
Clone the repo:  
```Git clone https://github.com/Cacutss/Asteroids```  
After that you should initialize the virtual environment:  
```Source venv/bin/activate```  
Then you can run it with:  
```python main.py```  
**Windows**  
To run on windows you should add the following lines after the imports on ```main.py```:  
```
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
```  
This is only so the windows scale modification doesn't apply to the game window.  
