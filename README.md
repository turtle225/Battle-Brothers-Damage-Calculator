# Battle-Brothers-Damage-Calculator
A script that simulates the damage formula used in Battle Brothers, returning expected hits until death, injury, heavy injury, and morale check given whatever scenario you provide. Also returns % chance of death by hit, and can also return % chance of first injuries or morale by hit. 

Includes over 70 different switches from unique weapon cases, perks, attachments, race, etc. to create almost any scenario you can imagine from in game. There are 31 attacker presets and 37 defender presets provided for convenience.

IMPORTANT NOTE: 4/3/2020: Split Man is currently overvalued in the calculator. This is because I allow it to deal armor ignoring damage on the secondary hit as you would expect that it should be able to do based on the info card and description. The actual game code doesn't have any armor ignoring logic, meaning the secondary hit cannot deal hp damage through armor. This makes Split Man signficantly worse. It is unclear whether or not this is intended behavior or a bug, so I'm not making changes until we see some confirmation one way or the other. Sorry and thank you.

Includes a lot of comments to help make the code easy and intuitive to understand. 

BBCalc.py is the main calculator for general use. BBNimbleBattery.py will run 12 common Nimble sets given your scenario. BBRaisingHp.py will run a given scenario at various hp counts. BB1HanderBattery.py will run all of the top end 1Handers against a given target. BB2HanderBattery.py will run all of the top end 2Handers against a given target. BBAttackerVsEnemies.py will run a given attacker against 26 enemies from the game. BBEnemiesVsDefender.py will run 31 enemies against a given defender. BBHitChance.py is a rehash of the main calculator with a very basic addition of a hit chance variable.

Also included is a file called data.txt which includes information on hp/armor statistics and calculator relevant perks for all enemies as well as weapon data for most weapons and Beasts. 

IMPORTANT:

For instruction on setting up the calculator and how to use it once it is ready, please refer to the Installation and User Guide documents provided in the repository. I walk through step by step how to setup the calculator and use it with pictures and examples. Although I do not have a gui, the calculator is easy to use once you know how. The guide will help you get it running.

An alternative method to use the calculator is to load it into Repl.it.

https://repl.it/

You don't have to sign up, choose "new repl" in the top right. Choose "Import from GitHub" and put my link url

https://github.com/turtle225/Battle-Brothers-Damage-Calculator

Once it loads in, on the top right you can configure the "run" button if you wish to use it. Select Python from the drop down and in the box type "python BBCalc.py" without the quotes. This will make it so that the green run button runs the main calculator, but this won't work for the other calculators.

Alternatively, don't worry about the run button, you can run any of the calculator versions by typing "python calcname.py" without the quotes into the command line on the right, where calcname is the name of the calculator you wish to use. Remember to press your Tab button to autocomplete the command for convenience.

Using Replit skips the first half of the installation and user guide. Refer to part 2 to understand how to edit and use the calculator (note that it is unlikely that the user guide will load in Replit, open it elsewhere on your computer). Make sure any edits you make are done saving before you run the calculator. You can see a greyed out "saved" status next to the open file tab.

The advantage to using Replit is that it is faster and easier to setup than getting your own VSCode going. The downside is that it makes the code scrunched and hideous to look at, which makes it hard to read the helpful comments I tried to put in. It may also take longer to compute (lower trials variable if it is taking too long).

Limitations:

Most of the scripts do not factor in hit chance and I do not plan on adding it in. If there is a demand for it then I may consider expanding on the current BBHitChance.py version. Bleeding damage is going to be an approximation due to the sandbox nature of the calculator. Since the calculator cannot know for sure when "turns" pass and therefore when to apply Bleeding damage, it is forced to make an educated guess. The way I did it was to apply Bleeding damage every two attacks, (which is 1 turn for Cleavers), based on the current number of Bleeding stacks. The calculator depends on the user to create scenarios that make sense. You can give Split Man to a Pike and the calculator will run, but of course that data is meaningless because Pikes do not have Split Man. I included a file with enemy and weapon data for reference, as well as wrote many comments in the code to make it as user friendly as possible.

Thank you, I hope you enjoy it.

Author: turtle225

Contact: turtl225e@gmail.com

Special Thanks:

-- Abel (aka) Villain Joueur: For grabbing the damage formula out of the game code, writing the damage page on the wiki, and for 
helping me with many questions along the way.

-- Wall (aka) Wlira: For helping me with some questions along the way and having an existing calculator for me to test against. Also for pointing out Replit as an option for using the calculator.

-- You: If you are using the calculator, thank you! If you find any bugs or have feedback/questions/suggestions, you can usually find me on the Steam forums or send me an email.
