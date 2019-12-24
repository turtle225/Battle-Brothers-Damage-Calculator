#Battle Brothers Damage Calculator:
#Welcome. Modify the below values as necessary until you reach the line ----- break.
#The calculator expects you to make smart decisions, such as not giving Xbow Mastery to a Hammer. 
#Don't give yourself infinite loops by doing silly things like running with 0 damage. 
#Written in Python 3.7, earlier versions of Python 3 should work, but Python 2 will not.

#Attacker Stats: #Example is Ancient Bladed Pike, follow that formatting.
Mind = 55        #Mind = 55
Maxd = 80        #Maxd = 80
Headchance = 30  #Headchance = 30
Ignore = 30      #Ignore = 30
ArmorMod = 125   #ArmorMod = 125

#Defender Stats:
Def_HP = 100
Def_Helmet = 120  
Def_Armor = 95   
Fatigue = -15    #Fatigue value only effects Nimble.

Trials = 100000 #Number of trials to run through. More trials leads to more accurate results but longer compute times.

#DEFENDER FLAGS: Set these values to 1 if they apply and 0 otherwise.
#Perks:
NineLives = 0
Resilient = 0           #Reduces Bleeding duration.
SteelBrow = 0
Nimble = 0 
Forge = 0
Indomitable = 0
#Attachments: Note: Only 1 attachment should be selected.
AdFurPad = 0            #Additional Fur Padding.
Boneplate = 0           
HornPlate = 0           #Only select against melee attacks.
UnholdFurCloak = 0      #Only select against range attacks.
#Light Padding Replacement -- Modify the Fatigue value directly if you wish to apply this. Has no effect except for Nimble.

#ATTACKER FLAGS: Set these values to 1 if they apply and 0 otherwise.
#Weapons:
DoubleGrip = 0          #Only 1Handers are valid for DoubleGrip. Dagger Puncture tests should not be given DoubleGrip.
TwoHander20 = 0         #Damage +20. Applies to the single target 2Hander attacks Cudgel (Mace), Pound (Flail), Smite (Hammer), Overhead Strike (Long/GreatSword).
FlailLash = 0           #Gaurantees headshot. Also apply to 3Head Hail special.
Flail3Head = 0          #3Head Flail.
Hammer10 = 0            #Guarantees at least 10 hp damage, applies to 1H Hammer and Polehammer.
DestroyArmor = 0        #Will use Destroy Armor instead of regular attack if opponent's body armor is greater than 150% of expected max armor damage.
DestroyArmorMastery = 0 #Hammer Mastery. Will use Destroy Armor instead of regular attack if opponent's body armor is greater than 150% of expected max armor damage.
Axe1H = 0               #Applies bonus damage to Headshots. Gets negated by Steelbrow.
SplitMan = 0            #Applies to single target 2HAxe except for Longaxe.
AoE2HAxe = 0            #Applies to Round Swing and Split in Two (Bardiche), reduces Ignore by 10%.
CleaverBleed = 0        #5 bleed damage per bleed tick, don't enable against Undead.
CleaverMastery = 0      #10 bleed damage per bleed tick, don't enable against Undead. Used by Honor Guards, Conqueror, Necrosavants, 
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
Duelist = 0             #All Duelists should also be given DoubleGrip except for Throwing weapons.
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

#RACE FLAGS (ATTACKER): Set these values to 1 if they apply and 0 otherwise. If late game only set the second option.
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
Ambusher = 0            #Ignore * 1.4
AmbusherDay200 = 0      #Ignore * 1.5
Skirmisher = 0          #Ignore * 1.25
Overseer = 0            #Ignore * 1.1
Wolfrider = 0           #Ignore * 1.25
MasterArcher = 0        #Ignore * 1.25
FrenziedDirewolf = 0    #Damage +20%.
UnholdDay90 = 0         #Damage +10%.
LindwurmDay170 = 0      #Damage +10%.

#RACE FLAGS (DEFENDER): Set these values to 1 if they apply and 0 otherwise. (I put this down here out of the way since it is niche).
Undead = 0              #Immunity to Injury, Bleeding, and Morale.
Savant = 0              #Immunity to Injury and Morale.
SkeletonVsPierce = 0    #50% health damage reduction for Ancient Dead and Alps vs. Daggers, Spears, and Pikes.
SkeletonVsJavelin = 0   #75% health damage reduction for Ancient Dead and Alps vs. Javelins. 
SkeletonVsArrow = 0     #90% health damage reduction for Anciend Dead and Alps vs. Arrows.
PossessedUndead = 0     #25% damage reduction. Necromancer buff.
FallenBetrayerD = 0     #25% armor damage reduction for Watermill Betrayers.

# ------------------------------------------------------------------------
#IMPORTANT --- ALL BELOW FIELDS SHOULD NOT BE MODIFIED. --- IMPORTANT
#DO NOT MODIFY BELOW FIELDS UNLESS YOU KNOW WHAT YOU ARE DOING.

#Dependencies:
import random
import statistics
import collections
import math

#Base damage modifiers:
if TwoHander20 == 1:
    Mind += 20
    Maxd += 20
Mind = abs(Mind)
Maxd = abs(Maxd)

#Headchance modifiers:
if Juggler == 1:
    Headchance += 5
if KillerOnTheRun == 1:
    Headchance += 10
if FlailLash == 1:
    Headchance = 100
Headshotchance = Headchance

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

#Armor damage modifiers:
ArmorMod = ArmorMod/100

#Nimble calculation:
if Fatigue > 0 and Nimble == 1:
    Fatigue *= -1
Fatigue = min(0, Fatigue + 15)
if Nimble == 1:
    NimbleMod = 1.0 - 0.6 + pow(abs(Fatigue),1.23)*.01
    NimbleMod = min(1,NimbleMod)
else:
    NimbleMod = 1

#Headshot damage modifiers:
HeadMod = 1.5
if SteelBrow == 1:
    HeadMod = 1
else:
    if Brute == 1:
        HeadMod += .15
    if Axe1H == 1:
        HeadMod += .5

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
if FrenziedDirewolf == 1:
    DamageMod *= 1.2
if UnholdDay90 == 1:
    DamageMod *= 1.1
if LindwurmDay170 == 1:
    DamageMod *= 1.1

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

print("-----") #Added for readability. If this annoys you then remove this line.
print("HP = " + str(Def_HP) + ", Helmet = " + str(Def_Helmet) + ", Armor = " + str(Def_Armor))
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
                #IF the helmet did get destoryed by the attack, do the following.
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
                    hits_until_1st_injury.append(count)
            elif CripplingStrikes ==1 or Shamshir == 1:
                if math.floor(hp_roll + .4999) >= Def_HP / 6:
                    Injury = 1
                    hits_until_1st_injury.append(count)
            else: 
                if math.floor(hp_roll + .4999) >= Def_HP / 4:
                    Injury = 1
                    hits_until_1st_injury.append(count)
        
        #Morale check:
        if MoraleCheck == 0:
            if Fearsome == 1:
                if math.floor(hp_roll + .4999) > 0:
                    MoraleCheck = 1
                    hits_until_1st_morale.append(count)
            else:
                if math.floor(hp_roll + .4999) >= 15:
                    MoraleCheck = 1
                    hits_until_1st_morale.append(count)

        #Fearsome:    
        if Fearsome == 1:
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
                hits_until_death.append(count)
                NumberFearsomeProcs.append(FearsomeProcs)
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

#CREDITS:
#Author: turtle225
#Special Thanks:
#-- Abel (aka) Villain Joueur: For grabbing the damage formula out of the game code, writing the damage page on the wiki, and for helping me with many questions along the way.
#-- Wall (aka) Wlira: For helping me with some questions along the way and having an existing calculator for me to test against.
#-- You: If you are using the calculator, thank you! If you find any bugs or have feedback/suggestions, I am most reachable on the Steam forums.

#History:
#Version 1.0.0 (12/24/2019)
#-- First released on Github.