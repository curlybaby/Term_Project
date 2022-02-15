import numpy as np
import time
import random
from queue import PriorityQueue
from skimage import io
class hepsi1:
	'''
	This is the random player used in the colab example.
	Edit this file properly to turn it into your submission or generate a similar file that has the same minimal class structure.
	You have to replace the name of the class (ME461Group) with one of the following (exactly as given below) to match your group name
		atlas
		backspacex
		ducati
		hepsi1
		mechrix
		meturoam
		nebula
		ohmygroup
		tulumba
	After you edit this class, save it as groupname.py where groupname again is exactly one of the above
	'''

	def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
		self.name = userName # your object will be given a user name, i.e. your group name
		self.maxStep = maxStepSize # maximum length of the returned path from run()
		self.maxTime = maxTime # run() is supposed to return before maxTime
		colorz = {
			'black':((1,1,1), 0, 13),
			'clr100':((225, 1, 1), 100, 1),
			'clr50':((1, 255, 1), 50, 2), 
			'clr30':((1, 1, 255), 30, 2),
			'clr20':((200, 200, 1), 20, 2),
			'clr10':((255, 1, 255), 10, 2), 
			'clr9':((1, 255, 255), 9, 3),
			'clr8':((1,1,150), 8, 3),
			'clr7':((120,120,40), 7, 3),
			'clr6':((150,1,150), 6, 3),
			'clr5':((1,150,150), 5, 3),
			'clr4':((222,55,222), 4, 3),
			'clr3':((1, 99, 55), 3, 3),
			'clr2':((200, 100, 10),2, 3),
			'clr1':((100, 10, 200),1, 3)
		}
		self.clrDictionary = colorz
		
	def run(self, img, info):
		myinfo = info[self.name]
		imS = img.shape[0] # assume square image and get size
		# get current location
		loc, game_point = list(info[self.name][0]),info[self.name][1]
		def bestOption(loc,img):
			whereami=list(loc)

			def findNeighbor(loc,stepsize):
				(y,x) = loc
				neighArr = [(y+stepsize, x), (y-stepsize, x), (y, x-stepsize), (y,x+stepsize)] #calculate the 4-neighbors
				return neighArr

			pointdic = {} #initialize the dictionary to store the points
			centerpoints = [[675, 675], [675, 575], [675, 475], [675, 375], [675, 275], [675, 175], [675, 75], [575, 675], [575, 575], [575, 475], [575, 375], [575, 275], [575, 175], [575, 75], [475, 675], [475, 575], [475, 475], [475, 375], [475, 275], [475, 175], [475, 75], [375, 675], [375, 575], [375, 475], [375, 375], [375, 275], [375, 175], [375, 75], [275, 675], [275, 575], [275, 475], [275, 375], [275, 275], [275, 175], [275, 75], [175, 675], [175, 575], [175, 475], [175, 375], [175, 275], [175, 175], [175, 75], [75, 675], [75, 575], [75, 475], [75, 375], [75, 275], [75, 175], [75, 75]]
			pickme = PriorityQueue() #initialize the empty priority queue to sort the options
			for k,m in enumerate(centerpoints):
				for key in self.clrDictionary: #we should iterate each key of the dictionary to match colors of the maze with corresponding points
					if np.array_equal(img[m[0],m[1],:],np.array(self.clrDictionary[key][0])): #check if the colors match
						pointdic[tuple(m)] = self.clrDictionary[key][1] #if the colors match, put the corresponding point from the key to the center dictionary
			initLocs = [[25, 175],[25, 375],[25, 575],[175, 25],[375, 25],[575, 25],[175, 725],[375, 725],[575, 725]]
			if whereami in initLocs:
				neighAr=findNeighbor(whereami,50)
				for i,j in enumerate(neighAr):
					if j in pointdic:
						goal=[j[0],j[1]]
			else:
				#adjust loc to center point later
				#egemennnn aklın bı sey geldi xd
				#0ın altına düşmemeliyiz !!
				neighAr1=findNeighbor(whereami,100)
				for a,b in enumerate(neighAr1):
					sum=0
					if b in pointdic:
						sum=0
						neighAr2=findNeighbor(b,100)
						sum= sum + 4*pointdic[b]
						for k,t in enumerate(neighAr2):
							if t in pointdic:
								sum=sum+ 2*pointdic[t]
								neighAr3=findNeighbor(t,100)
								for l,m in enumerate(neighAr3):
									if m in pointdic:
										sum=sum+ 1.5*pointdic[m]
						if game_point-pointdic[b] >= 0:
							pickme.put((-sum,b))
						if game_point-pointdic[b] <= 0 and pointdic[b]!=0:
							pickme.put((sum,b))
							

				goal = pickme.get()[1]
			return goal

		goal = list(bestOption(loc,img))

		def pathfinder(loc,goal):
			x= goal[1]-loc[1]
			y= goal[0]-loc[0]
			i=0
			path= []
			if x>0:
				i=0
				while i<=x:
					path.append([loc[0], loc[1]+i])
					i=i+1
			elif x<0:
				while i<=-x:
					path.append([loc[0], loc[1]-i])
					i=i+1
			elif y>0:
				i=0
				while i<=y:
					path.append([loc[0]+i, loc[1]])
					i=i+1
			elif y<0:
				while i<=-y:
					path.append([loc[0]-i, loc[1]])
					i=i+1
			return path
		path = pathfinder(list(loc),goal)
		print(path)
		return [goal]
 
