"""Modules : ce qui est propre à une frame (puis plus tard aux armes et compagnons).

Un module est un fichier Python modules/warframes/<frame en minuscules>.py, avec des constantes facultatives :
CAPACITES, AJOUTS (étiquettes ajoutées aux étiquettes automatiques), PASSIF, AUGMENTS, CENTRALE, BOUCLES, NE_PAS_REMPLACER, ARME_EXALTEE, DEFENSE, PIEGES.
Une frame sans module marche quand même : le moteur tire ses étiquettes des pages du wiki.
"""
import importlib, re


def warframe(name):
    base = re.sub(r"\s+(Prime|Umbra)$", "", name or "").strip()
    mod = re.sub(r"[^a-z0-9]+", "_", base.lower()).strip("_")
    try:
        return importlib.import_module(f"{__name__}.warframes.{mod}")
    except ModuleNotFoundError:
        return None
