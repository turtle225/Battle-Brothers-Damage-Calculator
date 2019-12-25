# Battle-Brothers-Damage-Calculator
A script that simulates the damage formula used in Battle Brothers, returning expected hits until death, injury, and morale check given whatever scenario you provide. Also returns % chance of death by hit. 

Includes over 70 different switches from unique weapon cases, perks, attachments, race, etc. to create almost any scenario you can imagine from in game.

Includes a lot of comments to help make the code easy and intuitive to understand. 

Sample Output for an Ancient Bladed Pike test:

HP = 100, Helmet = 120, Armor = 95
Nimble% = .4
Death in 6.08715 hits on average.
St. Dev: 0.66829585
% hits to die (4, 0.579), (5, 16.556), (6, 56.496), (7, 26.309), (8, 0.06)
First injury in 3.9028 hits on average.
First morale check in 1 hits on average.
2.85109 Fearsome procs on average.

User guide:

Step 1 - Install Python 3.x:
  
  The script is written in Python 3.7. Earlier versions of Python 3 should work but Python 2 will not.
  If you need help getting Python installed, refer to here: https://realpython.com/installing-python/
  Note: You may need to set up a path variable (likely in Windows). If you need help setting up your path variable, here is how to     do so in Windows: https://geek-university.com/python/add-python-to-the-windows-path/
  
Step 2 - Download or copy the BBCalc.py file from the Github repository:
  
  You can either download the file or create a new file on your computer with a .py extension and then copy/paste the raw code of the BBCalc.py file over to your file. 
  
Step 3 - Download a code editor for ease of use (recommended but optional):
  
  I use VSCode to make it easy to both edit and run the code easily. It also makes it look a lot prettier than a regular document.
  You can download it here, choose your correct operating system: https://code.visualstudio.com/
  I use the "Python" extension in VSCode, click on the blocks icon on the left and search Python and install the "Python" extension. While not necessary for the code to run properly, it helps with the general readability and if you want to edit anything. If you need help finding extensions, refer to here: https://code.visualstudio.com/docs/editor/extension-gallery
  
Step 4 - Use the calculator:
  
  If using VSCode, load your .py file into VSCode. Edit in your weapon and defender data at the top and apply any switches you wish to use to create the scenario that you wish to test. Then save the file (shortcut is ctrl-s). Then on the terminal in the bottom half of VSCode (or in a seperate terminal/command prompt), navigate to the directory where your .py file exists and run the script by writing "python BBCalc.py" without the quotes and hit enter. If you named your file differently then use whatever name you used. Once you've run python BBCalc.py once you can recall it again quickly by hitting the up arrow while in your terminal and hitting enter again.
  
  If not using VSCode, open your .py file in any form of text editor to edit in your weapon/defender data and apply any switches you wish to use. Save the file and then open a terminal or command prompt and navigate to the directory where your .py file exists. Run the file in the same way as described above. 
  
  Either way, running the calculator is as simple as editing the file to fit your needs, saving it, and then running the script in a terminal. Editing the file is easy is as easy as putting in your weapon/defender stats, and flipping any options you wish to use from 0 to 1. Once you get comfortable it shouldn't take more than a few seconds to edit and re-run when doing subsequent tests. 
  
If these instructions are in any way unclear then let me know how I can improve them.

Also included is a file called data.txt which includes information on hp/armor statistics and calculator relevant perks for all enemies as well as weapon data for most weapons and Beasts. 

Thank you.

Author: turtle225

Special Thanks:

-- Abel (aka) Villain Joueur: For grabbing the damage formula out of the game code, writing the damage page on the wiki, and for 
helping me with many questions along the way.

-- Wall (aka) Wlira: For helping me with some questions along the way and having an existing calculator for me to test against.

-- You: If you are using the calculator, thank you! If you find any bugs or have feedback/suggestions, I am most reachable on the Steam forums.
