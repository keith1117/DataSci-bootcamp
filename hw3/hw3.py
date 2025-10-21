import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CSV_PATH = "Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project_20251017.csv"

DATETIME_COL = hour_beginning
COUNT_COL    = Pedestrians
WEATHER_COL  = weather_summary
LOCATION_COL = location

df = pd.read_csv(CSV_PATH)

def pick(cols, *candidates):
    low = {c.lower(): c for c in cols}
    for cand in candidates:
        for k, v in low.items():
            if cand in k:
                return v
    return None

if DATETIME_COL is None:
    DATETIME_COL = pick(df.columns, "datetime", "date_time", "timestamp", "date")
if COUNT_COL is None:
  
    COUNT_COL = pick(df.columns, "count", "pedestr", "brooklyn")
if WEATHER_COL is None:
    WEATHER_COL = pick(df.columns, "weather", "wx", "conditions", "summary")
if LOCATION_COL is None:
    LOCATION_COL = pick(df.columns, "location", "bridge", "site")

need = {"DATETIME_COL": DATETIME_COL, "COUNT_COL": COUNT_COL}
for k, v in need.items():
    if v is None:
        raise ValueError(f"Could not infer {k}. Please set it at the top of the script.")

df[DATETIME_COL] = pd.to_datetime(df[DATETIME_COL], errors="coerce")
df = df.dropna(subset=[DATETIME_COL, COUNT_COL])

if LOCATION_COL and LOCATION_FILTER_VALUE:
    df = df[df[LOCATION_COL].astype(str).str.contains(LOCATION_FILTER_VALUE, case=False, na=False)]

# Q1
wk = df[df[DATETIME_COL].dt.weekday < 5].copy()
wk["weekday_name"] = wk[DATETIME_COL].dt.day_name()

order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekday_counts = (wk.groupby("weekday_name")[COUNT_COL]
                    .sum()
                    .reindex(order))

print("\n[Q1] Weekday totals (Mon–Fri):")
print(weekday_counts)

plt.figure()
weekday_counts.plot(marker="o")
plt.title("Weekday Pedestrian Counts (Mon–Fri)")
plt.xlabel("Weekday")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Q2
df19 = df[df[DATETIME_COL].dt.year == YEAR].copy()

if WEATHER_COL is not None and WEATHER_COL in df19.columns:
    wx_dummies = pd.get_dummies(df19[WEATHER_COL].astype(str), prefix="wx")
    corr_matrix = pd.concat([df19[[COUNT_COL]].reset_index(drop=True), wx_dummies.reset_index(drop=True)], axis=1).corr()

    print(f"\n[Q2] Correlation matrix (counts vs. weather dummies) for {YEAR}:")
    print(corr_matrix.round(3))

    print(f"\n[Q2] Correlation with {COUNT_COL} (sorted):")
    print(corr_matrix[COUNT_COL].sort_values(ascending=False).round(3))
else:
    print("\n[Q2] No weather column detected; set WEATHER_COL at the top if available.")

# Q3
def time_of_day_from_hour(h):
    if   5 <= h < 12:  return "morning"
    elif 12 <= h < 17: return "afternoon"
    elif 17 <= h < 21: return "evening"
    else:              return "night"

df["hour"] = df[DATETIME_COL].dt.hour
df["time_of_day"] = df["hour"].apply(time_of_day_from_hour)

tod_summary = (df.groupby("time_of_day")[COUNT_COL]
                 .mean()
                 .reindex(["morning","afternoon","evening","night"]))

print("\n[Q3] Average pedestrian counts by time-of-day:")
print(tod_summary)

plt.figure()
tod_summary.plot(kind="bar")
plt.title("Average Pedestrian Counts by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Average Count")
plt.tight_layout()
plt.show()
