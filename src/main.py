"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # --- Test Profile 1: Pop / Happy ---
    # High energy, upbeat, electronic pop listener.
    # Expected top results: Sunrise City, Gym Hero, Rooftop Lights
    # user_prefs = {
    #     "genre":               "pop",
    #     "mood":                "happy",
    #     "target_energy":       0.80,
    #     "likes_acoustic":      False,
    #     "target_valence":      0.82,
    #     "target_danceability": 0.80,
    # }

    # --- Test Profile 2: Jazz / Peaceful ---
    # Low energy, acoustic, mellow listener. Substantially different from Profile 1.
    # Expected top results: Coffee Shop Stories, Moonlight Sonata Dreams, Old Oak Road
    user_prefs = {
        "genre":               "jazz",
        "mood":                "peaceful",
        "target_energy":       0.25,
        "likes_acoustic":      True,
        "target_valence":      0.65,
        "target_danceability": 0.35,
    }

    k = 5
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print("\n" + "=" * 50)
    print(f"  Top {k} Recommendations for You")
    print("=" * 50)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Score: {score:.2f} / 8.30")
        print(f"    Why:   {explanation.replace(' | ', chr(10) + '           ')}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
