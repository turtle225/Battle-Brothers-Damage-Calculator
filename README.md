# Battle-Brothers-Damage-Calculator
A script that simulates the damage formula used in Battle Brothers, returning expected hits until death, injury, and morale check given whatever scenario you provide. Also returns % chance of death by hit. 

Includes over 70 different switches from unique weapon cases, perks, attachments, race, etc. to create almost any scenario you can imagine from in game. There are 31 attacker presets and 37 defender presets provided for convenience.

Includes a lot of comments to help make the code easy and intuitive to understand. 

BBCalc.py is the main calculator for general use. BBNimbleBattery.py will run 12 common Nimble sets given your scenario. BBRaisingHp.py will run a given scenario at various hp counts. BB1HanderBattery.py will run all of the top end 1Handers against a given target. BB2HanderBattery.py will run all of the top end 2Handers against a given target. BBAttackerVsEnemies.py will run a given attacker against 26 enemies from the game. BBEnemiesVsDefender.py will run 31 enemies against a given defender. BBHitChance.py is a rehash of the main calculator with a very basic addition of a hit chance variable.

Also included is a file called data.txt which includes information on hp/armor statistics and calculator relevant perks for all enemies as well as weapon data for most weapons and Beasts. 

User guide:

Step 1 - Install Python 3.x:
  
  The script is written in Python 3.7. Earlier versions of Python 3 should work but Python 2 will not.
  If you need help getting Python installed, refer to here: https://realpython.com/installing-python/
  Note: You may need to set up a path variable (likely in Windows). If you need help setting up your path variable, here is how to do so in Windows: https://geek-university.com/python/add-python-to-the-windows-path/
  
Step 2 - Download or copy the BBCalc.py file (and the other .py files if you wish) from the Github repository:
  
  You can either download the file or create a new file on your computer with a .py extension and then copy/paste the raw code of the BBCalc.py file over to your file. 
  
Step 3 - Download a code editor for ease of use (recommended but optional):
  
  I use VSCode to make it easy to both edit and run the code easily. It also makes it look a lot prettier than a regular document.
  You can download it here, choose your correct operating system: https://code.visualstudio.com/
  I use the "Python" extension in VSCode, click on the blocks icon on the left and search Python and install the "Python" extension. While not necessary for the code to run properly, it helps with the general readability and if you want to edit anything. If you need help finding extensions, refer to here: https://code.visualstudio.com/docs/editor/extension-gallery
  
Step 4 - Use the calculator:
  
  If using VSCode, load your .py file into VSCode. Edit in your weapon and defender data at the top and apply any switches you wish to use to create the scenario that you wish to test. Then save the file (shortcut is ctrl-s). Then on the terminal in the bottom half of VSCode (or in a seperate terminal/command prompt), navigate to the directory where your .py file exists and run the script by writing "python BBCalc.py" without the quotes and hit enter. If you named your file differently then use whatever name you used. Once you've run python BBCalc.py once you can recall it again quickly by hitting the up arrow while in your terminal and hitting enter again.
  
  If not using VSCode, open your .py file in any form of text editor to edit in your attacker/defender data and apply any switches you wish to use. Save the file and then open a terminal or command prompt and navigate to the directory where your .py file exists. Run the file in the same way as described above. 
  
  Either way, running the calculator is as simple as editing the file to fit your needs, saving it, and then running the script in a terminal. Editing the file is as easy as putting in your attacker/defender stats, and flipping any options you wish to use from 0 to 1. Once you get comfortable, it shouldn't take more than a few seconds to edit and re-run when doing subsequent tests. Get used to the rhythm of: Edit .py file -> ctrl + s -> click in terminal -> up arrow -> enter.
  
If these instructions are in any way unclear then let me know how I can improve them. If you need help, send me an email.

Limitations:

Most of the scripts do not factor in hit chance and I do no plan on adding it in. If there is a demand for it then I may considering expanding on the current BBHitChance.py version. Bleeding damage is going to be an approximation due to the sandbox nature of the calculator. Since the calculator cannot know for sure when "turns" pass and therefore when to apply Bleeding damage, it is forced to make an educated guess. The way I did it was to apply Bleeding damage every two attacks, (which is 1 turn for Cleavers), based on the current number of Bleeding stacks. The calculator depends on the user to create scenarios that make sense. You can give Split Man to a Pike and the calculator will run, but of course that data is meaningless because Pikes do not have Split Man. I included a file with enemy and weapon data for reference, as well as wrote many comments in the code to make it as user friendly as possible.

Thank you, I hope you enjoy it.

Author: turtle225

Contact: turtl225e@gmail.com

Special Thanks:

-- Abel (aka) Villain Joueur: For grabbing the damage formula out of the game code, writing the damage page on the wiki, and for 
helping me with many questions along the way.

-- Wall (aka) Wlira: For helping me with some questions along the way and having an existing calculator for me to test against.

-- You: If you are using the calculator, thank you! If you find any bugs or have feedback/questions/suggestions, you can usually find me on the Steam forums or send me an email.
