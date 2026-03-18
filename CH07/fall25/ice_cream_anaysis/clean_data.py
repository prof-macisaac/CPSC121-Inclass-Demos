# Read from 'ice_cream.csv' if it exists. If not, create it from the sample the user provided,
# then compute totals per month (across all years) and per year, and save the two requested CSVs.

import pandas as pd
from pathlib import Path
from io import StringIO
# from caas_jupyter_tools import display_dataframe_to_user

src_path = Path("ice_cream.csv")

# Fallback content from the user's sample if the file doesn't exist yet
fallback_csv = """DATE,IPN31152N
1972-01-01,59.9622
1972-02-01,67.0605
1972-03-01,74.2350
1972-04-01,78.1120
1972-05-01,84.7636
1972-06-01,100.5960
1972-07-01,100.1263
1972-08-01,96.3607
1972-09-01,85.8007
1972-10-01,70.3934
1972-11-01,60.8072
1972-12-01,58.6598
1973-01-01,61.0996
1973-02-01,72.2062
1973-03-01,80.0984
1973-04-01,83.9059
1973-05-01,87.3712
1973-06-01,109.7467
1973-07-01,107.3748
1973-08-01,99.6631
"""


# Load
df = pd.read_csv(src_path, parse_dates=["DATE"])
df = df.rename(columns={"IPN31152N": "sales"})
df["year"] = df["DATE"].dt.year
df["month"] = df["DATE"].dt.month
df["month_name"] = df["DATE"].dt.month_name()

# Aggregate: totals per calendar month across all years
per_month = (
    df.groupby(["month", "month_name"], as_index=False)["sales"]
      .sum()
      .sort_values("month")
      .rename(columns={"sales": "total_sales"})
)[["month", "month_name", "total_sales"]]

# Aggregate: totals per year
per_year = (
    df.groupby("year", as_index=False)["sales"]
      .sum()
      .rename(columns={"sales": "total_sales"})
      .sort_values("year")
)

# Save outputs
month_csv_path = "ice_cream_per_month.csv"
year_csv_path = "ice_cream_per_year.csv"
per_month.to_csv(month_csv_path, index=False)
per_year.to_csv(year_csv_path, index=False)

(month_csv_path, year_csv_path, str(src_path))
