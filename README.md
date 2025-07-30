# 📊 Campaign Performance Report (Meta & TikTok)

This project simulates and analyzes campaign performance data across Meta and TikTok platforms. The goal is to practice data analysis workflows from data generation to insight extraction, with a focus on digital marketing metrics.

---

## 📁 Project Structure

```

campaign-performance-report/
├── data/
│   ├── meta\_campaign\_data.csv
│   ├── tiktok\_campaign\_data.csv
├── notebooks/
│   └── generate\_mock\_data.py
├── scripts/
│   └── campaign\_analysis.ipynb
├── .gitignore
├── README.md
└── requirements.txt

```

---

## 🎯 Objectives

- Simulate campaign data for Meta and TikTok platforms.
- Analyze campaign performance across multiple dimensions:
  - By platform (Meta vs TikTok)
  - By campaign name
  - By device type
- Visualize trends in impressions, clicks, conversions, and cost efficiency.
- Extract actionable insights to optimize ad spending.

---

## 🧰 Tech Stack

- **Language**: Python
- **Libraries**:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `random`, `datetime`

---

## 📌 Key Metrics Simulated

| Metric            | Description                                        |
|-------------------|----------------------------------------------------|
| `impressions`     | Number of ad views                                 |
| `clicks`          | Number of user clicks                              |
| `conversions`     | Number of desired actions (purchase/sign-up)       |
| `spend`           | Amount spent on campaign                           |
| `platform`        | Ad platform (Meta or TikTok)                       |
| `device`          | Device category (Mobile or Desktop)                |
| `CTR`             | Click Through Rate = Clicks / Impressions          |
| `CVR`             | Conversion Rate = Conversions / Clicks             |
| `CPA`             | Cost Per Action = Spend / Conversions              |

---

## 📈 Sample Analysis & Visualizations

- Top-performing campaigns based on conversion rate
- Cost efficiency by platform and device
- Correlation between spend and conversions
- Platform trends: Meta vs TikTok in engagement and ROI

---

## 🔍 Key Insights

- Meta campaigns generally have a higher CTR, while TikTok shows better CPA on mobile.
- Desktop users convert at a higher rate on Meta.
- Campaign C3 shows high engagement but low conversion, indicating creative or targeting issues.

---

## ✅ Next Steps

- Integrate real data sources (Meta Ads API, TikTok Ads API)
- Build dashboard version in Streamlit or Tableau
- Include time-based trend analysis for monthly performance

---

## 👤 Author

- **Name:** Pham Ba Phuoc
- **GitHub:** https://github.com/pbphuoc3927/campaign-performance-report
- **LinkedIn:** https://www.linkedin.com/in/pham-ba-phuoc-61a02527a/