class Movie:
    __watched_movies = 0

    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name):
        self.name = new_name

    def change_director(self, new_director):
        self.director = new_director

    def watch(self):
        if not self.watched:
            Movie.__watched_movies += 1
            self.watched = True

    def __repr__(self):
        return (
            f"Movie name: {self.name}; "
            f"Movie director: {self.director}. "
            f"Total watched movies: {Movie.__watched_movies}"
        )
