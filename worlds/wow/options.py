"""
Option definitions for World of Warcraft
"""
from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, PerGameCommonOptions)

class WoWRace(Choice):
    display_name = "Character Race"
    default = 0
    option_human = 0
    option_dwarf = 1
    option_gnome = 2
    option_night_elf = 3
    option_draenei = 4
    option_orc = 5
    option_troll = 6
    option_tauren = 7
    option_forsaken = 8
    option_blood_elf = 9
    #option_random = 10

class WoWClass(Choice):
    display_name = "Character Class"
    default = 0
    option_warrior = 0
    option_death_knight = 1
    option_paladin = 2
    option_hunter = 3
    option_shaman = 4
    option_rogue = 5
    option_druid = 6
    option_priest = 7
    option_warlock = 8
    option_mage = 9
    #option_random = 10

class StartingZone(Choice):
    """
    Determines which zone you start in. Currently unsupported.

    - Normal = The zone assigned to your race
    - Elwynn Forest = Default Human starting zone
    - Dun Morogh = Default Dwarf and Gnome starting zone
    - Teldrassil = Default Night Elf starting zone
    - Azuremyst Isle = Default Draenei starting zone
    - Durotar = Default Orc and Troll starting zone
    - Mulgore = Default Tauren starting zone
    - Tirisfal Glades = Default Forsaken starting zone
    - Eversong Woods = Default Blood Elf starting zone
    - Random = Any starting zone
    """
    display_name = "Starting Zone"
    default = 0
    option_normal = 0
    option_elwynn_forest = 1
    option_dun_morogh = 2
    option_teldrassil = 3
    option_azuremyst_isle = 4
    option_durotar = 5
    option_mulgore = 6
    option_tirisfal_glades = 7
    option_eversong_woods = 8
    #option_random = 9

class RandomizeSpells(Toggle):
    """
    Choose to either shuffle spells into the pool (default), or randomize which spells you can get from your entire class list
    """
    display_name = "Shuffle/Randomize Spells"

class Goal(Choice):
    """
    Choose what the goal of the game is.
    For now, choose which level to end at.
    """
    display_name = "Goal"
    default = 0
    option_level_10 = 0
    option_level_20 = 1
    option_level_30 = 2
    option_level_40 = 3
    option_level_50 = 4
    option_level_60 = 5
    option_level_70 = 6
    option_level_80 = 7

class ExpBoost(Range):
    """
    Multiplies gained experience.

    1 is default
    2 is double
    10 is the max
    """
    display_name = "Exp Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class StartingHeirlooms(OptionSet):
    """
    Players can choose a few heirlooms they would like to start with.
    """
    display_name = "Starting Heirlooms"
    valid_keys = ["Tattered Dreadmist Robe","Tattered Dreadmist Mantle","Stained Shadowcraft Tunic","Preened Ironfeather Breastplate","Stained Shadowcraft Spaulders",
        "Preened Ironfeather Shoulders","Champion's Deathdealer Breastplate","Mystical Vest of Elements","Champion Herod's Shoulder","Mystical Pauldrons of Elements",
        "Polished Breastplate of Valor","Polished Spaulders of Valor","Exquisite Sunderseer Mantle","Lasting Feralheart Spaulders","Exceptional Stormshroud Shoulders",
        "Prized Beastmaster's Mantle","Aged Pauldrons of The Five Thunders","Pristine Lightforge Spaulders","Strengthened Stockade Pauldrons",

        "Balanced Heartseeker","Venerable Dal'Rend's Sacred Charge","Venerable Mass of McGowan","Devout Aurastone Hammer","Charmed Ancient Bone Bow",
        "Bloodied Arcanite Reaper","Repurposed Lava Dredger","Dignified Headmaster's Charge","Battleworn Thrash Blade","Grand Staff of Jordan","Reforged Truesilver Champion",
        "Sharpened Scarlet Kris","The Blessed Hammer of Grace","Upgraded Dwarven Hand Cannon",

        "Swift Hand of Justice","Discerning Eye of the Beast","Dread Pirate Ring","Inherited Insignia of the Alliance","Inherited Insignia of the Horde"]

class Traps(Toggle):
    """
    Choose if traps should be enabled.
    Traps are random debuffs.
    """
    display_name = "Enable Traps"

class WoWDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__

class PrimaryProfessions(OptionSet):
    """
    Adds quests that require the player to have specific professions in order to accept and complete.
    It is highly recommended to choose a maximum of two per character.
    Server owners can let players learn more than two primary professions in the config.
    """
    display_name = "Primary Professions"
    valid_keys = ["Skinning", "Herbalism", "Mining", "Leatherworking", "Alchemy", "Inscription", "Blacksmithing", "Jewelcrafting", "Tailoring", "Enchanting"]

class Fishing(Toggle):
    """
    Adds quests that require the player to have trained fishing.
    """
    display_name = "Enable Fishing Quests"

class FirstAid(DefaultOnToggle):
    """
    Adds quests that require the player to have trained first aid.
    """
    display_name = "Enable First Aid Quests"

class Cooking(DefaultOnToggle):
    """
    Adds quests that require the player to have trained cooking.
    """
    display_name = "Enable Cooking Quests"


@dataclass
class WorldOfWarcraftOptions(PerGameCommonOptions):
    wow_race: WoWRace
    wow_class: WoWClass
    randomize_spells: RandomizeSpells
    starting_zone: StartingZone
    goal: Goal
    exp_boost: ExpBoost
    starting_heirlooms: StartingHeirlooms
    traps: Traps
    death_link: WoWDeathLink
    primary_professions: PrimaryProfessions
    fishing: Fishing
    first_aid: FirstAid
    cooking: Cooking
