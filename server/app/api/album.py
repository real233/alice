"""
Contains all the album routes.
"""
from typing import List

from app import api
from app import helpers
from app import models
from app.lib import albumslib
from app.lib import trackslib
from flask import Blueprint
from flask import request
from app.functions import FetchAlbumBio

album_bp = Blueprint("album", __name__, url_prefix="")


@album_bp.route("/")
def say_hi():
    """Returns some text for the default route"""
    return "^ _ ^"


@album_bp.route("/albums")
def get_albums():
    """returns all the albums"""
    albums = []

    for song in api.DB_TRACKS:
        al_obj = {"name": song["album"], "artist": song["artists"]}

        if al_obj not in albums:
            albums.append(al_obj)

    return {"albums": albums}


@album_bp.route("/album/tracks", methods=["POST"])
def get_album_tracks():
    """Returns all the tracks in the given album."""
    data = request.get_json()

    album = data["album"]
    artist = data["artist"]

    songs = trackslib.get_album_tracks(album, artist)
    albumhash = helpers.create_album_hash(album, artist)
    index = albumslib.find_album(api.ALBUMS, albumhash)
    album = api.ALBUMS[index]

    album.count = len(songs)
    album.duration = albumslib.get_album_duration(songs)

    return {"songs": songs, "info": album}


@album_bp.route("/album/bio", methods=["POST"])
def get_album_bio():
    """Returns the album bio for the given album."""
    data = request.get_json()
    fetch_bio = FetchAlbumBio(data["album"], data["albumartist"])
    bio = fetch_bio()

    if bio is None:
        return {"bio": "No bio found."}, 404

    return {"bio": bio}


@album_bp.route("/album/artists", methods=["POST"])
def get_albumartists():
    """Returns a list of artists featured in a given album."""
    data = request.get_json()

    album = data["album"]
    artist = data["artist"]

    tracks: List[models.Track] = []

    for track in api.TRACKS:
        if track.album == album and track.albumartist == artist:
            tracks.append(track)

    artists = []

    for track in tracks:
        for artist in track.artists:
            if artist not in artists:
                artists.append(artist)

    final_artists = []
    for artist in artists:
        artist_obj = {
            "name": artist,
            "image": helpers.check_artist_image(artist),
        }
        final_artists.append(artist_obj)

    return {"artists": final_artists}
