import webbrowser 

class Movie(): #Google Style Guide for Python suggests that names of classes should start in UpperCase
    """This class provides a way to store movie related information""" #Triple quotes is used to add documentation for the file
    
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube): #defining the init function for class Movie()
        self.title = movie_title #creating an instance variable that will receive the movie title as a string value
        self.storyline = movie_storyline #creating an instance variable that will receive the plot of the movie as a string value
        self.poster_image_url = poster_image #creating an instance variable that will receive the URL of the image file which displays the poster of the movie
        self.trailer_youtube_url = trailer_youtube #creating an instance variable that will receive the URL of movie trailer

    def show_trailer(self): #defining a function to display the trailer video
        webbrowser.open(self.trailer_youtube_url)
