import numpy as np
import random
from queue import PriorityQueue
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

			pointdic = {} #initialize the dictionary to store the points
			
			centerpoints = [[675, 675], [675, 575], [675, 475], [675, 375], [675, 275], [675, 175], [675, 75], [575, 675], [575, 575], [575, 475], [575, 375], [575, 275], [575, 175], [575, 75], [475, 675], [475, 575], [475, 475], [475, 375], [475, 275], [475, 175], [475, 75], [375, 675], [375, 575], [375, 475], [375, 375], [375, 275], [375, 175], [375, 75], [275, 675], [275, 575], [275, 475], [275, 375], [275, 275], [275, 175], [275, 75], [175, 675], [175, 575], [175, 475], [175, 375], [175, 275], [175, 175], [175, 75], [75, 675], [75, 575], [75, 475], [75, 375], [75, 275], [75, 175], [75, 75]]
			
			for k,m in enumerate(centerpoints):
				for key in self.clrDictionary: #we should iterate each key of the dictionary to match colors of the maze with corresponding points
					if np.array_equal(img[m[0],m[1],:],np.array(self.clrDictionary[key][0])): #check if the colors match
						pointdic[tuple(m)] = self.clrDictionary[key][1] #if the colors match, put the corresponding point from the key to the center dictionary
			initLocs = [[25, 175],[25, 375],[25, 575],[175, 25],[375, 25],[575, 25],[175, 725],[375, 725],[575, 725]]
			
			def findNeighbor(firstneighbor,stepsize):
				(y,x) = firstneighbor
				neighArr = [(y+stepsize, x), (y-stepsize, x), (y, x-stepsize), (y,x+stepsize)] #calculate the 4-neighbors
				return neighArr

			def closestSq(loc,center):
				myqueue = PriorityQueue()
				for i,j in enumerate(centerpoints):
					dist = abs(loc[0]-j[0]) + abs(loc[1]-j[1])
					if 0 < dist <= 105:
						myqueue.put((dist,tuple(j)))
				costloc =[]
				for i in range(len(myqueue.queue)):
					costloc.append(myqueue.get())
				return costloc
			
			pickme = PriorityQueue() #silinebilir
			#adjust loc to center point later
			#egemennnn aklın bı sey geldi xd
			#0ın altına düşmemeliyiz !!
			
			firstneighbor = closestSq(whereami,centerpoints)
			flag=0
			for a,b in enumerate(firstneighbor):
				sum=0
				if game_point >= 100:
					flag=1
					sum=0
					neighAr2=findNeighbor(b[1],100)
					sum= sum + 4*pointdic[b[1]]
					for k,t in enumerate(neighAr2):
						if t in pointdic:
							sum=sum+ 2*pointdic[t]
							neighAr3=findNeighbor(t,100)
							for l,m in enumerate(neighAr3):
								if m in pointdic:
									sum=sum+ 1.5*pointdic[m]
					pickme.put((-sum/b[0],b[1]))
				else:
					if game_point - pointdic[b[1]] >= 0:
						flag=1
						if pointdic[b[1]] == 0:
							pickme.put(((random.randint(100,110)),b[1]))
						else:
							pickme.put(((game_point - pointdic[b[1]]),b[1]))
			if flag == 0:
				locList=[[loc[0]+50,loc[1]+50],[loc[0]-50,loc[1]+50],[loc[0]+50,loc[1]-50],[loc[0]-50,loc[1]-50]]
				goal= random.choice(locList)
			else:
				goal= pickme.get()[1]
			return goal
				
				

		goal = list(bestOption(loc,img))
		

		if [goal[0],loc[1]]==[goal[0],goal[1]]:
			return [[goal[0],goal[1]]]
		else:
			return [[goal[0],loc[1]],[goal[0],goal[1]]]
