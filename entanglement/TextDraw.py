import pygame
pygame.init()

bgimg =[ pygame.image.load("menu_bg\\mainbg_0001.png"),
         pygame.image.load("menu_bg\\mainbg_0002.png"),
         pygame.image.load("menu_bg\\mainbg_0003.png"),
         pygame.image.load("menu_bg\\mainbg_0004.png"),
         pygame.image.load("menu_bg\\mainbg_0005.png")
        ]
def text_Draw(text,font,textcolor,size):
    fonte = pygame.font.Font(font,int((size-5)/2))
    img = fonte.render(text,True,textcolor)
    return img

def bg_draw(val):
    if (val>=5):
        val = 1
    return bgimg[val]
