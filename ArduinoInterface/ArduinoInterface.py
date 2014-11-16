"""
Python Serial Library for arduino communication
Dietrich Lucas (alias Kestrel)
October 2013

######################################
baudrates disponible : Serial.BAUDRATES

Erreurs possibles : 
  UnicodeDecodeError : Erreur de lecture
  InvalidPort : port de com invalide ou non disponible (occopé, etc...)
  InvalidBaudRate : Rate invalide
"""

from serial import Serial

from time import time, sleep

from decorator import *

# ports de communications disponibles
ARDUINO_PORTS = ("com3", "com4", "com6", "com10")

# classe interface pour la communication série 
# le logiciel ALN3D sur un arduino
class ArduinoSerialCom(Serial):
  
  # mise on place de la communication série avec un arduino
  # @param port : port de communication Windows : "com3, 4", Linux: "/dev/tt0..."
  # @param baudrate : bauds par secondes
  # @param wait_ard_ready : temps à attendre pour etre sur que l'arduino est ready
  #         si False : On n'attend pas, si True : on attend le premier message
  # @param timeout en seconde, attente pour la lecture
  #     si False pas d'attente
  #     si True attente complète
  # sinon si
  def __init__(self, port, baudrate, wait_ready = True, timeout = True):
    
    # si le port n'est pas utilisé
    if port not in ARDUINO_PORTS:
      raise InvalidPort(port)
      
    # si le baudrate n'existe pas
    if baudrate not in Serial.BAUDRATES:
      raise InvalidBaudRate(baudrate)
    
    # on appel le constructeur parent
    Serial.__init__(self, port, baudrate, timeout = timeout)
    
    # connection start : temps de début de connexion
    self.connection_start = time()

    # on dort un petit moment
    if not isinstance(wait_ready, bool):
      time.sleep(wait_ready)
     
    # temps qu'on n'a pas de réponse on attend
    elif True:
      while not self.read():
        continue
       
      # temps nécéssaire pour obtenir la première connexion
      self.connection_first_answer = time() - self.connection_start
      print(self.connection_first_answer)
  
  
  
  # on lit la ligne on la décode afin de récupérer une liste des données la composant
  def readformatedline(self, separator = False):
    data = self.readline().decode().strip("\r\n")
    
    # si vide on renvoie False
    if len(data) == 0:
      return False
    
    # s'il y un séparateur on divise
    if separator:
      return data.split(separator)
      
    return data
  
  
   # on lit le caractère entrant :
   # @see Serial.read
  def readformated(self):
    return Serial.read(self).decode()
  
  
  # envoie du text à l'arduino
  def writeString(self, string):
    return self.write(string.encode())  
  
  # on convertit une chaine de byte en une chaine de caractères (UTF-8)
  @staticmethod
  @isType(bytes)
  def decode(byte):
    return byte.decode()
  
  
  # supprime les caractères de fin de ligne WINDOWS
  @staticmethod
  @isType(str)
  def rmEndline(string):
    return string.strip("\r\n")
  
  
  # supprime les tabulations
  @staticmethod
  @isType(str)
  def rmTab(string):
    return string.remove("\t")
  
  
  # supprime les espaces
  @staticmethod
  @isType(str)
  def rmSpace(string):
    return string.remove(" ")
  
  
  # extrait un nombre d'une chaine de caractère
  @staticmethod
  @isType(str)
  def extractNumber(string):
    pass
  
  
# port série invalide
class InvalidPort(Exception):
  def __init__(self, port):
    Exception.__init__(self, "Unused, unknown, unreacheable or invalid communication port {}".format(port))
  
  
# baudrate invalide
class InvalidBaudRate(Exception):
  def __init__(self, port):
    Exception.__init__(self, "Invalid baudrate {}".format(baudrate))
