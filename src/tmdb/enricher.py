from typing import Any


class TMDBEnricher :

    def enrich(self,
                details : dict[str,Any],
                credits : dict[str,Any],
                keywords : dict[str,Any]) -> dict[str,Any] :
        
        return {
            "tmdbId": details.get("id"),
            "title": details.get("title"),
            "overview": details.get("overview", ""),
            "genres": self._extract_genres(details),
            "keywords": self._extract_keywords(keywords),
            "director": self._extract_director(credits),
            "cast": self._extract_cast(credits),
            "runtime": self._extract_runtime(details),
            "release_year": self._extract_release_year(details),
            "vote_average": details.get("vote_average"),
            "vote_count": details.get("vote_count"),
            "popularity": details.get("popularity"),
            "original_language": details.get("original_language"),
        }


    def _normalize_tokens(self, items : list[str]) -> str :
        
        return " ".join(
            item.strip().replace(" ", "_")
            for item in items
            if item.strip()
        )


    def _extract_genres(self, details : dict[str, Any]) -> str :
        
        genres = [
            genre["name"]
            for genre in details.get("genres",[])
        ]

        return self._normalize_tokens(genres)


    def _extract_keywords(self, keywords : dict[str, Any]) -> str :
    
        keyword_list = [
            keyword["name"]
            for keyword in keywords.get("keywords",[])
        ]

        return self._normalize_tokens(keyword_list)


    def _extract_director(self, credits : dict[str, Any]) -> str :
        
        directors = [
            crew_member["name"]
            for crew_member in credits.get("crew",[])
            if crew_member.get("job") == "Director"
        ]

        return self._normalize_tokens(directors)


    def _extract_cast(self, credits : dict[str,Any]) -> str :
        
        cast_list = [
            actor["name"]
            for actor in credits.get("cast",[])[:5]
        ]

        return self._normalize_tokens(cast_list)


    def _extract_release_year(self, details : dict[str,Any]) -> int | None :
        
        release_date = details.get("release_date")

        if not release_date :
            return None
        
        try :
            return int(release_date[:4])
        
        except (ValueError,TypeError) :
            return None


    def _extract_runtime(self, details : dict[str,Any]) -> int | None :
        
        return details.get("runtime")