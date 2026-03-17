# 📊 Social Media Analytics Dashboard

> A comprehensive social media analytics project that analyses **8,000 posts** across **Instagram, YouTube, and Facebook** throughout 2024 — uncovering peak engagement times, best-performing content formats, platform-wise trends, and day-by-day performance insights using Python and Power BI.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Key Insights Covered](#key-insights-covered)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Power BI Dashboard](#power-bi-dashboard)
- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)

---

## Overview

This project dives deep into social media performance data across three major platforms — **Instagram, YouTube, and Facebook** — for the full year of **2024**. It answers critical questions every content creator and social media manager needs:

- 🕐 **When** is the best time to post for maximum engagement?
- 📅 **Which day** of the week drives the most interactions?
- 🎬 **What content format** (Reel, Video, Image, Shorts, Carousel, Text) performs best?
- 📱 **Which platform** dominates for each content category?
- 📈 **What is the engagement rate** trend across time slots and categories?

The analysis is delivered through both a **Python-based analytical pipeline** and an interactive **Power BI Dashboard** with DAX measures for dynamic KPIs.

---

## Key Insights Covered

### ⏰ Peak Time Analysis
- Engagement broken down by **Time Slot**: Morning, Afternoon, Evening, Night
- Hourly analysis (Hour 0–23) to pinpoint the exact best posting window
- Platform-specific peak times for Instagram, YouTube, and Facebook

### 📅 Day-of-Week Engagement
- Identifies the **most engaging day** (highest avg engagement rate)
- Identifies the **least engaging day** to avoid low-performance posting
- Heatmap of engagement by Day × Time Slot

### 🎬 Content Format Performance
- Compares **Reel, Video, Image, Shorts, Carousel, Text** formats
- Shows which format gets the most **Reach, Likes, Comments, Shares**
- Cross-analysis: which format performs best on which platform

### 📱 Platform Comparison
- Head-to-head metrics: Instagram vs YouTube vs Facebook
- Content category performance per platform:
  - 🎓 Education | 🏅 Sports | 💼 Business | 💻 Tech | 🌿 Lifestyle | 🎭 Entertainment

### 📊 Engagement Metrics Tracked
| Metric | Description |
|---|---|
| `Reach` | Total accounts the post reached |
| `Likes` | Number of likes received |
| `Comments` | Number of comments |
| `Shares` | Number of shares/retweets |
| `Engagement` | Total interactions (Likes + Comments + Shares) |
| `Engagement_Rate` | Engagement ÷ Reach (key performance indicator) |

---

## Dataset

**File:** `Social_Media_Analytics_2024_8k.csv`

| Property | Value |
|---|---|
| Total Records | 8,000 posts |
| Time Period | January 2024 – December 2024 |
| Platforms | Instagram, YouTube, Facebook |
| Content Categories | Education, Sports, Business, Tech, Lifestyle, Entertainment |
| Content Formats | Reel, Video, Image, Shorts, Text, Carousel |
| Time Slots | Morning, Afternoon, Evening, Night |

### Column Reference

| Column | Type | Description |
|---|---|---|
| `Platform` | String | Instagram / YouTube / Facebook |
| `Post_Date` | Date | Date of post (YYYY-MM-DD) |
| `Post_Time` | Time | Exact time of posting (HH:MM) |
| `Day` | String | Day of the week (Monday–Sunday) |
| `Hour` | Integer | Hour of posting (0–23) |
| `Time_Slot` | String | Morning / Afternoon / Evening / Night |
| `Content_Category` | String | Topic category of the post |
| `Content_Format` | String | Format type (Reel, Video, Image, etc.) |
| `Reach` | Integer | Total post reach |
| `Likes` | Integer | Number of likes |
| `Comments` | Integer | Number of comments |
| `Shares` | Integer | Number of shares |
| `Engagement` | Integer | Total interactions |
| `Engagement_Rate` | Float | Engagement ÷ Reach ratio |

---

## Project Structure

```
Social_Media_Analytical_Dashboard/
├── data/
│   └── Social_Media_Analytics_2024_8k.csv     # Main dataset (8,000 rows)
├── src/
│   ├── data_preprocessing.py                   # Data loading, cleaning, feature prep
│   ├── eda.py                                  # Exploratory data analysis & plots
│   ├── engagement_analysis.py                  # Peak time, day & format analysis
│   └── platform_comparison.py                  # Cross-platform performance metrics
├── powerbi/
│   └── Vishal_Social_Media_Insights_Analytics.pbix   # Power BI dashboard file
├── outputs/
│   ├── peak_time_heatmap.png
│   ├── day_engagement_chart.png
│   ├── platform_comparison.png
│   ├── content_format_performance.png
│   └── engagement_rate_trends.png
├── notebooks/
│   └── social_media_analysis.ipynb             # Full analysis notebook
├── requirements.txt
└── README.md
```

---

## Power BI Dashboard

The file `Vishal_Social_Media_Insights_Analytics.pbix` contains a fully interactive Power BI dashboard with:

### 📌 Dashboard Pages
| Page | Content |
|---|---|
| **Overview** | Total reach, likes, comments, shares KPIs across all platforms |
| **Engagement by Time** | Peak hour & time slot analysis with drill-through |
| **Day Analysis** | Best vs worst performing days per platform |
| **Content Performance** | Format-wise and category-wise engagement breakdown |
| **Platform Comparison** | Instagram vs YouTube vs Facebook side-by-side metrics |

### 🔢 Key DAX Measures Used
```dax
-- Average Engagement Rate
Avg Engagement Rate = AVERAGE('SocialMedia'[Engagement_Rate])

-- Total Reach
Total Reach = SUM('SocialMedia'[Reach])

-- Best Performing Day
Best Day = 
TOPN(1,
    SUMMARIZE('SocialMedia', 'SocialMedia'[Day], "AvgEng", [Avg Engagement Rate]),
    [AvgEng], DESC
)

-- Engagement Rate by Platform
Engagement by Platform = 
CALCULATE([Avg Engagement Rate],
    ALLEXCEPT('SocialMedia', 'SocialMedia'[Platform])
)

-- Peak Time Slot
Peak Time Slot =
TOPN(1,
    SUMMARIZE('SocialMedia', 'SocialMedia'[Time_Slot], "AvgEng", [Avg Engagement Rate]),
    [AvgEng], DESC
)
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Social_Media_Analytical_Dashboard.git
cd Social_Media_Analytical_Dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Run Python Analysis
```bash
# Full EDA and visualisations
python src/eda.py

# Engagement analysis (peak time, day, format)
python src/engagement_analysis.py

# Platform comparison
python src/platform_comparison.py
```

### Open Power BI Dashboard
1. Open **Power BI Desktop**
2. Load `powerbi/Vishal_Social_Media_Insights_Analytics.pbix`
3. Refresh data source pointing to `data/Social_Media_Analytics_2024_8k.csv`

### Run Jupyter Notebook
```bash
jupyter notebook notebooks/social_media_analysis.ipynb
```

---

## Tech Stack

| Tool / Library | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, groupby analysis |
| `numpy` | Numerical computations, aggregations |
| `matplotlib` | Static charts — bar, line, heatmaps |
| `seaborn` | Statistical visualisations — heatmaps, boxplots |
| `Power BI` | Interactive dashboard with slicers & drill-throughs |
| `DAX` | Custom KPI measures inside Power BI |
| `Jupyter Notebook` | Interactive exploratory analysis |

---

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/new-analysis`
3. Commit your changes: `git commit -m "Add platform-wise hourly breakdown"`
4. Push to the branch: `git push origin feature/new-analysis`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Vishal**
- GitHub: Vishal-ds-0308 
- Dataset: `Social_Media_Analytics_2024_8k.csv` — 8,000 posts across Instagram, YouTube & Facebook (2024)
