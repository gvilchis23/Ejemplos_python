'''
Created on 10/02/2013

@author: infest48
'''
#rock-paper-scissors-lizard-spock
import random

def rspls(guess):
    number_user=name_to_number(guess)
    number_computer= random.randint(0,5)
    resultado = (number_computer - number_user) % 5
    if(resultado >0 and resultado<=2):
        nombre=number_to_name(number_computer)
        print "usuario"+number_to_name(number_user)
        print "computer "+nombre
        print "gana "+nombre
    elif(resultado>2):
        nombre=number_to_name(number_user)
        print "usuario "+nombre
        print "computer"+number_to_name(number_computer)
        print "gana "+nombre
    else:
        print "usuario "+number_to_name(number_user)
        print "computer "+number_to_name(number_computer)
        print "empate"
        
def name_to_number(name):
    if name == "rock":
        number=0   
    elif name =="spock":
        number=1   
    elif name == "paper":
        number=2  
    elif name =="lizard":
        number=3
    elif name =="scissors":
        number=4
    return number

def number_to_name(number):
    if number == 0:
        name="rock"  
    elif number == 1:
        name="spock"
    elif number == 2:
        name="paper"
    elif number == 3:
        name="lizard"
    elif number == 4:
        name="scissors"
    return name


rspls("rock")
rspls("spock")
rspls("paper")
rspls("lizard")
rspls("scissors")
