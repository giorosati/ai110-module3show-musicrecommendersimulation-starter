"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
from src.recommender import load_songs, recommend_songs, get_max_score


def save_recommendations(recommendations, user_prefs, k, max_score, filepath="output/recommendations.txt"):
    """Save the recommendation output to a text file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(f"  Top {k} Recommendations for You\n")
        f.write("=" * 50 + "\n")
        f.write(f"\nProfile: genre={user_prefs.get('genre')} | mood={user_prefs.get('mood')} | "
                f"energy={user_prefs.get('target_energy')} | acoustic={user_prefs.get('likes_acoustic')}\n")
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            f.write(f"\n#{i}  {song['title']} by {song['artist']}\n")
            f.write(f"    Score: {score:.2f} / {max_score:.2f}\n")
            f.write(f"    Why:   {explanation.replace(' | ', chr(10) + '           ')}\n")
        f.write("\n" + "=" * 50 + "\n")
    print(f"\nResults saved to {filepath}")


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # --- Test Profile 1: Pop / Happy ---
    # High energy, upbeat, electronic pop listener.
    # Expected top results: Sunrise City, Gym Hero, Rooftop Lights
    user_prefs = {
        "genre":               "pop",
        "mood":                "happy",
        "target_energy":       0.80,
        "likes_acoustic":      False,
        "target_valence":      0.82,
        "target_danceability": 0.80,
    }

    # --- Test Profile 2: Jazz / Peaceful ---
    # Low energy, acoustic, mellow listener. Substantially different from Profile 1.
    # Expected top results: Coffee Shop Stories, Moonlight Sonata Dreams, Old Oak Road
    # user_prefs = {
    #     "genre":               "jazz",
    #     "mood":                "peaceful",
    #     "target_energy":       0.25,
    #     "likes_acoustic":      True,
    #     "target_valence":      0.65,
    #     "target_danceability": 0.35,
    # }

    # --- Test Profile 3: High-Energy EDM ---
    # Maximum energy, electronic, built for dancing.
    # Expected top results: Voltage Rush, Gym Hero, Storm Runner
    # user_prefs = {
    #     "genre":               "edm",
    #     "mood":                "energetic",
    #     "target_energy":       0.95,
    #     "likes_acoustic":      False,
    #     "target_valence":      0.60,
    #     "target_danceability": 0.90,
    # }

    # --- Test Profile 4: Chill Lofi ---
    # Low energy, acoustic, focused study listener.
    # Expected top results: Focus Flow, Midnight Coding, Library Rain
    # user_prefs = {
    #     "genre":               "lofi",
    #     "mood":                "focused",
    #     "target_energy":       0.40,
    #     "likes_acoustic":      True,
    #     "target_valence":      0.58,
    #     "target_danceability": 0.60,
    # }

    # --- Test Profile 5: Deep Intense Rock ---
    # High energy, aggressive, low valence listener.
    # Expected top results: Storm Runner, Iron Horizon, Night Drive Loop
    # user_prefs = {
    #     "genre":               "rock",
    #     "mood":                "intense",
    #     "target_energy":       0.90,
    #     "likes_acoustic":      False,
    #     "target_valence":      0.45,
    #     "target_danceability": 0.65,
    # }

    k = 5
    max_score = get_max_score()
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print("\n" + "=" * 50)
    print(f"  Top {k} Recommendations for You")
    print("=" * 50)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Score: {score:.2f} / {max_score:.2f}")
        print(f"    Why:   {explanation.replace(' | ', chr(10) + '           ')}")

    print("\n" + "=" * 50)

    save_recommendations(recommendations, user_prefs, k, max_score)


if __name__ == "__main__":
    main()
