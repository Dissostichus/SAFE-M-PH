Installation
============

Emplacement du programme
------------------------

La première étape consiste à installer le programme permettant d'utiliser le pH mètre.
Ce programme est en accès libre sur le site internet GitHub sur le compte `fmetivier <https://github.com/fmetivier/pH_meter_V2.0>`_.

https://github.com/fmetivier/pH_meter_V2.0

Charger le répertoire
---------------------

Afin d'utiliser le programme vous avez besoin de charger le répertoire dans lequel il se trouve. Ce répertoire
contient l'ensemble des codes et dossiers nécessaires à la bonne utilisation des pH mètres.

Vous pouvez cloner le répertoire en saisissant directement dans le terminal la commande::

    git clone https://github.com/SAFE-M/SAFE-M-PH.git

.. note:: 

    Attention, avant d'importer le programme vérifiez bien que vous vous situez dans votre répertoire de travail.

Mise en place du pH mètre
-------------------------

Avant de lancer le programme, branchez le pH-mètre avec le cable d’alimentation à un des ports USB
de l’ordinateur. Branchez ensuite la sonde pH sur le boitier du pH-mètre. Devissez le capuchon de la
sonde, rincez la avec de l’eau distillée ou de l’eau claire si vous n’avez pas d’eau distillée
à votre disposition. Séchez délicatement puis plongez le pH-mètre dans la solution à mesurer. 

Démarrage du programme
----------------------

Vous êtes maintenant prêt à faire fonctionner le pH-mètre. Vous devez avoir un dossier nommé ``pH_meter_V2.0``, qui contient :

``Programme pH mètre_V2.py``:
    Il s'agit du programme principal permettant d'intéragir avec le pH-mètre au travers d'un interface dans le terminal.

``lib_pH.py``:
    Ce code contient l'ensemble des fonctions nécessaire au fonctionnement du programme principal.

``DATA``:
    Ces dans ce dossier que vont être enregistrées les données acquisent lors des mesures de pH.

``CALIB``:
    Ce dossier contient les données de toutes les calibrations du pH mètre effectuées, ce qui permet notamment de les réutiliser.

``FIGURES``:
    Comme son nom l'indique, ce dossier regroupe l'ensemble des graphique permettant de visualiser les données mesurées et de suivre l'évolution du pH
    des solutions analysées.

``send_ph_T_Uno``:
    Ce dossier contient le script à charger sur la carte Arduino permettant de communiquer les données de voltage et de température, mesurées par les sondes, à l'ordinateur.

``Fritzing``:
    Contient une image représentant l'agencement et le branchement des différents composants du pH mètre.

``compare.py``:
    Ce programme permet d'évaluer la précision et fiabilité des pH-mètres construits à partir de carte Arduino par rapport à un pH mètre de laboratoire Hanna.

``__pycache__``: 
    Ce répertoire automatiquement créé par Python stocke les fichiers compilés des modules Python utilisés.

``Mauel_d_utilisation_pH_metre.pdf``:
    Cours manuel explicitant l'utilisation du pH mètre.

``CITATION.cff``:
    Métadonnées à utiliser pour citer cd logiciel si vous souhaités l'utiliser.

``README.md``:
    Documentation du pH mètre.

Essayons de lancer le programme pour voir comment celui-ci fonctionne. Saisissez simplement::

    # A l'intérieur du dossier pH_meter_V2/ 
    python3 'Programme pH mètre_V2.py'

Cela devrait lancer le programme dans le terminal et vous dire que vous que la connexion avec l'Arduino est établie,
vous donner les paramètres de régression de la calibration par défaut du pH mètre ainsi qu'une figure de la courbe de calibration. De plus le programme affiche l'interface 
du MENU PRINCIPAL.

Vous devriez obtenir::

    -> python3 'Programme pH mètre_V2.py' 
    Connexion établie avec le port /dev/ttyACM0
    pH-mètre connecté  au port /dev/ttyACM0
    Les paramètres a et b de notre regression linéaire sont [0.01323408 2.15989141]
    Pour un voltage de 600 le pH prédit est de 10.10033889796552
    0.99985

        ===========================================================================
        MENU PRINCIPAL
        ===========================================================================
        Que souhaitez-vous faire ?
        1 - Calibrer
        2 - Mesurer
        3 - Représenter graphiquement
        4 - Quitter
        ===========================================================================
        ? 

.. warning::

    Si le pH mètre n'est pas correctement branché à l'ordinateur 
    ou que l'Arduino ne parvient à se connecter au port d'accès un message d'erreur devrait apparaître de la forme::

        -> python3 'Programme pH mètre_V2.py'
        /!\ Port de connexion non détecté. Merci de rétablir la connexion non établie : connexion au processeur dans les réglages avant utilisation.
        Attention aucun arduino disponible

Ajout d'un nouveau pH-mètre au programme
----------------------------------------

Si le programme ne parvient pas à se connecter avec un nouveau pH-mètre cela peut être du au fait qu'il n'est pas encore enregistré dans la liste des connexions 
disponibles. Pour y remédier ouvrez le logiciel Arduino présent sur votre ordinateur. Une fois la fenêtre ouverte assurez vous que le pH-mètre est bien branché à un port USB de 
votre oridnateur. En haut à gauche de la fenêtre, allez dans l'onglet ``Outils`` et selectionnez l'option ``Récupérer les informations de la carte``. 

.. image:: ./_static/fig_arduino.png

En cliquant sur cette option une seconde fenêtre devrait apparaitre au centre de votre écran, intitulée ``Information de la carte``. Copiez le code ``SN``.

.. image:: ./_static/fig_info.png

Dans le repertoire ``pH_meter_V2.0`` contenant l'ensemble des fichiers nécessaires au fonctionnement du programme, ouvrez dans un éditeur de texte, par exemple **gedit**,
le fichier ``lib_pH.py``. Dans ce fichier, juste après l'entête **# ACCES ARDUINO**, vous allez pouvoir modifier la fonction ``port_connexion``::

    def port_connexion(br = 9600 , portIN = '') :
    """
    Établit la connexion au port série.

    Parameters
    ----------
    br : int
        Flux de données en baud.
    portIN : string
        Identifiant du port série sur lequel le script doit lire des données.

    Returns
    -------
    port : string
        Identifiant du port série sur lequel le script doit lire des données.
    s : serial.tools.list_ports_common.ListPortInfo / string
        Objet Serial sur lequel on peut appliquer des fonctions d'ouverture, de lecture et de fermeture du port série affilié. En cas d'échec de connexion, 's' sera une chaîne de caractères "erreur".

    """

    arduino_list=['7513931383135150F0D1','85035323234351504260','85035323234351E09062','75439313737351402252','8503532323435130F142','75330303934351B05162']

    if portIN == '' :
        ports = list(serial.tools.list_ports.comports())
    else :
        ports = [portIN]  
    i = 0 
    conn = False
    while conn == False :
        try :
            port = ports[i] 
            if portIN == '' and (port.manufacturer == 'Arduino (www.arduino.cc)' or port.serial_number in arduino_list ):
                port = port.device
                port = (port).replace('cu','tty')
                s = serial.Serial(port=port, baudrate=br, timeout=5) 
                conn = True  
                print('Connexion établie avec le port', port)
            else :
                s = serial.Serial(port=port, baudrate=br, timeout=5)
                conn = True
                print('Connexion établie avec le port', port)
        except :
            i += 1
            if i >= len(ports) :
                print("/!\ Port de connexion non détecté. Merci de rétablir la connexion non établie : connexion au processeur dans les réglages avant utilisation.")
                s = 'error' 
                portIN = '' 
                conn = True
            pass     
    return port , s

Dans cette fonction, ajouter à la liste ``arduino_list`` le code SN du nouveau pH-mètre :

.. image:: ./_static/fig_list_arduino.png

Sauvegardez les modifications et relancez le programme. Le pH-mètre devrait maintenant correctement se connecter.

Le programme est désormais lancé et le pH-mètre prêt à être utilisé.

La suite 
~~~~~~~~

Il est maintenant temps de passer aux étapes suivantes:

:ref:`calibration`

:ref:`mesure`

:ref:`graph`