# coding=utf-8
## SI 507 F17 Project 2 - Objects
# Due Date:
import requests
import json
import unittest

## Instructions for each piece to be completed for this project can be found in the file, below.

## To see whether your problem solutions are passing the tests, you should run the Python file:
# si507f17_project2_objects_tests.py, which should be saved in the same directory as this file.

## (DO NOT change the name of this file! Make sure to re-save it with the name si507f17_project2_objects_code.py if you change the name. Otherwise, we will not be able to grade it!)


print("\n*** *** PROJECT 2 *** ***\n")

## Useful additional references for this part of the homework from outside class material:
## - the iTunes Search API documentation:
## - the following chapters from the textbook (also referred to in SI 506): https://www.programsinformationpeople.org/runestone/static/publicpy3/Classes/ThinkingAboutClasses.html, https://www.programsinformationpeople.org/runestone/static/publicpy3/Classes/ClassesHoldingData.html, https://www.programsinformationpeople.org/runestone/static/publicpy3/UsingRESTAPIs/cachingResponses.html
## - and possibly other chapters, as a reference!

## The first problem to complete for this project can be found below.


#########


## You can search for a variety of different types of media with the iTunes Search API: songs, movies, ebooks and audiobooks... (and more) You'll definitely need to check out the documentation to understand/recall how the parameters of this API work: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/

## Here, we've provided functions to get and cache data from the iTunes Search API, but looking at the information in that documentation will help you understand what is happening when the second function below gets invoked.
## Make sure you understand what the function does, how it works, and how you could invoke it to get data from iTunes Search about e.g. just songs corresponding to a certain search term, just movies, or just books.
## Refer to the textbook sections about caching, linked above, to help understand these functions!

## You may want to try them out and see what data gets returned, in order to complete the problems in this project.

'''function to organize cache strings in your cache dictionary based on search terms'''
def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys()) # sort search terms
    res = [] # results list
    for k in alphabetized_keys: # for parameters in your list of param keys
        if k not in private_keys: # if the search terms aren't already in the dictionary, add them in this format
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

'''function that takes in your search terms to create a cache file/dictionary with the search terms you used'''
def sample_get_cache_itunes_data(search_term,media_term="all"):
	CACHE_FNAME = 'cache_file_name.json'
	try: # if the file already exists...
	    cache_file = open(CACHE_FNAME, 'r')
	    cache_contents = cache_file.read() # convert to string
	    CACHE_DICTION = json.loads(cache_contents) # create a json dict object from the str contents of the cache file
	    cache_file.close()
	except: # if the file doesn't exist yet...
	    CACHE_DICTION = {} # create an empty cash dictionary
	baseurl = "https://itunes.apple.com/search"
	params = {}
	params["media"] = media_term
	params["term"] = search_term
	unique_ident = params_unique_combination(baseurl, params) # creates unique identifier in cache dictionary
	if unique_ident in CACHE_DICTION: # if you already searched for this term before...
		return CACHE_DICTION[unique_ident] # return that json dictionary
	else: # if your search term is new...
		CACHE_DICTION[unique_ident] = json.loads(requests.get(baseurl, params=params).text) # use .requests to get new data and add it to the cache
		full_text = json.dumps(CACHE_DICTION) # convert that cache diction object into a string so we can put it into a file
		cache_file_ref = open(CACHE_FNAME,"w") # open the cache file so we can write to it
		cache_file_ref.write(full_text) # put our updated cache dictionary in there (will overwrite old data)
		cache_file_ref.close() # close the file
		return CACHE_DICTION[unique_ident]

'''TESTING CACHE and parsing through search result data'''
sample_media = sample_get_cache_itunes_data("Lemony Snicket")["results"][0] # it worked! search results show up in cache file
# print (sample_media)
print (sample_media["collectionName"])
print (sample_media["artistName"])
print (sample_media["collectionViewUrl"])
print (sample_media["collectionId"])
# print (media_sample) # prints first result item in res dictionary
# print (media_sample2)

## [PROBLEM 1] [250 POINTS]
print("\n***** PROBLEM 1 *****\n")
## For problem 1, you should define a class Media, representing ANY piece of media you can find on iTunes search.
class Media(object):
    def __init__(self,media_dict):
        self.author = media_dict["artistName"]
        self.title = media_dict["trackName"]
        self.itunes_URL = media_dict["trackViewUrl"]
        self.itunes_id = media_dict["trackId"]


    def __str__(self):
        return "{} by {}".format(self.title,self.author)

    def __repr__(self):
        return "ITUNES MEDIA: {}".format(self.itunes_id)

    def __len__(self):
        return 0

    def __contains__(self,title):
        return title in self.title #returns either true or false

    def csv_string(self): # for problem 4 later, all other classes will inherit
        return "{},{},{},{},{}\n".format(self.title,self.author,self.itunes_id,self.itunes_URL,self.__len__())

## [PROBLEM 2] [400 POINTS]
print("\n***** PROBLEM 2 *****\n") ## In 2 parts.
# print (sample_song["collectionName"])
# print (sample_song["trackNumber"])
# print (sample_song["primaryGenreName"])
# print (sample_song["trackTimeMillis"])
class Song(Media): # Song class is at this point an EXACT replica of class Media
    def __init__(self,song_dict):
        super().__init__(song_dict) # to inherit and change, we need this the inheritance line which draws from the "super class" or parent (Media) class. We want the same + more. This is when you need the inheritance line.
        self.album = song_dict["collectionName"]
        self.track_number = song_dict["trackNumber"]
        self.genre = song_dict["primaryGenreName"]
        self.length = song_dict["trackTimeMillis"]

    def __len__(self):
        # don't need to inherit Media, because we are overwriting it with your own code
        return int(self.length/1000) # number of seconds in the song

print ("tesing Problem 2 - Song")
sample_song = sample_get_cache_itunes_data("coldplay","music")["results"][0]
s = Song(sample_song)
print (s) # should return string
print (s.title) # should provide title
print ("Something" in s.title) # should return true
print (len(s))
print (s.csv_string())

class Movie(Media):
    def __init__(self,media_dict):
        super().__init__(media_dict) # inheriting from parent class
        self.rating = media_dict["contentAdvisoryRating"]
        self.genre = media_dict["primaryGenreName"]
        try:
            self.description = media_dict["longDescription"].encode("utf8")
            self.length = media_dict["trackTimeMillis"]
        except:
            self.description = None
            self.length = 0

    def __len__(self):
        return int(self.length/60000)

    def title_words_num(self):
        count = 0
        try:
            for w in self.description.split(): # split description by spaces and make a list of words
                count += 1
            return count
        except:
            return 0

print ("tesing Problem 2 - Movie")
sample_movie = sample_get_cache_itunes_data("Jennifer Lawrence","movie")["results"][0]
m = Movie(sample_movie)
print (m) # invoking string method
print (m.title) # invoking instance variable from parent class
print ("Hunger" in m.title)
print (len(m))


## [PROBLEM 3] [150 POINTS]
print("\n***** PROBLEM 3 *****\n")
media_samples = sample_get_cache_itunes_data("love")["results"] # media type
song_samples = sample_get_cache_itunes_data("love","music")["results"] # song type
movie_samples = sample_get_cache_itunes_data("love","movie")["results"] # movie type

media_list = [Media(media_dict) for media_dict in media_samples]
song_list = [Song(song_dict) for song_dict in song_samples]
movie_list = [Movie(movie_dict) for movie_dict in movie_samples]
print (len(media_list)) # 50
print (len(song_list)) # 50
print (len(movie_list)) # 50


## [PROBLEM 4] [200 POINTS]
print("\n***** PROBLEM 4 *****\n")

# Headers
file_list = ["media.csv","movies.csv","songs.csv"]
for name in file_list:
    f = open(name, "w")
    f.write("title,artist,id,url,length\n")
    f.close()

# Content
def csv_content(file_name,list_name):
    f = open(file_name,"a+")
    for obj in list_name:
        f.write(obj.csv_string())
    f.close()

csv_content("media.csv",media_list)
csv_content("movies.csv",movie_list)
csv_content("songs.csv",song_list)

# f = open("media.csv","a+")
# for obj in media_list:
#     f.write(obj.csv_string())
# f.close()
#
# f = open("movies.csv","a+")
# for obj in movie_list:
#     f.write(obj.csv_string())
# f.close()
#
# f = open("songs.csv","a+")
# for obj in song_list:
#     f.write(obj.csv_string())
# f.close()



# mfile = open("media.csv","w")
# for media in media_list:
#     mfile.write(media.csv_string())
#     # mfile.write("{},{},{},{},{}".format(media.title,media.author,media.itunes_id,media.itunes_URL,media.__len__()))

## There are no provided tests for this problem -- you should check your CSV files to see that they fit this description to see if this problem worked correctly for you. IT IS VERY IMPORTANT THAT YOUR CSV FILES HAVE EXACTLY THOSE NAMES!

## You should use the variables you defined in problem 3, iteration, and thought-out use of accessing elements of a class instance, to complete this!

## HINT: You may want to think about what code could be generalized here, and what couldn't, and write a function or two -- that might make your programming life a little bit easier in the end, even though it will require more thinking at the beginning! But you do not have to do this.

## HINT #2: *** You MAY add other, non-required, methods to the class definitions in order to make this easier, if you prefer to!

## It is perfectly fine to write this code in any way, as long as you rely on instances of the classes you've defined, and the code you write results in 3 correctly formatted CSV files!

## HINT #3: Check out the sections in the textbook on opening and writing files, and the section(s) on CSV files!

## HINT #4: Write or draw out your plan for this before you actually start writing the code! That will make it much easier.
