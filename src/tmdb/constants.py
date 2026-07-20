TMDB_BASE_URL = "https://api.themoviedb.org/3"

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3

MAX_CAST = 5

from typing import Literal

Resource = Literal[
    "details",
    "credits",
    "keywords",
]

RESOURCE_DETAILS = "details"
RESOURCE_CREDITS = "credits"
RESOURCE_KEYWORDS = "keywords"