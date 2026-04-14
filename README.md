# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Design Explanation
Each Song stores seven attributes: categorical descriptors genre and mood, and numeric audio features energy, acousticness, valence, danceability, and tempo_bpm. The UserProfile stores matching preferences: favorite_genre, favorite_mood, target_energy, and a likes_acoustic boolean.

The Recommender scores each song using weighted proximity — for numeric features, 1 - |song_value - user_target| rewards closeness over raw magnitude. Categorical features contribute 1.0 for a match, 0.0 otherwise. Weights reflect signal strength:


score = 0.30 × energy_proximity
      + 0.25 × genre_match
      + 0.20 × mood_match
      + 0.15 × acousticness_proximity
      + 0.05 × valence_proximity
      + 0.03 × danceability_proximity
      + 0.02 × tempo_proximity
Every song is scored independently, then sorted descending, and the top k are returned.

Real-World vs. This Version
Real platforms like Spotify infer preferences from implicit behavior — skips, replays, saves — and combine collaborative filtering, deep audio models, and real-time context signals to recommend songs users didn't know they wanted.

This version prioritizes transparency over sophistication. Preferences are declared explicitly, every score is traceable to specific features and weights, and there is no learning loop. It is an honest content-based recommender — the right foundation for understanding recommendation mechanics before adding behavioral complexity.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

Music Curator v0.1

---

## 2. Intended Use

This recommender suggests up to 10 songs from a growing catalog based on a user's preferred genre, mood, energy level, and acoustic preference. It is designed as a functional content-based filtering system intended to scale as the catalog expands. While it currently uses a small dataset for development and testing, it is built with real recommendation logic and is not limited to educational use.

---

## 3. How It Works (Short Explanation)

How Real-World Recommenders Work

Platforms like Spotify and YouTube predict what users will love by combining two approaches. Collaborative filtering analyzes the behavior of millions of users — skips, replays, saves, and playlist adds — to find listeners with similar taste and surface songs those listeners love. Content-based filtering takes a different angle, analyzing the attributes of the music itself — tempo, energy, mood, genre — to find songs that sound and feel similar to ones you already enjoy. Real platforms layer both approaches together, adding contextual signals like time of day and device type, and use reinforcement learning to continuously improve based on what users actually do next.

What This Version Prioritizes

This simulation uses a pure content-based approach. Rather than inferring preferences from behavior, the user declares them explicitly through a profile that stores a favorite genre, a preferred mood, a target energy level, and an acoustic preference. Each song is scored by measuring how close its attributes are to those targets using a weighted proximity formula — features with stronger predictive signal, like energy and genre, carry more weight than features that are more redundant, like danceability and tempo. Every score is fully traceable, making this version transparent and easy to reason about, at the cost of the serendipity and personalization depth that behavioral data provides.

Each Song in the catalog is described by seven attributes. Two are categorical: genre (such as pop, lofi, rock, or jazz) and mood (such as happy, chill, intense, or focused). Five are numeric and measured on a 0 to 1 scale: energy (overall intensity), acousticness (organic vs. electronic sound), valence (musical positivity), and danceability (suitability for dancing). tempo_bpm is also numeric but measured in beats per minute, so it is normalized to a 0 to 1 scale before scoring.

The UserProfile stores four preference fields that map directly to song attributes: favorite_genre, favorite_mood, target_energy (a number between 0 and 1), and likes_acoustic (a true or false flag that is converted to a target acousticness value of 0.85 for acoustic preference or 0.15 for electronic preference). This direct mapping is what makes weighted proximity scoring possible — every user preference has a corresponding song attribute to compare agains

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

