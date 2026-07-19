import os 
import requests
from dotenv import load_dotenv
from typing import Any

from src.tmdb.constants import (
    TMDB_BASE_URL,
    REQUEST_TIMEOUT,
)

from src.tmdb.exceptions import (
    TMDBError,
    AuthenticationError,
    MovieNotFoundError,
    RateLimitError,
    APIRequestError,
)

load_dotenv()

class TMDBClient :


    def __init__(self):
        
        self.api_key = os.getenv("TMDB_API_KEY")

        if not self.api_key :
            raise AuthenticationError (
                "TMDB_API_KEY not found in environment variables"
            )
        
        self.session = requests.Session()


    def _request(self, endpoint : str, params : dict[str,Any] | None = None) -> dict :

        if params is None :
            params = {}

        params["api_key"] = self.api_key

        url = f"{TMDB_BASE_URL}{endpoint}"

        try :
            response = self.session.get(
                url,
                params = params,
                timeout = REQUEST_TIMEOUT,
            ) 
        except requests.RequestException as e :
            raise APIRequestError(f"Network error : {e}") from e


        if response.status_code == 401 :
            raise AuthenticationError("Invalid TMDB API key.")
        
        if response.status_code == 404 :
            raise MovieNotFoundError("Movie not found.")
        
        if response.status_code == 429 :
            raise RateLimitError("TMDB rate limit exceeded.")
        
        if not response.ok :
            raise APIRequestError(f"TMDB request failed with status code {response.status_code}.")
        
        return response.json()


    def get_movie_details(self, movie_id : int) -> dict :

        return self._request(f"/movie/{movie_id}")


    def get_movie_credits(self, movie_id : int) -> dict :

        return self._request(f"/movie/{movie_id}/credits")


    def get_movie_keywords(self, movie_id : int) -> dict :

        return self._request(f"/movie/{movie_id}/keywords")