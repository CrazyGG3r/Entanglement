import pygame
import rand_Tit as t
import TextDraw 
import ALPHABET as alph

pygame.init()
#screen display stuff=-=-=-=-=-=-=-=-=-=-=---=-=--=-=-=--=
scrn_h = 768
scrn_w = 1380
screen = pygame.display.set_mode((scrn_w,scrn_h))

title = t.titleselect()
pygame.display.set_caption(title)
#end of screendisplay setting =-=-=-=--=-=-=-=-=-=-=-=--=-=

#clockinit()+++=-=-=--=-=-=--==-=-
clock = pygame.time.Clock()
v = 0
w = 0 
#clock end=-=-=-=-=-=-=-=-=-=-==--=

fontcolor = (255,255,255)


def draw_ENTANGLEMEMT(v):
    if(v>=10):
        v=0
    startpos = 400
    offset = 50
    screen.blit(alph.lettE[v],((startpos+(offset*0)),170))
    screen.blit(alph.lettN[v],((startpos+(offset*1)),170))
    screen.blit(alph.lettT[v],((startpos+(offset*2)),170))
    screen.blit(alph.lettA[v],((startpos+(offset*3)),170))
    screen.blit(alph.lettN[v],((startpos+(offset*4)),170))
    screen.blit(alph.lettG[v],((startpos+(offset*5)),170))
    screen.blit(alph.lettL[v],((startpos+(offset*6)),170))
    screen.blit(alph.lettE[v],((startpos+(offset*7)),170))
    screen.blit(alph.lettM[v],((startpos+(offset*8)),170))
    screen.blit(alph.lettE[v],((startpos+(offset*9)),170))
    screen.blit(alph.lettN[v],((startpos+(offset*10)),170))
    screen.blit(alph.lettT[v],((startpos+(offset*11)),170))

    
 


#menu loop=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=
run = True
while run:
    if(v>=5):
        v = 0
    else:
        v+=1
    if(w>=10):
        w = 0
    else:
        w+=1
    clock.tick(1.5)
    screen.fill((0,0,0))
    screen.blit((TextDraw.bg_draw(v)),(0,0))
    draw_ENTANGLEMEMT(w)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
    pygame.display.update()
pygame.quit()
#menu loop end-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=