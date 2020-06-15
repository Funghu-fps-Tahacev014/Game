import pygame

(width, height) = (700, 700)
running = True

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
# msg dan sonra back ground değerine tuple gelmeli örn:(255,255,255) 
def single(screen,pos,font,color,msg,*background):
    if type(background[0]) == tuple and len(background[0]) == 3:
        text = font.render(msg, True, color, background)
    else: 
        text = font.render(msg,True,color)
    screen.blit(text,pos)
    return text.get_width() ,text.get_height()


#args ın "0" ıncı indeksi tuple olduğunda onu back ground olarak kullanacak rowNline ve gap 2 li tuple olacak
def menu(screen, pos, font ,color ,lineNcollum , gap, *args):
    gapx , gapy = gap
    posx , posy = pos
    collum , line= lineNcollum
    
    if type(args[0]) == tuple or type(args[0]) == dict:
        for i in range(collum + 1):
            if i == 1:
                size=(single(screen, pos, font, color, args[i], args[0]))
                posx= posx + gapx + size[0]
            if i > 1:
                size=(single(screen,(posx , posy) , font ,color ,args[i] ,args[0]))
                posx= posx + gapx + size[0]
    else:
        pass

            



pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME")


font1 = pygame.font.SysFont("Arial",25)

def main():
    global running, screen, colors         
    screen.fill((255,0,0))
    clock = pygame.time.Clock()
    menutype ='mainmenu'
    showmenu = 0

    while running:
        clock.tick(60)
        ev = pygame.event.get()
        #sonra bu kısmı kaldır
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos=drawCircle()
                
                #pygame.display.update(pygame.Rect((pos[0]-20,pos[1]-20),(40,40)))   bu satır sadece dairenin olduğu yeri yenilemeyi sağlıyor 
                
            if event.type == pygame.QUIT:
                running = False
        if menutype == "mainmenu" and showmenu == 0:
            single(screen,(200,200), font1, (255,255,255) ,"Kebab" , colors['blue'])
            menu(screen,(0,0),font1,colors['white'],(3,4),(10,10),colors['olive'],"kebab yes","yes","no","YEmek","elma","birşeyler")
            showmenu=1
        pygame.display.flip()#bu satır tüm ekranı yeniliyor

        

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawCircle():
    pos = getPos()
    pygame.draw.circle(screen, (0,0,255), pos, 20)
    return (pos)


if __name__ == '__main__':
   main()
    

    

