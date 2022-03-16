from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)


@app.get('/')
def index():
    #Test code to create a movie
    #movie_repository_singleton.create_movie('Test Movie Title','Test Director',5)
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    movies = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, data=movies)



@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page

    title = request.form.get('title')
    director = request.form.get('director')
    rating = int(request.form.get('rating'))
    movie_repository_singleton.create_movie(title,director,rating)

    return redirect('/movies')
    


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    movies = movie_repository_singleton.get_all_movies()
    py_search_title = request.args.get('search_title_1', 'none')



    return render_template('search_movies.html', search_active=True, search_title=py_search_title , data=movies )
