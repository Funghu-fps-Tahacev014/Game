import pygame
from menu import *
(width, height) = (700, 700)
running = True
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME")


font1 = pygame.font.SysFont("Arial",25)


activemenu = []
colors = {
              "white" : (255, 255, 255),
              "silver" : (255, 255, 255),
              "gray" : (128, 128, 128),
              "black" : (0, 0, 0),
              "red" : (255, 0, 0),
              "maroon" : (128, 0, 0),
              "yellow" : (255, 255, 0),
              "olive" : (128, 128, 0),
              "lime" : (0, 255, 0),
              "green" : (0, 128, 0),
              "cyan" : (0, 255, 255),
              "aqua" : (0, 255, 255),
              "teal" : (0, 128, 128),
              "blue" : (0, 0, 255),
              "navy" : (0, 0, 128),
              "fuchsia" : (255, 0, 255),
              "magenta" : (255, 0, 255),
              "purple" : (128, 0, 128),
              "orange" : (255, 100, 0),
              "gold" : (255, 187, 0),
              "brown" : (117, 74, 49),
              "pink" : (255, 140, 180)
             }

menus = {
            "mainmenu" : menu(screen, (0,0), font1, colors['white'], (1,3), (10,10), "continue","New Game", "Test", background = True, backcolor = colors['olive'], size = (100,50), width = 0, backgroundcolor = colors["magenta"]),
            "Test" : menu(screen, (0,0), font1, colors['white'], (2,3), (10,10), "elma yes","elma yes","elma no","elma","elma","elma", background = True, backcolor = colors['olive'], size = (100,50), width = 0, backgroundcolor = colors["maroon"])
    }
               
print(type(menus["Test"]))
#Game
#classes_____________________________________________________________________
class market:
    def __init__(self):
        #price
        self.marketelements = {
                      "food"          : 3,
                      "infintiary"    : 5,
                      "bowman"        : 10,
                      "cavalry"       : 13,
                      "supportpeople" : 7
                       }
        self.a = 1
market = market()
class country:
    def __init__(self, name):
        self.armysize = 0
        self.armypower = 0

        self.bowpower = 0
        self.cavalrypower = 0
        self.infintiarypower = 0

        self.cavalry = 0
        self.infintiary = 0
        self.bowman = 0

        self.prosperity = 0
        self.food = 0
        self.money = 0

        self.tradepower = 1
        self.tradepowerlimit = 999
        self.charisma = 1
        self.charismalimit = 999

        self.enemies = []
   
    def calculate(self):
        self.bowpower = self.bowman + self.armypower
        self.cavalrypower = self.cavalry + self.armypower
        self.infintiarypower = self.infintiary + self.armypower

    def buy(self,itemname):
        self.money -= market.marketelements[itemname]
        if itemname == "food":
            self.food += 1 * self.tradepower
            if self.tradepower != self.tradepowerlimit:
                self.tradepower += 0.2
        if itemname == "infintiary":
            self.infintiary += 1 * self.tradepower
            if self.tradepower != self.tradepowerlimit:
                self.tradepower += 0.2
        if itemname == "calvary":
            self.calvary += 1 * self.tradepower
            if self.tradepower != self.tradepowerlimit:
                self.tradepower += 0.2
        if itemname == "bowman":
            self.bowman += 1 * self.tradepower
            if self.tradepower != self.tradepowerlimit:
                self.tradepower += 0.2
        if itemname == "supportpeople":
            self.prosperity += 2 * self.charisma
            if self.charisma != self.charismalimit:
                self.charisma += 0.5
        else:pass
#____________________________________________________________________________________________________________________________________________________________________________________
def startwar(country1,country2):
    while country1.cavalry > 0 and country2.cavalry > 0:
        country2.cavalry -= country1.cavalrypower
        country1.cavalry -= country2.cavalrypower
    


def main():
    global running, screen, colors, activemenu , menus, showmenu        
    screen.fill((255,0,0))
    clock = pygame.time.Clock()
    showmenu = True
    activemenu = menus["mainmenu"]

    while running:
        clock.tick(60)
        ev = pygame.event.get()
        #sonra bu for döngüsünü kaldır
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #1== leftclick 2== middle click 3== right click 4== scroll
                #forward 5== scroll back
                if event.button == 1: 
                    checkhitmenu()

            if event.type == pygame.QUIT:
               running = False
               break 
           
        if showmenu == True:
            screen.fill(activemenu.backgroundcolor)
            showmenu = False    
            for x in activemenu.menu_elements:
                x.render()

        pygame.display.flip()#bu satır tüm ekranı yeniliyor
def get_MousePos():
    pos = pygame.mouse.get_pos()
    return (pos)
def checkhitmenu():
    global activemenu_rects, activemenu, showmenu
    posx,posy = get_MousePos() 
    a = 0
    for i in activemenu.menu_rects:
        if posx >= i.left and posx <= i.right and posy >= i.top and posy <= i.bottom :
            print(activemenu.menu_elements[a].msg)
#___________game______________________________________________________________________________________________________________________________________________________________________________________
            try:
                if menus[activemenu.menu_elements[a].msg]:
                    activemenu = menus[activemenu.menu_elements[a].msg]
                    showmenu = True
                

            except :
                pass
        a+=1
        pass
if __name__ == '__main__':
   main()