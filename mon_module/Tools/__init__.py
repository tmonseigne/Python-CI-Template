"""
Ce sous-package contient des outils utilitaires pour le projet SampleMaker.

**Modules disponibles** :

- Drawing : Fournit des fonctions de dessin génériques.
- Monitoring : Fournit un module de surveillance des ressources système pendant l'exécution de tests.
- Utils : Fournit des fonctions d'assistance génériques.

**Fonctionnalités principales** :

- Tous les modules peuvent être importés directement via `from mon_module.Tools import <module>`.

"""

# Exemple d'importation des modules pour un accès direct
from .Drawing import draw_test_section, get_color_map_by_name
from .Monitoring import Monitoring
from .Utils import add_extension, add_suffix, get_timestamp_for_files, print_error, print_warning

# Définir la liste des symboles exportés
__all__ = ["Drawing", "Monitoring", "Utils",
		   "draw_test_section", "get_color_map_by_name",
		   "add_extension", "add_suffix", "get_timestamp_for_files", "print_error", "print_warning"]
