from django.db import models
from Accounts.models import Snoze_User
# Create your models here.
class Song(models.Model):
    '''
        A basic song table representing the songs uploaded by the users of the App
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    duration = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    label = models.CharField(max_length=100,default='no label')

class Album(models.Model):
    '''
        A basic album table
    '''
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)

class Playlist(models.Model):
    '''
        Playlist table. private is boolean specifying whether the playlist is visiblie 
        publically or no.
    '''
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
    
class Like(models.Model):
    '''
        Entry in this table that represents that the user has liked the coresponding song.
    '''
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Snoze_User, on_delete = models.CASCADE)

'''class Comment(models.Model):
    song_id = models.ForeignKey(Songs, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Snoze_User, on_delete = models.CASCADE)
    comment = models.CharField(max_length=500)
    '''

class Favourite_Playlist(models.Model):
    '''
        An entry in this table represents that the user has favourted the corresponding playlist
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)

class Favourite_Song(models.Model):
    '''
        An entry in this table represents that the user has favourted the corresponding playlist
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

class Recent(models.Model):
    '''
        This table is like a stack for the users. A song played by the user would first be checked for 
        in this table, if not found an entry would be made in this table else the song field from this 
        table would be retrieved and the time would be retrieved.
        Also the table would delete the songs that the is has the minimum value in the last_played
        when the decided limit for the recent songs is reached. (for premium users there will be no limit)
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    last_played = models.DateTimeField(auto_now=True) 
