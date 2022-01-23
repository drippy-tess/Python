from typing import Dict
import time
import os
import re

validMail = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
validPassword = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

def emailBekeres() -> str:
    validAdress: str = None
    while(validAdress == None):
        validAdress = input("Kérem adjon meg egy E-mail címet! \n")
        if(re.fullmatch(validMail, validAdress)):
            return validAdress
        else:
            print("A megadott E-mail cím nem megfelelő!")
            time.sleep(3)
            os.system("cls")
            
def jelszoBekeres() -> str:
    validPass: str = None
    while(validPass == None):
        validPass = input("Kérem adjon meg egy jelszót! \n")
        if((re.fullmatch(validPassword, validPass)) and (len(validPass) > 7) and (validPass.islower() for validPass in validPass) and (validPass.isupper() for validPass in validPass) and (validPass.isdigit() for validPass in validPass)):
            return validPass
        else:
            print("Helytelen jelszó!")
            time.sleep(3)
            os.system("cls")

def isUserExists(email: str, password: str) -> bool:
    users: Dict[str, str] = {
        'hetfo@test.com': 'Testjelszo1',
        'kedd@test.com': 'Testjelszo2',
        'szerda@test.com': 'Testjelszo3',
        'csutortok@test.com': 'Testjelszo4',
        'pentek@test.com': 'Testjelszo5',
        'szombat@test.com': 'Testjelszo6',
        'vasarnap@test.com': 'Testjelszo7'
    }
    isExists: bool = ((email, password) in users.items())
    return isExists