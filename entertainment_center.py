import website_display #this file is used to generate a website that will take the data from the movies array and display them. It must be in the same folder as this current file
import media #importing code from media.py file that contains the class Movie() which contains the blueprint for creating the trailer website

hobbit_1 = media.Movie("The Hobbit: An Unexpected Journey (2012)",
                        "A reluctant Hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home, and the gold within it from the dragon Smaug.",
                        "https://2.bp.blogspot.com/-V5I_5YjkfE4/UJR2X404iUI/AAAAAAAAOHY/xgvn5gEGveA/s1600/TheHobbitBilboPoster.jpg",
                        "https://www.youtube.com/watch?v=WJULoHnwoRI")

hobbit_2 = media.Movie("The Hobbit: The Desolation of Smaug (2013)",
                     "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.",
                     "https://4.bp.blogspot.com/-n5nNrvfsRC8/Uns-i0reRUI/AAAAAAAARhI/rrYsP4NAFqk/s1600/HobbitTDOSBilboScenePoster.jpg",
                     "https://www.youtube.com/watch?v=OPVWy1tFXuc")

hobbit_3 = media.Movie("The Hobbit: The Battle of the Five Armies (2014)",
                          "Bilbo and company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.",
                          "https://3.bp.blogspot.com/-l5AhORjOdoo/VKC7n3-glTI/AAAAAAAAG3s/irqEXFQPI6c/s1600/Hobbit%2BFive%2BArmies.jpg",
                          "https://www.youtube.com/watch?v=iVAgTiBrrDA")

lotr_1 = media.Movie("The Lord of the Rings: The Fellowship of the Ring (2001)",
                      "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
                      "https://3.bp.blogspot.com/-VWuVhrUsUy0/UXV-V8tC1SI/AAAAAAAAAhY/85bcC6fVxsg/s1600/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_6426d3da.jpg",
                      "https://www.youtube.com/watch?v=V75dMMIW2B4")

lotr_2 = media.Movie("The Lord of the Rings: The Two Towers (2002)",
                      "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",
                      "http://musingsfromus.com/wp-content/uploads/2011/04/The-Lord-of-the-Rings-The-Two-Towers-2002-Poster-Aragorn.jpg",
                      "https://www.youtube.com/watch?v=cvCktPUwkW0")

lotr_3 = media.Movie("The Lord of the Rings: The Return of the King (2003)",
                      "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
                      "https://upload.wikimedia.org/wikipedia/id/thumb/0/0d/EsdlaIII.jpg/220px-EsdlaIII.jpg",
                      "https://www.youtube.com/watch?v=r5X-hFf6Bwo")


movies = [hobbit_1,hobbit_2,hobbit_3,lotr_1,lotr_2,lotr_3] #this array contains the variable which in turn contain the information for the different movies to be displayed on the trailer website

website_display.open_movies_page(movies) #takes in a list or an array of movies

