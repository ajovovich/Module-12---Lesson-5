from flask import Flask, jsonify

#Task 1
def merge_sort(titles):
    if len(titles) <= 1:
        return titles

    def merge(left, right):
        sorted_list = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list

    mid = len(titles) // 2
    left_half = merge_sort(titles[:mid])
    right_half = merge_sort(titles[mid:])
    return merge(left_half, right_half)


video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

sorted_titles = merge_sort(video_titles)
print(sorted_titles)

#Task 2

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

@app.route('/sort', methods=['GET'])
def sort_videos():
    sorted_titles = merge_sort(video_titles)
    return jsonify(sorted_titles)

if __name__ == '__main__':
    app.run(debug=True)

