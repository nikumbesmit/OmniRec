class TMDBError(Exception):
    """Base exception for all TMDB errors."""
    pass


class AuthenticationError(TMDBError):
    """Raised when the API key is invalid."""
    pass


class MovieNotFoundError(TMDBError):
    """Raised when a movie does not exist."""
    pass


class RateLimitError(TMDBError):
    """Raised when the TMDB rate limit is exceeded."""
    pass


class APIRequestError(TMDBError):
    """Raised for unexpected API errors."""
    pass