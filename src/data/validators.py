import pandas as pd
import warnings

class DataValidator :

    """
        Validates datases before they enter the pipeline.
        Raise ValueError if validation fails...
    """

    def validate_movies(self,movies : pd.DataFrame) -> None :
         required_columns = {
             "movieId",
             "title",
             "genres"
         }

         missing = set(required_columns) - set(movies.columns)

         duplicates = movies[movies.duplicated(subset=["movieId"],keep="first")]
         duplicate_movie_ids = duplicates["movieId"].to_list()

         null_title = movies["title"].isnull().sum()
         null_genres = movies["genres"].isnull().sum()

         if missing :
             raise ValueError (
                 f"Missing required columns : {missing}"
             )
         
         if duplicate_movie_ids :
             raise ValueError (
                 f"Duplicate MovieId's : {duplicate_movie_ids}"
             )
         
         if null_title > 0 :
             raise ValueError (
                 f"No. of empty titles : {null_title}"
             )
         
         if null_genres > 0 :
             raise ValueError (
                 f"No. of empty genres : {null_genres}"
             )
         
         return None 
    
    
    def validate_ratings(self,ratings : pd.DataFrame) -> None :
        
         required_columns = {
             "userId",
             "movieId",
             "rating",
             "timestamp"
         }

         missing = set(required_columns) - set(ratings.columns)

         null_movie_ids = ratings["movieId"].isna().sum()
         null_rating = ratings["rating"].isna().sum()

         valid_rating = ratings["rating"].between(0.5,5.0).all()

         if missing :
             raise ValueError (
                 f"Missing required columns : {missing}"
             )

         if null_movie_ids > 0 :
             raise ValueError (
                 f"No. of missing Movie id's : {null_movie_ids}"
             )
         
         if null_rating > 0  :
             raise ValueError (
                 f"No. of null ratings : {null_rating}"
             )
         
         if not valid_rating :
             raise ValueError (
                 "Data contains rating outside the range 0.5 - 5.0"
             )


    def validate_tags(self,tags : pd.DataFrame) -> None :
        
         required_columns = {
             "userId",
             "movieId",
             "tag",
             "timestamp"
         }

         missing = set(required_columns) - set(tags.columns)

         null_movie_ids = tags["movieId"].isna().sum()
         null_tags = tags["tag"].isna().sum()

         if missing :
             raise ValueError (
                f"Missing required columns : {missing}"
            )
         
         if null_movie_ids > 0 :
             raise ValueError (
                 f"No. of missing Movie id's : {null_movie_ids}"
             )
         
         if null_tags > 0  :
             raise ValueError (
                 f"No. of null tags : {null_tags}"
             )


    def validate_links(self,links : pd.DataFrame) -> None :
        
         required_columns = {
             "movieId",
             "imdbId",
             "tmdbId"
         }

         missing = set(required_columns) - set(links.columns)

         duplicates = links[links.duplicated(subset=["movieId"],keep="first")]
         duplicate_movie_ids = duplicates["movieId"].to_list()

         null_tmdb_ids = links["tmdbId"].isna().sum()

         if missing :
             raise ValueError (
                 f"Missing required columns : {missing}"
             )
         
         if duplicate_movie_ids :
             raise ValueError (
                 f"Duplicate movie ids : {duplicate_movie_ids}"
             )
         if null_tmdb_ids > 0 :
             warnings.warn(
                f"{null_tmdb_ids} movies are missing TMDB IDs.",
                UserWarning,
             )
         
