import pandas as pd 


class MetadataFeatureEngineer :

    """
    Transforms movie metadata into features
    used by recommendation models.
    """

    def clean_genres(self,movie_features : pd.DataFrame) -> pd.DataFrame :

        movie_features["genres"] = movie_features["genres"].str.replace("|", " ", regex = False )

        return movie_features

    def clean_tags(self,movie_features : pd.DataFrame) -> pd.DataFrame :
        
        movie_features["tags"] = movie_features["tags"].fillna("")

        return movie_features

    def create_metadata(self,movie_features : pd.DataFrame) -> pd.DataFrame :
        
        movie_features = self.clean_genres(movie_features)
        movie_features = self.clean_tags(movie_features)

        movie_features["metadata"] = movie_features["genres"] + " " + movie_features["tags"]

        movie_features["metadata"] = (
            movie_features["metadata"]
            .str.lower()
            .str.replace(r"\s+"," " ,regex=True)
            .str.strip()
        )

        movie_features["metadata"] = (
            movie_features["metadata"]
            .apply(
                lambda text : " ".join(dict.fromkeys(text.split()))
            )
        )

        return movie_features