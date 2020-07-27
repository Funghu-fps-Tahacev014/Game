import pygame
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




class menu:
    def __init__(self, screen, pos: tuple, font ,color: tuple ,collumNline: tuple , gap: int, *msg: str, background = False, backcolor: tuple = (0,0,0), size = (30,30), width = 0, backgroundcolor = (255,0,0)):
        self.menu_elements = []
        self.menu_rects = []
        self.gapx ,  self.gapy = gap
        self.posx ,  self.posy = pos
        self.sizex ,  self.sizey = size
        self.collum ,  self.line= collumNline
        self.a=0
   
        self.screen = screen
        self.pos = pos
        self.font = font
        self.color = color
        self.msg = msg
        self.background = background
        self.backcolor = backcolor
        self.size = size
        self.width = width
        self.backgroundcolor = backgroundcolor
        for x in range( self.line):
           for i in range( self.collum):
               menu_element=single( self.screen, ( self.posx, self.posy),  self.font,  self.color,  self.msg[i+ self.a],  self.background,  self.backcolor,  self.size,  self.width)
               self.menu_elements.append(menu_element)
               self.menu_rects.append(pygame.Rect(( self.posx, self.posy), self.size))
               self.posx =  self.posx +  self.gapx +  self.sizex
           if self.collum != 1:
             self.a+=2
           else:
               self.a+=1
           self.posx =  self.pos[0]
           self.posy =  self.posy +  self.sizey +  self.gapy