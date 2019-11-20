# reduce-colours

This algorithm allows you to reduce the number of colours inside an original image to a desired number of colours (*n*).

## Fast tutorial:

  1. `pip install -r requirements.txt`
  2. `py ui/main_gui.py`

## Slower tutorial:
  * First, download [Python 3.7](https://www.python.org/downloads/)
  * Do this OR the next step:
    * Download [GIT for Windows](https://gitforwindows.org/) (if you're using Windows)
    * Open a command prompt where you want to put the program's files (`SHIFT + right click` > "open command prompt here")
    * Write `git clone https://github.com/Coul33t/reduce-colours.git`: this will copy the content of this repository to your machine
  * Do this OR the previous step:
    * Download the ZIP file (green icon in the top right corner of this repository)
    * Extract it where you want to put the program's files
    * Open a command prompt in the folder (`SHIFT + Right click` on the folder, then > "open command prompt here")
  * Write `pip install -r requirements.txt` in the command prompt (this will install all the required libraries for the program to run corectly)
  * Write `py ui/main_gui.py` (this will launch the program)
  
### Libraries used:
  * Skimage (Scikit image)
  * OpenCV (unusued right now)
  * PIL
  * Numpy
  * Libtcod (unused right now)
 
### TODO: 
 * Args parser (input image and *n*)
 * Allow to specify regions to exclude for the colour reduction
 * Initial and final colours display in terminal with libtcod
