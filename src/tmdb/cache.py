import json
from typing import Any
from pathlib import Path
from src.tmdb.fetcher import Resource


class TMDBCache :

    def __init__(self , cache_dir : str = "data/cache/tmdb") :
        
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    
    def _cache_path(self, movie_id : int , resource: Resource) -> Path :

        return self.cache_dir / f"{movie_id}_{resource}.json"


    def exists(self , movie_id : int ,resource: Resource) -> bool :
        
        return self._cache_path(movie_id,resource).exists()


    def load(self, movie_id : int, resource: Resource) -> dict[str,Any] | None :
        
        cache_file = self._cache_path(movie_id,resource)

        if not cache_file.exists() :
            return None
        
        with cache_file.open("r" , encoding="utf-8") as file :
            return json.load(file)
            
        
    def save(self, movie_id : int ,resource : Resource, data : dict[str,Any]) -> None :      

        cache_file = self._cache_path(movie_id,resource)

        with cache_file.open("w", encoding="utf-8") as file :

            json.dump(data, file, indent=4, ensure_ascii=False)  


    def delete(self, movie_id : int, resource: Resource) -> None :
        
        cache_file = self._cache_path(movie_id, resource) 

        if cache_file.exists() :
            cache_file.unlink()
