#imports

import pygame
import time
import random

#inits

screen_width = 600
screen_height = 400

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)
pygame.display.update()

#variables

running = True
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

#classes

class Head:
	x=0
	y=0
	direction = "right"
	points = 0
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.direction = "right"
		self.points = 0
	def render(self):
		pygame.draw.rect(window, red, pygame.Rect(self.x,self.y,20,20))
	def walk(self):
		if  self.direction == "right":
			self.setX(self.getX()+20)
		elif self.direction == "left":
			self.setX(self.getX()-20)
		elif self.direction == "up":
			self.setY(self.getY()-20)
		elif self.direction == "down":
			self.setY(self.getY()+20)
		if(self.x < 0):
			self.setX(screen_width-20)
		elif(self.x >screen_width-20):
			self.setX(0)
		if(self.y < 0):
			self.setY(screen_height-20)
		elif(self.y > screen_height-20):
			self.setY(0)
		for seg in tail:
			if self.getX() == seg.getX() and self.getY() == seg.getY():
				gameover()

	#getters x setter
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def setX(self,newx):
		self.x = newx
	def setY(self,newy):
		self.y = newy
	def setDir(self,newDir):
		if self.direction == "right" and newDir != "left":
			self.direction = newDir
		if self.direction == "up" and newDir != "down":
			self.direction = newDir
		if self.direction == "left" and newDir != "right":
			self.direction = newDir
		if self.direction == "down" and newDir != "up":
			self.direction = newDir
class Segment:
	x=0
	y=0
	pattern = None
	def __init__(self,x,y,pattern):
		self.x = x
		self.y = y
		self.pattern = pattern
	def render(self):
		pygame.draw.rect(window, blue, pygame.Rect(self.x,self.y,20,20))

	def follow(self):
		self.setX(self.pattern.getX())
		self.setY(self.pattern.getY())

	#getters x setters
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def setX(self,newx):
		self.x = newx
	def setY(self,newy):
		self.y = newy

class Fruit:
	x=0
	y=0
	def __init__(self):
		init = False
		while not init:
			self.x = random.randint(0,(screen_width-20)/20)*20
			self.y = random.randint(0,(screen_height-20)/20)*20
			isfree = True
			for seg in tail:
				if self.x == seg.getX() and self.y == seg.getY():
					isfree = False
			if(isfree):
				init = True
			else:
				break

	def tick(self):
		for seg in tail:
			if self.x == seg.getX() and self.y == seg.getY():
				newsegment = Segment(tail[len(tail)-1].getX(),tail[len(tail)-1].getY(),tail[len(tail)-1])
				addPoints(1)
				tail.append(newsegment)
				init = False
				while not init:
					self.x = random.randint(0,(screen_width-20)/20)*20
					self.y = random.randint(0,(screen_height-20)/20)*20
					isfree = True
					for seg in tail:
						if self.x == seg.getX() and self.y == seg.getY():
							isfree = False
					if(isfree):
						init = True
					else:
						break
	def render(self):
		pygame.draw.rect(window, green, pygame.Rect(self.x,self.y,20,20))

	#getters setter bla bla bla
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def setX(self,newx):
		self.x = newx
	def setY(self,newy):
		self.y = newy

#instances

def addPoints(pointsAdd):
	head.points+=1

def gameover():
	quit()

tail = []
head = Head(20,20)
segment = Segment(10,20,head)
tail.append(segment)

fruit = Fruit()

#gameloop
while running:
	pygame.draw.rect(window, white, pygame.Rect(0,0,screen_width,screen_height))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				head.setDir("up")
			elif event.key == pygame.K_DOWN:
				head.setDir("down")
			elif event.key == pygame.K_RIGHT:
				head.setDir("right")
			elif event.key == pygame.K_LEFT:
				head.setDir("left")
	#tick
	#the secret is the order of updating, the last following the next one :)
	time.sleep(0.1)#10 frames per second
	for seg in reversed(tail):
		seg.follow()
	head.walk()
	fruit.tick()
	#render
	fruit.render()
	for seg in reversed(tail):
		seg.render()
	head.render()
		#score
	score = font.render(str(head.points), True, black)
	window.blit(score,(20,20))
	pygame.display.update()

	#By Ierokirykas