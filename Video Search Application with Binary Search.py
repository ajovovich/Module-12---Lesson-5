from flask import Flask, request, jsonify

def binary_search(titles, target):
    left, right = 0, len(titles) - 1
    while left <= right:
        mid = (left + right) // 2
        if titles[mid] == target:
            return mid
        elif titles[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


video_titles = [
    "Artificial Intelligence Revolution",
    "Cooking Masterclass: Italian Cuisine",
    "Digital Photography Essentials",
    "Exploring the Cosmos",
    "Financial Planning for Beginners",
    "Fitness Fundamentals: Strength Training",
    "History Uncovered: Ancient Civilizations",
    "Nature's Wonders: National Geographic",
    "The Art of Coding",
    "Travel Diaries: Discovering Europe"
]


video_titles.sort()

index = binary_search(video_titles, "The Art of Coding")
print(f"Video found at index: {index}" if index != -1 else "Video not found")

#Task 2
app = Flask(__name__)


video_titles.sort()

@app.route('/search', methods=['GET'])
def search_video():
    query = request.args.get('title', '')
    index = binary_search(video_titles, query)
    if index != -1:
        return jsonify({"message": "Video found", "title": video_titles[index]})
    else:
        return jsonify({"message": "Video not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

