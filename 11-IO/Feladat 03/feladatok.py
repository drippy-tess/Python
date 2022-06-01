from roplabda import Roplabda
from roplabdaio import RoplabdaIO
from typing import *
import io
import os

class Feladatok:

    @staticmethod
    def utoJatekos(jatekosok: List[Roplabda]) -> None:
        utok: List[Roplabda] = []
        
        for jatekos in jatekosok:
            if(jatekos.poszt == "ütõ"):
                utok.append(jatekos)

        RoplabdaIO.write("utok.txt", utok)

    @staticmethod
    def csapattagok(jatekosok: List[Roplabda]) -> None:
        csapatokTagjai: Dict[str, str] = {}

        for jatekos in jatekosok:
            csapatokTagjai.update(jatekos.nev)
        
        RoplabdaIO.write("csapattagok.txt", csapatokTagjai)

    @staticmethod
    def magassagok(jatekosok: List[Roplabda]) -> None:
        temp: int = 0

        for i in range(0, len(jatekosok)-1, 1):
            for j in range(i + 1, len(jatekosok), 1):
                if(jatekosok[j] < jatekosok[i]):
                    temp = jatekosok[i]
                    jatekosok[i] = jatekosok[j]
                    jatekosok[j] = temp

        RoplabdaIO.write("magaslatok.txt", temp)

    @staticmethod
    def nemzetisegek(jatekosok: List[Roplabda]) -> None:
        new: List[Roplabda] = []
        
        for jatekos in jatekosok:
            new.append(jatekos.orszag)

        RoplabdaIO.write("nemzetisegek.txt", new)

    @staticmethod
    def magasabbMintAtlag(jatekosok: List)