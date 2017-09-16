#-*- encoding: UTF-8-*-
from datetime import datetime
import LabX

now = datetime.now()

class MusicStore(object):
    
    def __init__(self):
        self.__owner = "sem dono"
        self.__openTime = 9
        self.__closeTime = 21
	self.__titles = []
        
    def set_owner(self, owner):
        self.__owner = owner

    def set_openTime(self, openTime):
        self.__openTime = openTime
        
    def set_closeTime(self, closeTime):
        self.__closeTime = closeTime
        
    def get_openTime(self):
        return self.__openTime
        
    def get_closeTime(self):
        return self.__closeTime
    
    def isOpen(self):
        if(self.__openTime >= now.hour and self.__closeTime < now.hour):
            return True
        return False
        
    def get_owner(self):
        return self.__owner
        
    def displayHoursOfOperation(self):
        print("Diariamente das " + str(self.__openTime) + " - " + str(self.__closeTime))

    def getOpenClosedMessage(self):
	if(self.isOpen()):
		print("Loja está aberta")
		return
	print("Loja está fechada")
	
    def addTitles(self, title):
        self.__titles.append(title)
        
    def get_titles(self):
        return self.__titles

    def displayMusicTitles(self):
	for i in range(len(self.__titles)):
		print(self.__titles[i])

class TestMusicStore(object):
    
    if __name__=="__main__":
        c = MusicStore()
        c.getOpenClosedMessage();
        c.owner = "Roberto"
        c.displayHoursOfOperation()
	x = LabX.MusicTitle()
	x.artist = "Ivete Sangalo"
	x.title = "A Festa"
	y = LabX.MusicTitle()
	y.title = "Luna Nueva"
	y.artist = "Diego Torres"
	c.addTitles(x)
	c.addTitles(y)
	c.displayMusicTitles()
	print(c.owner)
        
