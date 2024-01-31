# This is a sample Python script.

# Press Ctrl+Alt+R to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import vobject
import re

FILE_NAME = 'pse-notion-contacts-dir-export-240130'

patterns = {
    'Contact Info': {
        'discord': r'(?:discord:)\s*(@?\w+)(?:#\d+)?',
        'github': r'(?:github:)\s*(?:https?://github.com/)?(@?\w+)',
        'email': r'(?:email:)\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})',
        'telegram': r'(?:telegram:|tg:)\s*(@?\w+)',
    },
    'Availability': {'tz': r'((UTC|GMT)\s*([+-]?\d{1,2})?)'}
    # Add more patterns as needed
}


def clean_projects_teams_col(input_str):
    if isinstance(input_str, str):
        # Use regular expression to remove content within brackets
        cleaned_str = re.sub(r'\(.*?\)', '', input_str)

        # Trim the resulting string
        cleaned_str = cleaned_str.strip()
        return f"PSE ({cleaned_str})"
    else:
        return "PSE"


def clean_name_col(input_str):
    cleaned_str = re.sub(r'\(.*?\)', '', input_str)
    return cleaned_str.strip()


def parse_csv():
    df = pd.read_csv(f"data/{FILE_NAME}.csv")

    for category, pattern_dict in patterns.items():
        for key, pattern in pattern_dict.items():
            # treat category column as string
            extracted = df[category].str.extract(pattern, flags=re.IGNORECASE)
            # keep only the first match if there are multiple matches
            df[key] = extracted.iloc[:, 0]
            # remove any whitespace in the values of the key column
            df[key] = df[key].str.strip()

    df['tz'] = df['tz'].str.replace('GMT', 'UTC')

    df['nickname'] = df[['Notion Handle', 'discord', 'telegram', 'github', "ENS Address"]].apply(
        lambda x: ','.join(x.dropna()), axis=1)

    df.rename(columns={'Name': 'fn'}, inplace=True)
    df['fn'] = df['fn'].apply(clean_name_col)

    df['org'] = df['Projects & Teams'].apply(clean_projects_teams_col)

    return df


def create_vcards(contacts_df):
    vcards = []
    # create a vCard for each row in the dataframe
    for index, row in contacts_df.iterrows():
        # create a vCard
        vcard = vobject.vCard()

        for key in ['fn', 'nickname', 'org', 'tz', 'email']:
            # only if value is not null or not na or not empty string
            if row[key] and not pd.isna(row[key]) and row[key].strip():
                vcard.add(key).value = row[key]

        for key in ['discord', 'telegram', 'github']:
            if row[key] and not pd.isna(row[key]) and row[key].strip():
                vcard.add(f"x-{key}").value = row[key]

        vcards.append(vcard)

    return vcards


def write_vcf(contacts_df):
    with open(f"data/pse.vcf", 'w') as f:
        for vcard in create_vcards(contacts_df):
            # print(vcard.serialize())
            f.write(vcard.serialize())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    contacts = parse_csv()
    cards = create_vcards(contacts)
    print(cards)
    write_vcf(parse_csv())
