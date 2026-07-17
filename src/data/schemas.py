from dataclasses import dataclass
from typing import Optional

@dataclass
class Item :

    item_id : str
    domain : str            # movie | book | music
    title : str
    creator : str            # director | author | artist
    genres : str
    description : str
    language : str
    release_year : Optional[int]
    popularity : Optional[float]
    average_rating : Optional[float]

@dataclass
class User :

    user_id : str
    username : str
    preferred_language : Optional[str] = None

@dataclass
class Interaction :

    user_id : str
    item_id : str
    event_type: str        # like, view, rate, save, play
    rating : Optional[float] = None
    timestamp : Optional[str] = None