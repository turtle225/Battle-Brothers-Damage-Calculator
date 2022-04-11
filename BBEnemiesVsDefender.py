#Battle Brothers Damage Calculator -- Enemies Vs. Defender Version 1.6.3:
#Welcome. Modify the below values as necessary until you reach the line ----- break.

#This version of the calculator will run 35 different enemies against a given defender.
#Attacker specific perks, weapons, and traits are automatically applied.
#If you wish to more easily compare two test cases, run the script once in two separate terminals.

#Note: Since this calculator runs multiple times per launch, default trials has been lowered. Adjust this to your preferences.
Trials = 10000 #Number of trials to run through. More trials leads to more accurate results but longer compute times.

#Data Returns: Set these values to 1 if you want more data returned, and 0 if you want less data returned.
#Note: If injuries/morale do not occur because defender is Undead then they will not display even if checked here. 
DeathMean = 1          #Returns the average number of hits until death.
DeathStDev = 1         #Returns standard deviation of hits until death.
DeathPercent = 1       #Returns % chance of death by each hit.
InjuryMean = 1         #Returns average number of hits until first injury.
InjuryPercent = 0      #Returns % chance of first injury by each hit.
HeavyInjuryMean = 1    #Returns average number of hits until chance of first heavy injury (heavy injuries are not guaranteed even when threshold is met).
HeavyInjuryPercent = 0 #Returns % chance of first heavy injury chance by each hit.
MoraleMean = 0         #Returns average number of hits until first morale check.
MoralePercent = 0      #Returns % chance of first morale check by each hit.
#IMPORTANT: Be cautious about blindly trusting the following two values. They can be useful for comparisons,
#but scoring high in these doesn't necessarily mean something is always better. As an example, this test
#values surviving against Ambushers with equal value as surviving against Chosen, this skews the results in favor of heavy armor.
TotalMean = 1          #Returns the total of mean hits to die for each test added together at the very end.
AverageMeanPerTest = 1 #Returns average hits to die against the whole test group.

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
Nimble = 0
Forge = 0
Indomitable = 0
#Attachments: Note: Only 1 attachment should be selected.
#IMPORTANT: Attachments will automatically add armor or subtract Fatigue. Use the base armor/Fatigue values in the Defender Stats section or else you will double dip the attachment.
Wolf_Hyena = 0          #+15 armor.
LindwurmCloak = 0       #+60 armor, -3 Fatigue.
AdFurPad = 0            #Additional Fur Padding. 33% reduced armor ignoring damage. -2 Fatigue.
Boneplate = 0           #Absorbs first body hit. -2 Fatigue.
HornPlate = 0           #Only select against melee attacks. +30 armor, 10% damage reduction. WARNING: Applies to all enemies if selected.
UnholdFurCloak = 0      #Only select against range attacks. +10 armor, 20% damage reduction. WARNING: Applies to all enemies if selected.
SerpentSkin = 0         #Only select in Handgonne tests. +30 armor, -2 Fatigue, 33% damage reduction. WARNING: Applies to all enemies if selected.
#Light Padding Replacement -- Modify the Fatigue value directly if you wish to apply this. Has no effect except for Nimble.
#Traits:
Ironjaw = 0             #Reduces injury susceptibility.
GloriousEndurance = 0   #The Bear's unique trait. Reduces damage by 5% each time you are hit, up to a 25% max reduction.

#Defender Preset: Set these values to 1 if you wish to use a defender preset, and 0 otherwise.
#A preset will automatically set defender stats and defender perks.
#Does not disable perks that shouldn't be active. For example, Don't activate Nimble and then check the Orc Warrior Preset.
DPreNimbleBro = 0       # 120hp, 120/95, Nimble (A generic Nimble line with just Nimble).
DPreNimbleBroBP = 0     # 120hp, 120/80 Nimble, Bone Plates.
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
DPreOutlawHeavy = 0     # 75hp, 125/105.
DPreConscript = 0       # 55hp, 105/110, Nimble. (-16 Fat)
DPreOfficer = 0         # 100hp, 290/290, Forge.
DPreAssassinHeavy = 0   # 80hp, 140/120, Nimble. (-15 Fat)

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
Flail2HPound = 0        #Ignore +10% on body hits and +20% on headshots. Applies to 2H Flail Pound attack. Apply the +20 damage from Pound using the TwoHander20 switch.
FlailMastery = 0        #Flail Mastery. Will apply an extra 10% armor ignore on headshots for Pound. Does nothing unless Flail2HPound is set.
Hammer10 = 0            #Guarantees at least 10 hp damage, applies to 1H Hammer and Polehammer.
DestroyArmor = 0        #Will use Destroy Armor once and then switch to normal attacks.
DestroyArmorMastery = 0 #Hammer Mastery. Will use Destroy Armor once and then switch to normal attacks.
DestroyArmorTwice = 0   #Uses Destroy Armor two times instead of 1. Does nothing unless DestroyArmor or DestroyArmorMastery are set.
Axe1H = 0               #Applies bonus damage to Headshots. Gets negated by SteelBrow.
SplitMan = 0            #Applies to single target 2HAxe except for Longaxe.
AoE2HAxe = 0            #Applies to Round Swing and Split in Two (Bardiche), reduces Ignore by 10%.
CleaverBleed = 0        #5 bleed damage per bleed tick.
CleaverMastery = 0      #10 bleed damage per bleed tick. 
Decapitate = 0          #Cleaver Decapitate. Will use Decapitate for all attacks.
SmartDecap50 = 0        #Switches from normal Cleaver attacks to Decapitate once opposing hp is <= 50%.
SmartDecap33 = 0        #Switches from normal Cleaver attacks to Decapitate once opposing hp is <= 33.33%.
Shamshir = 0            #Shamshir special, acts like Crippling Strikes.
ShamshirMastery = 0     #Sword Mastery with Gash, 50% reduction to injury threshold instead of 33%.
Sword2HSplit = 0        #Ignore +5%. Applies to Greatsword Split attack. Does not apply to Overhead or Swing.
Puncture = 0            #Dagger Puncture. Do not apply Double Grip
Deathblow = 0           #Qatal special. Ignore +20%. Damage x1.33. Assumes target is always setup for Deathblow value in calculation.
Spearwall = 0           #Warning: May take a long time to compute against durable targets, considering lowering number of trials. 
AimedShot = 0           #HP Damage +10% for Bows. +5% Armor Ignore.
XbowMastery = 0         #Ignore +20%.
R2Throw = 0             #Throwing Mastery for 1 or 2 Range.
R3Throw = 0             #Throwing Mastery for 3 Range.    
Scatter = 0             #Ranged attacks that hit an unintended target deal 75% damage.
#Perks:
CripplingStrikes = 0
Executioner = 0
HeadHunter = 0          #Will carry over HH stacks between kills as happens in game.
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
Dazed = 0               #Damage -25%. Set this if you want to simulate the attacker always being Dazed.
Distracted = 0          #Damage -35%. Set this if you want to simulate the attacker always being Distracted (applied by Nomads).
Mushrooms = 0           #Damage +25%. Set this to simulate a Mushroom enhanced brother.

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
Ambusher = 0            #Ignore * 1.25
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
APreCryptCleaver = 0    #Ancient Dead: 60-80, 25% Ignore, 120% Armor, Fearsome, Cleaver Mastery.
APreKhopesh = 0         #Necrosavant: 35-55, 25% Ignore, 120% Armor, HeadHunter, Crippling, Double Grip, CleaverBleed.
APreFHGreatAxe = 0      #Fallen Hero: 80-100, 40 %Ignore, 150% Armor, Fearsome, Split Man.
APreBerserkChain = 0    #Orc Berserker: 50-100, 30% Ignore, 125% Armor, 40% Head, TwoHander20, Flail2HPound, FlailMastery, Berserker.
APreHeadSplitter = 0    #Orc Young/Warrior: 35-65, 30% Ignore, 130% Armor, 1HAxe, Warrior.
APreHeadChopper = 0     #Orc Young/Warrior: 40-70, 25% Ignore, 110% Armor, Cleaver Mastery, Warrior.
APreMansplitter = 0     #Orc Warlord: 90-120, 40% Ignore, 160% Armor, Split Man, Fearsome, Warlord.
APreReinBoondock = 0    #Goblin Ambusher: 30-50, 35% Ignore, 60% Armor, Ambusher.
APreSpikedImpaler = 0   #Goblin Overseer: 50-70, 50% Ignore, 75% Armor, Overseer, Xbow Mastery.
APre2HSpikedMace = 0    #Chosen: 50-70, 60% Ignore, 115% Armor, Crippling, Executioner, TwoHander20.
APre2HSkullHammer = 0   #Chosen: 45-65, 60% Ignore, 180% Armor, Crippling, Executioner, TwoHander20.
APreHeavyRustyAxe = 0   #Chosen: 75-90, 50% Ignore, 150% Armor, Crippling, Executioner, Split Man.
APreRustyWarblade = 0   #Chosen: 60-80, 35% Ignore, 110% Armor, Crippling, Executioner, Cleaver Mastery.
APreBillhook = 0        #Billman: 55-85, 30% Ignore, 140% Armor, 30% Head.
APreHeavyXbow = 0       #Arbalester: 50-70, 50% Ignore, 75% Armor, XbowMastery.
APreFightingAxe = 0     #Knight: 35-55, 30% Ignore, 130% Armor, 1HAxe, Crippling, Executioner.
APreWingedMace = 0      #Sergeant: 35-55, 40% Ignore, 110% Armor, Duelist, Double Grip
APreGreatsword = 0      #Zweihander: 85-100, 25% Ignore, 100% Armor, 30% Head, TwoHander20.
APreFlailDGrip = 0      #Raider: 25-55, 30% Ignore, 100% Armor, 35% Head, Double Grip, Executioner.
APreLongAxe = 0         #Raider: 70-95, 30% Ignore, 110% Armor, 30% Head, Executioner. 
APreMedXbow = 0         #Marksman: 40-60, 50% Ignore, 70% Armor, Xbow Mastery.
APreNobleSword = 0      #Swordmaster: 45-50, 20% Ignore, 85% Armor, Duelist, Double Grip, Crippling, Executioner.
APreWarbow = 0          #Master Archer: 50-70, 35% Ignore, 65% Armor, Crippling, Executioner, HeadHunter, Master Archer. 
APrePoleMace = 0        #Conscript: 60-75, 40% Ignore, 120% Armor, 30% Head.
APreHandgonne = 0       #Gunner: 35-75, 25% Ignore, 90% Armor, Fearsome.
APre2HScimitar = 0      #Officer: 65-85, 25% Ignore, 110% Armor, Crippling, Executioner.
APreQatal = 0           #Assassin: 30-45, 20% Ignore, 70% Armor, Duelist, Double Grip, Executioner.
APreFDirewolf = 0       #Frenzied Direwolf: 30-50, 20% Ignore, 70% Armor, Executioner, Frenzied Direwolf.
APreNachTier3 = 0       #Tier 3 Nachzehrer: 55-80, 10% Ignore, 75% Armor.
APreLindwurm = 0        #Lindwurm Head: 80-140, 35% Ignore, 140% Armor, Fearsome.
APreUnhold = 0          #Unhold: 40-80, 40% Ignore, 80% Armor, Crippling.
APreSchrat = 0          #Schrat: 70-100, 50% Ignore, 80% Armor, Crippling.

#Attacker presets:
def PresetCalc():
    global Mind,Maxd,Headchance,Ignore,ArmorMod,Fearsome,CleaverMastery,HeadHunter,CripplingStrikes,DoubleGrip,CleaverBleed,TwoHander20,Berserker,Axe1H,Warrior,SplitMan,Warlord,Ambusher,Overseer,XbowMastery,Executioner,Duelist,MasterArcher,FrenziedDirewolf,Hammer10,Flail2HPound,FlailMastery
    if APreAncientSword == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 38, 43, 25, 20, 80, 1
    if APreBladedPike == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 55, 80, 30, 30, 125, 1
    if APreWarscytheAoE == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 55, 80, 25, 25, 104, 1
    if APreCryptCleaver == 1: 
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome, CleaverMastery = 60, 80, 25, 25, 120, 1, 1
    if APreKhopesh == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, HeadHunter, CripplingStrikes, DoubleGrip, CleaverBleed = 35, 55, 25, 25, 120, 1, 1, 1, 1
    if APreFHGreatAxe == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome, SplitMan = 80, 100, 25, 40, 150, 1, 1
    if APreBerserkChain == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, TwoHander20, Flail2HPound, FlailMastery, Berserker = 50, 100, 40, 30, 125, 1, 1, 1, 1
    if APreHeadSplitter == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Axe1H, Warrior = 35, 65, 25, 30, 130, 1, 1
    if APreHeadChopper == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CleaverMastery, Warrior = 40, 70, 25, 25, 110, 1, 1
    if APreMansplitter == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, SplitMan, Fearsome, Warlord = 90, 120, 25, 40, 160, 1, 1, 1
    if APreReinBoondock == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Ambusher = 30, 50, 25, 35, 60, 1
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
        Mind, Maxd, Headchance, Ignore, ArmorMod = 55, 85, 30, 30, 140
    if APreHeavyXbow == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, XbowMastery = 50, 70, 25, 50, 75, 1
    if APreFightingAxe == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Axe1H, CripplingStrikes, Executioner = 35, 55, 25, 30, 130, 1, 1, 1
    if APreWingedMace == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Duelist, DoubleGrip = 35, 55, 25, 40, 110, 1, 1
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
    if APrePoleMace == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod = 60, 75, 30, 40, 120
    if APreHandgonne == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 35, 75, 25, 25, 90, 1
    if APre2HScimitar == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CleaverMastery, CripplingStrikes, Executioner = 65, 85, 25, 25, 110, 1, 1, 1
    if APreQatal == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Duelist, DoubleGrip, Executioner = 30, 45, 25, 20, 70, 1, 1, 1
    if APreFDirewolf == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Executioner, FrenziedDirewolf = 30, 50, 25, 20, 70, 1, 1
    if APreNachTier3 == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod = 55, 80, 25, 10, 75
    if APreLindwurm == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, Fearsome = 80, 140, 25, 35, 140, 1
    if APreUnhold == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes = 40, 80, 25, 40, 80, 1
    if APreSchrat == 1:
        Mind, Maxd, Headchance, Ignore, ArmorMod, CripplingStrikes = 70, 100, 25, 50, 80, 1

#Defender preset automation:
if DPreNimbleBro == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble = 120, 120, 95, -15, 1
if DPreNimbleBroBP == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble, Boneplate = 120, 120, 80, -13, 1, 1
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
if DPreOutlawHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor = 75, 125, 105
if DPreConscript == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble = 55, 105, 110, -16, 1
if DPreOfficer == 1:
    Def_HP, Def_Helmet, Def_Armor, Forge = 100, 290, 290, 1
if DPreAssassinHeavy == 1:
    Def_HP, Def_Helmet, Def_Armor, Fatigue, Nimble = 80, 140, 120, -15, 1

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

#Fatigue force negative:
if Fatigue > 0 and Nimble == 1:
    Fatigue *= -1

#Attachment modifiers:
AttachMod = 1
if UnholdFurCloak == 1:
    AttachMod = .8
    Def_Armor += 10
if HornPlate == 1:
    AttachMod = .9
    Def_Armor += 30
if SerpentSkin == 1:
    AttachMod = .66
    Def_Armor += 30
    Fatigue -= 2

if Wolf_Hyena == 1:
    Def_Armor += 15
if LindwurmCloak == 1:
    Def_Armor += 60
    Fatigue -= 3

if AdFurPad == 1:
    AdFurPadMod = .66
    Fatigue -= 2
else: 
    AdFurPadMod = 1

if Boneplate == 1:
    Fatigue -= 2

#Nimble calculation:
def NimbleCalc():
    global NimbleMod
    NimFat = Fatigue
    if NimFat > 0 and Nimble == 1:
        NimFat *= -1
    NimFat = min(0, NimFat + 15)
    if Nimble == 1:
        NimbleMod = 1.0 - 0.6 + pow(abs(NimFat),1.23)*.01
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

total = 0 #This is used when adding means for when you have that data output checked at the very top.

print("-----") #Added for readability. If this annoys you then remove this line.

def calc():
    global Headshotchance,Ignore,Mind,Maxd,ArmorMod,total,HHStack

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
    if Flail2HPound == 1:
        Flail2HBodyshot = Ignore + .1
        Flail2HHeadshot = Ignore + .2
        if FlailMastery == 1:
            Flail2HHeadshot += .1
    if Sword2HSplit == 1:
        Ignore += .05
    if Deathblow == 1:
        Ignore += .2
    if AimedShot == 1:
        Ignore += .05
    if XbowMastery == 1:
        Ignore += .2
    if Ambusher == 1:
        Ignore *= 1.25
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
    if AoE2HAxe == 1:
        Ignore -= .1
    if Ignore > 1:
        Ignore = 1

    #HeadHunter
    HHStack = 0

    #Damage modifiers:
    DamageMod = 1
    if DoubleGrip == 1:
        DamageMod *= 1.25
    if Flail3Head == 1:
        DamageMod *= .33
    if Deathblow == 1:
        DamageMod *= 1.33
    if Spearwall == 1:
        DamageMod *= .5
    if R2Throw == 1:
        DamageMod *= 1.3
    if R3Throw == 1:
        DamageMod *= 1.2
    if Scatter == 1:
        DamageMod *= .75
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
        DamageMod *= .75
    if Distracted == 1:
        DamageMod *= .65
    if Mushrooms == 1:
        DamageMod *= 1.25
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

    if AimedShot == 1:
        AimedShotMod = 1.1
    else:
        AimedShotMod = 1

    #Bleeding damage:
    BleedDamage = 0
    if CleaverBleed == 1:
        BleedDamage = 5
    if CleaverMastery == 1:
        BleedDamage = 10
    if Indomitable == 1 and BleedDamage > 0:
        BleedDamage = math.floor(BleedDamage / 2)

    #Lists for later analysis:
    hits_until_death = [] #This list will hold how many hits until death for each iteration.
    hits_until_1st_injury = [] #This list will hold how many hits until first injury for each iteration.
    hits_until_1st_heavy_injury_chance = [] #This list will hold how many hits until a chance of heavy injury for each iteration.
    hits_until_1st_morale = [] #This list will hold how many hits until first morale check for each iteration.
    NumberFearsomeProcs = [] #This list will hold number of Fearsome procs for each iteration (only displays if Fearsome is checked).
    Forge_bonus_armor = [] #This list will hold the amount of extra armor provided by Forge for each iteration (only displays if Forge is checked).
    hits_until_1st_poison = [] #This list will hold how many hits until first poisoning against Ambushers (only displays if Ambusher is checked)

    print("HP = " + str(Def_HP) + ", Helmet = " + str(Def_Helmet) + ", Armor = " + str(Def_Armor))
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
        HeavyInjuryChance = 0
        UseHeadShotInjuryFormula = 0
        UseHeadShotInjuryFormulaHeavy = 0
        FirstMoraleCheck = 0
        FearsomeProcs = 0
        Bleedstack1T = 0
        Bleedstack2T = 0
        ForgeSaved = 0                      #Tracker to add the amount of armor gained from Forge for each iteration.
        Poison = 0                          #Tracker for when first poisoning occurs against Ambushers.
        
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
            if DestroyArmor == 1 and count == 0:
                DArmorMod = 1.5
            elif DestroyArmor == 1 and count == 1 and DestroyArmorTwice == 1:
                DArmorMod = 1.5
            elif DestroyArmorMastery == 1 and count == 0:    
                DArmorMod = 2
            elif DestroyArmorMastery == 1 and count == 1 and DestroyArmorTwice == 1:
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
            #Gladiator - The Bear - Glorious Endurance:
            if GloriousEndurance == 1:
                if SplitMan == 1:
                    GladMod = 1 - (.05 * (count * 2))
                else:
                    GladMod = 1 - (.05 * count)
                if GladMod < .75:
                    GladMod = .75
            else:
                GladMod = 1
            #Executioner:
            if Injury == 1 and Executioner == 1:
                ExecMod = 1.2
            else:
                ExecMod = 1
            #HeadHunter:
            if HeadHunter == 1:
                if HHStack == 1:
                    Headshotchance = 100
                else:
                    Headshotchance = Headchance

            #Begin damage rolls:
            hp_roll = random.randint(Mind,Maxd) #Random roll to determine unmodified hp damage.
            head_roll = random.randint(1,100) #Random roll to determine if hit is a headshot.
            if head_roll <= Headshotchance: #If headshot, do the following code blocks.
                #Headshot Injury Flag -- Headshot injuries use a different formula. This flag will signal later when Injury is checked.
                UseHeadShotInjuryFormula = 1
                UseHeadShotInjuryFormulaHeavy = 1
                #HeadHunter check -- Lose current stack if you had one. Gain stack if you didn't.
                if HeadHunter == 1:
                    if HHStack == 0:
                        HHStack = 1
                    elif HHStack == 1:
                        HHStack = 0
                #2H Flail Check -- Have a higher armor ignoring% on Pound for headshots compared to bodyshots.
                if Flail2HPound == 1:
                    Ignore = Flail2HHeadshot
                #Destroy armor check -- if Destroy Armor special is active do this code block and skip the rest.
                if DArmorMod != 1:
                    hp_roll = 10 #DestroyArmor forces hp damage to = 10.
                    hp -= hp_roll 
                    armor_roll = random.randint(Mind,Maxd) * ArmorMod * DArmorMod * GladMod * IndomMod * DamageMod *  ExecMod
                    ForgeSaved += armor_roll - armor_roll * ForgeMod
                    armor_roll = min(helmet,(armor_roll * ForgeMod))
                    helmet = math.ceil(helmet - armor_roll) #Rounding armor damage.
                #If not DestoryArmor, and no armor is present, apply damage directly to hp.
                elif helmet == 0:
                    hp_roll = hp_roll * NimbleMod * SkeletonMod * GladMod * IndomMod * ((DamageMod *  ExecMod * AimedShotMod) * DecapMod) * HeadMod
                    if Hammer10 == 1: #If 1H Hammer, deal 10 damage minimum.
                        hp_roll = max(hp_roll,10)
                    hp = math.ceil(hp - hp_roll) #Rounding hp damage.
                #Otherwise, do the following.
                else:
                    armor_roll = random.randint(Mind,Maxd) * ArmorMod * GladMod * IndomMod * DamageMod *  ExecMod
                    ForgeSaved += armor_roll - armor_roll * ForgeMod #Calculate how much armor is saved by Forge.
                    armor_roll = min(helmet,(armor_roll * ForgeMod)) #Applying Forge, and armor damage cannot exceed current armor.
                    helmet -= armor_roll #Armor damage applied to helmet.
                    #If the helmet does not get destroyed by the attack, do the following.
                    if helmet > 0:
                        hp_roll = max(0,(hp_roll * Ignore * NimbleMod * SkeletonMod * GladMod * IndomMod * ((DamageMod *  ExecMod * AimedShotMod) * DecapMod) - (helmet * 0.1)) * HeadMod)
                        if Hammer10 == 1:
                            hp_roll = max(hp_roll,10) 
                        helmet = math.ceil(helmet)
                        hp = math.ceil(hp - hp_roll)
                    #If the helmet did get destoryed by the attack, do the following.
                    else:
                        OverflowDamage = max(0,(hp_roll * (1 - Ignore) * NimbleMod * SkeletonMod * GladMod * IndomMod * ((DamageMod *  ExecMod * AimedShotMod) * DecapMod) - armor_roll))
                        hp_roll = (hp_roll * Ignore * NimbleMod * SkeletonMod * GladMod * IndomMod * ((DamageMod *  ExecMod * AimedShotMod) * DecapMod) + OverflowDamage) * HeadMod
                        if Hammer10 == 1:
                            hp_roll = max(hp_roll,10)
                        hp = math.ceil(hp - hp_roll)
                #If SplitMan is active, do the following code block for the bonus body hit.
                if SplitMan == 1:
                    if BoneplateMod == 1:
                        BoneplateMod = 0
                    else:
                        SMhp_roll = random.randint(Mind,Maxd) * .5
                        if body == 0:
                            SMhp_roll = SMhp_roll * NimbleMod * GladMod * IndomMod * AttachMod
                            hp = math.ceil(hp - SMhp_roll)
                        else:
                            SMarmor_roll = random.randint(Mind,Maxd) * .5 * ArmorMod * GladMod * IndomMod * AttachMod
                            ForgeSaved += SMarmor_roll - SMarmor_roll * ForgeMod
                            SMarmor_roll = min(body,(SMarmor_roll * ForgeMod))
                            body -= SMarmor_roll
                            if body > 0:
                                SMhp_roll = max(0,(SMhp_roll * Ignore * NimbleMod * AdFurPadMod * GladMod * IndomMod * AttachMod - (body * 0.1)))
                                body = math.ceil(body)
                                hp = math.ceil(hp - SMhp_roll)
                            else:
                                OverflowDamage = max(0,(SMhp_roll * (1 - Ignore * AdFurPadMod) * NimbleMod * GladMod * IndomMod * AttachMod - SMarmor_roll))
                                SMhp_roll = SMhp_roll * Ignore * NimbleMod * AdFurPadMod * GladMod * IndomMod * AttachMod + OverflowDamage
                                hp = math.ceil(hp - SMhp_roll)
                        
            else: #If not a headshot, do the following. 
                #2H Flail Check -- Have a higher armor ignoring% on Pound for headshots compared to bodyshots.
                if Flail2HPound == 1:
                    Ignore = Flail2HBodyshot
                #Bone Plates check -- Attack is negated if Boneplates are online, then turns off Boneplates until next trial.
                if BoneplateMod == 1:
                    BoneplateMod = 0
                    hp_roll = 0
                else:
                    if DArmorMod != 1:
                        hp_roll = 10
                        hp -= hp_roll
                        armor_roll = random.randint(Mind,Maxd) * ArmorMod * DArmorMod * GladMod * IndomMod * DamageMod *  ExecMod
                        ForgeSaved += armor_roll - armor_roll * ForgeMod
                        armor_roll = min(body,(armor_roll * ForgeMod))
                        body = math.ceil(body - armor_roll)
                    elif body == 0 or Puncture == 1:
                        hp_roll = hp_roll * NimbleMod * SkeletonMod * GladMod * IndomMod * AttachMod * ((DamageMod *  ExecMod * AimedShotMod) * DecapMod)
                        if Hammer10 == 1:
                            hp_roll = max(hp_roll,10)
                        hp = math.ceil(hp - hp_roll)
                    else:
                        armor_roll = random.randint(Mind,Maxd) * ArmorMod * GladMod * IndomMod * DamageMod *  ExecMod * AttachMod
                        ForgeSaved += armor_roll - armor_roll * ForgeMod
                        armor_roll = min(body,(armor_roll * ForgeMod))
                        body -= armor_roll
                        if body > 0:
                            hp_roll = max(0,(hp_roll * Ignore * NimbleMod * SkeletonMod * AdFurPadMod * GladMod * IndomMod * AttachMod * ((DamageMod *  ExecMod * AimedShotMod) * DecapMod) - (body * 0.1)))
                            if Hammer10 == 1:
                                hp_roll = max(hp_roll,10)
                            body = math.ceil(body)
                            hp = math.ceil(hp - hp_roll)
                        else:
                            OverflowDamage = max(0,(hp_roll * (1 - Ignore * AdFurPadMod) * NimbleMod * SkeletonMod * GladMod * IndomMod * AttachMod * ((DamageMod *  ExecMod * AimedShotMod) * DecapMod) - armor_roll))
                            hp_roll = hp_roll * Ignore * NimbleMod * SkeletonMod * AdFurPadMod * GladMod * IndomMod * AttachMod * ((DamageMod *  ExecMod * AimedShotMod) * DecapMod) + OverflowDamage
                            if Hammer10 == 1:
                                hp_roll = max(hp_roll,10)
                            hp = math.ceil(hp - hp_roll)
                #If SplitMan is active, do the following code block for the bonus head hit.
                if SplitMan == 1:
                    SMhp_roll = random.randint(Mind,Maxd) * .5
                    if helmet == 0:
                        SMhp_roll = SMhp_roll * NimbleMod * GladMod * IndomMod
                        hp = math.ceil(hp - SMhp_roll)
                    else:
                        SMarmor_roll = random.randint(Mind,Maxd) * .5 * ArmorMod * GladMod * IndomMod
                        ForgeSaved += SMarmor_roll - SMarmor_roll * ForgeMod
                        SMarmor_roll = min(helmet,(SMarmor_roll * ForgeMod))
                        helmet -= SMarmor_roll
                        if helmet > 0:
                            SMhp_roll = max(0,(SMhp_roll * Ignore * NimbleMod * GladMod * IndomMod - (helmet * 0.1)))
                            helmet = math.ceil(helmet)
                            hp = math.ceil(hp - SMhp_roll)
                        else:
                            OverflowDamage = max(0,(SMhp_roll * (1 - Ignore) * NimbleMod * GladMod * IndomMod - SMarmor_roll))
                            SMhp_roll = SMhp_roll * Ignore * NimbleMod * GladMod * IndomMod + OverflowDamage
                            hp = math.ceil(hp - SMhp_roll)

            count += 1 #Add +1 to the number of hits taken. 

            #Injury check:
            if UseHeadShotInjuryFormula == 1:
                if Injury == 0 and Undead != 1 and Savant != 1:
                    if CripplingStrikes == 1 and ShamshirMastery == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/192):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP * (5/48):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        UseHeadShotInjuryFormula = 0
                    elif CripplingStrikes == 0 and ShamshirMastery == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/128):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP * (5/32):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        UseHeadShotInjuryFormula = 0
                    elif CripplingStrikes == 1 and Shamshir == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/144):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP * (5/36):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        UseHeadShotInjuryFormula = 0
                    elif CripplingStrikes == 1 or Shamshir == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/96):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP * (5/24):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        UseHeadShotInjuryFormula = 0
                    else: 
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/64):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP * (5/16):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        UseHeadShotInjuryFormula = 0

            else: #Use body injury formula.
                if Injury == 0 and Undead != 1 and Savant != 1:
                    if CripplingStrikes == 1 and ShamshirMastery == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/48):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP / 12:
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                    elif CripplingStrikes == 0 and ShamshirMastery == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/32):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP / 8:
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                    elif CripplingStrikes == 1 and Shamshir == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/36):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP / 9:
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                    elif CripplingStrikes == 1 or Shamshir == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/24):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP / 6:
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                    else: 
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/16):
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)
                        else: 
                            if math.floor(hp_roll) >= Def_HP / 4:
                                Injury = 1
                                if Flail3Head == 1:
                                    hits_until_1st_injury.append(count/3)
                                else:
                                    hits_until_1st_injury.append(count)

            #Heavy injury check: Heavy injuries are not guaranteed even when conditions are met, so this is only checking for chance of heavy injury.
            if UseHeadShotInjuryFormulaHeavy == 1:
                if HeavyInjuryChance == 0 and Undead != 1 and Savant != 1:
                    if CripplingStrikes == 1 and ShamshirMastery == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/96):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP * (5/24):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        UseHeadShotInjuryFormulaHeavy = 0
                    elif CripplingStrikes == 0 and ShamshirMastery == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/64):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP * (5/16):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        UseHeadShotInjuryFormulaHeavy = 0
                    elif CripplingStrikes == 1 and Shamshir == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/72):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP * (5/18):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        UseHeadShotInjuryFormulaHeavy = 0
                    elif CripplingStrikes == 1 or Shamshir == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/48):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP * (5/12):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        UseHeadShotInjuryFormulaHeavy = 0
                    else: 
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (25/32):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP * (5/8):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        UseHeadShotInjuryFormulaHeavy = 0

            else: #Use body injury formula.
                if HeavyInjuryChance == 0 and Undead != 1 and Savant != 1:
                    if CripplingStrikes == 1 and ShamshirMastery == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/24):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP / 6:
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                    elif CripplingStrikes == 0 and ShamshirMastery == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/16):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP / 4:
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                    elif CripplingStrikes == 1 and Shamshir == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/18):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP * (2/9):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                    elif CripplingStrikes == 1 or Shamshir == 1:
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/12):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP / 3:
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                    else: 
                        if Ironjaw == 1:
                            if math.floor(hp_roll) >= Def_HP * (5/8):
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)
                        else:
                            if math.floor(hp_roll) >= Def_HP / 2:
                                HeavyInjuryChance = 1
                                if Flail3Head == 1:
                                    hits_until_1st_heavy_injury_chance.append(count/3)
                                else:
                                    hits_until_1st_heavy_injury_chance.append(count)                    
            
            #Morale check:
            if FirstMoraleCheck == 0:
                if Fearsome == 1:
                    if math.floor(hp_roll) > 0:
                        FirstMoraleCheck = 1
                        if Flail3Head == 1:
                            hits_until_1st_morale.append(count/3)
                        else:
                            hits_until_1st_morale.append(count)
                else:
                    if math.floor(hp_roll) >= 15:
                        FirstMoraleCheck = 1
                        if Flail3Head == 1:
                            hits_until_1st_morale.append(count/3)
                        else:
                            hits_until_1st_morale.append(count)

            #Fearsome:    
            if Fearsome == 1:
                if Flail3Head != 1:
                    if math.floor(hp_roll) > 0 and math.floor(hp_roll) < 15:
                        FearsomeProcs += 1
                else:
                    if Flail3Head == 1 and count % 3 == 1:
                        if math.floor(hp_roll) > 0 and math.floor(hp_roll) < 15:
                            FearsomeProcs += 1

            #Bleeding check:
            if (CleaverBleed == 1 or CleaverMastery == 1) and Undead != 1:
                #If damage taken >= 6 and Decapitate isn't in play, then apply a 2 turn bleed stack.
                if math.floor(hp_roll) >= 6 and DecapMod == 1 and Decapitate != 1:
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

            #Poison check:
            if Ambusher == 1:
                if Poison == 0:
                    if math.floor(hp_roll) >= 6:
                        Poison = 1
                        hits_until_1st_poison.append(count)

            #If death occurs, check for NineLives and otherwise add the hitcount to the list for later analysis and start the next trial.
            if hp <= 0: 
                if NineLivesMod == 1:
                    hp = random.randint(11,15)
                    NineLivesMod = 0
                    Bleedstack1T = 0
                    Bleedstack2T = 0
                elif Fearsome == 1:
                    if Forge == 1:
                        Forge_bonus_armor.append(ForgeSaved)
                    if Flail3Head == 1:
                        hits_until_death.append(count/3)
                    else:
                        hits_until_death.append(count)
                    NumberFearsomeProcs.append(FearsomeProcs)
                else:
                    if Forge == 1:
                        Forge_bonus_armor.append(ForgeSaved)
                    if Flail3Head == 1:
                        hits_until_death.append(count/3)
                    else:
                        hits_until_death.append(count)

    #Analysis on data collection:
    HitsToDeath = statistics.mean(hits_until_death)
    total += HitsToDeath
    StDev = statistics.stdev(hits_until_death)
    hits_until_death.sort()
    HitsToDeathCounter = collections.Counter(hits_until_death)
    HitsToDeathPercent = [(i,HitsToDeathCounter[i]/len(hits_until_death)*100) for i in HitsToDeathCounter]
    if Undead != 1 and Savant != 1:
        if len(hits_until_1st_injury) != 0:
            hits_to_injure = statistics.mean(hits_until_1st_injury)
            hits_until_1st_injury.sort()
            HitsToInjureCounter = collections.Counter(hits_until_1st_injury)
            HitsToInjurePercent = [(i,HitsToInjureCounter[i]/len(hits_until_death)*100) for i in HitsToInjureCounter]
        if len(hits_until_1st_heavy_injury_chance) != 0:
            hits_to_1st_heavy_injury_chance = statistics.mean(hits_until_1st_heavy_injury_chance)
            hits_until_1st_heavy_injury_chance.sort()
            HitsToHeavyInjuryChanceCounter = collections.Counter(hits_until_1st_heavy_injury_chance)
            HitsToHeavyInjuryChancePercent = [(i,HitsToHeavyInjuryChanceCounter[i]/len(hits_until_death)*100) for i in HitsToHeavyInjuryChanceCounter]
        if len(hits_until_1st_morale) != 0:
            hits_to_morale = statistics.mean(hits_until_1st_morale)
            hits_until_1st_morale.sort()
            HitsToMoraleCounter = collections.Counter(hits_until_1st_morale)
            HitsToMoralePercent = [(i,HitsToMoraleCounter[i]/len(hits_until_death)*100) for i in HitsToMoraleCounter]
        if Fearsome == 1:
            AvgFearsomeProcs = statistics.mean(NumberFearsomeProcs)
    if Forge == 1:
        if len(Forge_bonus_armor) != 0:
            AvgForgeArmor = statistics.mean(Forge_bonus_armor)
    if Ambusher == 1:
        if len(hits_until_1st_poison) != 0:
            hits_to_posion = statistics.mean(hits_until_1st_poison)

    #Results:
    if DeathMean == 1:
        print("Death in " + str(HitsToDeath) + " hits on average.")
    if DeathStDev == 1:
        print("StDev: " + str(StDev))
    if DeathPercent == 1:
        print("% Hits to die: " + str(HitsToDeathPercent))
    if Undead != 1 and Savant != 1:
        if len(hits_until_1st_injury) == 0:
            if InjuryMean == 1 or InjuryPercent == 1:
                print("No chance of injury.")
        else:        
            if InjuryMean == 1:
                print("First injury in " + str(hits_to_injure) + " hits on average.")
            if InjuryPercent == 1:
                print("% First injury in: " + str(HitsToInjurePercent))
        if len(hits_until_1st_heavy_injury_chance) == 0:
            if HeavyInjuryMean == 1 or HeavyInjuryPercent == 1:
                print("No chance of heavy injury.")
        else:
            if HeavyInjuryMean == 1:
                print("Chance of first heavy injury in " + str(hits_to_1st_heavy_injury_chance) + " hits on average.")
            if HeavyInjuryPercent == 1:
                print("% First heavy injury chance in: " + str(HitsToHeavyInjuryChancePercent))
        if len(hits_until_1st_morale) != 0:
            if MoraleMean == 1:
                print("First morale check in " + str(hits_to_morale) + " hits on average.")
            if MoralePercent == 1:
                print("% First morale in: " + str(HitsToMoralePercent))
        if Fearsome == 1:
            print (str(AvgFearsomeProcs) + " Fearsome procs on average.")
    if Forge == 1:
        print(str(AvgForgeArmor) + " bonus armor from Forge on average.")
    if Ambusher == 1:
        print("First poison in " + str(hits_to_posion) + " hits on average.")
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
APreFHGreatAxe = 1
PresetCalc()
print("Fallen Hero - Greataxe:")
calc()
APreFHGreatAxe = 0

Fearsome = 0
SplitMan = 0
APreBerserkChain = 1
PresetCalc()
print("Orc Berserker - Berserk Chain:")
calc()
APreBerserkChain = 0

TwoHander20 = 0
Flail2HPound = 0
FlailMastery = 0
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
APreWingedMace = 1
PresetCalc()
print("Sergeant - Winged Mace:")
calc()
APreWingedMace = 0

Duelist = 0
DoubleGrip = 0
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
Executioner = 0
APrePoleMace = 1
PresetCalc()
print("Conscript - PoleMace:")
calc()
APrePoleMace = 0

APreHandgonne = 1
PresetCalc()
print("Gunner - Handgonne:")
calc()
APreHandgonne = 0

Fearsome = 0
APre2HScimitar = 1
PresetCalc()
print("Officer - 2H Scimitar:")
calc()
APre2HScimitar = 0

CleaverMastery = 0
CripplingStrikes = 0
APreQatal = 1
PresetCalc()
print("Assassin - Qatal:")
calc()
APreQatal = 0

DoubleGrip = 0
Duelist = 0
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

#Will print totals for you if the appropriate switches are turned on at the top of the code. Again, be cautious about blindly trusting these numbers.
if TotalMean == 1:
    TotalMean = total
    print(str(TotalMean) + " hits to die total against this test group.")
if AverageMeanPerTest == 1:
    AverageMeanPerTest = TotalMean / 35
    print(str(AverageMeanPerTest) + " hits to die on average against this test group.")

#CREDITS:
#Author: turtle225
#Contact: turtl225e@gmail.com
#Copyright 2019, turtle225. All rights reserved.
#Special Thanks:
#-- Abel (aka) Villain Joueur: For grabbing the damage formula out of the game code, writing the damage page on the wiki, and for helping me with many questions along the way.
#-- Wall (aka) Wlira: For helping me with some questions along the way and having an existing calculator for me to test against.
#-- You: If you are using the calculator, thank you! If you find any bugs or have feedback/questions/suggestions, you can usually find me on the Steam forums or send me an email.
#-- Overhype: For making an amazing game for us to play.

#History:
#Version 1.0.0 (12/28/2019)
#-- First released on Github.
#Version 1.0.1 (12/29/2019)
#-- Fixed an issue where Nimble above 40% would drop to 40% after the first iteration.
#Version 1.0.2 (1/21/2020)
#-- Changed rounding logic to always round damage down after in game evidence suggested this was the case.
#Version 1.1.0 (2/6/2020)
#-- Added in headshot injury formula logic which is different than body injury logic.
#-- Added sorting to the return of %chance of death by hit so that it ascends from low to high instead of coming out randomly.
#-- Added in ability to return %chance of injury and morale by hit. 
#-- Added a tracker that checks for the first chance of receiving a heavy injury. 
#-- Added options to adjust the verbosity of the data returned to allow the user to easily choose what gets output.
#Version 1.1.1 (2/19/2020)
#-- Reworked Destroy Armor logic to make the results it provides more useful to the user.
#-- Destroy Armor will now be used once or twice and then switch to normal attacks, rather then checking armor levels like it used to.
#Version 1.1.2 (3/16/2020)
#-- Fixed an error in order of calculations for Goblin Overseer which incorrectly had his Ignore% at 75% instead of the correct 77% (Thanks Abel).
#-- Fixed an error with AimedShot where it provided bonus damage against hp and armor when it should only boost against hp (Thanks Abel).
#-- Added logic for Indomitable halving Bleed damage whereas before it wasn't doing so.
#-- Added option for Puncture tests.
#-- Added option for ranged shots that scatter into unintended targets.
#Version 1.1.4 (4/15/2020)
#-- Added logic to return the average amount of armor gained when using Forge.
#-- Added logic to return time of first poisoning against Ambushers.
#-- Added option to give 2HFlails their +10% Ignore on single target attacks (thank you Andre27 for pointing this out).
#-- Added option to give 2HSwords their +5% Ignore on their Split attack (thank you Andre27 for pointing this out).
#-- Added Flail2HIgnore to the Orc Berserker preset.
#-- Added data output option to show output of the total hits to die against the entire enemy group.
#-- Added data output option to show output of the average hits to die against the entire enemy group.
#Version 1.5.0 (8/13/2020)
#-- Updated calculator with Blazing Deserts changes, see below for details.
#-- Reworked HeadHunter for Blazing Deserts change.
#-- Also removed HH option to not count stacks between kills as it doesn't make sense to calculate that way.
#-- Adjusted Nine Lives to clear existing Bleed stacks when it procs.
#-- Added ShamshirMastery to account for new logic with Sword Mastery.
#-- Adjusted injury logic to account for new Shamshir Mastery.
#-- Added The Bear's unique perk - Glorious Endurance.
#-- Changed Dazed to -25% damage instead of -35% damage.
#-- Changed Mushrooms to +25% damage global instead of its previous effect.
#-- Added Distracted effect that is applied by Nomads.
#-- Changed Ambusher ignore modifier to 1.25 (down from 1.4).
#-- Changed Ambusher presets to use a 30-50 Boondock Bow (up from 25-40).
#-- Removed AmbusherDay200 entry.
#-- Added Qatal special - Deathblow.
#-- Changed Fallen Hero preset to use a Greataxe instead of Winged Mace to demonstrate their most threatening loadout.
#-- Changed Sergeant preset to use a Winged Mace instead of Warhammer to make him more neutral to his loadout options.
#-- Added 4 new attacker presets and 4 new defender presets.
#-- Changed Billhook preset as per Billhook nerf.
#-- Added 4 more enemies to the test group.
#Version 1.5.1 (9/4/2020)
#-- Updated Conscript preset as per nerf to 55 HP.
#Version 1.5.2 (9/28/2020)
#-- Added Ironjaw option and logic.
#Version 1.5.3 (11/5/2020)
#-- Fixed inaccuracies with the Crypt Cleaver preset where I hadn't realized it had gotten nerfed in Blazing Deserts.
#Version 1.5.4 (1/14/2021)
#-- Fixed a mistake introduced in version 1.5 when I added 4 enemies to the test group. I had left the mean division at 31 enemies instead of changing to 35, which was inflating the mean hits to die score.
#Version 1.5.5 (1/30/2021)
#-- Changed attachments to automatically apply +Armor and -Fatigue, as per recent attachment changes.
#-- Added Wolf/Hyena, Lindwurm, and Serpent attachments as additional options.
#-- Changed Nimble with Bone Plate defender preset to use Padded Leather (80) so that it can still be at -15 after Bone Plate nerf.
#Version 1.6 (7/17/2021)
#-- Updated Lindwurms to have 35% armor ignore after they were "nerfed" from 40% after a game bug was fixed (where they had been doing 0% prior).
#Version 1.6.1 (3/10/2022) - Of Flesh and Faith DLC release.
#-- Added new 2HFlail logic as per the change where Pound does +10% ignore on headshots (and +20% with Flail Mastery)
#-- Changed Flail2HIgnore swtich to Flail2HPound and also added FlailMastery switch.
#-- Changed Nine Lives to retrun 11-15 hp, up from 5-10.
#-- Changed Handgonne attacker preset to have 90% armor damage, down from 100%.
#-- Changed R2Throw (two range Throwing) switch to deal +30% damage, down from +40%.
#-- Added +5% armor ignore to Aimed Shot (this is not a new game change, just something I never realized before).
#Version 1.6.2 (3/14/2022)
#-- Adjusted Orc Berserker preset for new buff to Berserk Chain to 50-100, up from 40-100.
#Version 1.6.3 (4/11/2022)
#-- Fixed a bug with Forge + Split Man interaction where having low armor with Forge was giving much better survivability than it should have been against Split man.