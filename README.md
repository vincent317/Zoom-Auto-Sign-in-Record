# Zoom-Auto-Sign-in-Record

### A Python project that automatically signs in to a Zoom meeting room and starts recording. 

# Software Prerequisites
- Zoom >= 5.2.1 (make sure you double-check your Zoom version)
- Python >= 3.6 
- [Captura v8.0.0](https://github.com/MathewSachin/Captura/releases/tag/v8.0.0)
- Python libraries:
  - keyboard
  - PyAutoGUI
  - pandas
  - subprocess
  - tkinter

# Some Settings
  - After downloading Captura, make sure you install the FFMpeg video package (under the video setting), otherwise the video will lose frame.
  - Change the Captura recording frame to **10**, otherwise the video will lose frame.
 
# How should I use it?
  1. Make sure you have started Zoom and signed in.
     <br /> **Note.** Do not start Captura.  <br /> <br />
  2. Open terminal and do ```python gui.py```. <br /> <br /> 
  3. Entering your class time, meeting ID, class length, and meeting password (if there's one). 
     <br /> **Note.** If your meeting has a password, type Fpassword (ex. F123); if not, type Tpassword (ex. T123).
     <br /> **Note.** If your class starts at 2:00, just put (02:00). Do **NOT** put several minutes early (ex. 01:58). <br /> <br /> 
  4. Click All Set button. <br /> <br /> 
  5. Enjoy your sleep! Your class will be automatically recorded in Captura's default save path. 
     <br /> **Note.** Do **NOT** move your mouse after clicking all set button. 
     
# Issues
  Send me a PR or email me (dpeng12@terpmail.umd.edu). 
