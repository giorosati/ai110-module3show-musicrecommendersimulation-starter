# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Song Genie

---

## 2. Intended Use  

This recommender generates ranked song suggestions from a 20-track catalog based on a declared user taste profile. It assumes the user can accurately describe their preferences in advance using genre, mood, energy level, and acoustic preference — there is no behavioral learning or implicit feedback. It is designed as a functional content-based filtering system that demonstrates real recommendation mechanics, and while it currently uses a small catalog for development and testing, it is built to scale as the catalog grows and is not limited to classroom use.

---

## 3. How the Model Works  

Every song in the catalog is described by six attributes: its genre (like pop, jazz, or lofi), its mood (like happy, chill, or intense), and four numeric qualities measured on a scale from 0 to 1 — energy, acousticness, valence (how positive or bright it sounds), and danceability. The user provides a taste profile that sets a target value for each of these attributes, plus a flag for whether they prefer acoustic or electronic-sounding music.

To score a song, the system checks each attribute one at a time. For genre and mood, the song either matches or it does not — a match adds a fixed number of points. For the numeric features, the score is based on how close the song's value is to the user's target: a perfect match earns the full points for that feature, and the score decreases the further apart the two values are. All six feature scores are added together to produce a single number for that song. Every song in the catalog is scored this way, then sorted from highest to lowest, and the top results are returned.

The main change from the starter logic was replacing a placeholder that returned songs in their original order with this weighted proximity approach, and separating the scoring of one song from the ranking of all songs so each piece of logic stays focused and easy to adjust.

---

## 4. Data  

The catalog contains 20 songs across 17 genres including pop, lofi, rock, jazz, ambient, synthwave, indie pop, hip-hop, classical, r&b, metal, folk, country, edm, blues, reggae, and latin. Moods represented include happy, chill, intense, relaxed, focused, moody, energetic, peaceful, romantic, angry, nostalgic, uplifting, and melancholic. The original starter dataset had 10 songs — 10 additional songs were added to increase genre and mood diversity and extend the numeric range of features like tempo and energy.

Despite this expansion, several parts of musical taste are absent or underrepresented. No songs represent K-pop, indie rock, gospel, soul, funk, or classical crossover genres. The catalog skews toward Western music styles and contains no non-English language genres beyond a single latin track. Lofi is the only genre with more than one song (three entries), giving lofi users a structural advantage in result variety that users of every other genre do not have. The data was manually authored rather than sourced from real listening data, so the attribute values reflect the author's judgment rather than measured audio features.

---

## 5. Strengths  

The system works best for users whose taste sits clearly at one end of the spectrum — either high-energy electronic listeners or low-energy acoustic listeners. For both extremes, the energy and acousticness features pull in the same direction and the top results feel immediately correct. The pop/happy profile consistently surfaced Sunrise City as the top result across all weight configurations, which matched intuition since it was the only song with both a genre and mood match combined with a close energy value. The jazz/peaceful and chill/lofi profiles also produced sensible top results, correctly separating Coffee Shop Stories from Focus Flow based on genre and mood bonuses even though both songs have similar numeric profiles.

The scoring captures two patterns particularly well. First, it correctly penalizes songs that are far from the user's energy target even if everything else matches — a high-energy user will not be recommended a quiet ambient track regardless of genre. Second, the acousticness feature cleanly separates electronic from organic-sounding music, which is one of the most perceptible differences between genres like edm and folk. A user who says they dislike acoustic music will reliably get electronic, produced-sounding tracks at the top of their list, and vice versa.  

---

## 6. Limitations and Bias 

The most significant weakness discovered during testing is the genre hard wall — because genre matching is all-or-nothing, a song in a closely related genre (such as "indie pop" for a "pop" user) receives zero genre points and can rank below a weaker match that happens to share the exact genre label. Under the standard weights, the genre bonus represents 24% of the maximum possible score, making this the single largest source of unfair results. A sensitivity test that halved the genre weight immediately allowed Rooftop Lights and Concrete Jungle to break into the top 5 for the pop/happy profile, confirming that the genre penalty was suppressing songs the user would likely enjoy. A second weakness is the binary acousticness target, which maps a user's acoustic preference to either 0.85 or 0.15 — penalizing moderately acoustic genres like r&b, reggae, and country for any user, regardless of their actual preference. Together these two biases mean the system tends to over-reward users whose declared genre has multiple catalog entries and whose taste falls near the acoustic extremes, while underserving users with nuanced or cross-genre preferences.

---

## 7. Evaluation  

Five distinct user profiles were tested to verify the recommender behaved as expected across a range of preferences: Pop / Happy (high energy, electronic), Jazz / Peaceful (low energy, acoustic), High-Energy EDM (maximum energy, high danceability), Chill Lofi (low energy, focused, acoustic), and Deep Intense Rock (high energy, low valence). For each profile, the expected top results were defined in advance and compared against the actual output — for example, the jazz profile was expected to surface Coffee Shop Stories and Moonlight Sonata Dreams, which it did.

The most surprising result came from a sensitivity test that doubled the energy weight and halved the genre weight. Under those conditions, Rooftop Lights (indie pop) overtook Gym Hero (pop) for the pop/happy profile because its energy (0.76) was closer to the target (0.80) than Gym Hero's (0.93), and two non-pop songs — Concrete Jungle and Night Drive Loop — broke into the top 5 entirely on energy proximity alone. This confirmed that under the standard weights, the genre bonus was actively suppressing songs the user would likely enjoy.

A second comparison was run between the jazz/peaceful profile and the chill/lofi profile to verify the scorer responded correctly to similar but distinct preferences — both are low-energy and acoustic, but the genre and mood bonuses correctly separated their top results. Output from every test run was saved automatically to `output/recommendations.txt` for side-by-side review.

---

## 8. Future Work  

The most impactful improvement would be replacing the binary acousticness flag with a continuous numeric target, allowing users to express a preference anywhere on the 0 to 1 scale rather than being forced to choose between two extremes. A second improvement would be adding partial credit for adjacent genres — grouping genres into families (pop / indie pop / r&b, or folk / country / blues) and awarding a smaller genre bonus for songs in the same family rather than zero points for any non-exact match. This would directly address the genre hard wall bias identified during testing.

For diversity, a simple rule limiting the top results to at most two songs per genre would prevent cases where a user receives five nearly identical tracks. Handling more complex tastes would require moving beyond a single declared profile — for example, allowing users to define a primary and secondary preference, or weighting recent listening history more heavily than a static profile.

**What this system is designed for:** Exploring how content-based recommendation logic works, testing how weight changes affect rankings, and serving as a foundation for a larger catalog-based recommender. It is well suited to cases where preferences can be stated explicitly and transparency in how recommendations are made matters more than surprise or serendipity.

**What it should not be used for:** Recommending music to real users in a production setting. The catalog is too small to provide meaningful variety, preferences are declared rather than learned, and the system has no ability to adapt to changing taste over time or detect when a user's stated preferences do not match their actual listening behavior.

---

## 9. Personal Reflection  

Building this recommender made it clear that the hardest part of a recommendation system is not the math — it is deciding what to measure and how much each measurement should matter. Before this project, features like energy or acousticness felt like abstract data points, but after watching how changing a single weight shifted an entire ranking, it became obvious how much these design choices shape what a user actually experiences.

The most unexpected discovery was how much the genre bonus was doing behind the scenes. During the sensitivity test, halving the genre weight immediately brought two songs into the top five that had been invisible under the standard configuration — not because they were bad matches, but because the genre penalty had been quietly overruling the numeric evidence. That felt like a real insight into how real-world systems can encode bias invisibly, not through bad intentions but through design decisions that seem reasonable until you test them.

This changed how I think about apps like Spotify or YouTube. What looks like a smart, personalized recommendation is really the output of hundreds of weight decisions made by engineers — and those weights determine whose taste gets served well and whose gets ignored. Building even a simple version of this system makes it much harder to take a recommendation at face value without wondering what assumptions are buried inside it.

I was surprised that AI made a very simple error in calculating the total possible points during my testing different weights. As I switched back and forth with different weights, AI actually caught its error, which was also surprising.

I would like to expand the database of songs to hundreds of entries of which I am familiar with. With this expanded data I could better evaluate how well the weights and algorithm choices are matching what I think the recommendations should be. 
