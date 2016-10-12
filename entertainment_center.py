import media

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
                     
theMatrix = media.Movie("The Matrix",
                        "A programmer turn super human to uncover the secrets of the matrix.",
                        "http://www.imdb.com/title/tt0133093/mediaviewer/rm2882537984",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y8")
                        
#print(avatar.storyline)
#avatar.show_trailer()
theMatrix.show_trailer()