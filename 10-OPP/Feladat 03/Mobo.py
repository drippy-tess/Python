class​ ​Mobo​:
​    ​def​ ​__init__​(​self​, ​gyarto​: ​str​, ​tipus​: ​str​, ​chipset​: ​str​): 
​        ​super​().​__init__​() 
 
​        ​self​.​gyarto​ ​=​ ​gyarto 
​        ​self​.​tipus​ ​=​ ​tipus 
​        ​self​.​chipset​ ​=​ ​chipset 
    
    def​ ​__str__​(​self​) ​->​ ​str​: 
​       ​return​ ​f"Az alaplap gyártója és típusa: ​{​self​.​gyarto​}​ ​{​self​.​tipus​}​, Chipset fajtája: ​{​self​.​chipset​}​"