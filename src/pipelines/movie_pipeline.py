from pathlib import Path
import pandas as pd
from src.data.loader import load_csv
from src.data.constants import RAW_DATA_DIR

class MoviePipeline :

    """Pipeline for Unified Movie Dataset Building """
    
    def load_datasets(self) :
        
        movies = load_csv(RAW_DATA_DIR / "movielens" / "movies.csv")
        ratings = load_csv(RAW_DATA_DIR / "movielens" / "ratings.csv")
        tags = load_csv(RAW_DATA_DIR / "movielens" / "tags.csv")
        links = load_csv(RAW_DATA_DIR / "movielens" / "links.csv")

        return movies, ratings, links , tags

    def aggregate_ratings(self) :
        pass

    def aggregate_tags(self) :
        pass

    def merge_datasets(self) :
        pass
    
    def save_processed_dataset(self) :
        pass 