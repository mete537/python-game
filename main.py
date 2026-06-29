import pgzrun
import pygame


pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)

WIDTH = 1400
HEIGHT = 800
TITLE = 'KAYIP HEDİYELER'
FPS = 30 
ilkk = Actor('ilkk')
saneeiki = Actor('saneeiki')
sahnee3 = Actor('sahnee3')
sonsahne2= Actor('sonsahne2')
cocuk3 =Actor('cocuk3',(100, 500))
hamdiye =Actor('hamdiye',(1200,610))
hamdiyeiki= Actor('hamdiyeiki',(1200,610))

hamdiyeüç = Actor('hamdiyeüç',(1200,610))

kotu2 = Actor('kotu2',(900,540))
oyunbitti5= Actor('oyunbitti5')
oyunbitti5.pos = (WIDTH//2, HEIGHT//2)
kazanma = Actor('kazanma')
başlangiç1  = Actor('başlangiç1')
ilk_sahne = False
sahne_2 = False
sahne_3 = False
son_sahne= False
game_over = False
GO = False
speed = 60
kotu_1 = True
vy = 0
gravity = 2
jump_vel = -46
pygame.mixer.music.load(r"c:\Users\KURSAD METE\Desktop\mö\sounds\muzik.ogg")
pygame.mixer.music.play(-1)

mode = 'menu'
menu_active = True

def draw():
    
    global ilk_sahne, sahne_2, sahne_3, son_sahne, count, GO, kotu_1, game_over, mode, menu_active, vy
    
    if mode == 'menu':
        başlangiç1.draw()
        screen.draw.text("KAYIP HEDİYELER", pos=(350, 150), fontsize=80)
        screen.draw.text("Hediyeler kayip! Onlari bulmalisin!", pos=(300, 280), fontsize=40)
        screen.draw.text(" SPACE tuşuna basarak oyunu başlat", pos=(300, 450), fontsize=35)
        return
    
    if GO == True:    
        oyunbitti5.draw()
        screen.draw.text("OYUN BİTTİ!", pos=(500, 300), fontsize=80, color="red")
        screen.draw.text("TEKRAR OYNAMAK İÇİN R TUSUNA BASIN", pos=(350, 400), fontsize=40, color="white")
        if keyboard.r:
            ilk_sahne = True
            sahne_2 = False
            sahne_3 = False
            son_sahne = False
            GO = False
            cocuk3.x = 100
            cocuk3.y = 540
            kotu2.x = 900
            kotu2.y = 540
            vy = 0
        return
    if mode == 'game over':
        oyunbitti5.draw()
    if kotu_1 == True:
        kotu2.draw()
    
    if ilk_sahne == True:
        
        
        ilkk.draw()
        cocuk3.draw()
        hamdiye.draw()
        kotu2.draw()
        screen.draw.text("hediyeler kayip onlari bulmalisin", pos=(50,30), fontsize = 30)
        if cocuk3.colliderect(hamdiye):
            
            ilk_sahne = False
            sahne_2 = True
            cocuk3.x = 100
            cocuk3.y = 400
            kotu2.x = 900
            kotu2.y = 540
    elif sahne_2 == True:
        speed = 60
        saneeiki.draw()    
        cocuk3.draw()         
        hamdiyeiki.draw()
        kotu2.draw()
        if cocuk3.colliderect(hamdiyeiki):
            
            sahne_2 = False 
            sahne_3 = True
            cocuk3.x = 100
            cocuk3.y = 400
            kotu2.x = 900
            kotu2.y = 600
    elif sahne_3 == True:
        speed = 60
        sahnee3.draw()
        cocuk3.draw()
        hamdiyeüç.draw()
        kotu2.draw()

        if cocuk3.colliderect(hamdiyeüç):
            
            sahne_3 = False 
            son_sahne = True
            cocuk3.x = 60
            cocuk3.y = 400
            kotu2.x = -1000
            kotu_1 = False
    elif son_sahne == True:
        speed = 60
        sonsahne2.draw()
        cocuk3.draw()
        kazanma = True
        screen.draw.text("AFERİN TÜM HEDİYELERİ TOPLADIN!", pos=(0,0), fontsize = 60)
        screen.draw.text("MENÜYE DÖNMEK İÇİN R TUSUNA BASIN", pos=(300, 150), fontsize=35)
        if keyboard.r:
            mode = 'menu'
            ilk_sahne = False
            sahne_2 = False
            sahne_3 = False
            son_sahne = False
            GO = False
            cocuk3.x = 100
            cocuk3.y = 540
            kotu2.x = 900
            kotu2.y = 540
            kotu_1 = True
            vy = 0
    
def update(dt):
    global GO,kotu_1,game_over,mode,ilk_sahne,menu_active,vy
    
    if mode == 'menu':
        if keyboard.space:
            mode = 'game'
            menu_active = False
            ilk_sahne = True
            vy = 0
        return
    
    if GO == True:
        return
    
    #on_mouse_move(pos)
    if cocuk3.colliderect(kotu2):
        GO = True
    if cocuk3.colliderect(kotu2):
        #mode = 'game over'
        game_over = True
    if keyboard.left and cocuk3.x > 10:
        cocuk3.image = "cocuksol3"
        cocuk3.x -= 8

    if keyboard.right and cocuk3.x < 1150:
        cocuk3.image = "cocuksağ3"
        cocuk3.x += 8

    if keyboard.up and cocuk3.y == 540:
        vy = jump_vel
        cocuk3.image = "cocukzip3"

    
    if vy != 0 or cocuk3.y < 540:
        cocuk3.y += vy
        vy += gravity
        if cocuk3.y >= 540:
            cocuk3.y = 540
            vy = 0

    if kotu2.x > -20:
        kotu2.x -= 2
    else:
        kotu2.x = 1100 
    if sahne_2 == True:
        if kotu2.x > -20:
            kotu2.x -= 1
        else:
            kotu2.x = 1100 

    
    if sahne_3 == True:
        if kotu2.x > -20:
            kotu2.x -= 1
        else:
            kotu2.x = 1100
    
        
    if kotu2.x > -20:
        kotu2.x = kotu2.x - 2        
    if sahne_2 == True:
        if keyboard.right and cocuk3.x < 1150: 
            cocuk3.x +=  6
            cocuk3.image = 'cocuksağ3'
        elif keyboard.left and cocuk3.x > 10:
            cocuk3.x -= 6
            cocuk3.image = 'cocuksol3'

    if sahne_3 == True:
        if keyboard.right and cocuk3.x < 1150:
            cocuk3.x += 6
            cocuk3.image = 'cocuksağ3'
        elif keyboard.left and cocuk3.x >10 :
            cocuk3.x -= 6
            cocuk3.image = 'cocuksol3' 

    if son_sahne == True:
        kotu_1 = False
        game_over = False
        GO = False
        if keyboard.right and cocuk3.x <1150:
            cocuk3.x += 4
            cocuk3.image = 'cocuksağ3'
        elif keyboard.left and cocuk3.x >10 :
            cocuk3.x -= 4
            cocuk3.image = 'cocuksol3' 
        if keyboard.up and cocuk3.y == 540 :
            vy = jump_vel
            cocuk3.image = "cocukzip3"
        
        
            
    
pgzrun.go()