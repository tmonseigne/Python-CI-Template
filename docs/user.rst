Guide de l'utilisateur
======================

.. role:: python(code)
   :language: python

.. role:: console(code)
   :language: console

Installation
------------

Ce guide vous aidera à installer le projet étape par étape.
Il inclut des instructions pour les débutants, avec des options supplémentaires pour les utilisateurs qui souhaitent utiliser **Chocolatey** et **Visual Studio Code**.


Étape 1 : Téléchargement depuis GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Rendez-vous sur `la page GitHub du projet <https://github.com/tmonseigne/Python-CI-Template>`_.
2. Cliquez sur **Code** (le bouton vert).
3. Choisissez **Download ZIP** pour télécharger les fichiers du projet sur votre ordinateur.
4. Extrayez les fichiers dans un dossier accessible (par exemple, :console:`C:\\Git\\Python-CI-Template`).


Étape 2 : Installation de Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Téléchargez Python depuis le `site officiel <https://www.python.org/downloads/>`_.
2. Pendant l'installation, assurez-vous de cocher l'option **Add Python to PATH**.
3. Une fois installé, vérifiez que Python fonctionne :

   - Ouvrez un terminal ou une invite de commande (:console:`PowerShell` sur Windows).
   - Tapez la commande suivante :console:`python --version` et appuyez sur **Entrée**

.. note::
   Vous devriez voir une version de Python (par exemple, :console:`Python 3.x.x`).


Étape 3 : Création d'un environnement virtuel (optionnel)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un environnement virtuel permet de gérer les dépendances du projet de manière isolée.

1. Ouvrez un terminal ou une invite de commande (:console:`PowerShell` sur Windows) dans le dossier où vous avez extrait les fichiers du projet.
   Exemple pour :console:`C:\\Git\\Python-CI-Template`. Ouvrez le terminal et tapez la commande suivante  :console:`cd C:\\Python-CI-Template` et appuyez sur **Entrée**
2. Créez un environnement virtuel avec la commande suivante :console:`python -m venv venv`
3. Activez l'environnement virtuel :

   - Sous Windows : :console:`.\venv\Scripts\activate`
   - Sous macOS/Linux : :console:`source venv/bin/activate`

4. Vous verrez maintenant :console:`(venv)` au début de votre invite de commande, indiquant que l'environnement virtuel est actif.


Étape 4 : Installation des dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Ouvrez un terminal ou une invite de commande (:console:`PowerShell` sur Windows) dans le dossier où vous avez extrait les fichiers du projet.
   Exemple pour :console:`C:\\Git\\Python-CI-Template`. Ouvrez le terminal et tapez la commande suivante  :console:`cd C:\\Git\\Python-CI-Template` et appuyez sur **Entrée**
2. Assurez-vous que l'environnement virtuel est activé si vous le souhaitez (voir Étape 3).
3. Installez les dépendances nécessaires avec la commande : :console:`python -m pip install -r requirements.txt`

C'est terminé ! 🎉 Vous avez installé et configuré Python pour votre module avec succès.

Utilisation
-----------

Ici, vous pouvez ajouter des exemples d'utilisation.

FAQ
---

**1. Pourquoi utiliser un environnement virtuel ?**
Pour éviter les conflits entre les dépendances de différents projets.

**2. Et si je n'ai pas `pip install` ?**
Cela signifie que Python n'est pas bien installé. Reprenez l'Étape 2 et assurez-vous d'avoir ajouté Python au `PATH`.

**3. Où puis-je trouver plus d'aide ?**
Consultez la documentation officielle de Python ou contactez le support du projet.
