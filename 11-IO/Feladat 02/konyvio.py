from konyv import Konyv
from typing import *
import io
import os

class KonyvIO:
    def __init__(konyv) -> None:
        super().__init__()

    @staticmethod
    def read(fileName: str) -> List[Konyv]:
        oneLine:str = None
        allLines:List[str]=[]
        
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))#visszaadja azt a mappát amiben dolgozunk
            path: str = os.path.join(here, fileName)#összefűzi a mappát a mi fájlnevünkkel 

            with open(path,encoding='latin-1', mode="r") as file:
                for line in file:
                    oneLine = line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")

        konyvek: List[Konyv] = []
        konyv: Konyv = None
        
        adatok: List[str] = []
        
        kerNev: str = None
        vezNev: str = None
        szulDatum: str = None
        cim: str = None
        isbn = int = 0
        kiado: str = None
        kiadasiEv: str =None
        ar: int = 0
        tema: str = None
        oldalSzam: int = 0
        honorarium: int = 0


        for line in allLines:
            adatok = line.split('\t')

            kerNev = adatok[0]
            vezNev = adatok[1]
            szulDatum = adatok[2]
            cim = adatok[3]
            isbn = adatok[4]
            kiado = adatok[5]
            kiadasiEv = adatok[6]
            ar = adatok[7]
            tema = adatok[8]
            oldalSzam = adatok[9]
            honorarium = adatok[10]

            konyv = Konyv(kerNev, vezNev, szulDatum, cim, isbn, kiado, kiadasiEv, ar, tema, oldalSzam, honorarium)
            konyvek.append(konyv)

        return konyvek

    @staticmethod
    def write(fileName: str, konyvek: List[Konyv]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))#visszaadja azt a mappát amiben dolgozunk
            path: str = os.path.join(here, fileName)#összefűzi a mappát a mi fájlnevünkkel 
            
            with open(path, encoding="latin-1", mode="w") as file:
                for konyv in konyvek:
                    file.write(f"{konyv.vezNev} {konyv.kerNev} {konyv.szulDatum} {konyv.cim} {konyv.isbn} {konyv.kiado} {konyv.kiadasiev} {konyv.ar} {konyv.tema}, {konyv.oldalSzam} {konyv.honorarium}")
        except Exception as ex:
            print(f"{ex}")