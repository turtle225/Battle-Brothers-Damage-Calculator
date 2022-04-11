# Battle-Brothers-Damage-Calculator
Updated for Of Flesh and Faith

Latest Update: 4/11/2022 - Fixed a bug where having Forge with low armor against Split Man was giving much better survivability than it should have been. Heavy armor Forge vs. Split Man tests were unlikely to be impacted by this bug, as they tend to die before armor was destroyed anyway.

A script that simulates the damage formula used in Battle Brothers, returning expected hits until death, injury, heavy injury, and morale check given whatever scenario you provide. Also returns % chance of death by hit, and can also return % chance of first injuries or morale by hit. 

Includes over 80 different switches from unique weapon cases, perks, attachments, race, etc. to create almost any scenario you can imagine from in game. There are 35 attacker presets and 41 defender presets provided for convenience.

Includes a lot of comments to help make the code easy and intuitive to understand. 

BBCalc.py is the main calculator for general use. BBNimbleBattery.py will run 15 common Nimble sets given your scenario. BBRaisingHp.py will run a given scenario at various hp counts. BB1HanderBattery.py will run all of the top end 1Handers against a given target. BB2HanderBattery.py will run all of the top end 2Handers against a given target. BBAttackerVsEnemies.py will run a given attacker against 30 enemies from the game. BBEnemiesVsDefender.py will run 35 enemies against a given defender. BBHitChance.py is a rehash of the main calculator with a very basic addition of a hit chance variable.

Also included is a file called data.txt which includes information on hp/armor statistics and calculator relevant perks for all enemies as well as weapon data for most weapons and Beasts. 

At the bottom of each calculator is a version history, where you can see changelogs to compare with if you have an older version, or just want to see what new features have been added.

IMPORTANT:

For instruction on setting up the calculator and how to use it once it is ready, please refer to the Installation and User Guide documents provided in the repository. I walk through step by step how to setup the calculator and use it with pictures and examples. Although I do not have a gui, the calculator is easy to use once you know how. The guide will help you get it running. The guide assists with setting up VSCode which is my preferred way to use the calculator, but if you want to use a different IDE then you can do so, or if you don't want to bother with any user setup then use Replit (see below).

An alternative method to use the calculator is to load it into Repl.it. 

https://repl.it/

You don't have to sign up, choose "start coding" or "new repl"  in the top right. Choose "Import from GitHub" and put my link url

https://github.com/turtle225/Battle-Brothers-Damage-Calculator

Once it loads in, on the top right you can configure the "run" button if you wish to use it (it isn't necessary). To do so select Python from the drop down and in the box type "python BBCalc.py" without the quotes. This will make it so that the green run button runs the main calculator, but this won't work for the other calculators.

Alternatively, don't worry about the run button, you can run any of the calculator versions by typing "python calcname.py" without the quotes into the command line on the right, where calcname is the name of the calculator you wish to use. Remember to press your Tab button to autocomplete the command for convenience.

Using Replit skips the first half of the installation and user guide. Refer to part 2 to understand how to edit and use the calculator (note that it is unlikely that the user guide will load in Replit, open it elsewhere on your computer). Make sure any edits you make are done saving before you run the calculator. You can see a greyed out "saved" status next to the open file tab.

The advantage to using Replit is that it is faster and easier to setup than getting your own VSCode going. Once you have the calculator loaded in Replit, you can also save that url link as a bookmark/favorite to quickly load the calculator again later without having to upload it into Replit again. The downside is that it makes the code scrunched and hideous to look at, which makes it hard to read the helpful comments I tried to put in. It may also take longer to compute (lower trials variable if it is taking too long).

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

-- Overhype: For making an amazing game for us to play.

Prior Update: 3/13/2022 - Adjusted Orc Berserker preset for Berserk Chain damage buff.

Prior update: 3/10/2022 - Added the changes that occurred from the Of Flash and Faith dlc balance pass. Notably, 2H Flails got reworked and that logic has been configured. HeadHunter change only effects the hit chance version of the calculator. Nine Lives, Handgonne, Throwing, and Fearsome changes are all in. Also added +5% armor ignore to Aimed Shot which I never realized it had before.

Prior update: 7/17/2021 - Added morale check/drop mechanics and tracking. You can now see the expected number of hits before the defender will fall to Wavering, Breaking, or Fleeing morale. Added Fearsome logic to this as well. Currently, only the main BBCalc.py script has been updated with these new options. As a disclaimer, a 1v1 sandbox calculator isn't going to be able to truly capture the dynamic nature of morale checks in game as there are many things that cause morale drops beyond just damage, and there are many external factors that influence resolve such as Banner/Leader auras, hidden adjacency bonuses, rallying, etc.
