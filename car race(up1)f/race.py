import pgzrun
import os
import time
#................................
TITLE = 'race game'
WIDTH = 610
HEIGHT = 599
#HIGHT = 417
os.environ["SDL_VIDEO_CENTERED"] = '1'
#................................
#--game-picture--
gameMap = Actor("back")
#gameMapE = Actor("errorr")
icons = Actor("icons",(320,520))
car1 = Actor("car1",(348,332))
car2 = Actor("car2",(368,344))
start = Actor("start")
menu1 = Actor("menu",(260,50))
menu2 = Actor("menu",(580,40))
menuWindow = Actor("mw",(307,207))
exit = Actor("exit",(225,210))
continuep = Actor("continue",(380,210))
menuWindow1 = Actor("mw",(307,207))
continuep1 = Actor("continue",(225,210))
about = Actor("aboutt",(380,210))
aboutB = Actor("about",(300,300))
exit1 = Actor("exit",(310,400))
#--game-performance----
wheel = Actor("wheel",(331,163))
#end = Actor("end",(250,332))
#--help & loading-picture--
car1H = Actor("car1h",(75,75))
ku = Actor("ku",(223,28))
kd = Actor("kd",(223,70))
kl = Actor("kl",(180,70))
kr = Actor("kr",(266,70))
car2H = Actor("car2h",(50,225))
kw = Actor("kw",(145,245))
ks = Actor("ks",(145,277))
ka = Actor("ka",(113,277))
kdd = Actor("kdd",(177,277))
help1 = Actor("bala",(358,340))
help2 = Actor("turn1",(380,62))
help3 = Actor("turn2",(530,62))
help4 = Actor("turn3",(530,140))
help5 = Actor("turn4",(275,165))
help6 = Actor("turn4",(70,365))
help7 = Actor("turn5",(70,530))
#--point--picture-----
pointPic1 = Actor("point",(457,169))
pointPic2 = Actor("point",(427,134))
pointPic3 = Actor("point",(458,62))
pointPic4 = Actor("point",(501,25))
pointPic5 = Actor("point",(267,139))
pointPic6 = Actor("point",(244,170))
pointPic7 = Actor("point",(272,286))
pointPic8 = Actor("point",(241,394))
pointPic9 = Actor("point",(170,396))
pointPic10 = Actor("point",(91,360))
pointPic11 = Actor("point",(310,568))
pointPic12 = Actor("point",(132,540))
#----------------

gameMenu = False #----------
openMenu1 = False
openMenu2 = False
menuTab = False
loadingTab = False
car1Score = 0 #yellow
car2Score = 0 #white
#--performance-bool--
accessCar1 = False
accessCar2 = False
accessMove = False
Gperformanc = False
startShow = False
anglePlus1 = False
anglePlus2 = False
anglePlus3 = False
accessS = False
#--point--bool----
car11 = True
car12 = True
car13 = True
car14 = True
car15 = True
car16 = True
car17 = True
car18 = True
car19 = True
car110 = True
car111 = True
car112 = True
#--point--bool----
car21 = True
car22 = True
car23 = True
car24 = True
car25 = True
car26 = True
car27 = True
car28 = True
car29 = True
car210 = True
car211 = True
car212 = True
#.................
def draw():
    global accessS , gameMenu , accessMove , startShow , openMenu1 , openMenu2 , menuTab , loadingTab , Gperformanc , accessCar1 ,accessCar2 ,anglePlus1,anglePlus2,anglePlus3
#--lobby
    screen.clear()
    start.draw()
    icons.draw()
    menu2.draw()
#--lobby-menu
    if openMenu2 == True : 
        menuWindow1.draw()
        continuep1.draw()
        about.draw()
#--about-window
    if menuTab == True :  
        aboutB.draw()
        screen.draw.text("This racing game is completely made \n with Python programming language",(50,210),fontsize = 40 ,color = "red")
        screen.draw.text("Made by Python Master programming team",(50,300),fontsize = 35 ,color = "blue")
        exit1.draw()
#--loading-window
    if loadingTab == True :
        screen.clear()
        gameMap.draw()
        car1H.draw()
        screen.draw.text("Control the yellow car",(12,20),fontsize = 25 ,color = "yellow")
        ku.draw()
        kd.draw()
        kl.draw()
        kr.draw()
        screen.draw.text("_________",(0,100),fontsize = 60 ,color = "black")
        car2H.draw()
        screen.draw.text("Control the white car",(25,183),fontsize = 25 ,color = "white")
        kw.draw()
        ks.draw()
        ka.draw()
        kdd.draw()
#--
        help1.draw()
        help2.draw()
        help3.draw()
        help4.draw()
        help5.draw()
        help6.draw()
        help7.draw()
#--
        if 0 <= car1H.angle <= 70 or 280 <= car1H.angle <= 350 or 560 <= car1H.angle <= 630 or 840 <= car1H.angle <= 910 or 1120 <= car1H.angle <= 1190 :
            screen.draw.text("loading . . .",(415,540),fontsize = 50 ,color = "black")
        if 70 <= car1H.angle <= 140 or 350 <= car1H.angle <= 420 or 630 <= car1H.angle <= 700 or 910 <= car1H.angle <= 980 or 1190 <= car1H.angle <= 1260 :
            screen.draw.text("loading   . .",(415,540),fontsize = 50 ,color = "black")
        if 140 <= car1H.angle <= 210 or 420 <= car1H.angle <= 490 or 700 <= car1H.angle <= 770 or 980 <= car1H.angle <= 1050 or 1260 <= car1H.angle <= 1330 :
            screen.draw.text("loading .   .",(415,540),fontsize = 50 ,color = "black")
        if 210 <= car1H.angle <= 280 or 490 <= car1H.angle <= 560 or 770 <= car1H.angle <= 840 or 1050 <= car1H.angle <= 1120 or 1330 <= car1H.angle <= 1400 :
            screen.draw.text("loading . .  ",(415,540),fontsize = 50 ,color = "black")        
#--game-Window
    if gameMenu == True :
        #Gperformanc = True
        screen.clear()
        gameMap.draw()
        #end.draw()
        pointPic1.draw()
        pointPic2.draw()
        pointPic3.draw()
        pointPic4.draw()
        pointPic5.draw()
        pointPic6.draw()
        pointPic7.draw()
        pointPic8.draw()
        pointPic9.draw()
        pointPic10.draw()
        pointPic11.draw()
        pointPic12.draw()
        car1.draw()
        car2.draw()
        screen.draw.text("white car",(15,15),fontsize = 55 ,color = "white")
        screen.draw.text(f"score : {car2Score}",(50,55),fontsize = 35 ,color = "white")
        screen.draw.text("_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_",(205,0),fontsize = 3 ,color = "black")
        screen.draw.text("_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_\n_",(205,-2),fontsize = 3 ,color = "black")
        screen.draw.text("yellow car",(415,215),fontsize = 55 ,color = "yellow")
        screen.draw.text(f"score : {car1Score}",(466,255),fontsize = 35 ,color = "yellow")
        menu1.draw()
    if Gperformanc == True :
#--start-game & performance--
        screen.draw.text("Go ",(253,123),fontsize = 105 ,color = "darkBlue")
        wheel.draw()
        if 4199 >= wheel.angle >= 100 :
            screen.draw.text("1",(350,123),fontsize = 110 ,color = "gold") 
            anglePlus1 = True
        if 8999 >= wheel.angle >= 4200 :
            screen.draw.text("2",(350,123),fontsize = 110 ,color = "gold") 
            anglePlus2 = True
        if 16999 >= wheel.angle >= 9000 :
            screen.draw.text("3",(350,123),fontsize = 110 ,color = "gold")
            anglePlus3 = True
        if 21999 >= wheel.angle >= 17000 :
            screen.draw.text("Go",(350,123),fontsize = 110 ,color = "gold")
        if 23000 >= wheel.angle >= 22000 :
            screen.draw.text("Go",(350,123),fontsize = 110 ,color = "gold")
        
            accessS = True
#--performance-left-side
        screen.draw.text("white car : ",(15,120),fontsize = 32 ,color = "white")
        if accessCar2 == False :
            screen.draw.text("Rady",(135,120),fontsize = 32 ,color = "red")
        if accessCar2 == True :
            screen.draw.text("Rady",(135,120),fontsize = 32 ,color = "darkgreen")
        screen.draw.text("if you are rady press 'TAB' key",(8,150),fontsize = 20 ,color = "white")
#--performance-right-side
        screen.draw.text("yellow car",(415,215),fontsize = 55 ,color = "yellow")
        screen.draw.text(f"score : {car1Score}",(466,255),fontsize = 35 ,color = "yellow")
        screen.draw.text("yellow car : ",(420,320),fontsize = 32 ,color = "yellow")
        if accessCar1 == False :
            screen.draw.text("Rady",(545,320),fontsize = 32 ,color = "red")      
        if accessCar1 == True :
            screen.draw.text("Rady",(545,320),fontsize = 32 ,color = "darkgreen")
        screen.draw.text("if you are rady press 'SPACE' key",(412,348),fontsize = 18 ,color = "yellow")

#--game-menu
    if openMenu1 == True :
        menuWindow.draw()
        exit.draw()
        continuep.draw()
#................
def update():
    global accessS,startShow,Gperformanc,accessMove,accessCar1,accessCar2,loadingTab,anglePlus1,anglePlus2,anglePlus3, gameMenu , car1Score , car2Score ,car11,car12,car13,car14,car15,car16,car17,car18,car19,car110,car111,car112,  car21,car22,car23,car24,car25,car26,car27,car28,car29,car210,car211,car212
#--car1H & car2H-show
    if loadingTab == True :
        car1H.angle += 4
        car2H.angle += 4
        if car1H.angle == 1400 :
            gameMenu = True
            loadingTab = False
            Gperformanc = True
#--game-performance-
    if Gperformanc == True :
        if keyboard.SPACE :
                accessCar1 = True
        if keyboard.TAB :
                accessCar2 = True
    if accessCar2 == True and accessCar1 == True :
        startShow = True
    if startShow == True :
        wheel.angle += 30
        if anglePlus1 == True :
            wheel.angle += 15
        if anglePlus2 == True :
            wheel.angle += 30
            anglePlus1 = False
        if anglePlus3 == True :
            wheel.angle += 31 
            anglePlus2 = False
    #if wheel.angle == 22000 :
        #accessS = True
    if accessS == True : 
            Gperformanc = False
            startShow = False
            accessMove = True
#--car1-move
    if accessMove == True :
        if keyboard.up :
            car1.y -= 2
            car1.angle = 0
        if keyboard.down :
            car1.y += 2
            car1.angle = 180
        if keyboard.left :
            car1.x -= 2
            car1.angle = 90
        if keyboard.right :
            car1.x += 2
            car1.angle = 270
        if keyboard.up and keyboard.left :
            car1.angle = 45
        if keyboard.up and keyboard.right :  
            car1.angle = -45 
        if keyboard.down and keyboard.left :  
            car1.angle = 135
        if keyboard.down and keyboard.right :   
            car1.angle = 225  
#--car2-move
        if keyboard.w :
            car2.y -= 2
            car2.angle = 0
        if keyboard.s :
            car2.y += 2
            car2.angle = 180
        if keyboard.a :
            car2.x -= 2
            car2.angle = 90
        if keyboard.d :
            car2.x += 2
            car2.angle = 270
        if keyboard.w and keyboard.a :
            car2.angle = 45
        if keyboard.w and keyboard.d :  
            car2.angle = -45 
        if keyboard.s and keyboard.a :  
            car2.angle = 135
        if keyboard.s and keyboard.d :   
            car2.angle = 225
#--car 1--point
    if car1.colliderect(pointPic1) and car11==True :
        car1Score += 2
        car11 = False
    if car1.colliderect(pointPic2) and car12==True :
        car1Score += 2
        car12 = False
    if car1.colliderect(pointPic3) and car13==True :
        car1Score += 2
        car13 = False
    if car1.colliderect(pointPic4) and car14==True :
        car1Score += 2
        car14 = False
    if car1.colliderect(pointPic5) and car15==True :
        car1Score += 2
        car15 = False
    if car1.colliderect(pointPic6) and car16==True :
        car1Score += 2
        car16 = False
    if car1.colliderect(pointPic7) and car17==True :
        car1Score += 2
        car17 = False
    if car1.colliderect(pointPic8) and car18==True :
        car1Score += 2
        car18 = False
    if car1.colliderect(pointPic9) and car19==True :
        car1Score += 2
        car19 = False
    if car1.colliderect(pointPic10) and car110==True :
        car1Score += 2
        car110 = False
    if car1.colliderect(pointPic11) and car111==True :
        car1Score += 2
        car111 = False
    if car1.colliderect(pointPic12) and car112==True :
        car1Score += 2
        car112 = False
#--car 2--point
    if car2.colliderect(pointPic1) and car21==True :
        car2Score += 2
        car21 = False
    if car2.colliderect(pointPic2) and car22==True :
        car2Score += 2
        car22 = False
    if car2.colliderect(pointPic3) and car23==True :
        car2Score += 2
        car23 = False
    if car2.colliderect(pointPic4) and car24==True :
        car2Score += 2
        car24 = False
    if car2.colliderect(pointPic5) and car25==True :
        car2Score += 2
        car25 = False
    if car2.colliderect(pointPic6) and car26==True :
        car2Score += 2
        car26 = False
    if car2.colliderect(pointPic7) and car27==True :
        car2Score += 2
        car27 = False
    if car2.colliderect(pointPic8) and car28==True :
        car2Score += 2
        car28 = False
    if car2.colliderect(pointPic9) and car29==True :
        car2Score += 2
        car29 = False
    if car2.colliderect(pointPic10) and car210==True :
        car2Score += 2
        car210 = False
    if car2.colliderect(pointPic11) and car211==True :
        car2Score += 2
        car211 = False
    if car2.colliderect(pointPic12) and car212==True :
        car2Score += 2
        car212 = False  
#--crash-car1-
    if car1.x >= 593 :
        car1.x = 593
    if car1.x <= 17 :
        car1.x = 17
    if car1.y >= 580 :
        car1.y = 580
    if car1.y <= 18 :
        car1.y = 18
#--
    if car1.x >= 390 and car1.y >= 185 :
        car1.x = 390
    if car1.x >= 391 and car1.y >= 180 :
        car1.y = 180
#--
    if car1.x <= 325 and car1.y <= 114 :
        car1.x = 325
    if car1.x <= 324 and car1.y <= 120 :
        car1.y = 120
#--
    if car1.x <= 225 and car1.y <= 314 :
        car1.x = 225
    if car1.x <= 222 and car1.y <= 320 :
        car1.y = 320
#-------
    if 397 <= car1.x <= 525 :
        if 79 <= car1.y <= 100 :
            car1.y = 79
        if 100 <= car1.y <= 120 :
            car1.y = 120    
#--
    if 95 <= car1.y <= 105 :
        if 389 <= car1.x <= 470 :
            car1.x = 389
        if 470 <= car1.x <= 535 :
            car1.x = 535
#--
    if 89 <= car1.x <= 318 :
        if 479 <= car1.y <= 495 :
            car1.y = 479
        if 500 <= car1.y <= 521 :
            car1.y = 521 
#--
    if 187 <= car1.y <= 513 :
        if 288 <= car1.x <= 301 :
            car1.x = 288
        if 301 <= car1.x <= 327 :
            car1.x = 327
#--
    if 386 <= car1.y <= 513 :
        if 83 <= car1.x <= 90 :
            car1.x = 83
        if 90 <= car1.x <= 123 :
            car1.x = 123
#-- 
    if 302 <= car1.x <= 311 :
        if 179 <= car1.y <= 200 :
           car1.y = 179
#--
    if 97 <= car1.x <= 106 :
        if 379 <= car1.y <= 400 :
           car1.y = 379
#--
    if 290 <= car1.y <= 414 :
        if 186 <= car1.x <= 200 :
            car1.x = 186
        if 200 <= car1.x <= 225 :
            car1.x = 225
#--
    if 200 <= car1.x <= 208 :
        if 370 <= car1.y <= 421 :
           car1.y = 421
#--crash-car2-

    if car2.x >= 593 :
        car2.x = 593
    if car2.x <= 17 :
        car2.x = 17
    if car2.y >= 580 :
        car2.y = 580
    if car2.y <= 18 :
        car2.y = 18
#--
    if car2.x >= 390 and car2.y >= 185 :
        car2.x = 390
    if car2.x >= 391 and car2.y >= 180 :
        car2.y = 180
#--
    if car2.x <= 325 and car2.y <= 114 :
        car2.x = 325
    if car2.x <= 324 and car2.y <= 120 :
        car2.y = 120
#--
    if car2.x <= 223 and car2.y <= 314 :
        car2.x = 223
    if car2.x <= 222 and car2.y <= 320 :
        car2.y = 320
#-------
    if 397 <= car2.x <= 525 :
        if 79 <= car2.y <= 100 :
            car2.y = 79
        if 100 <= car2.y <= 120 :
            car2.y = 120    
#--
    if 95 <= car2.y <= 105 :
        if 389 <= car2.x <= 470 :
            car2.x = 389
        if 470 <= car2.x <= 535 :
            car2.x = 535
#--
    if 89 <= car2.x <= 318 :
        if 479 <= car2.y <= 495 :
            car2.y = 479
        if 500 <= car2.y <= 521 :
            car2.y = 521 
#--
    if 187 <= car2.y <= 513 :
        if 288 <= car2.x <= 301 :
            car2.x = 288
        if 301 <= car2.x <= 327 :
            car2.x = 327
#--
    if 386 <= car2.y <= 513 :
        if 83 <= car2.x <= 90 :
            car2.x = 83
        if 90 <= car2.x <= 123 :
            car2.x = 123
#-- 
    if 302 <= car2.x <= 311 :
        if 179 <= car2.y <= 200 :
           car2.y = 179
#--
    if 97 <= car2.x <= 106 :
        if 379 <= car2.y <= 400 :
           car2.y = 379
#--
    if 290 <= car2.y <= 414 :
        if 186 <= car2.x <= 200 :
            car2.x = 186
        if 200 <= car2.x <= 225 :
            car2.x = 225
#--
    if 200 <= car2.x <= 208 :
        if 370 <= car2.y <= 421 :
           car2.y = 421
#..............
def on_mouse_down(pos,button) :
    global gameMenu , openMenu1 , openMenu2 , menuTab , loadingTab , gameMap
#--start-key
    if icons.collidepoint(pos) and button == mouse.LEFT :
        if openMenu2 == False and menuTab == False :
            sounds.click.play()
            loadingTab = True
#--game-menu-key
    if menu1.collidepoint(pos) and button == mouse.LEFT :
        if gameMap == True :
            sounds.click.play()
            openMenu1 = True
#--exit-game-key
    if exit.collidepoint(pos) and button == mouse.LEFT :
        if openMenu1 == True :
            sounds.click.play()
            gameMenu = False
            openMenu1 = False
#--game-continue-key
    if continuep.collidepoint(pos) and button == mouse.LEFT :
        sounds.click.play()
        openMenu1 = False
#--lobby-menu-key
    if menu2.collidepoint(pos) and button == mouse.LEFT :
        if gameMap == False and loadingTab == False :
            sounds.click.play()
            openMenu2 = True
#--lobby-continue-key
    if continuep1.collidepoint(pos) and button == mouse.LEFT :
        sounds.click.play()
        openMenu2 = False
#--about-key
    if about.collidepoint(pos) and button == mouse.LEFT :
        if openMenu2 == True :
            sounds.click.play()
            menuTab = True
            openMenu2 = False
#--exit-about-key
    if exit1.collidepoint(pos) and button == mouse.LEFT :
        sounds.click.play()
        menuTab = False
    

    print(pos)
pgzrun.go()
