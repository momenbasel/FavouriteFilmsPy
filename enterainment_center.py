import media
import fresh_tomatoes
toy_story = media.Movie("Toy story",
                        "A Story of boy and his toys comes to life",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar= media.Movie("Avatar",
                    "a marine on alien life",
                    "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
the_god_father = media.Movie("the god father","The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR3,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=sY1S34973zA")
big_hero_6 = media.Movie("Big Hero 6","The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_SY1000_CR0,0,699,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=rD5OA6sQ97M")
movies = [toy_story, avatar, the_god_father , big_hero_6]
fresh_tomatoes.open_movies_page(movies)
