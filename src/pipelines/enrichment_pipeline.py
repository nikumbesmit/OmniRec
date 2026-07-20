from typing import Any
import pandas as pd 

from src.tmdb.fetcher import TMDBFetcher
from src.tmdb.enricher import TMDBEnricher 


class EnrichmentPipeline :


    def __init__(self,
                 fetcher : TMDBFetcher,
                 enricher : TMDBEnricher):
        
        self.fetcher = fetcher
        self.enricher = enricher


    def enrich_movies(self, movie_features : pd.DataFrame) -> pd.DataFrame :

        enriched_movies = []

        for _, movie in movie_features.iterrows() :

            tmdb_id = int(movie["tmdbId"])

            details = self.fetcher.fetch_details(tmdb_id)
            credits = self.fetcher.fetch_credits(tmdb_id)
            keywords = self.fetcher.fetch_keywords(tmdb_id)

            enriched_movie = self.enricher.enrich(
                details = details,
                credits = credits,
                keywords = keywords,
            )

            complete_movie = {
                **movie.to_dict(),
                **enriched_movie,
            }


            enriched_movies.append(complete_movie)

        return pd.DataFrame(enriched_movies)


