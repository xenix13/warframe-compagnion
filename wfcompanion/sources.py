"""Liste des sources de données (toutes publiques)."""

ITEMS = "https://raw.githubusercontent.com/WFCD/warframe-items/master/data/json/"
DROPS = "https://raw.githubusercontent.com/WFCD/warframe-drop-data/gh-pages/data/"

# nom local -> URL
SOURCES = {
    # données du jeu (warframe-items, WFCD)
    "Mods.json": ITEMS + "Mods.json",
    "Arcanes.json": ITEMS + "Arcanes.json",
    "Warframes.json": ITEMS + "Warframes.json",
    "Primary.json": ITEMS + "Primary.json",
    "Secondary.json": ITEMS + "Secondary.json",
    "Melee.json": ITEMS + "Melee.json",
    "Resources.json": ITEMS + "Resources.json",
    "Misc.json": ITEMS + "Misc.json",
    "Sentinels.json": ITEMS + "Sentinels.json",
    "Pets.json": ITEMS + "Pets.json",
    # tables de drop officielles (warframe-drop-data, WFCD)
    "drops_info.json": DROPS + "info.json",
    "drops_all.slim.json": DROPS + "all.slim.json",
    "drops_resourceByAvatar.json": DROPS + "resourceByAvatar.json",
}

WIKI_API = "https://wiki.warframe.com/api.php"
