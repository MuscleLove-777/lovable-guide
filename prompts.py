"""Lovableバイブコーディング完全ガイド - プロンプト定義

Lovable特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはAIアプリビルダーLovableの日本語エキスパートです。"
    "バイブコーディング（自然言語でアプリを作る手法）に精通し、"
    "初心者からプロダクト開発者まで幅広い読者に実践的な情報を届けるプロのテックライターです。"
    "Lovableの最新アップデートを常にキャッチアップし、"
    "Bolt.new、Replit Agent、v0などの競合AIビルダーとの比較も客観的に行えます。"
    "Supabase連携やStripe決済実装など、フルスタック開発の実装テクニックにも詳しいです。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な手順・解説。スクリーンショットの代わりに操作手順を箇条書きで明示）

## バイブコーディング実践テクニック
（プロンプトの書き方・修正指示のコツ・効率的な開発フロー）

## 他のAIビルダーとの比較
（Bolt.new / Replit Agent / v0 / Claude Artifacts との違いを表形式で整理）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "Lovable 使い方": "Lovable 使い方、Lovable 始め方、Lovable 初心者、Lovable 無料、Lovable アプリ開発",
    "Lovable 料金・プラン": "Lovable 料金、Lovable 無料 有料 違い、Lovable Pro プラン、Lovable 月額、Lovable クレジット",
    "Lovable vs Bolt.new": "Lovable Bolt.new 比較、Lovable Bolt.new 違い、AIビルダー 比較 2026、どっちがいい",
    "Lovable 最新ニュース": "Lovable アップデート、Lovable 新機能、Lovable リリース、AIビルダー 最新",
    "バイブコーディング": "バイブコーディング、vibe coding、バイブコーディング やり方、AI コーディング 自然言語",
    "Lovable テクニック": "Lovable Supabase 連携、Lovable Stripe 決済、Lovable デプロイ、Lovable カスタマイズ",
    "AIアプリビルダー比較": "AIアプリビルダー 比較、Replit Agent、v0 dev、Claude Artifacts、ノーコード AI",
    "Lovable 活用事例": "Lovable SaaS 開発、Lovable ポートフォリオ、Lovable LP作成、Lovable 副業、Lovable 事例",
}

# ニュースソース
NEWS_SOURCES = [
    "Lovable公式ブログ (https://lovable.dev/blog)",
    "Lovable公式X (https://x.com/lovaborai)",
    "TechCrunch (https://techcrunch.com/tag/ai-app-builder/)",
    "Product Hunt (https://www.producthunt.com/products/lovable)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "AIアプリビルダーLovableに関するキーワードを選んでください。\n"
    "日本のユーザーが検索しそうな実用的なキーワードを意識してください。\n"
    "「Lovable 使い方」「Lovable 料金」「Lovable vs Bolt.new」「バイブコーディング」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "Lovableバイブコーディング完全ガイド用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """Lovable特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、AIアプリビルダーLovableの専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- 具体的な操作手順やプロンプト例を含める
- Supabase連携・Stripe決済・デプロイ方法など実践的なテクニックを含める
- 他AIビルダーとの客観的な比較を含める
- 初心者にもわかりやすく、専門用語には補足説明を付ける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""
