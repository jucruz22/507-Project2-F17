# SI 507 F17 - Project 2

### DEADLINE: October 1, 2017, 11:59 PM TO BE SUBMITTED ON CANVAS

## Basics

We have provided here a few files:

* This README
* A code file, `si507f17_project2_objects_code.py`
* A file with tests, `si507f17_project2_objects_tests.py`

## Instructions

You should **fork** this repository to your own GitHub account.

You should then **clone** your fork of the repository, so you have your own copy and can make edits on your own computer.

You should follow the instructions inside `si507f17_project2_objects_code.py` to edit that code file in order to complete the problems in this project.

To test whether you have succeeded at completing these problems, you can run the test file: e.g. `python si507f17_project2_objects_tests.py`, and view the test output.

(**DO NOT** change the names of the code files! That's very important for grading and for testing.)

As you make changes, you should make commits to your Git repository, and push them to your cloned GitHub repository.

## To submit

1. Commit and push before the deadline (or once you have used any late days you choose to use):
* The final version of your code file
* The same test file you had originally (don't make changes to it unless directed by an instructor)
* All .CSV files you create as a result of running the project

2. Submit **the full URL of your GitHub repository, the clone you make** to the Project 2 assignment on the SI 507 Canvas site. Submitting to the Canvas site before 11:59 PM will make your assignment on time and allow our grading script to work.

If you submit using (a) late day(s), you should do so by 11:59 PM on whatever day that is.


## FYI

You may add additional complication to the code if you choose, so long as you pass the tests! and you may make your own design decisions for these classes you define, as long as you still follow the instructions and come up with the desired test results.

## Code description
'''PROBLEM 1'''
## class Media
The Media class constructor should accept one dictionary data structure representing a piece of media from iTunes as input to the constructor.
It should instatiate at least the following instance variables:
- title
- author
- itunes_URL
- itunes_id (e.g. the value of the track ID, whatever the track is in the data... a movie, a song, etc)

The Media class should also have the following methods:
- a special string method, that returns a string of the form 'TITLE by AUTHOR'
- a special representation method, which returns "ITUNES MEDIA: <itunes id>" with the iTunes id number for the piece of media (e.g. the track) only in place of "<itunes id>"
- a special len method, which, for the Media class, returns 0 no matter what. (The length of an audiobook might mean something different from the length of a song, depending on how you want to define them!)
- a special contains method (for the in operator) which takes one additional input, as all contains methods must, which should always be a string, and checks to see if the string input to this contains method is INSIDE the string representing the title of this piece of media (the title instance variable)

'''PROBLEM 2'''
Now, you'll define 2 more different classes, each of which *inherit from* class Media:
In the class definitions, you can assume a programmer would pass to each class's constructor only a dictionary that represented the correct media type (song, movie).
- class Song
- class Movie

Below follows a description of how each of these should be different from the Media parent class.

### class Song:

Should have the following additional instance variables:
- album (the album title)
- track_number (the number representing its track number on the album)
- genre (the primary genre name from the data iTunes gives you)
- Should have the len method overridden to return the number of seconds in the song. (HINT: The data supplies number of milliseconds in the song... How can you access that data and convert it to seconds?)

### class Movie:

Should have the following additional instance variables:
- rating (the content advisory rating, from the data)
- genre
- description (if none, the value of this instance variable should be None) -- NOTE that this might cause some string encoding problems for you to debug!
## HINT: Check out the Unicode sub-section of the textbook! This is a common type of Python debugging you'll encounter with real data... but using the right small amount of code to fix it will solve all your problems.
- Should have the len method overridden to return the number of minutes in the movie (HINT: The data returns the number of milliseconds in the movie... how can you convert that to minutes?)
- Should have an additional method called title_words_num that returns an integer representing the number of words in the movie description. If there is no movie description, this method should return 0.

'''PROBLEM 3'''
In this problem, you'll write some code to use the definitions you've just written. First, here we have provided some variables which hold data about media overall, songs, and movies.

## NOTE: (The first time you run this file, data will be cached, so the data saved in each variable will be the same each time you run the file, as long as you do not delete your cached data.)

You may want to do some investigation on these variables to make sure you understand correctly what type of value they hold, what's in each one! Use the values in these variables above, and the class definitions you've written, in order to create a list of each media type, including "media" generally.

- a list of Media objects saved in a variable media_list,
- a list of Song objects saved in a variable song_list,
- a list of Movie objects saved in a variable movie_list.

## You may use any method of accumulation to make that happen.

'''PROBLEM 4'''
## Finally, write 3 CSV files:
- movies.csv
- songs.csv
- media.csv

## Each of those CSV files should have 5 columns each:
- title
- artist
- id
- url (for the itunes url of that thing -- the url to view that track of media on iTunes)
- length
