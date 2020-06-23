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
# msg dan sonra back ground değerine tuple gelmeli örn:(255,255,255) veya colors dan değer
class single:
    def __init__(self,screen, pos, font, color, msg, background = False, backcolor = (0,0,0), size = (30,30), width = 0):
        self.screen = screen
        self.pos = pos
        self.font = font
        self.color = color
        self.msg = msg
        self.background = background
        self.backcolor = backcolor
        self.size = size
        self.width = width
        self.activeted = False

        self.text = "Empty"
        self.text_x = 0
        self.text_y = 0
        if self.background:
            self.text = self.font.render(self.msg, True, self.color)
            self.text_x = self.size[0]/2 - self.text.get_width()/2 + self.pos[0]
            self.text_y = self.size[1]/2 - self.text.get_height()/2 + self.pos[1]
        else:
            self.text = self.font.render(self.msg, True, self.color)
            self.text_x = self.size[0]/2 - self.text.get_width()/2 + self.pos[0]
            self.text_y = self.size[1]/2 - self.text.get_height()/2 + self.pos[1]
    def render(self):
        if self.background:
            pygame.draw.rect(self.screen,self.backcolor,(self.pos,self.size),self.width)
            self.screen.blit(self.text,(self.text_x,self.text_y))
        else:
            self.screen.blit(self.text,(self.text_x,self.text_y))



#args ın "0" ıncı indeksi tuple olduğunda onu back ground olarak kullanacak rowNline ve gap 2 li tuple olacak
def menu(screen, pos, font ,color ,collumNline , gap, *msg, background = False, backcolor = (0,0,0), size = (30,30), width = 0):
    menu_elements = []
    menu_rects = []
    gapx , gapy = gap
    posx , posy = pos
    sizex , sizey = size
    collum , line= collumNline
    a=0
    for x in range(line):
        for i in range(collum):
            menu_element=single(screen, (posx,posy), font, color, msg[i+a], background, backcolor, size, width)
            menu_elements.append(menu_element)
            menu_rects.append(pygame.Rect((posx,posy),size))
            posx = posx + gapx + sizex
        a+=2
        posx = pos[0]
        posy = posy + sizey + gapy

    return menu_elements, menu_rects

            



pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME")


font1 = pygame.font.SysFont("Arial",25)



activemenu = []
activemenu_rects = []

def main():
    global running, screen, colors, activemenu,activemenu_rects         
    screen.fill((255,0,0))
    clock = pygame.time.Clock()
    menutype ='mainmenu'
    showmenu = 0

    single1=single(screen,(200,200), font1, (255,255,255),"Kebab OwO",size = (70,90))


    mainmenu,mainmenu_rects = menu(screen, (0,0), font1, colors['white'], (2,3), (10,10), "kebab yes","yes","no","YEmek","elma","birşeyler", background = True, backcolor = colors['olive'], size = (100,50), width = 0)

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
        if menutype == "mainmenu" and showmenu == 0:               
            showmenu=1
            for x in mainmenu:
                x.render()
            activemenu = mainmenu
            activemenu_rects = mainmenu_rects
            print(activemenu_rects)
        pygame.display.flip()#bu satır tüm ekranı yeniliyor

        

def get_MousePos():
    pos = pygame.mouse.get_pos()
    return (pos)
def checkhitmenu():
    global activemenu_rects, activemenu
    posx,posy = get_MousePos() 
    a=0
    for i in activemenu_rects:
        if posx >= i.left and posx <= i.right and posy >= i.top and posy <= i.bottom :
            activemenu[a].activeted = True
            print(activemenu[a].msg)
        a+=1
        pass



if __name__ == '__main__':
   main()