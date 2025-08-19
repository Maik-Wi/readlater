# Read Later RSS Service

This is a small Flask-based web application that provides a simple "read later" service.
It allows you to save articles (title, URL, and content) and then access them via an RSS feed or a JSON API.

## Features
- Save articles through a POST request (`/add`).
- Retrieve all saved articles as JSON (`/articles`).
- Get an RSS feed of all saved articles (`/rss`).
- Simple token-based authentication via `?auth=YOUR_TOKEN`.
- Minimal landing page with redirect.

## Deployment
The app is deployed and running on [fly.io](https://fly.io).

## Compatibility
This service is compatible with the **"Read Later"** function of **[Bibbot](https://github.com/stefanw/bibbotp)**.

## Running locally
1. Clone the repository
```bash
git clone https://github.com/yourusername/read-later-service.git
cd read-later-service
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
AUTH_TOKEN=your-secret-token flask run --host=0.0.0.0 --port=8080
```

## Endpoints
- /add (POST) – Add a new article (title, url, content required).
- /articles (GET) – List all saved articles.
- /rss (GET) – RSS feed with all saved articles.
- /?auth=TOKEN – Authentication is required for all protected endpoints.

## License
[GPLv3](https://github.com/Maik-Wi/readlater/blob/main/LICENSE)
