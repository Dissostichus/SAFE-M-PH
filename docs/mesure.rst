.. _mesure:

Mesures du pH
=============

.. warning::

    Il est important que la solution à mesurer soit dans les mêmes conditions de pression mais surtout de
    température que les solutions tampons lors de la calibration, puisque la correction du pH en fonction de
    la température s’effectue pendant la calibration. Si la température de votre solution évolue au cours du
    temps une nouvelle calibration est nécessaire.

Préparation
-----------

Après avoir oté le capuchon de protection, plongez la sonde pH ainsi que la sonde de température dans la solution à mesurer. 
Agitez l’électrode pendant quelques secondes puis stabilisez-la. 

Sélectionnez dans le ``MENU PRINCIPAL`` l’option ``2 - Mesurer`` en appuyant sur la touche ``2`` de votre clavier
puis valider avec la touche **Entrée**. 
Le programme vous demande alors si vous êtes prêt à initier les mesures, appuyez sur **Entrée** lorsque vous le serez.

.. note::

    Pour avoir des mesures précises, il est nécessaire que l’instrument ait été étalonné au préalable. Si les mesures sont effectuées dans des échantillons
    successifs, il est recommandé de rincer l’électrode entre chaque échantillon, afin de ne pas contaminer
    les échantillons entre-eux.

Prise de mesure
---------------

Une fois l’opération lancée, **10** valeurs de pH sont mesurées, pour ces 10 valeurs le programme va afficher
le **temps** (en secondes) de la prise mesure par rapport à l'initiation des mesures, la **température moyenne**
et **l’écart-type des mesures de température**, le **voltage moyen**, **l’écart-type des mesures de voltage**, le **pH moyen** mesuré, **l’écart-type
des mesures de pH** et enfin une valeur de la **stabilité**::

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
    
    -> 2

    Prêt à mesurer ?

    Les mesures commencent

    Temps: 0.00
    Température: 25.54 +/- 0.02
    Voltage: 760.00 +/- 2.86
    PH: 8.83 +/- 0.08
    Stabilité: 2.14
    
    Temps: 2.65
    Température: 25.55 +/- 0.02
    Voltage: 761.64 +/- 1.67
    PH: 8.78 +/- 0.05
    Stabilité: 2.94

La stabilité est un coefficient qui représente l’ecart entre **10** valeurs de pH mesurées et les **10** valeurs mesurées précedentes. 
La mesure de la sonde est considérée comme stabilisée lorque que le coeffcient de stabilité est proche de **zéro**. 
Tant que la valeur du coeffcient de stabilité n’est pas satisfaisante le programme continue d’effectuer des mesures. 

Une fois une stabilité satisfaisante atteinte, le programme arrête ses mesures et demande à l'utilisateur s'il souhaite continuer ou non la prise de mesures. 
L’utilisateur a alors le choix de poursuivre les mesures en répondant par ``O``, ``o``, ``Y`` ou ``y``. Le programme effectue alors 20 mesures
supplémentaires avant de reproposer de continuer ou non. 

Si l’utilisateur juge que le nombre de mesures est suffisant et souhaite s’arrêter là, il répond alors à la question posée avec ``N`` ou ``n``. 
Le programme propose alors à l'utilisateur s'il souhaite voir la :ref:`graph` qu'il vient de mesurer. 
L’ensemble des mesures est enregistré dans un fichier ``csv`` de la forme ``fichier mesure Day Month H_min_sec Year.csv`` dans le dossier ``DATA``.

.. warning::

    Si vous souhaitez enregistrer l'évolution des valeurs de pH de vos données en fonction du temps référez-vous maintenant à la prochaine étape : 

    :ref:`graph`


Mesures d'Alcalinité
--------------------

Si vous souhaitez utilisez ces pH mètre pour une mesure d’alcalinité la procédure est la même mais poursuivez les mesures jusqu’à la fin de votre titrage avec l'option ::
    
    Continuer les mesures (O/N) ? 

    -> N 

Le titrage peut être considéré comme terminé une fois la valeur seuil de pH atteinte à **pH 3.7**. 

Assurez vous que la mesure de pH soit bien stabilisée avant d’ajouter un nouvel incrément de **HCl**. 

La représentation graphique de vos mesure aux termes du titrage ainsi que le fichier contenant les données
mesurées, enregistré dans le dossier ``DATA``, vous permettront de déterminer l’alcalinité à partir des méthodes de
**Gran** et de **Culberson**.