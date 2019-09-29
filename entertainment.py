import media
import fresh_tomatoes

# Movie details

avatar = media.Movie("Avatar", "Avatar is a 3-D science fiction epic film."
                     "In a distant future, humanity discovers the planet"
                     "'Alpha Centauri B-4',and for those scientists and"
                     " astronauts who've traversed the gulf between"
                     "neighboring suns and arrived on its alien soil"
                     " know it as 'Pandora'.", "https://images-na.ssl"
                     "-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5B"
                     "Ml5BanBnXkFtZTcwODc5MTUwMw"
                     "@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8"
                     )

annabelle = media.Movie("Annabelle", "This movie is about the story of the"
                        " person dead and living in the form of doll which"
                        "is named as Annabelle",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcSFJXO-"
                        "WgGmu29wKPaaR2lPco4z3krUU_Aqiktmz4XtxGvys3Cn",
                        "https://www.youtube.com/watch?v=jdUysoK6tdQ"
                        )             
bahubali_the_conclusion = media.Movie("Bahubali: The Conclusion",
                                      "The movie which is the conclusion of"
                                      " Bahubali the beginning which"
                                      "tells why kattappa had killed Bahubali",
                                      "http://images.mapsofindia.com/hindi/my"
                                      "-india/2017/05/bahubali2-hindi.jpg",
                                      "https://www.youtube.com/watch?v=G62HrubdD6o"
                                      )                                       
ohm_shanthi_oshaana = media.Movie("Ohm Shanthi Oshaana",
                                  "A movie with tells the love story"
                                  "of a girl", "https://madaboutmoviez"
                                  ".files.wordpress.com/2014/02/ohm-shant"
                                  "hi-oshaana-nazriya-and-nivin.jpg?w=1200",
                                  "https://www.youtube.com/watch?v=M5-mzpNvnrY"
                                  )

thuppaki = media.Movie("Thuppaki",
                       "A movie which tells the story of a army man",
                       "https://akm-img-a-in.tosshub.com/indiatoday/images/story/201207/vijay-660_071712121837.jpg",
                       "https://www.youtube.com/watch?v=aW_j4pNvG98"
                       )                     
secret_life_of_pets = media.Movie("The Secret life of pets",
                                  "The life of pets apart from the"
                                  " outside the world", "https://lh3.google"
                                  "usercontent.com/-dV3U8bE-O2g/V5NDl7oXEwI"
                                  "/AAAAAAAAOVY/D29-wJEMFhk/s660/cover.png",
                                  "https://www.youtube.com/watch?v=i-80SGWfEjM"
                                  )
# creating a list of all the movies
list_of_movies = [
                  avatar,
                  annabelle,
                  bahubali_the_conclusion,
                  ohm_shanthi_oshaana,
                  thuppaki,
                  secret_life_of_pets
                  ]

# sending the list to fresh_tomatoes.py file to open web page
fresh_tomatoes.open_movies_page(list_of_movies)
