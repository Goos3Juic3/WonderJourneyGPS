def score_places(places, category_weights):
    scored = []

    for place in places:
        preference_score = category_weights.get(place["type"], 0)
        rating_boost = place["rating"] - 3
        total_score = round(preference_score + rating_boost, 2)

        scored_place = {
            **place,
            "score": total_score,
            "label": "LIKE" if total_score > 0 else "DISLIKE"
        }
        scored.append(scored_place)

    scored.sort(key=lambda p: p["score"], reverse=True)
    return scored


def build_pros_and_cons(scored_places, limit=3):
    pros = [
        f'{place["name"]} ({place["type"]})'
        for place in scored_places
        if place["label"] == "LIKE"
    ][:limit]

    cons = [
        f'{place["name"]} ({place["type"]})'
        for place in scored_places
        if place["label"] == "DISLIKE"
    ][:limit]

    return pros, cons
