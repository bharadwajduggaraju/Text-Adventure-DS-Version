from fighting.effects import Effect
from fighting.moveList import Move
from entities.character import Character
from entities.enemies import Enemy

#Effect format:
#exampleEffect = Effect(name, damage, duration, wounds, op_phys, op_ment, op_delay)
fire = Effect("Burning", 3, 3, True)
electro = Effect("Electrocuted", 10, 1, True)
intox = Effect("Intoxicated", 0, 30, False, 0, 1)
weak = Effect("Weakened", 0, 30, False, 1)
rally = Effect("Rallying", 0, 5, False, -1, -1)
flinch = Effect("Flinching", 0, 1, False, 1)
effects = { #May or may not be helpful, depending on use.
  "Fire": fire,
  "Electrocution": electro,
  "Intoxication": intox,
  "Weakness": weak,
  "Flinching": flinch,
  "Rally": rally
}
#Rally = [rally] #Was included, probably unnecessary

#Format of making a new move
#exampleMove = Move(name, damageTrait, damageMult, critChanceTrait, critChanceMult, failChanceTrait, failChanceMult, comboTimeTrait, comboMult, accuracyTrait, accuracyMult, effects, effectLevelTrait, effectMult, charactersHitTrait, hitMult, op_TargetType)
damage = Move("Damaging Spell", "MagicalAffinity", 2, "MagicalControl", 2, "MagicalControl", 1, "PhysicalGrace", 0, "MagicalConcentration", 2, effects, "MagicalAffinity", 1, "MagicalAffinity", 0)
element = Move("Elemental Spell", "MagicalAffinity", 1, "MagicalControl", 1, "MagicalControl", 1, "PhysicalGrace", 0, "MagicalConcentration", 1, effects, "MagicalAffinity", 3, "MagicalAffinity", 0)
area = Move("Area Spell", "MagicalAffinity", 1, "MagicalControl", 2, "MagicalControl", 1, "PhysicalGrace", 0, "MagicalConcentration", 1, effects, "MagicalAffinity", 1, "MagicalAffinity", 0)
heal = Move("Healing Spell", "MagicalAffinity", -2, "MagicalControl", 0, "MagicalControl", 1, "PhysicalGrace", 0, "MagicalConcentration", 3, effects, "MagicalAffinity", 0, "MagicalAffinity", 0, 1)
rally = Move("Rallying Cry", "MagicalAffinity", 0, "MagicalControl", 0, "MagicalControl", 0, "PhysicalGrace", 0, "SocialPresence", 4, [rally], "SocialHeart", 1, "SocialHeart", 1)
attack = Move("Physical Attack", "PhysicalSkill", 1, "PhysicalSkill", 1, "MagicalControl", 0, "PhysicalGrace", 2, "PhysicalGrace", 2, effects, "SocialHeart", 0, "PhysicalGrace", 0)
spells = {
  "Damage": damage,
  "Element": element,
  "Area": area,
  "Heal": heal,
  "Rally": rally,
  "Attack": attack,
}

#Example = Character(name, HP, MaxHP, SP, MaxSP, MP, MaxMP, SPresence, SHeart, SStability, PGrace, PSkill, PPoise, MAffinity, MControl, MConcentration, InventoryList, TraumaList, EffectsList, TagsList, Move, Move2, Move3, op_maxDeaths, op_deaths)
Esteri = Character("Esteri", 11, 11, 16, 16, 3, 3, 3, 3, 1, 5, 4, 3, 0, 0, 1, [], [], [], [], attack, rally, area)
Cressida = Character("Cressida", 9, 9, 6, 6, 15, 15, 4, 3, 3, 0, 1, 3, 2, 3, 3, [], [], [], [], heal, damage, rally)
Kosu = Character("Kosu", 14, 14, 13, 13, 3, 3, 4, 5, 3, 3, 4, 1, 0, 0, 0, [], [], [], [], attack, rally, element)
Ai = Character("Ai", 11, 11, 5, 5, 14, 14, 1, 4, 0, 0, 1, 0, 4, 5, 5, [], ['grief'], [], [], damage, element, area)
#We had determined that Ai starts with grief
Amaliyah = Character("Amaliyah", 11, 11, 16, 16, 3, 3, 3, 3, 1, 5, 4, 3, 4, 0, 1, [], [], [], [], attack, element, heal)
characters = {
  "Esteri": Esteri,
  "Cressida": Cressida,
  "Kosugade": Kosu,
  "Ai": Ai,
  "Amaliyah": Amaliyah,
}

#Example = Enemy(name, maxHP, HP, TimeGiven, AC, damage, op_effects)
Joke = Enemy("The Joker", 1, 1, 0, 100, 0)
#T1 Kirin
InexperiencedKirin = Enemy("Inexperienced Kirin", 10, 10, 10, 3, 1)
#T2 Kirin
NormalKirin = Enemy("Kirin", 30, 30, 10, 3, 3)
#T3 Kirin
VeteranKirin = Enemy("Veteran Kirin", 50, 50, 10, 10, 3)
#Special Kirin
BossKirin = Enemy("The Boss Kirin", 100, 100, 10, 10, 3)
#T1 Bandits
Bandit = Enemy("Bandit", 10, 10, 10, 10, 2)
BanditThug = Enemy("Bandit Thug", 15, 15, 10, 13, 1)
BanditRuffian = Enemy("Bandit Ruffian", 7, 7, 10, 8, 5)
#T2 Bandits
BanditFugitive = Enemy("Bandit Fugitive", 20, 20, 7, 13, 4)
BanditBruiser = Enemy("Bandit Bruiser", 30, 30, 7, 16, 2)
BanditHitman = Enemy("Bandit Hitman", 15, 15, 7, 9, 10)
#T3 Bandits
BanditElite = Enemy("Bandit Elite", 40, 40, 4, 15, 8)
BanditStalwart = Enemy("Bandit Stalwart", 65, 65, 4, 18, 4)
BanditAssassin = Enemy("Bandit Assassin", 15, 15, 4, 12, 20)
#Cave Monsters
Dronae = Enemy("Dronae", 20, 20, 10, 3, 2)
#Pixies
DarkPixie = Enemy("Dark Pixie", 15, 15, 5, 3, 3)
enemies = {
  "joke": Joke,
  "baby kirin": InexperiencedKirin,
  "teen kirin": NormalKirin,
  "kirin": NormalKirin,
  "boss kirin": BossKirin,
  "bandit": Bandit,
  "bandit thug": BanditThug,
  "bandit ruffian": BanditRuffian,
  "bandit fugitive": BanditFugitive,
  "bandit bruiser": BanditBruiser,
  "bandit hitman": BanditHitman,
  "bandit elite": BanditElite,
  "bandit stalwart": BanditStalwart,
  "bandit assassin": BanditAssassin,
}
