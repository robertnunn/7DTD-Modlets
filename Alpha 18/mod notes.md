# FIND A WAY TO QUERY GIT FOR WHAT FILES HAVE BEEN CHANGED.
**write a script to compile a list of all the folders that have been changed and only update those zip files, instead of everything.**

## vehicle mods:
- aluminum gyro frame: two versions, one that increases speed and km/L, one that adds inventory space
- fuel efficiency mods for vehicles: increase km/L, decrease turbo speed

## extra item mods: (bold means done)
- **improved insulation mods**: adds 7, 10 cold/heat resist instead of 5. costs 2x,3x as much in materials
- **military plating mod**: bring back the A17 version, adds +3 to armor, crafted like other plating mods but uses military fiber
- **backpack frame**: only installs on chest armor, adds 4-6 inv slots (assuming pack mule isn't maxed)
- **long-fall boots**: like from portal, negates all fall damage
- **still suit**: only installs on chests armor, reduces water consumption rate (just like in Dune)
- animal detector(?): only installs in helmets, show animals on compass like the huntsman perk but doesn't require sneaking. Longer range than perk?
- zombie detector(?!): only installs in helmets, shows zombies instead of animals? can you even do this?
- diamond edge: installs in melee tools/weapons, adds a bunch of block damage and entity damage
- obsidian edge: installs in melee tools/weapons, adds block/entity damage, but greatly reduces durability (obsidian is sharp as fuck, but fragile as shit)

## update UI mod with:
elevation (helpful for flying, especially in fog/rain/snow)
body temp/outside temp

## Adventure mods
- **scenario**: the players are soldiers/PMCs whose heli/plane crashed on the wasteland island they were supposed to extract a HVT from. Random quality from starting bundle items represents damage sustained to (or lack of funds to purchase) high-quality tools/weapons. 
    - one spawn point or multiple spawns? Would represent different teams that might want to meet up for safety or help finishing the mission/escaping
    - spawn in a room? would fit with a crash scenario where the team was unconscious for a some time (hours? a day?)
- **quest line**: players awaken from the crash, open their bags, allocate skill points, begin searching for the mcguffins
    - players seek out radio equipment (random location could represent other teams that got eaten by zambies) to radio for extraction, get told to find their objective then they'll be extracted (not enough time to regroup and try again)
        - players likely tell command that everyone is dead or zombified, so their HVT is likely dead. Command says that they were hoping for the HVT, but acquiring the data archive he had will suffice.
    - players find out early on that a horde of zombies is coming (this is the time limit for players to escape) in roughly X days (i.e., non-zero BloodMoonRange in serverconfig.xml, but players can hear them coming from a ways off, and since they move so slowly they are alerted at ~10am-noon) and it's impressed upon them that this is nothing to fuck with (behemoths?)
        - players find this out from a helpful drone operator who isn't exactly supposed to tell them this, so this heads-up is all they get.
    - players go find mcguffin #1, then head back to the radio, get the coords for the extraction point
        - evac is swarming with zombies, and must be cleared
        - should evac be a random location (RandomGoto) or a POI with a helipad/landing strip? (Goto) Find a crashed plane POI and recover a black box?
    - upon arriving at the evac point, players find a crashed aircraft, what was supposed to be their escape. black box data indicates that some unknown weapon brought down the aircraft. players have to head to a larger military base (an actual installation) to read the data they got from their HVT
    - arriving at the base, players have to fight their way to a working terminal (deep inside the base)
        - have to upgrade a specific type of block in the facility (this represents fixing the radio or the computer)
        - before entering the facility proper, players encounter hostile mercs trying to loot the place. Another hire? Hoping to ransom the data/material?
    - after deciphering the data, players find the location of the two experimental weapons that brought down their aircraft. 
    - while investigating the first site, players find evidence of an illegal bioweapons lab run by the same corp that developed the weapons that brought them down.
        - use the resident evil mansion POI
- **changes from vanilla**:
    - no skill points on leveling up, you get all your skill points right at the beginning from the intro quest
    - how many skill points to get? 100? 75? 150?
        - 80 points to max every attribute (16pts/att)
            - 1,1,1,1,2,2,2,3,3 : 2-10
        - 45 skills (all but one have 5 levels)
        - parkour 5 requires 21 points
        - pack mule 5 requires 10 points
    - more likely to find working vehicle parts? makes it easier to get a vehicle and get moving. Alternatively, give the GROUP one 4x4 (with extra seats)
    - more zombies spawning in cities than usual
    - zombies are much tougher at night (they also sprint)
    - can't put silencers on shotguns anymore
    - dramatically increase the heat generated from workstations, more modest increase in heat from firearms (specifically firearms (and explosives), not (cross)bows or melee)
    - add these:
        - beaker recipe, better silencers, better starting inventory (entrenching tool), copy schematics, extra item mods, fatal headshots, free relays, money stacks, no boiled water dysentery, repair wrench, two extra 4x4 seats, vehicles enhanced? (maybe a lesser version?), weapon damamge 2x
    - remove these: (usually easier to remove them from loot tables than delete them outright)
        - living off the land, you're not there or in one place long enough to plant crops and harvest them
        - healing factor, you're not fucking wolverine
        - daring adventurer, no traders so no quests so no rewards to choose
        - gyrocopter, makes it too easy (loot, recipes)
        - normal intro quest line
        - better barter, no traders, don't want players to waste their points
        - quest notes, challenges, treasure maps, etc (loot)
        - ability to craft workstations? Would force the group to find working versions of them.    
        - normal animals, shit's fucked and so are the aminals (spawning)
- **quest technical details**:
    - \<reward type="Quest" id=""/> this is how you setup a quest chain
    - offer_key is the popup you get at the beginning of a quest
    - is there a way to specify spawn distance for quests?
    - "Goto" objective type uses the id="" as a filter to find the closest POI with a name that matches it
        - is there a way to specify a minimum distance to search in?