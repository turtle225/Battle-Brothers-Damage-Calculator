#Battle Brothers Damage Calculator -- Enemies Vs. Defender version:
#Welcome. Modify the below values as necessary until you reach the line ----- break.

#This version of the calculator will run 31 different enemies against a given defender.
#Attacker specific perks, weapons, and traits are automatically applied.
#If you wish to more easily compare two test cases, run the script once in two separate terminals.

#Note: Since this calculator runs multiple times per launch, default trials has been lowered. Adjust this to your preferences.
Trials = 10000 #Number of trials to run through. More trials leads to more accurate results but longer compute times.

#Defender Stats: #Note: If you wish to use a defender Preset, skip the defender sections and check the Preset section instead.
Def_HP = 100
Def_Helmet = 120
Def_Armor = 95   
Fatigue = -15    #Fatigue value only effects Nimble.

#DEFENDER FLAGS: Set these values to 1 if they apply and 0 otherwise. If you select a Preset then leave these on 0.
#Perks:
NineLives = 0
Resilient = 0           #Reduces Bleeding duration.
SteelBrow = 0
Nimble = 1 
Forge = 0
Indomitable = 0
#Attachments: Note: Only 1 attachment should be selected.
AdFurPad = 0            #Additional Fur Padding.
Boneplate = 0           
HornPlate = 0           #Only select against melee attacks.
UnholdFurCloak = 0      #Only select against range attacks.

#Defender Preset: Set these values to 1 if you wish to use a defender preset, and 0 otherwise.
#A preset will automatically set defender stats and defender perks.
#Does not disable perks that shouldn't be active. For example, Don't activate Nimble and then check the Orc Warrior Preset.
DPreNimbleBro = 0       # 120hp, 120/95, Nimble (A generic Nimble line with just Nimble).
DPreNimbleBroBP = 0     # 120hp, 120/95 Nimble, Bone Plates.
DPreForgeBro = 0        # 80hp, 300/300, Forge (A generic Forge line with just Forge).
DPreForgeBroAFP = 0     # 80hp, 300/300, Forge, Additional Fur Padding.
DPreAncientLegion = 0   # 55hp, 130/135, Forge, SteelBrow, Undead. (Manually apply Skeleton flag if necessary).
DPreHonorGuard = 0      # 65hp, 180/210, Forge, SteelBrow, Undead. (Manually apply Skeleton flag if necessary).
DPreArmGangerHeavy = 0  # 130hp, 140/115, Forge, Undead.
DPreFHeroHeavy = 0      # 180hp, 255/260, Forge, Undead.
DPreYoungHeavy = 0      # 125hp, 120/120.
DPreBerserkerHeavy = 0  # 250hp, 120/110, Resilient.
DPreWarriorLight = 0    # 200hp, 240/280, Resilient.
DPreWarriorHeavy = 0    # 200hp, 360/400, Resilient.
DPreWarlord = 0         # 300hp, 500/500.
DPreSkirmisherHeavy = 0 # 40hp, 90/90.
DPreAmbusher = 0        # 40hp, 25/35.
DPreShaman = 0          # 70hp, 35/45.
DPreOverseer = 0        # 70hp, 120/180.
DPreReaverHeavy = 0     # 80hp, 145/95, Resilient.
DPreChosenLight = 0     # 130hp, 145/140, Forge, Resilient.
DPreChosenHeavy = 0     # 130hp, 190/230, Forge, Resilient.
DPreBarbKing = 0        # 150hp, 250/270, Forge, Resilient.
DPreBeastmaster = 0     # 70hp, 130/95, Resilient.
DPreFootmanHeavy = 0    # 70hp, 215/150, Forge.
DPreBillman = 0         # 70hp, 80/130, Forge.
DPreArbalester = 0      # 60hp, 80/65.
DPreBannerHeavy = 0     # 80hp, 215/150, SteelBrow.
DPreKnight = 0          # 125hp, 300/300, Forge. 
DPreSergeant = 0        # 100hp, 0/150, Nimble, SteelBrow. (-18 Fat)
DPreZweiHeavy = 0       # 90hp, 160/240, Forge, SteelBrow. 
DPreRaiderHeavy = 0     # 70hp, 140/115.
DPreMarkman = 0         # 60hp, 45/70.
DPreLeaderHeavy = 0     # 100hp, 250/230, NineLives.
DPreMercenaryHeavy = 0  # 90hp, 230/260, Forge.
DPreMercRange = 0       # 65hp, 115/115, Nimble. (-18 Fat)
DPreHedgeKnight = 0     # 150hp, 300/300, Forge, Resilient.
DPreSwordmaster = 0     # 70hp, 70/115, Nimble, SteelBrow. (-15 Fat)
DPreMasterArcher = 0    # 80hp, 30/115, Nimble, SteelBrow. (-12 Fat)

# ------------------------------------------------------------------------
#IMPORTANT --- ALL BELOW FIELDS SHOULD NOT BE MODIFIED. --- IMPORTANT
#DO NOT MODIFY BELOW FIELDS UNLESS YOU KNOW WHAT YOU ARE DOING.

#Dependencies:
import random
import statistics
import collections
import math
import sys

#Attacker Stats: Note: This version of the calculator does not allow for attacker inputs.
Mind = 95
Maxd = 115
Headchance = 25
Ignore = 50
ArmorMod = 125

#Weapons:
DoubleGrip = 0           
TwoHander20 = 0         #Note: This is manually applied in this version of the calculator. Damage +20. Applies to the single target 2Hander attacks Cudgel (Mace), Pound (Flail), Smite (Hammer), Overhead Strike (Long/GreatSword).
FlailLash = 0           #Gaurantees headshot. Also apply to 3Head Hail special.
Flail3Head = 0          #3Head Flail. Returns number of swings rather than number of hits.
Hammer10 = 0            #Guarantees at least 10 hp damage, applies to 1H Hammer and Polehammer.
DestroyArmor = 0        #Will use Destroy Armor instead of regular attack if opponent's body armor is greater than 150% of expected max armor damage.
DestroyArmorMastery = 0 #Hammer Mastery. Will use Destroy Armor instead of regular attack if opponent's body armor is greater than 150% of expected max armor damage.
Axe1H = 0               #Applies bonus damage to Headshots. Gets negated by SteelBrow.
SplitMan = 0            #Applies to single target 2HAxe except for Longaxe.
AoE2HAxe = 0            #Applies to Round Swing and Split in Two (Bardiche), reduces Ignore by 10%.
CleaverBleed = 0        #5 bleed damage per bleed tick.
CleaverMastery = 0      #10 bleed damage per bleed tick. 
Decapitate = 0          #Cleaver Decapitate. Will use Decapitate for all attacks.
SmartDecap50 = 0        #Switches from normal Cleaver attacks to Decapitate once opposing hp is <= 50%.
SmartDecap33 = 0        #Switches from normal Cleaver attacks to Decapitate once opposing hp is <= 33.33%.
Shamshir = 0            #Shamshir special, acts like Crippling Strikes.
Spearwall = 0           #Warning: May take a long time to compute against durable targets, considering lowering number of trials. 
AimedShot = 0           #Damage +10% for Bows.
XbowMastery = 0         #Ignore +20%.
R2Throw = 0             #Throwing Mastery for 1 or 2 Range.
R3Throw = 0             #Throwing Mastery for 3 Range.             
#Perks:
CripplingStrikes = 0
Executioner = 0
HeadHunter = 0          #Will start each trial with base Headshot chance.
HHCarryOver = 0         #Uncheck regular HH if you use this. Causes HeadHunter stacks to carry over to subsequent trials rather than resetting to better approximate how HH really works.
Duelist = 0             #Note: Duelist should not be applied in this version of the calculator.
KillingFrenzy = 0
Fearsome = 0            #Will also return # of Fearsome procs, which are all attacks that deal 1-14 damage.
#Traits:
Brute = 0               #Headshot damage +15%.
Drunkard = 0            #Damage +10%.
Huge = 0                #Damage +10%.
Tiny = 0                #Damage -15%.
#Backgrounds:
Juggler = 0             #Headchance +5%.
KillerOnTheRun = 0      #Headchance +10%.
#Injuries:
BrokenArm = 0           #Damage -50%. Heavy blunt/body.
SplitShoulder = 0       #Damage -50%. Heavy cutting/body.
CutArmSinew = 0         #Damage -40%. Light cutting/body.
InjuredShoulder = 0     #Damage -25%. Light piercing/body.
#Other:
Dazed = 0               #Damage -35%. Set this if you want to simulate the attacker always being Dazed.
Mushrooms1x = 0         #Applies a 30% buff on the first attack, 20% on the second, 10% on the third, and then 0% after. Only apply for Melee.
Mushrooms2x = 0         #Applies to two attacks per turn instead of 1 for weapons that can attack twice per turn.

#RACE FLAGS (ATTACKER):
#Note: This version of the calculator runs preset enemies, so these are automatically applied when required.
Young = 0               #Damage +15%.
Berserker = 0           #Damage +20%.
BerserkerDay190 = 0     #Damage +30%.
Warrior = 0             #Damage +15%.
WarriorDay200 = 0       #Damage +25%.
Warlord = 0             #Damage +35%.
WarlordDay200 = 0       #Damage +45%.
Conqueror = 0           #Damage +35%. Monolith.
FallenBetrayer = 0      #Damage +25%. Watermill.
FallenHeroDay100 = 0    #Damage +10%.
ArmoredZombieDay100 = 0 #Damage +10%.
BarbKing = 0            #Damage +20%.
HedgeKnight = 0         #Damage +20%.
BrigandLeader = 0       #Armor Damage + 20%.
Ambusher = 0            #Ignore * 1.4
AmbusherDay200 = 0      #Ignore * 1.5
Skirmisher = 0          #Ignore * 1.25
Overseer = 0            #Ignore * 1.1
Wolfrider = 0           #Ignore * 1.25
MasterArcher = 0        #Ignore * 1.25
FrenziedDirewolf = 0    #Damage +20%.
UnholdDay90 = 0         #Damage +10%.
LindwurmDay170 = 0      #Damage +10%.

#RACE FLAGS (DEFENDER): Note: This calculator assumes that your bro is the defender, so these flags don't logically apply.
Undead = 0              #Immunity to Injury, Bleeding, and Morale.
Savant = 0              #Immunity to Injury and Morale.
SkeletonVsPierce = 0    #50% health damage reduction for Ancient Dead and Alps vs. Daggers, Spears, and Pikes.
SkeletonVsJavelin = 0   #75% health damage reduction for Ancient Dead and Alps vs. Javelins. 
SkeletonVsArrow = 0     #90% health damage reduction for Anciend Dead and Alps vs. Arrows.
PossessedUndead = 0     #25% damage reduction. Necromancer buff.
FallenBetrayerD = 0     #25% armor damage reduction for Watermill Betrayers.

#Attacker Preset: Note: This version of the calculator automatically applies attacker data.
#A preset will atutomatically set attacker stats and attacker perks.
#Attacker presets do not include the late game day related buffs that some races get.
#Does not disable perks that shouldn't be active. For example, don't activate Duelist and then check the Chosen Preset.
APreAncientSword = 0    #Ancient Dead: 38-43, 20% Ignore, 80% Armor, Fearsome.
APreBladedPike = 0      #Ancient Dead: 55-80, 30% Ignore, 125% Armor, 30% Head, Fearsome.
APreWarscytheAoE = 0    #Ancient Dead: 55-80, 25% Ignore, 104% Armor, Fearsome.
APreCryptCleaver = 0    #Ancient Dead: 65-85, 25% Ignore, 110% Armor, Fearsome, Cleaver Mastery.
APreKhopesh = 0         #Necrosavant: 35-55, 25% Ignore, 120% Armor, HeadHunter, Crippling, Double Grip, CleaverBleed.
APreWingedMace = 0      #Fallen Hero: 35-55, 40% Ignore, 110% Armor, Fearsome.
APreBerserkChain = 0    #Orc Berserker: 40-100, 30% Ignore, 125% Armor, 40% Head, TwoHander20, Berserker.
APreHeadSplitter = 0    #Orc Young/Warrior: 35-65, 30% Ignore, 130% Armor, 1HAxe, Warrior.
APreHeadChopper = 0     #Orc Young/Warrior: 40-70, 25% Ignore, 110% Armor, Cleaver Mastery, Warrior.
APreMansplitter = 0     #Orc Warlord: 90-120, 40% Ignore, 160% Armor, Split Man, Fearsome, Warlord.
APreReinBoondock = 0    #Goblin Ambusher: 25-40, 35% Ignore, 60% Armor, Ambusher.
APreSpikedImpaler = 0   #Goblin Overseer: 50-70, 50% Ignore, 75% Armor, Overseer, Xbow Mastery.
APre2HSpikedMace = 0    #Chosen: 50-70, 60% Ignore, 115% Armor, Crippling, Executioner, TwoHander20.
APre2HSkullHammer = 0   #Chosen: 45-65, 60% Ignore, 180% Armor, Crippling, Executioner, TwoHander20.
APreHeavyRustyAxe = 0   #Chosen: 75-90, 50% Ignore, 150% Armor, Crippling, Executioner, Split Man.
APreRustyWarblade = 0   #Chosen: 60-80, 35% Ignore, 110% Armor, Crippling, Executioner, Cleaver Mastery.
APreBillhook = 0        #Billman: 60-90, 30% Ignore, 150% Armor, 30% Head.
APreHeavyXbow = 0       #Arbalester: 50-70, 50% Ignore, 75% Armor, XbowMastery.
APreFightingAxe = 0     #Knight: 35-55, 30% Ignore, 130% Armor, 1HAxe, Crippling, Executioner.
APreWarHammer = 0       #Sergeant: 30-40, 50% Ignore, 225% Armor, Duelist, Double Grip, Hammer10.
APreGreatsword = 0      #Zweihander: 85-100, 25% Ignore, 100% Armor, 30% Head, TwoHander20.
APreFlailDGrip = 0      #Raider: 25-55, 30% Ignore, 100% Armor, 35% Head, Double Grip, Executioner.
APreLongAxe = 0         #Raider: 70-95, 30% Ignore, 110% Armor, 30% Head, Executioner. 
APreMedXbow = 0         #Marksman: 40-60, 50% Ignore, 70% Armor, Xbow Mastery.
APreNobleSword = 0      #Swordmaster: 45-50, 20% Ignore, 85% Armor, Duelist, Double Grip, Crippling, Executioner.
APreWarbow = 0          #Master Archer: 50-70, 35% Ignore, 65% Armor, Crippling, Executioner, HeadHunter, Master Archer. 
APreFDirewolf = 0       #Frenzied Direwolf: 30-50, 20% Ignore, 70% Armor, Executioner, Frenzied Direwolf.
APreNachTier3 = 0       #Tier 3 Nachzehrer: 55-80, 10% Ignore, 75% Armor.
APreLindwurm = 0        #Lindwurm Head: 80-140, 40% Ignore, 140% Armor, Fearsome.
APreUnhold = 0          #Unhold: 40-80, 40% Ignore, 80% Armor, Crippling.
APreSchrat = 0          #Schrat: 70-100, 50% Ignore, 80% Armor, Crippling.

#Attacker presets:
def PresetCalc():
    global Mind,Maxd,Headchance,Ignore,ArmorMod,Fearsome,CleaverMastery,HeadHunter,CripplingStrikes,DoubleGrip,CleaverBleed,TwoHander20,Berserker,Axe1H,Warrior,SplitMan,Warlord,Ambusher,Overseer,XbowMastery,Executioner,Duelist,MasterArcher,FrenziedDirewolf,Hammer10
    if APreAncientSword == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 38, 43, 25, 20, 80, 1
    if APreBladedPike == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 55, 80, 30, 30, 125, 1
    if APreWarscytheAoE == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 55, 80, 25, 25, 104, 1
    if APreCryptCleaver == 1: 
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome, CleaverMastery = 65, 85, 25, 25, 110, 1, 1
    if APreKhopesh == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, HeadHunter, CripplingStrikes, DoubleGrip, CleaverBleed = 35, 55, 25, 25, 120, 1, 1, 1, 1
    if APreWingedMace == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 35, 55, 25, 40, 110, 1
    if APreBerserkChain == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, TwoHander20, Berserker = 40, 100, 40, 30, 125, 1, 1
    if APreHeadSplitter == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Axe1H, Warrior = 35, 65, 25, 30, 130, 1, 1
    if APreHeadChopper == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CleaverMastery, Warrior = 40, 70, 25, 25, 110, 1, 1
    if APreMansplitter == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, SplitMan, Fearsome, Warlord = 90, 120, 25, 40, 160, 1, 1, 1
    if APreReinBoondock == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Ambusher = 25, 40, 25, 35, 60, 1
    if APreSpikedImpaler == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Overseer, XbowMastery = 50, 70, 25, 50, 75, 1, 1
    if APre2HSpikedMace == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes, Executioner, TwoHander20 = 50, 70, 25, 60, 115, 1, 1, 1
    if APre2HSkullHammer == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes, Executioner, TwoHander20 = 45, 65, 25, 60, 180, 1, 1, 1
    if APreHeavyRustyAxe == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes, Executioner, SplitMan = 75, 90, 25, 50, 150, 1, 1, 1
    if APreRustyWarblade == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes, Executioner, CleaverMastery = 60, 80, 25, 35, 110, 1, 1, 1
    if APreBillhook == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod = 60, 90, 30, 30, 150
    if APreHeavyXbow == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, XbowMastery = 50, 70, 25, 50, 75, 1
    if APreFightingAxe == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Axe1H, CripplingStrikes, Executioner = 35, 55, 25, 30, 130, 1, 1, 1
    if APreWarHammer == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Duelist, DoubleGrip, Hammer10 = 30, 40, 25, 50, 225, 1, 1, 1
    if APreGreatsword == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, TwoHander20 = 85, 100, 30, 25, 100, 1
    if APreFlailDGrip == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Executioner, DoubleGrip = 25, 55, 35, 30, 100, 1, 1
    if APreLongAxe == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Executioner = 70, 95, 30, 30, 110, 1 
    if APreMedXbow == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, XbowMastery = 40, 60, 25, 50, 70, 1
    if APreNobleSword == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Duelist, DoubleGrip, CripplingStrikes, Executioner = 45, 50, 25, 20, 85, 1, 1, 1, 1
    if APreWarbow == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes, Executioner, MasterArcher, HeadHunter = 50, 70, 25, 35, 65, 1, 1, 1, 1
    if APreFDirewolf == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Executioner, FrenziedDirewolf = 30, 50, 25, 20, 70, 1, 1
    if APreNachTier3 == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod = 55, 80, 25, 10, 75
    if APreLindwurm == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 80, 140, 25, 40, 140, 1
    if APreUnhold == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes = 40, 80, 25, 40, 80, 1
    if APreSchrat == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes = 70, 100, 25, 50, 80, 1

#Defender preset automation:
if DPreNimbleBro == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble = 120, 120, 95, -15, 1
if DPreNimbleBroBP == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble, Boneplate = 120, 120, 95, -15, 1, 1
if DPreForgeBro == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge = 80, 300, 300, 1
if DPreForgeBroAFP == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, AdFurPad = 80, 300, 300, 1, 1
if DPreAncientLegion == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, SteelBrow, Undead = 55, 130, 135, 1, 1, 1
if DPreHonorGuard == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, SteelBrow, Undead = 65, 180, 210, 1, 1, 1
if DPreArmGangerHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, Undead = 130, 140, 115, 1, 1
if DPreFHeroHeavy ==  1:
    Def_HP, Def_Helmet, Def_Armor, Forge, Undead = 180, 255, 260, 1, 1
if DPreYoungHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor = 125, 120, 120
if DPreBerserkerHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Resilient = 250, 120, 110, 1
if DPreWarriorLight == 1:
    Def_HP, Def_Helmet, Def_Armor, Resilient = 200, 240, 280, 1
if DPreWarriorHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Resilient = 200, 360, 400, 1
if DPreWarlord == 1:
    Def_HP, Def_Helmet, Def_Armor = 300, 500, 500
if DPreSkirmisherHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor = 40, 90, 90
if DPreAmbusher == 1:
    Def_HP, Def_Helmet, Def_Armor = 40, 25, 35
if DPreShaman == 1:
    Def_HP, Def_Helmet, Def_Armor = 70, 35, 45
if DPreOverseer == 1:
    Def_HP, Def_Helmet, Def_Armor = 70, 120, 180
if DPreReaverHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Resilient = 80, 145, 95, 1
if DPreChosenLight == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, Resilient = 130, 145, 140, 1, 1
if DPreChosenHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, Resilient = 130, 190, 230, 1, 1
if DPreBarbKing == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, Resilient = 150, 250, 270, 1, 1
if DPreBeastmaster == 1:
    Def_HP, Def_Helmet, Def_Armor, Resilient = 70, 130, 95, 1
if DPreFootmanHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge = 70, 215, 150, 1
if DPreBillman == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge = 70, 80, 130, 1
if DPreArbalester == 1:
    Def_HP, Def_Helmet, Def_Armor = 60, 80, 65
if DPreBannerHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, SteelBrow = 80, 215, 150, 1
if DPreKnight == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge = 125, 300, 300, 1
if DPreSergeant == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble, SteelBrow = 100, 0, 150, -18, 1, 1
if DPreZweiHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, SteelBrow = 90, 160, 240, 1, 1
if DPreRaiderHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor = 70, 140, 115
if DPreMarkman == 1:
    Def_HP, Def_Helmet, Def_Armor = 60, 45, 70
if DPreLeaderHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, NineLives = 100, 250, 230, 1
if DPreMercenaryHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge = 90, 230, 260, 1
if DPreMercRange == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble = 65, 115, 115, -18, 1
if DPreHedgeKnight == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge, Resilient = 150, 300, 300, 1, 1
if DPreSwordmaster == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble, SteelBrow = 70, 70, 115, -15, 1, 1
if DPreMasterArcher == 1:   
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble, SteelBrow = 80, 30, 115, -12, 1, 1

#Error Handling
if (Mind == 0 and Maxd == 0) or Mind < 0 or Maxd < 0:
    sys.exit("Damage must be positive.")
if Mind > Maxd:
    sys.exit("Min damage must be <= Max damage.")
if Ignore < 0:
    sys.exit("Ignore must be positive.")
if ArmorMod <= 0:
    sys.exit("Armor damage must be positive.")
if Def_HP <= 0 or Def_Helmet < 0 or Def_Armor < 0:
    sys.exit("Hp and armor must be positive or 0.")
if Def_HP > 500 or Def_Helmet > 500 or Def_Armor > 500:
    sys.exit("Hp and armor must be <= 500.")
if Trials < 2:
    sys.exit("Trials must be >= 2.")

#Nimble calculation:
def NimbleCalc():
    global Fatigue,NimbleMod
    if Fatigue > 0 and Nimble == 1:
        Fatigue *= -1
    Fatigue = min(0, Fatigue + 15)
    if Nimble == 1:
        NimbleMod = 1.0 - 0.6 + pow(abs(Fatigue),1.23)*.01
        NimbleMod = min(1,NimbleMod)
    else:
        NimbleMod = 1

#Indomitable:
if Indomitable == 1:
    IndomMod = .5
elif PossessedUndead == 1: #This works just like Indom and they will never be both used together, so I put this here instead of writing a new variable.
    IndomMod = .75
else:
    IndomMod = 1

#Racial defense modifier:
if SkeletonVsPierce == 1:
    SkeletonMod = .5
elif SkeletonVsJavelin == 1:
    SkeletonMod = .25
elif SkeletonVsArrow == 1:
    SkeletonMod = .1
else:
    SkeletonMod = 1

#Attachment modifiers:
AttachMod = 1
if UnholdFurCloak == 1:
    AttachMod = .8
if HornPlate == 1:
    AttachMod = .9

if AdFurPad == 1:
    AdFurPadMod = .66
else: 
    AdFurPadMod = 1

print("-----") #Added for readability. If this annoys you then remove this line.

def calc():
    global Headshotchance,Ignore,Mind,Maxd,ArmorMod

    #Base damage modifiers:
    if TwoHander20 == 1:
        Mind += 20
        Maxd += 20

    #Armor damage modifiers:
    ArmorMod = ArmorMod/100
    if BrigandLeader == 1:
        ArmorMod += .2

    #Headshot damage modifiers:
    HeadMod = 1.5
    if SteelBrow == 1:
        HeadMod = 1
    else:
        if Brute == 1:
            HeadMod += .15
        if Axe1H == 1:
            HeadMod += .5

    #Headchance modifiers:
    Headshotchance = Headchance
    if Juggler == 1:
        Headshotchance += 5
    if KillerOnTheRun == 1:
        Headshotchance += 10

    #Ignore modifiers:
    Ignore = Ignore/100
    if Ambusher == 1:
        Ignore *= 1.4
    if AmbusherDay200 ==1:
        Ignore *= 1.5
    if Skirmisher == 1:
        Ignore *= 1.25
    if Overseer == 1:
        Ignore *= 1.1
    if Wolfrider == 1:
        Ignore *= 1.25
    if MasterArcher == 1:
        Ignore *= 1.25
    if Duelist == 1:
        Ignore += .25
    if XbowMastery == 1:
        Ignore += .2
    if AoE2HAxe == 1:
        Ignore -= .1
    if Ignore > 1:
        Ignore = 1

    #Damage modifiers:
    DamageMod = 1
    if DoubleGrip == 1:
        DamageMod *= 1.25
    if Flail3Head == 1:
        DamageMod *= .33
    if Spearwall == 1:
        DamageMod *= .5
    if R2Throw == 1:
        DamageMod *= 1.4
    if R3Throw == 1:
        DamageMod *= 1.2
    if AimedShot == 1:
        DamageMod *= 1.1
    if KillingFrenzy == 1:
        DamageMod *= 1.25
    if Huge == 1:
        DamageMod *= 1.1
    if Tiny == 1:
        DamageMod *= .85
    if Drunkard == 1:
        DamageMod *= 1.1
    if BrokenArm == 1:
        DamageMod *= .5
    if SplitShoulder == 1:
        DamageMod *= .5
    if CutArmSinew == 1:
        DamageMod *= .6
    if InjuredShoulder == 1:
        DamageMod *= .75
    if Dazed == 1:
        DamageMod *= .65
    if Young == 1:
        DamageMod *= 1.15
    if Berserker == 1:
        DamageMod *= 1.2
    if BerserkerDay190 == 1:
        DamageMod *= 1.3
    if Warrior == 1:
        DamageMod *= 1.15
    if WarriorDay200 == 1:
        DamageMod *= 1.25
    if Warlord == 1:
        DamageMod *= 1.35
    if WarlordDay200 == 1:
        DamageMod *= 1.45
    if Conqueror == 1:
        DamageMod *= 1.35
    if FallenBetrayer == 1:
        DamageMod *= 1.25
    if FallenHeroDay100 == 1:
        DamageMod *= 1.1
    if ArmoredZombieDay100 == 1:
        DamageMod *= 1.1
    if BarbKing == 1:
        DamageMod *= 1.2
    if HedgeKnight == 1:
        DamageMod *= 1.2
    if FrenziedDirewolf == 1:
        DamageMod *= 1.2
    if UnholdDay90 == 1:
        DamageMod *= 1.1
    if LindwurmDay170 == 1:
        DamageMod *= 1.1

    #Bleeding damage:
    BleedDamage = 0
    if CleaverBleed == 1:
        BleedDamage = 5
    if CleaverMastery == 1:
        BleedDamage = 10

    #Lists for later analysis:
    hits_until_death = [] #This list will hold how many hits until death for each iteration.
    hits_until_1st_injury = [] #This list will hold how many hits until first injury for each iteration.
    hits_until_1st_morale = [] #This list will hold how many hits until first morale check for each iteration.
    NumberFearsomeProcs = [] #This list will hold number of Fearsome procs for each iteration (only displays if Fearsome is checked).

    print("HP = " + str(Def_HP) + ", Helmet = " + str(Def_Helmet) + ", Armor = " + str(Def_Armor))
    print(Mind,Maxd,Headchance,Ignore,ArmorMod)
    NimbleCalc()
    if Nimble == 1:
        print ("Nimble%: " + str(NimbleMod))

    #Begin the simulation.
    for i in range(0,Trials): #This will run a number of trials as set above by the trials variable.
        #Stat initialization:
        hp = Def_HP
        helmet = Def_Helmet
        body = Def_Armor   

        #Sets various flags to a default state at the start of each new trial. 
        if HeadHunter == 1:
            Headshotchance = Headchance
        if Boneplate == 1:
            BoneplateMod = 1
        else:
            BoneplateMod = 0
        if NineLives == 1:
            NineLivesMod = 1
        else:
            NineLivesMod = 0
        Injury = 0
        MoraleCheck = 0
        FearsomeProcs = 0
        Bleedstack1T = 0
        Bleedstack2T = 0
        
        count = 0 #Number of hits until death. Starts at 0 and goes up after each attack.

        while hp > 0: #Continue looping until death.
            #Check various modifiers that change over the course of one's life. These will be re-checked after each attack.
            #Decapitate:
            if Decapitate == 1:
                DecapMod = 2 - hp / Def_HP
            elif SmartDecap50 == 1 and hp <= Def_HP / 2:
                DecapMod = 2 - hp / Def_HP
            elif SmartDecap33 == 1 and hp <= Def_HP / 3:
                DecapMod = 2 - hp / Def_HP
            else:
                DecapMod = 1
            #Destory Armor:
            if DestroyArmor == 1 and body > Maxd * ArmorMod * DamageMod * 1.5:
                DArmorMod = 1.5
            elif DestroyArmorMastery == 1 and body > Maxd * ArmorMod * DamageMod * 1.5:
                DArmorMod = 2
            else:
                DArmorMod = 1
            #Battleforged:
            if Forge == 1:
                ForgeMod = 1 - ((helmet + body) *.0005)
                if FallenBetrayerD == 1:
                    ForgeMod *= .75
            else:
                ForgeMod = 1
            #Executioner:
            if Injury == 1 and Executioner == 1:
                ExecMod = 1.2
            else:
                ExecMod = 1
            #Mushrooms:
            if Mushrooms1x == 1:
                MushroomMod = max(1,(1.3 - (0.1 * count)))
            elif Mushrooms2x == 1:
                MushroomMod = 1.3
                if count >= 2:
                    MushroomMod = 1.2
                if count >= 4:
                    MushroomMod = 1.1
                if count >= 6:
                    MushroomMod = 1
            else:
                MushroomMod = 1

            #Begin damage rolls:
            hp_roll = random.randint(Mind,Maxd) #Random roll to determine unmodified hp damage.
            head_roll = random.randint(1,100) #Random roll to determine if hit is a headshot.
            if head_roll <= Headshotchance: #If headshot, do the following code blocks.
                #HeadHunter check -- Lose current HH stacks since this is a headshot.
                if HeadHunter == 1 or HHCarryOver == 1:
                    Headshotchance = Headchance
                #Destroy armor check -- if Destroy Armor special is active do this code block and skip the rest.
                if DArmorMod != 1:
                    hp_roll = 10 #DestroyArmor forces hp damage to = 10.
                    hp -= hp_roll 
                    armor_roll = min(helmet,(random.randint(Mind,Maxd) * ArmorMod * DArmorMod * ForgeMod * IndomMod * DamageMod * MushroomMod * ExecMod))
                    helmet = math.floor(helmet - armor_roll + .5) #Rounding armor damage.
                #If not DestoryArmor, and no armor is present, apply damage directly to hp.
                elif helmet == 0:
                    hp_roll = hp_roll * NimbleMod * SkeletonMod * IndomMod * DamageMod * MushroomMod * ExecMod * DecapMod * HeadMod
                    if Hammer10 == 1: #If 1H Hammer, deal 10 damage minimum.
                        hp_roll = max(hp_roll,10)
                    hp = math.floor(hp - hp_roll + .5) #Rounding hp damage.
                #Otherwise, do the following.
                else:
                    armor_roll = min(helmet,(random.randint(Mind,Maxd) * ArmorMod * ForgeMod * IndomMod * DamageMod * MushroomMod * ExecMod))
                    helmet -= armor_roll #Armor damage applied to helmet.
                    #If the helmet does not get destroyed by the attack, do the following.
                    if helmet > 0:
                        hp_roll = max(0,(hp_roll * Ignore * NimbleMod * SkeletonMod * IndomMod * DamageMod * MushroomMod * ExecMod * DecapMod - (helmet * 0.1)) * HeadMod)
                        if Hammer10 == 1:
                            hp_roll = max(hp_roll,10) 
                        helmet = math.floor(helmet + .5)
                        hp = math.floor(hp - hp_roll + .5)
                    #If the helmet did get destoryed by the attack, do the following.
                    else:
                        OverflowDamage = max(0,(hp_roll * (1 - Ignore) * NimbleMod * SkeletonMod * IndomMod * DamageMod * MushroomMod * ExecMod * DecapMod - armor_roll))
                        hp_roll = (hp_roll * Ignore * NimbleMod * SkeletonMod * IndomMod * DamageMod * MushroomMod * ExecMod * DecapMod + OverflowDamage) * HeadMod
                        if Hammer10 == 1:
                            hp_roll = max(hp_roll,10)
                        hp = math.floor(hp - hp_roll + .5)
                #If SplitMan is active, do the following code block for the bonus body hit.
                if SplitMan == 1:
                    if BoneplateMod == 1:
                        BoneplateMod = 0
                    else:
                        SMhp_roll = random.randint(Mind,Maxd) * .5
                        if body == 0:
                            SMhp_roll = SMhp_roll * NimbleMod * IndomMod * AttachMod
                            hp = math.floor(hp - SMhp_roll + .5)
                        else:
                            SMarmor_roll = min(body,(random.randint(Mind,Maxd) * .5 * ArmorMod * ForgeMod * IndomMod * AttachMod))
                            body -= SMarmor_roll
                            if body > 0:
                                SMhp_roll = max(0,(SMhp_roll * Ignore * NimbleMod * AdFurPadMod * IndomMod * AttachMod - (body * 0.1)))
                                body = math.floor(body + .5)
                                hp = math.floor(hp - SMhp_roll + .5)
                            else:
                                OverflowDamage = max(0,(SMhp_roll * (1 - Ignore * AdFurPadMod) * NimbleMod * IndomMod * AttachMod - SMarmor_roll))
                                SMhp_roll = SMhp_roll * Ignore * NimbleMod * AdFurPadMod * IndomMod * AttachMod + OverflowDamage
                                hp = math.floor(hp - SMhp_roll + .5)
                        
            else: #If not a headshot, do the following. 
                #HeadHunter check -- Gain a HH stack since this is a body hit.
                if HeadHunter == 1 or HHCarryOver == 1:
                    Headshotchance += 15
                #Bone Plates check -- Attack is negated if Boneplates are online, then turns off Boneplates until next trial.
                if BoneplateMod == 1:
                    BoneplateMod = 0
                    hp_roll = 0
                else:
                    if DArmorMod != 1:
                        hp_roll = 10
                        hp -= hp_roll
                        armor_roll = min(body,(random.randint(Mind,Maxd) * ArmorMod * DArmorMod * ForgeMod * IndomMod * DamageMod * MushroomMod * ExecMod))
                        body = math.floor(body - armor_roll + .5)
                    elif body == 0:
                        hp_roll = hp_roll * NimbleMod * SkeletonMod * IndomMod * DamageMod * MushroomMod * ExecMod * DecapMod * AttachMod
                        if Hammer10 == 1:
                            hp_roll = max(hp_roll,10)
                        hp = math.floor(hp - hp_roll + .5)
                    else:
                        armor_roll = min(body,(random.randint(Mind,Maxd) * ArmorMod * ForgeMod * IndomMod * DamageMod * MushroomMod * ExecMod * AttachMod))
                        body -= armor_roll
                        if body > 0:
                            hp_roll = max(0,(hp_roll * Ignore * NimbleMod * SkeletonMod * AdFurPadMod * IndomMod * DamageMod * MushroomMod * ExecMod * DecapMod * AttachMod - (body * 0.1)))
                            if Hammer10 == 1:
                                hp_roll = max(hp_roll,10)
                            body = math.floor(body + .5)
                            hp = math.floor(hp - hp_roll + .5)
                        else:
                            OverflowDamage = max(0,(hp_roll * (1 - Ignore * AdFurPadMod) * NimbleMod * SkeletonMod * IndomMod * DamageMod * MushroomMod * ExecMod * DecapMod * AttachMod - armor_roll))
                            hp_roll = hp_roll * Ignore * NimbleMod * SkeletonMod * AdFurPadMod * IndomMod * DamageMod * MushroomMod * ExecMod * DecapMod * AttachMod + OverflowDamage
                            if Hammer10 == 1:
                                hp_roll = max(hp_roll,10)
                            hp = math.floor(hp - hp_roll + .5)
                #If SplitMan is active, do the following code block for the bonus head hit.
                if SplitMan == 1:
                    SMhp_roll = random.randint(Mind,Maxd) * .5
                    if helmet == 0:
                        SMhp_roll = SMhp_roll * NimbleMod * IndomMod
                        hp = math.floor(hp - SMhp_roll + .5)
                    else:
                        SMarmor_roll = min(helmet,(random.randint(Mind,Maxd) * .5 * ArmorMod * ForgeMod * IndomMod))
                        helmet -= SMarmor_roll
                        if helmet > 0:
                            SMhp_roll = max(0,(SMhp_roll * Ignore * NimbleMod * IndomMod - (helmet * 0.1)))
                            helmet = math.floor(helmet + .5)
                            hp = math.floor(hp -SMhp_roll + .5)
                        else:
                            OverflowDamage = max(0,(SMhp_roll * (1 - Ignore) * NimbleMod * IndomMod - SMarmor_roll))
                            SMhp_roll = SMhp_roll * Ignore * NimbleMod * IndomMod + OverflowDamage
                            hp = math.floor(hp - SMhp_roll + .5)

            count += 1 #Add +1 to the number of hits taken. 

            #Injury check:
            if Injury == 0 and Undead != 1 and Savant != 1:
                if CripplingStrikes == 1 and Shamshir == 1:
                    if math.floor(hp_roll + .4999) >= Def_HP / 9:
                        Injury = 1
                        if Flail3Head == 1:
                            hits_until_1st_injury.append(count/3)
                        else:    
                            hits_until_1st_injury.append(count)
                elif CripplingStrikes ==1 or Shamshir == 1:
                    if math.floor(hp_roll + .4999) >= Def_HP / 6:
                        Injury = 1
                        if Flail3Head == 1:
                            hits_until_1st_injury.append(count/3)
                        else:
                            hits_until_1st_injury.append(count)
                else: 
                    if math.floor(hp_roll + .4999) >= Def_HP / 4:
                        Injury = 1
                        if Flail3Head == 1:
                            hits_until_1st_injury.append(count/3)
                        else:    
                            hits_until_1st_injury.append(count)
            
            #Morale check:
            if MoraleCheck == 0:
                if Fearsome == 1:
                    if math.floor(hp_roll + .4999) > 0:
                        MoraleCheck = 1
                        if Flail3Head == 1:
                            hits_until_1st_morale.append(count/3)
                        else:
                            hits_until_1st_morale.append(count)
                else:
                    if math.floor(hp_roll + .4999) >= 15:
                        MoraleCheck = 1
                        if Flail3Head == 1:
                            hits_until_1st_morale.append(count/3)
                        else:
                            hits_until_1st_morale.append(count)

            #Fearsome:    
            if Fearsome == 1:
                if Flail3Head != 1:
                    if math.floor(hp_roll + .4999) > 0 and math.floor(hp_roll + .4999) < 15:
                        FearsomeProcs += 1
                else:
                    if Flail3Head == 1 and count % 3 == 1:
                        if math.floor(hp_roll + .4999) > 0 and math.floor(hp_roll + .4999) < 15:
                            FearsomeProcs += 1

            #Bleeding check:
            if (CleaverBleed == 1 or CleaverMastery == 1) and Undead != 1:
                #NineLives check -- If the attack proc'd NineLives then any bleeding damage will kill you.
                if hp <= 0 and NineLivesMod == 1:
                    hp = 1
                    NineLivesMod = 0
                #If damage taken >= 6 and Decapitate isn't in play, then apply a 2 turn bleed stack.
                if math.floor(hp_roll + .4999) >= 6 and DecapMod == 1 and Decapitate != 1:
                    Bleedstack2T += 1
                #Every two attacks (1 turn for Cleavers), apply bleed damage based on current bleed stacks.
                #If Resilient, 2 turn bleed stacks apply damage and then are removed. Otherwise 2 turn bleed stacks apply damage and convert into 1 turn bleed stacks.
                if count % 2 == 0:
                    if Resilient == 1:
                        hp -= BleedDamage * Bleedstack2T
                        Bleedstack2T = 0
                    else:
                        hp -= BleedDamage * Bleedstack1T
                        Bleedstack1T = Bleedstack2T
                        hp -= BleedDamage * Bleedstack2T
                        Bleedstack2T = 0

            #If death occurs, check for NineLives and otherwise add the hitcount to the list for later analysis and start the next trial.
            if hp <= 0: 
                if NineLivesMod == 1:
                    hp = 1
                    NineLivesMod = 0
                elif Fearsome == 1:
                    if Flail3Head == 1:
                        hits_until_death.append(count/3)
                    else:
                        hits_until_death.append(count)
                    NumberFearsomeProcs.append(FearsomeProcs)
                else:
                    if Flail3Head == 1:
                        hits_until_death.append(count/3)
                    else:
                        hits_until_death.append(count)

    #Analysis on data collection:
    HitsToDeath = statistics.mean(hits_until_death)
    StDev = statistics.stdev(hits_until_death)
    counter = collections.Counter(hits_until_death)
    percent = [(i,counter[i]/len(hits_until_death)*100) for i in counter]
    if Undead != 1 and Savant != 1:
        if len(hits_until_1st_injury) != 0:
            hits_to_injure = statistics.mean(hits_until_1st_injury)
        if len(hits_until_1st_morale) != 0:
            hits_to_morale = statistics.mean(hits_until_1st_morale)
        if Fearsome == 1:
            AvgFearsomeProcs = statistics.mean(NumberFearsomeProcs)

    #Results:
    print("Death in " + str(HitsToDeath) + " hits on average.")
    print("StDev: " + str(StDev))
    print("% hits to die " + str(percent))
    if Undead != 1 and Savant != 1:
        if len(hits_until_1st_injury) != 0:
            print("First injury in " + str(hits_to_injure) + " hits on average.")
        if len(hits_until_1st_morale) != 0:
            print("First morale check in " + str(hits_to_morale) + " hits on average.")
        if Fearsome == 1:
            print (str(AvgFearsomeProcs) + " Fearsome procs on average.")
    print("-----") #Added for readability. If this annoys you then remove this line.

#The following will repeatedly run the scenario with different attackers.
APreAncientSword = 1
PresetCalc()
print("Ancient Dead - Ancient Sword:")
calc()
APreAncientSword = 0

APreBladedPike = 1
PresetCalc()
print("Ancient Dead - Bladed Pike:")
calc()
APreBladedPike = 0

APreWarscytheAoE = 1
PresetCalc()
print("Ancient Dead - Warscythe AoE:")
calc()
APreWarscytheAoE = 0

APreCryptCleaver = 1
PresetCalc()
print("Ancient Dead - Crypt Cleaver:")
calc()
APreCryptCleaver = 0

Fearsome = 0
CleaverMastery = 0
APreKhopesh = 1
PresetCalc()
print("Necrosavant - Khopesh:")
calc()
APreKhopesh = 0

HeadHunter = 0
CleaverBleed = 0
DoubleGrip = 0
CripplingStrikes = 0
APreWingedMace = 1
PresetCalc()
print("Fallen Hero - Winged Mace:")
calc()
APreWingedMace = 0

Fearsome = 0
APreBerserkChain = 1
PresetCalc()
print("Orc Berserker - Berserk Chain:")
calc()
APreBerserkChain = 0

TwoHander20 = 0
Berserker = 0
APreHeadSplitter = 1
PresetCalc()
print("Orc Young/Warrior - Head Splitter:")
calc()
APreHeadSplitter = 0

Axe1H = 0
APreHeadChopper = 1
PresetCalc()
print("Orc Young/Warrior - Head Chopper:")
calc()
APreHeadChopper = 0

CleaverMastery = 0
Warrior = 0
APreMansplitter = 1
PresetCalc()
print("Orc Warlord - Mansplitter:")
calc()
APreMansplitter = 0

SplitMan = 0
Fearsome = 0
Warlord = 0
APreReinBoondock = 1
PresetCalc()
print("Goblin Ambusher - Reinforced Boondock Bow:")
calc()
APreReinBoondock = 0

Ambusher = 0
APreSpikedImpaler = 1
PresetCalc()
print("Goblin Overseer - Spiked Impaler:")
calc()
APreSpikedImpaler = 0

Overseer = 0
XbowMastery = 0
APre2HSpikedMace = 1
PresetCalc()
print("Chosen - 2H Spiked Mace:")
calc()
APre2HSpikedMace = 0

APre2HSkullHammer = 1
PresetCalc()
print("Chosen - 2H Skull Hammer:")
calc()
APre2HSkullHammer = 0

TwoHander20 = 0
APreHeavyRustyAxe = 1
PresetCalc()
print("Chosen - Heavy Rusty Axe:")
calc()
APreHeavyRustyAxe = 0

SplitMan = 0
APreRustyWarblade = 1
PresetCalc()
print("Chosen - Rusty Warblade:")
calc()
APreRustyWarblade = 0

CripplingStrikes = 0
Executioner = 0
CleaverMastery = 0
APreBillhook = 1
PresetCalc()
print("Billman - Billhook:")
calc()
APreBillhook = 0

APreHeavyXbow = 1
PresetCalc()
print("Arbalester - Heavy Xbow:")
calc()
APreHeavyXbow = 0

XbowMastery = 0
APreFightingAxe = 1
PresetCalc()
print("Knight - Fighting Axe:")
calc()
APreFightingAxe = 0

Axe1H = 0
CripplingStrikes = 0
Executioner = 0
APreWarHammer = 1
PresetCalc()
print("Sergeant - Warhammer:")
calc()
APreWarHammer = 0

Duelist = 0
DoubleGrip = 0
Hammer10 = 0
APreGreatsword = 1
PresetCalc()
print("Zweihander - Greatsword:")
calc()
APreGreatsword = 0

TwoHander20 = 0
APreFlailDGrip = 1
PresetCalc()
print("Raider - Flail (Double Grip):")
calc()
APreFlailDGrip = 0

DoubleGrip = 0
APreLongAxe = 1
PresetCalc()
print("Raider - Longaxe:")
calc()
APreLongAxe = 0

Executioner = 0
APreMedXbow = 1
PresetCalc()
print("Marksman - Xbow:")
calc()
APreMedXbow = 0

XbowMastery = 0
APreNobleSword = 1
PresetCalc()
print("Swordmaster - Noble Sword:")
calc()
APreNobleSword = 0

Duelist = 0
DoubleGrip = 0
APreWarbow = 1
PresetCalc()
print("Master Archer - Warbow:")
calc()
APreWarbow = 0

CripplingStrikes = 0
HeadHunter = 0
MasterArcher = 0
APreFDirewolf = 1
PresetCalc()
print("Frenzied Direwolf:")
calc()
APreFDirewolf = 0

FrenziedDirewolf = 0
Executioner = 0
APreNachTier3 = 1
PresetCalc()
print("Nachzehrer - Tier 3:")
calc()
APreNachTier3 = 0

APreLindwurm = 1
PresetCalc()
print("Lindwurm - Head:")
calc()
APreLindwurm = 0

Fearsome = 0
APreUnhold = 1
PresetCalc()
print("Unhold:")
calc()
APreUnhold = 0

APreSchrat = 1
PresetCalc()
print("Schrat:")
calc()
APreSchrat = 0

CripplingStrikes = 0

#CREDITS:
#Author: turtle225
#Contact: turtl225e@gmail.com
#Copyright 2019, turtle225. All rights reserved.
#Special Thanks:
#-- Abel (aka) Villain Joueur: For grabbing the damage formula out of the game code, writing the damage page on the wiki, and for helping me with many questions along the way.
#-- Wall (aka) Wlira: For helping me with some questions along the way and having an existing calculator for me to test against.
#-- You: If you are using the calculator, thank you! If you find any bugs or have feedback/questions/suggestions, you can usually find me on the Steam forums or send me an email.

#History:
#Version 1.0.0 (12/28/2019)
#-- First released on Github.