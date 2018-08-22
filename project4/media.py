###################################################################################
# this is the parent class of entertainment_center or the specific film instances #
###################################################################################

# import webbrowser to view films in webbrowser

import webbrowser

class Film ():

	"""film is the parent class which will serve as the framework for each video instance"""

# need to initialize data, create self instances in addition to specifications of each video
# which serve as details to provide a robust description of each film. there are called 
# arguements 

	def __init__(self, title, length, rating):
		self.title=title
		self.length=length
		self.rating=rating

# this will print the information in each specification or instance mentioned above

	def info(self):
		print("Title : "+self.title)
		print("Length : "+self.length)
		print("Rating : "+self.rating)

    """creating child class which will allow specific instances to be referenced"""

class Video(Film):

# the child class is Video pointing to parent which is film
# inputs / arguements include video_description, video_category,
# video_director, video_image, video_trailer + instance variables
# the children or Video class is inheriting title, length and rating from parent

	def __init__(self,title,length,rating,video_description,video_category,video_director,video_image,video_trailer):
		Film.__init__(self,title,length,rating)
		self.description=video_description
		self.category=video_category
		self.director=video_director
		self.image=video_image
		self.trailer=video_trailer

# info method called above is leveraging a class method
# if info is called by Video class it will show all info
# associated with Video class which will override other arguments

	def info(self):
    """printing information of child class"""
		print("Title : "+self.title)
		print("Length : "+self.length)
		print("Rating : "+self.rating)
		print("Description : "+self.description)
		print("Category : "+self.category)
		print("Director : "+self.director)
		print("Image : "+self.image)
		print("Trailer : "+self.trailer)

# need to call out image and trailer seperately below

# present_image will show image of video
	def present_image(self):
    """taking video class and showing associated image for video"""
		webbrowser.open(self.image.url)

# present_trailer will show trailer
	def present_trailer(self):
    """taking video class and showing assocaited trailer for video"""
		webbrowser.open(self.trailer.url)
