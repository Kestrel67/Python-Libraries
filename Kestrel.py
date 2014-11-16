import re
import pickle
import hashlib
import math
import os.path as sys

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Kestrel Python Library Package - V 1.0"""

# Datas
__author__     = __maintainer__   = 'Lucas Dietrich'
__email__     = __contact__     = 'kestrel.3rd@gmail.com'
__alias__     = 'Kestrel'
__website__    = 'http://www.infrarouges.net'
__version__   = '1.0'
__copyright__   = __license__    = None
__credits__    = ['Lucas Dietrich']
__status__     = 'Development'
__deprecated__  = False
__date__      = '2013/05/12'

# Récupère une valeur de l'utilisateur et éxécute la fonction int réessaye tant qu'une erreur apparait
# @param string msg : Message à afficher
# @param function func : Fonciton à executer
# @return mixed
def get(msg, func = None):
  try:
    if func:
      return func(input(msg))
    return input(msg)
  except:
    return get(msg, func)
  
# enregistre un objet python dans un fichier
# @param string file : Chemin vers le fichier
# @param object obj : Objet à enregistrer
def objWrite(file, obj):
  with open(file, 'wb') as handle:
    myPickler = pickle.Pickler(handle)
    myPickler.dump(obj)
    handle.close()
  return obj
  
# récupère l'objet python enregistrer dans le fichier file
# @param string file : Chemin vers le fichier
# @return python object
def objRead(file):
  with open(file, 'rb') as handle:
    myUnpickler = pickle.Unpickler(handle)
    obj = myUnpickler.load()
    handle.close()
  return obj

# écris une donnée string dans le fichier file
# @param string file : Nom du fichier
# @param string|int string : Valeur à écrire
# @return int : nombre de lignes modifés
def write(file, string):
  with open(file, 'w') as handle:
    l = handle.write(str(string))
    handle.close()
    return l

# lit le contenue d'un fichier
# @param string file : Nom du fichier
# @return string : Contenue du fichier    
def read(file):
  with open(file, 'r') as handle:
    s = handle.read()
    handle.close()
    return s

# crée une clé avec l'algorythme algo
# @param string algo : Algorythme à utiliser
# @param string (binary) string : Chaine à encoder
# @param boolean hex : Afficher en hexadecimal ou non
# @return string
def __hashAlgo__(algo, string, hex):
  algo = hashlib.new(algo)
  algo.update(string.encode())
  if hex:
    return algo.hexdigest()
  return algo.digest()

# crée une clé md5 de string
# @param string (binary) string : Chaine à encoder
# @param boolean hex : Afficher en hexadecimal ou non
# @return string
def md5(string = b"", hex = True):
  return __hashAlgo__('md5', string, hex)

# crée une clé sha1 de string
# @param string (binary) string : Chaine à encoder
# @param boolean hex : Afficher en hexadecimal ou non
# @return string
def sha1(string = b"", hex = True):
  return __hashAlgo__('sha1', string, hex)

# crée une clé sha256 de string
# @param string (binary) string : Chaine à encoder
# @param boolean hex : Afficher en hexadecimal ou non
# @return string
def sha256(string = b"", hex = True):
  return __hashAlgo__('sha256', string, hex)
  
# crée une clé sha512 de string
# @param string (binary) string : Chaine à encoder
# @param boolean hex : Afficher en hexadecimal ou non
# @return string
def sha512(string = b"", hex = True):
  return __hashAlgo__('sha512', string, hex)

# vérifie l'existance du chemin path, si file vaux True,
# il vérifie si c'est un fichier, si file vaux false,
# il vérifie s'il s'agit d'un dossier,
# si file vaux None, alors il regarde si le fichier ou
# le dossier existe <=> si le chemin est valide
# @param string path : Chemin vers le fichier/dossier
# @param boolean|None type file : Fichier/dossier ou seulement vérifier l'existance
def exists(path, file = True):
  if sys.exists(path):
    if file:
      return sys.isfile(path)
    else:
      return sys.isdir(path)
  else:
    return False

# test regexp
def match(string, pattern):
  assert isinstance(string, str)
  assert isinstance(pattern, str)

  return bool(re.match(pattern, string))
  
 
