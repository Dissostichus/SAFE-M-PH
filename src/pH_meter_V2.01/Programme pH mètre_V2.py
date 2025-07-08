#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:34:52 2024

@author: Thibault Chardon, Thomas Gauthier-Brouart, Caroline Lu, François Métivier, Clara Palmieri
"""

from lib_pH import *


if __name__ == '__main__':

    plt.ion()

    try:
        port, s = port_connexion()
        print("pH-mètre connecté  au port %s" % (port))
    except:
        print("Attention aucun arduino disponible")
    
    interface ="""
    ===========================================================================
    MENU PRINCIPAL
    ===========================================================================
    Que souhaitez-vous faire ?
    1 - Calibrer
    2 - Mesurer
    3 - Représenter graphiquement
    4 - Quitter
    ===========================================================================
    ? """

    new_calib = False
    continuer = True
    calib3 = False
    continuer_calib = True
    default_model = default_Calibration()
    while continuer:
        
        continuer_calib = True
        
        x = input (interface)
        
        if x == '1':
            
            while continuer_calib :

                
                interface_calib ="""
    ===========================================================================
    MENU CALIBRATION
    ==========================================================================
    Voulez - vous :
    1 - Calibrer avec deux tampons (pH 7 et 4) ?
    2 - Calibrer avec trois tampons (pH 7, 4 et 10) ?
    3 - Calibrer à partir d'une calibration déjà existante dans le répertoire
    4 - Quitter le menu calibration et retourner au menu principal
    ===========================================================================
    ? """
                x_calib = input(interface_calib)
                if x_calib == '1':
                    calib3 = False
                    buffer_value = None
                    errorbuffers_values = [0.01, 0.01]
                    model = Calibration(calib3, buffer_value, buffers = [7, 4], n = 300, port_test = s)
                    new_calib=True

                elif x_calib == '2':
                    calib3 = True
                    errorbuffers_values = [0.01, 0.01, 0.01]
                    buffer_value = input('Quel est le pH de la troisième solution que vous souhaitez utilisez ? ( 9 / 10 / 11)')
                    if buffer_value == '9':
                        model = Calibration(calib3, buffer_value, buffers = [7, 4, 9], n = 300, port_test = s)
                    elif buffer_value == '10':
                        model = Calibration(calib3, buffer_value, buffers = [7, 4, 10], n = 300, port_test = s)
                    elif buffer_value == '11':
                        model = Calibration(calib3, buffer_value, buffers = [7, 4, 11], n = 300, port_test = s)
                    new_calib=True

                elif x_calib == '3':
                    buffer_existant = input('Cette option n\'est possible que pour des calibrations à 3 solutions, quel est le pH de la troisième solution de la calibration que vous souhaitez utilisez ? ( 9 / 10 / 11)')
                    if buffer_existant == '9':
                        model = Calibration_existante(buffer_existant)
                    elif buffer_existant == '10':
                        model = Calibration_existante(buffer_existant)
                    elif buffer_existant == '11':
                        model = Calibration_existante(buffer_existant)
                    new_calib = True

                elif x_calib == '4':
                    continuer_calib = False

        elif x == '2':
            y = input('Prêt à mesurer ?')
            if new_calib :
                measure(model, port_test = s)
            else : 
                measure(default_model, port_test = s)
        elif x == "3":
            graph()
        elif x == '4':
            continuer = False
    
    print('Fin du programme')