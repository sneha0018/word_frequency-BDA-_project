
from flask import Flask, render_template, request, jsonify
from collections import defaultdict
from time import perf_counter
import re

app = Flask(__name__)


def map_phase(text):
    words = re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())
    return [(word, 1) for word in words]


def shuffle_sort_phase(mapped_data):
    grouped_words = defaultdict(list)

    for word, count in mapped_data:
        grouped_words[word].append(count)

    return grouped_words


def reduce_phase(grouped_words):
    return {
        word: sum(counts)
        for word, counts in grouped_words.items()
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Please enter some text to analyze."}), 400

    start = perf_counter()

    mapped_data = map_phase(text)
    grouped_words = shuffle_sort_phase(mapped_data)
    word_counts = reduce_phase(grouped_words)

    processing_time = round((perf_counter() - start) * 1000, 2)

    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return jsonify({
        "total_words": len(mapped_data),
        "unique_words": len(word_counts),
        "most_frequent": sorted_words[0][0] if sorted_words else "-",
        "processing_time": processing_time,
        "results": [
            {"word": word, "count": count}
            for word, count in sorted_words
        ],
        "map_sample": mapped_data[:20],
        "groups": {
            word: counts
            for word, counts in sorted(grouped_words.items())
        }
    })


if __name__ == "__main__":
    app.run(debug=True)




# run (python app.py )