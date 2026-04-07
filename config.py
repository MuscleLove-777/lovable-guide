"""Lovableバイブコーディング完全ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Lovableバイブコーディング完全ガイド"
BLOG_DESCRIPTION = "AIアプリビルダーLovableの使い方・最新機能・Bolt.new比較を毎日更新。コード不要でフルスタックアプリを作る方法を完全解説。"
BLOG_URL = "https://musclelove-777.github.io/lovable-guide"
BLOG_TAGLINE = "Lovableでコード不要のフルスタックアプリ開発を実現するための日本語情報サイト"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/lovable-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Lovable 使い方",
    "Lovable 料金・プラン",
    "Lovable vs Bolt.new",
    "Lovable 最新ニュース",
    "バイブコーディング",
    "Lovable テクニック",
    "AIアプリビルダー比較",
    "Lovable 活用事例",
]

THEME = {
    "primary": "#ff6b6b",
    "accent": "#ffd93d",
    "gradient_start": "#ff6b6b",
    "gradient_end": "#ffd93d",
    "dark_bg": "#1a0a0f",
    "dark_surface": "#2d1520",
    "light_bg": "#fff5f5",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [8, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Lovable": [
        {"service": "Lovable", "url": "https://lovable.dev", "description": "Lovableでアプリを作る"},
    ],
    "Bolt.new": [
        {"service": "Bolt.new", "url": "https://bolt.new", "description": "Bolt.newを試す"},
    ],
    "Replit": [
        {"service": "Replit", "url": "https://replit.com", "description": "Replit Agentを使う"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI開発講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8098

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-HJLCFVY5TF"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
