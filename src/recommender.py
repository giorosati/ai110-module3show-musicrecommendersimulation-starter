from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read a CSV file of songs and return a list of dicts with numeric fields converted."""
    import csv
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    print(f"{len(songs)} songs loaded.")
    return songs

def score_song(song: Dict, user_prefs: Dict) -> Tuple[float, str]:
    """Score one song against a user profile and return a (score, explanation) tuple."""
    genre               = user_prefs.get("genre", "")
    mood                = user_prefs.get("mood", "")
    target_energy       = float(user_prefs.get("target_energy", 0.65))
    target_valence      = float(user_prefs.get("target_valence", 0.65))
    target_danceability = float(user_prefs.get("target_danceability", 0.65))
    acousticness_target = 0.85 if user_prefs.get("likes_acoustic") else 0.15

    score   = 0.0
    reasons = []

    if song["genre"] == genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_pts = 3.0 * (1 - abs(song["energy"] - target_energy))
    score += energy_pts
    reasons.append(f"energy proximity (+{energy_pts:.2f})")

    acoustic_pts = 1.5 * (1 - abs(song["acousticness"] - acousticness_target))
    score += acoustic_pts
    reasons.append(f"acousticness proximity (+{acoustic_pts:.2f})")

    valence_pts = 0.5 * (1 - abs(song["valence"] - target_valence))
    score += valence_pts
    reasons.append(f"valence proximity (+{valence_pts:.2f})")

    dance_pts = 0.3 * (1 - abs(song["danceability"] - target_danceability))
    score += dance_pts
    reasons.append(f"danceability proximity (+{dance_pts:.2f})")

    return score, " | ".join(reasons)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song in the catalog and return the top k results sorted highest to lowest."""
    if not songs:
        return []

    scored = [(song, *score_song(song, user_prefs)) for song in songs]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
