from flask import Flask, request, jsonify, Response, render_template_string
from feedgen.feed import FeedGenerator
import os
import json

app = Flask(__name__)

DATA_FILE = "data.json"

# Secret token for simple authentication
SECRET_TOKEN = os.environ.get('AUTH_TOKEN', 'your-secret-token')

# Ensure data file exists at startup
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def authenticate():
    # Check for valid token in query params
    token = request.args.get('auth')
    if not token or token != SECRET_TOKEN:
        return jsonify({"error": "Unauthorized: Invalid or missing token"}), 403

@app.route('/')
def home():
    # Simple loading page with redirect to external site
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    ...
    </html
    """
    return render_template_string(html_content)

@app.route('/add', methods=['POST'])
def add_article():
    auth_response = authenticate()
    if auth_response:
        return auth_response

    # Accept both JSON and form-data
    data = None
    if request.is_json:
        data = request.json
    else:
        data = request.form.to_dict()

    # Validate required fields
    if not all(key in data for key in ("title", "url", "content")):
        return jsonify({"error": "Missing fields (title, url, content required)"}), 400

    # Append new article to JSON file
    with open(DATA_FILE, "r+") as f:
        articles = json.load(f)
        articles.append(data)
        f.seek(0)
        json.dump(articles, f, indent=4)

    return jsonify({"message": "Article added successfully"}), 201

@app.route('/rss', methods=['GET'])
def rss_feed():
    auth_response = authenticate()
    if auth_response:
        return auth_response

    # Load stored articles and generate RSS feed
    with open(DATA_FILE, "r") as f:
        articles = json.load(f)

    fg = FeedGenerator()
    fg.title("Read Later")
    fg.link(href="http://readlater.maik.io", rel="self")
    fg.description("My little read later service")

    for article in articles:
        fe = fg.add_entry()
        fe.title(article["title"])
        fe.link(href=article["url"])
        fe.description(article["content"])

    rss_data = fg.rss_str(pretty=True)
    return Response(rss_data, mimetype='application/rss+xml')

@app.route('/articles', methods=['GET'])
def list_articles():
    auth_response = authenticate()
    if auth_response:
        return auth_response

    # Return all articles as JSON
    with open(DATA_FILE, "r") as f:
        articles = json.load(f)
    return jsonify(articles)

if __name__ == '__main__':
    # Run app on all interfaces, default port 8080
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
