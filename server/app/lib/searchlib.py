"""
This library contains all the functions related to the search functionality.
"""

from typing import List
from app import models, helpers
from app.lib import albumslib
from app import api


def get_tracks(query: str) -> List[models.Track]:
    """
    Gets all songs with a given title.
    """
    tracks = [track for track in api.TRACKS if query.lower() in track.title.lower()]
    return helpers.remove_duplicates(tracks)


def get_search_albums(query: str) -> List[models.Album]:
    """
    Gets all songs with a given album.
    """
    return albumslib.search_albums_by_name(query)


def get_artists(artist: str) -> List[models.Track]:
    """
    Gets all songs with a given artist.
    """
    return [track for track in api.TRACKS if artist.lower() in str(track.artists).lower()]
