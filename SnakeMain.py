 
import pygame  
import time
import random
pygame.init()  
empty = (225,225,225)
gray = (201,201,201)
red = "#A91B0D"
blue = "#8080FF"
turquoise = (64, 204, 228)
screen = pygame.display.set_mode((661, 661))  
pygame.display.set_caption('Snake game')
screen.fill(empty)
pygame.display.flip()
done = False  
nombre_de_carres = 5
coordonnes_left_right = 0
coordonnes_up_down = 0
direction = ''
Dcitionnaire_carres = {1 : [200,180], 2 : [200,180], 3 : [200,180], 4 : [200,180], 5 : [200,180]}
Position_fruit = [random.randint(0,32)*20, random.randint(0,32)*20]


## cadrillage
def quadrillage():
	for i in range(1, 100):
		global coordonnes_left_right, coordonnes_up_down
		pygame.draw.rect(screen,gray,pygame.Rect(coordonnes_left_right, coordonnes_up_down, 1, 1000))
		coordonnes_left_right += 20
		pygame.display.flip()
	coordonnes_left_right = 0
	coordonnes_up_down = 0
	for i in range (1,100):
		pygame.draw.rect(screen,gray,pygame.Rect(coordonnes_left_right, coordonnes_up_down, 1000, 1))
		coordonnes_up_down += 20
		pygame.display.flip()
quadrillage()
screen_quadrille = screen.copy()
nb_fois_boucle = 0

while not done:  
	nb_fois_boucle += 1
	coordonnes_left_right = 100
	compteur = -1
	coordonnes_left_right = 100
	coordonnes_up_down = 100

	##Faire apparaitre le pointage
	police = pygame.font.Font(None,50)
	texte = police.render("Nombre de point(s) : {0}".format(nombre_de_carres-5),True,pygame.Color(turquoise))
	screen.blit(texte, (30, 0))

	##faire apparaitre le fruit
	pygame.draw.rect(screen,red,pygame.Rect(Position_fruit[0], Position_fruit[1], 19, 19))

	##update les positions
	compteur = len(Dcitionnaire_carres.values())
	for i in range(1,len(Dcitionnaire_carres.values())):
		Dcitionnaire_carres[compteur][0] = Dcitionnaire_carres[compteur-1][0]
		compteur -= 1

	compteur = len(Dcitionnaire_carres.values())
	for i in range(1,len(Dcitionnaire_carres.values())):
		Dcitionnaire_carres[compteur][1] = Dcitionnaire_carres[compteur-1][1]
		compteur -= 1

	##update la position du carre 1
	pygame.event.pump()
	events = pygame.event.get()
	for event in events:
		## quitter le jeu
		if event.type == pygame.QUIT:  
			done = True  

		##touches pressees
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				direction = 'down'
				#break
			elif event.key == pygame.K_DOWN:
				direction = 'up'
				#break
			elif event.key == pygame.K_LEFT:
				direction = 'left'
				#break
			elif event.key == pygame.K_RIGHT:
				direction = 'right'
			elif event.key == pygame.K_Z:
				done = True
				#break
	if direction == 'up':
		Dcitionnaire_carres[1][1] += 20
	elif direction == 'down':
		Dcitionnaire_carres[1][1] -= 20
	elif direction == 'left':
		Dcitionnaire_carres[1][0] -= 20
	elif direction == 'right':
		Dcitionnaire_carres[1][0] += 20

	##dessiner selon les positions du dictionnaire
	for i in range(1, len(Dcitionnaire_carres.values())+1):
		pygame.draw.rect(screen,blue,pygame.Rect(list(Dcitionnaire_carres.values())[compteur][0], list(Dcitionnaire_carres.values())[compteur][1], 20, 20))
		compteur -=1
	pygame.display.flip()

	##regarder si en dehors de l'ecran
	##coordonees x
	a = Dcitionnaire_carres[1][0]
	if a < 0 or a > 660:
		##image.blit(screen, (100,100))
		##pygame.display.flip()
		##time.sleep(20)
		done = True
	compteur = 0

	##coordonees y
	b = Dcitionnaire_carres[1][1]
	if b > 660 or b < 0:
		##image.blit(screen, (100,100))
		##pygame.display.flip()
		done = True

	##regarder si meme positions 
	compteur = 2
	for i in range(1, len(Dcitionnaire_carres.values())-1):
		if list(Dcitionnaire_carres.values())[compteur][0] == Dcitionnaire_carres[1][0] and list(Dcitionnaire_carres.values())[compteur][1] == Dcitionnaire_carres[1][1]:
			if nb_fois_boucle > 40:
				##image.blit(screen, (100,100))
				##pygame.display.flip()
				##time.sleep(20)
				done = True
		compteur += 1

	##regarder si meme position que le fruit
	if Position_fruit[0] == Dcitionnaire_carres[1][0] and Position_fruit[1] == Dcitionnaire_carres[1][1]:
		Position_fruit = [random.randint(0,20)*20, random.randint(0,18)*20]

		##augmenter le nombre de carres
		Dcitionnaire_carres[nombre_de_carres] = [100,100]
		nombre_de_carres += 1


	time.sleep(0.05)
	##re-clear l'ecran
	screen.fill(empty)
	screen.blit(screen_quadrille, (0,0))



