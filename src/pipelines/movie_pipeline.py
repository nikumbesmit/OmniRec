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

        return {
            "movies" : movies,
            "ratings" : ratings,
            "links" : links,
            "tags" : tags,

        }

    def aggregate_ratings(self,ratings) :
        
        rating_summary = (
            ratings.groupby("movieId",as_index= False)
            .agg(
                average_rating = ("rating","mean"),
                rating_count = ("rating","count"),
            )
        )

        rating_summary["average_rating"] = (rating_summary["average_rating"].round(2))

        return rating_summary

    def aggregate_tags(self,tags) :
        
        tag_summary = (
            tags.groupby("movieId",as_index = False)
            .agg(
            tags = ("tag", lambda x : " ".join(x.dropna().astype(str)))
            )
        )
        
        return tag_summary
        

    def merge_datasets(self,movies,rating_summary,links,tag_summary) :
        
        movie_features = movies.merge(
            rating_summary,
            on = "movieId",
            how = "left"
        )

        movie_features = movie_features.merge(
            tag_summary,
            on = "movieId",
            how = "left"
        )

        movie_features = movie_features.merge(
            links,
            on = "movieId",
            how = "left"
        )

        return movie_features
    
    def save_processed_dataset(self) :
        pass 