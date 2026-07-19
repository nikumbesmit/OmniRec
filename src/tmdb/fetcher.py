from typing import Any,Literal 
from collections.abc import Callable
from src.tmdb.client import TMDBClient
from src.tmdb.cache import TMDBCache
from src.tmdb.constants import RESOURCE_DETAILS,RESOURCE_CREDITS,RESOURCE_KEYWORDS

Resource = Literal[
    "details",
    "credits",
    "keywords",
]

MovieFetcher = Callable[ [int], dict[str, Any]]


class TMDBFetcher :

    def __init__(self, client : TMDBClient, cache : TMDBCache):
        
        self.client = client
        self.cache = cache


    def _fetch_resource(self, movie_id : int, resource : Resource, fetch_func : MovieFetcher) -> dict[str,Any] :
        
        data = self.cache.load(movie_id,resource)

        if data is not  None :
            return data
        
        data = fetch_func(movie_id)

        self.cache.save(movie_id,resource,data)

        return data


    def fetch_details(self, movie_id : int) -> dict[str, Any] :

        return self._fetch_resource(
            movie_id,
            RESOURCE_DETAILS,
            self.client.get_movie_details,
        )


    def fetch_credits(self, movie_id : int) -> dict[str,Any] :
        
        return self._fetch_resource(
            movie_id,
            RESOURCE_CREDITS,
            self.client.get_movie_credits,
        )

    def fetch_keywords(self, movie_id : int) -> dict[str, Any] :
        
        return self._fetch_resource(
            movie_id,
            RESOURCE_KEYWORDS,
            self.client.get_movie_keywords,
        )