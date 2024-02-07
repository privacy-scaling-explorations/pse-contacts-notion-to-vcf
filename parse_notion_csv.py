import re

import pandas as pd

from config import PATTERNS, DEFAULT_NOTION_CONTACTS_CSV_FILE_PATH
from utils import clean_name_col, clean_projects_teams_col


def parse_notion_csv(
    file_path: str = DEFAULT_NOTION_CONTACTS_CSV_FILE_PATH,
) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)

        for category, pattern_dict in PATTERNS.items():
            for key, pattern in pattern_dict.items():
                # treat category column as string
                extracted = df[category].str.extract(pattern, flags=re.IGNORECASE)
                # keep only the first match if there are multiple matches
                df[key] = extracted.iloc[:, 0]
                # remove any whitespace in the values of the key column
                df[key] = df[key].str.strip()
                if key in ["discord", "github", "telegram"]:
                    df[key] = df[key].str.replace("@", "")

        df["tz"] = df["tz"].str.replace(" ", "")
        df["tz"] = df["tz"].str.replace("UTC+", "GMT-")
        df["tz"] = df["tz"].str.replace("UTC-", "GMT+")
        # make tz column the concatenation of "Etc/" and the value of the tz column
        df["tz"] = "Etc/" + df["tz"]

        df["nickname"] = df[
            ["Notion Handle", "discord", "telegram", "github", "ENS Address"]
        ].apply(lambda x: ",".join(set(x.dropna())), axis=1)

        df.rename(columns={"Name": "fn"}, inplace=True)
        df["fn"] = df["fn"].apply(clean_name_col)

        df["org"] = df["Projects & Teams"].apply(clean_projects_teams_col)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except pd.errors.ParserError:
        print(f"Invalid CSV file: {file_path}")
        exit(1)
    except pd.errors.EmptyDataError:
        print(f"Empty CSV file: {file_path}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)

    return df
