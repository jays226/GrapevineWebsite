from flask import Flask, request, redirect, make_response, url_for, session, render_template, jsonify
# from werkzeug.urls import quote as url_quote

import os

app = Flask('GrapevineHealth')

### TAGS: testimonials, diabetes, heart (dropdown menu)
### SEARCH BAR TO FILTER
### LIKED VIDEOS GO TO FAVORITES


def mp4helper() -> list:
    titles = []
    for i in os.listdir('static/videos'):
        titles.append({
            'title': i.split('.mp4')[0],
            'video_path': 'videos/' + i,
            'tags': []
        })
    return titles


videos = mp4helper()


@app.route('/')
def home():
    return redirect(url_for('library', external=True))


@app.route('/library')
def library():
    return render_template('library.html', videos=videos)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    filtered_videos = [video for video in videos if query in video.lower()]
    return jsonify(filtered_videos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
