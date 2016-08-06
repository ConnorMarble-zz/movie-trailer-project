import media
import fresh_tomatoes
 
#Initializing instances of Movie Class.
The_Matrix = media.Movie("The Matrix",
                         "The Matrix is a 1999 neo-noir science fiction action film" +
                         " written and directed by The Wachowskis.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg" # NOQA
                         ,
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

Pacific_Rim = media.Movie("Pacific Rim",
                          "The film is set in the future, when Earth is at war with the Kaiju," +
                          " colossal monsters which have emerged from an interdimensional portal on" +
                          " the bottom of the Pacific Ocean.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Pacific_Rim_FilmPoster.jpeg/220px-Pacific_Rim_FilmPoster.jpeg" # NOQA
                          ,
                          "www.youtube.com/watch?v=ecpyaRp8yYY")

Step_Brothers = media.Movie("Step Brothers",
                            "Brennan (Ferrell) and Dale (Reilly), two middle-aged men who" +
                            " are forced to live together as step brothers.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/StepbrothersMP08.jpg/220px-StepbrothersMP08.jpg" # NOQA
                            ,
                            "https://www.youtube.com/watch?v=ANjenc4W1_Q")

The_Dark_Knight = media.Movie("The Dark Knight",
                              "Bruce Wayne/Batman (Bale), James Gordon (Oldman) and Harvey Dent (Eckhart)" +
                              " form an alliance to dismantle organised crime in Gotham City, but are" +
                              " menaced by a criminal mastermind known as the Joker (Ledger) who seeks to" +
                              " undermine Batman's influence and create chaos.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg" # NOQA
                              ,
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

Star_Wars = media.Movie("Star Wars",
                        "The Rebel Alliance, led by Princess Leia (Fisher), and its attempt"  +
                        " to destroy the Galactic Empire's space station, the Death Star.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg" # NOQA
                        ,
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

Scream = media.Movie("Scream",
                     "Scream follows the character of Sidney Prescott (Campbell), a" +
                     " high school student in the fictional town of Woodsboro, California," +
                     " who becomes the target of a mysterious killer known as Ghostface.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/7/78/Scream_movie_poster.jpg/220px-Scream_movie_poster.jpg" # NOQA
                     ,
                     "https://www.youtube.com/watch?v=Bx3kBUq8UPg")

# Creating a List which holds all the movie instances.	
movies = [Scream,Star_Wars,The_Dark_Knight,Step_Brothers,Pacific_Rim,The_Matrix]

# Uses list of movie instances as input to generate an HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)
