# Home.py
LOGO_FILENAME = "kovue_logo.jpg" # 로고 파일 이름
PAGE_TITLE = "Kovue" # 페이지 제목
PAGE_ICON = "🎯" # 페이지 아이콘
PAGE_ROUTES = {
    "insight": {
        "label": "🧪 1. Ingredients & Insight",
        "path": "pages/1_Ingredients& Insight.py"
    },
    "reddit": {
        "label": "📊 2. Globlal_Trend(reddit)",
        "path": "pages/2_Globlal_Trend(reddit).py"
    },
    "youtube": {
        "label": "📈 3. Gobal_Tremd(youtube)",
        "path": "pages/3_Gobal_Tremd(youtube).py"
    },
    "seeding": {
        "label": "🌱 4. Seeding",
        "path": "pages/4_Seeding.py"
    },
    "performance": {
        "label": "📉 5. Performance",
        "path": "pages/5_Performance.py"
    }
}
SPACING_LARGE = 3
COLUMN_RATIO_LOGO = [1, 2, 1]
START = "시작하기"
BACK = "← 홈으로 돌아가기"