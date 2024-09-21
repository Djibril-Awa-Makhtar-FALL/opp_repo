# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:30:02 2024

@author: Djibril Awa Makhtar FALL

Point de Controle sur la Gestion des fichiers
"""
import numpy as np

# 1) Créez un nouveau fichier appelé « calculator_2.0.py »

# 2) Créez une classe appelée « Calculatrice » qui contient les éléments suivants :
    
class Calculatrice : 
    
    def __init__(self):
        
        # dictionnaire pour stocker les opérations mathématiques
        
        self.opretaions = {
            '+' : self.add,
            '-' : self.subtracttract,
            '*' : self.multiply,
            '/' : self.divide,
            
            }
        # ajout de la méthode add_opération
        
    def add_operation(self, symbole, fonction):
        """Ajoute une nouvelle opération au dictionnaire."""
        self.operations[symbole] = fonction
        
        # complément de la classe par les méthodes d'opérations
        
    def additionner(self, a, b):
        
        return a + b

    def soustraire(self, a, b):
        
        return a - b

    def multiplier(self, a, b):
        
        return a * b

    def diviser(self, a, b):
        
        if b == 0:
            
            raise ValueError("Division par zéro n'est pas autorisée.")
            
        return a / b
    
    # Ajout de la méthode calculer
    
    def calculer(self, operation, a, b):
        
        if operation in self.operations:
            
            return self.operations[operation](a, b)
        
        else:
            
            raise ValueError(f"L'opération '{operation}' n'est pas définie.")
            
"""3)  Créez des fonctions séparées pour les opérations mathématiques avancées (exponentiation, racine carrée, 
logarithme) et utilisez la méthode « add_operation » pour les ajouter au dictionnaire de la calculatrice."""
    
import math

def exponentiation(a, b):
    """Calcule a à la puissance b."""
    return a ** b

def racine_carre(a):
    """Calcule la racine carrée de a."""
    if a < 0:
        raise ValueError("La racine carrée d'un nombre négatif n'est pas définie.")
    return math.sqrt(a)

def logarithme(a, base=math.e):
    """Calcule le logarithme de a à la base spécifiée."""
    if a <= 0:
        raise ValueError("Le logarithme d'un nombre non positif n'est pas défini.")
    return math.log(a, base)

""" 4) Dans le programme principal, créez une instance de la classe Calculator
et utilisez une boucle while qui permet à l'utilisateur de continuer à effectuer
 des calculs jusqu'à ce qu'il choisisse de quitter."""
 
## Le reste des questions je l'ai pas bien saisi!!!
        
        
