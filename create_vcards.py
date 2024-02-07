import pandas as pd
import vobject


def create_vcards(contacts_df):
    vcards = []
    # create a vCard for each row in the dataframe
    for index, row in contacts_df.iterrows():
        # print(row["org"])
        # create a vCard
        vcard = vobject.vCard()

        vcard.add("version").value = "4.0"
        vcard.add("org").value = row["org"]

        for key in ["fn", "nickname", "tz", "email"]:
            # only if value is not null or not na or not empty string
            if row[key] and not pd.isna(row[key]) and row[key].strip():
                vcard.add(key).value = row[key]

        for key in ["discord", "telegram", "github"]:
            if row[key] and not pd.isna(row[key]) and row[key].strip():
                vcard.add(f"x-{key}").value = row[key]

        vcards.append(vcard.serialize())

    return vcards
