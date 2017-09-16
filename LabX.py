#-*- encoding: UTF-8-*-

class MusicTitle(object):
	

	def __init__(self):
		self.__title = "sem nome"
		self.__artist = "sem nome"

	def set_title(self, title):
        	self.__title = title
        
    	def get_title(self):
        	return self.__title
		
	def set_artist(self, artist):
        	self.__artist = artist
        
    	def get_artist(self):
        	return self.__artist
	
	def __repr__(self):
		return "Título: " + self.__title + "\nArtista: " + self.__artist

	artist = property(fget=get_artist, fset=set_artist)

	title = property(fget=get_title, fset=set_title)
	
