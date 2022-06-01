from roplabda import Roplabda
from typing import *
import io
import os

class RoplabdaIO:
    def __init__(roplabda) -> None:
        super().__init__()

    @staticmethod
    def read(fileName: str) -> List[Roplabda]:
        oneLine:str = None
        allLines:List[str]=[]
        
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))#visszaadja azt a mappát amiben dolgozunk
            path: str = os.path.join(here, fileName)#összefűzi a mappát a mi fájlnevünkkel 

            with open(path,encoding='utf-8', mode="r") as file:
                for line in file:
                    oneLine = line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")

        roplabdazok: List[Roplabda] = []
        roplabda: Roplabda = None
        
        adatok: List[str] = []
        
        nev: str = None
        magassag: int = None
        poszt: str = None
        nemzetiseg: str = None
        csapat: str = None
        orszag: str = None


        for line in allLines:
            adatok = line.split('\t')

            nev = adatok[0]
            magassag = adatok[1]
            poszt = adatok[2]
            nemzetiseg = adatok[3]
            csapat = adatok[4]
            orszag = adatok[5]

            roplabda = Roplabda(nev, magassag, poszt, nemzetiseg, csapat, orszag)
            roplabdazok.append(roplabda)

        return roplabdazok

    @staticmethod
    def write(fileName: str, roplabdazok: List[Roplabda]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))#visszaadja azt a mappát amiben dolgozunk
            path: str = os.path.join(here, fileName)#összefűzi a mappát a mi fájlnevünkkel 
            
            with open(path, encoding="utf-8", mode="w") as file:
                for roplabda in roplabdazok:
                    file.write(f"{roplabda.nev} {roplabda.magassag} {roplabda.poszt} {roplabda.nemzetiseg} {roplabda.csapat} {roplabda.orszag}\n")
        except Exception as ex:
            print(f"{ex}")