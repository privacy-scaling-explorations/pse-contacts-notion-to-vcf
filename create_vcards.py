import pandas as pd
import vobject

from config import DEFAULT_VCF_VERSION


def create_vcards(contacts_df):
    if not isinstance(contacts_df, pd.DataFrame):
        raise TypeError("contacts_df must be a pandas DataFrame")
    if contacts_df.empty:
        raise ValueError("contacts_df must not be empty")
    if contacts_df is None:
        raise ValueError("contacts_df must not be None")

    vcards = []
    # create a vCard for each row in the dataframe
    for index, row in contacts_df.iterrows():
        vcard = vobject.vCard()
        vcard.add("version").value = DEFAULT_VCF_VERSION

        try:
            vcard.add("org").value = row["org"]

            for key in ["fn", "nickname", "tz", "email"]:
                # only if value is not null or not na or not empty string
                if row[key] and not pd.isna(row[key]) and row[key].strip():
                    vcard.add(key).value = row[key]

            for key in ["discord", "telegram", "github"]:
                if row[key] and not pd.isna(row[key]) and row[key].strip():
                    vcard.add(f"x-{key}").value = row[key]

            vcards.append(vcard.serialize())
        except AttributeError:
            print(f"Missing required data in row {index}, skipping this contact.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit(1)

    return vcards
