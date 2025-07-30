import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()
np.random.seed(42)

# Cấu hình output
DATA_DIR = r"C:\Users\phuoc\campaign-performance-report\data"
os.makedirs(DATA_DIR, exist_ok=True)

# Thông tin chiến dịch mẫu
campaigns = ['Summer Sale', 'Back to School', 'Xmas Promo', 'Flash Deal']
adsets = ['Retargeting', 'Prospecting', 'Broad', 'Lookalike']
platforms = ['Meta', 'TikTok']
devices = ['Mobile', 'Desktop']

def generate_mock_ads_data(platform, n=200):
    base_date = datetime.today()
    data = []
    for i in range(n):
        row = {
            "date": (base_date - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
            "campaign": random.choice(campaigns),
            "adset": random.choice(adsets),
            "platform": platform,
            "spend": round(np.random.uniform(10, 500), 2),
            "impressions": random.randint(500, 10000),
            "clicks": random.randint(30, 1000),
            "conversions": random.randint(5, 100),
            "revenue": round(np.random.uniform(20, 2000), 2),
            "device": random.choice(devices)
        }
        data.append(row)
    return pd.DataFrame(data)

# Generate và export
meta_df = generate_mock_ads_data("Meta")
tiktok_df = generate_mock_ads_data("TikTok")

meta_df.to_csv(f"{DATA_DIR}/meta_ads.csv", index=False)
tiktok_df.to_csv(f"{DATA_DIR}/tiktok_ads.csv", index=False)

print("✅ Mock data generated: meta_ads.csv & tiktok_ads.csv")