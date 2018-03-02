import webbrowser


class Movie():

    # Get all the values from entertainer.py
    def __init__(self, mname, mstory, mimage, mURL):
        self.title = mname               # Assigns mname to the title
        self.storyline = mstory          # Assigns mstory to the storyline
        self.poster_image_url = mimage   # Assigns mimage to the variable
        self.trailer_youtube_url = mURL  # Assigns mURL to the trailer variable
