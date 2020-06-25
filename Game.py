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

menus={
            "mainmenu" : menu(screen, (0,0), font1, colors['white'], (1,2), (10,10), "continue","New Game", "Exit", background = True, backcolor = colors['olive'], size = (100,50), width = 0, backgroundcolor = colors["magenta"]),
            "Test" : menu(screen, (0,0), font1, colors['white'], (2,3), (10,10), "elma yes","elma yes","elma no","elma","elma","elma", background = True, backcolor = colors['olive'], size = (100,50), width = 0, backgroundcolor = colors["maroon"])
    }
        
       

print(type(menus["Test"]))
            




def main():
    global running, screen, colors, activemenu , menus, showmenu        
    screen.fill((255,0,0))
    clock = pygame.time.Clock()
    showmenu = True

    single1=single(screen,(200,200), font1, (255,255,255),"Kebab OwO",size = (70,90))

    
    activemenu = menus["Mainmenu"]

    while running:
        clock.tick(60)
        ev = pygame.event.get()
        #sonra bu for döngüsünü kaldır
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
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
    a=0
    for i in activemenu.menu_rects:
        if posx >= i.left and posx <= i.right and posy >= i.top and posy <= i.bottom :
            print(activemenu.menu_elements[a].msg)
            try:
                if menus[activemenu.menu_elements[a].msg]:
                    activemenu = menus[activemenu.menu_elements[a].msg]
                    showmenu = True
                #elif activemenu.menu_elements[a].msg = "blabla": blabla()   menu olmayan tuşları bu şekilde kullanacaz

            except :
                pass
        a+=1
        pass



if __name__ == '__main__':
   main()