# Adventure mod
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
    - upon arriving at the evac point, players find a crashed aircraft, what was supposed to be their escape. Flight recorder data is not readable by the tools they have, but they can play back the cockpit voice recording and this indicates that some unknown weapon brought down the aircraft. players have to head to a larger military base (an actual installation) to read the data they got from the FDR
    - arriving at the base, players have to fight their way to a working terminal (deep inside the base)
        - have to upgrade a specific type of block in the facility (this represents fixing the radio or the computer)
        - before entering the facility proper, players encounter hostile mercs trying to loot the place. Another hire? Hoping to ransom the data/material?
    - after deciphering the data, players find the location of the two experimental weapons that brought down their aircraft. 
    - while investigating the first site, players find evidence of an illegal bioweapons lab run by the same corp that developed the weapons that brought them down.
        - use the resident evil mansion POI
- **quest list**

    0. Players wake up, tell players they have received all their skill points up front and that they should spend them. They check their maps and realize that they'll need some wheels if they want to get this done in a reasonable period of time.
        - fetchkeep for the entrenching tool or something else guaranteed to be in the starting inventory
        - goto garage/mechanic POI
        - fetchkeep vehicle (4x4 or motorcycle)
    1. Players start looking for working radio equipment (theirs was lost in the crash)
        - goto cell tower poi
        - blockupgrade the control panel blocks to something else to indicate repairing the radio (needs 5 electrical parts)
    1. Command tells them that because their target is almost certainly dead, they still need to retrieve the scientific data he had as there is an unspecified time limit. Drone operator feeds them a warning about a HUGE horde of zombies and tells them that while they can stay ahead of it if they keep moving, eventually it WILL catch up with them
        - goto military base (decide which kind)
        - rally point
        - fetchfromcontainer "Nuclear Test Data"
    1. Data in hand, players head back to a radio to confirm they have the data and receive the extraction coordinates
        - goto cell tower poi
        - blockupgrade the control panel (repairing it with 5 electrical parts)
        - goto crashed plane or airport poi
    1. Finding their evac crashed, 
- **changes from vanilla**:
    + no skill points on leveling up, you get all your skill points right at the beginning from the intro quest
    + how many skill points to get? 100? 75? 150?
        - 80 points to max every attribute (16pts/att)
            - 1,1,1,1,2,2,2,3,3 : 2-10
        - 45 skills (all but one have 5 levels)
        - parkour 5 requires 21 points
        - pack mule 5 requires 10 points
    - more likely to find working vehicle parts? makes it easier to get a vehicle and get moving. Alternatively, give the GROUP one 4x4 (with extra seats)
        + reduce the storage on 4x4 and motorcycle: (9,4) and (9,2[1?])
    - more zombies spawning in cities than usual
    + zombies sprint at night (serverconfig.xml setting)
    + can't put silencers on shotguns anymore
    + dramatically increase the heat generated from workstations, more modest increase in heat from firearms (specifically firearms (and explosives), not (cross)bows or melee)
    + add these:
        - beaker recipe, better starting inventory (entrenching tool), copy schematics, extra item mods, fatal headshots, free relays, only zombie spawns, no boiled water dysentery, pickupable workstations, repair wrench, two extra 4x4 seats, vehicles enhanced(modest), weapon damamge 2x
    + remove these: (usually easier to remove them from loot tables than delete them outright)
        + living off the land, you're not there or in one place long enough to plant crops and harvest them
        + healing factor, you're not fucking wolverine
        + daring adventurer, no traders so no quests so no rewards to choose
        + animal tracker, no animals to track
        + better barter, no traders, don't want players to waste their points
        + gyrocopter, makes it too easy (loot, recipes)
        + normal intro quest line
        + quest notes, challenges, treasure maps, etc (loot)    
        + normal animals, shit's fucked and so are the aminals (spawning)
- **quest technical details**:
    - \<reward type="Quest" id=""/> this is how you setup a quest chain
    - offer_key is the popup you get at the beginning of a quest
    - is there a way to specify spawn distance for quests?
    - "Goto" objective type uses the id="" as a filter to find the closest POI with a name that matches it
        - is there a way to specify a minimum distance to search in?