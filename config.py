PATTERNS = {
    "Contact Info": {
        "discord": r"(?:discord:)\s*(@?\w+)(?:#\d+)?",
        "github": r"(?:github:)\s*(?:https?://github.com/)?(@?\w+)",
        "email": r"(?:email:)\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})",
        "telegram": r"(?:telegram:|tg:)\s*(?:https?://t.me/)?(@?\w+)",
    },
    "Availability": {"tz": r"((UTC|GMT)\s*([+-]?\d{1,2})?)"},
    # Add more patterns as needed
}

DEFAULT_NOTION_CONTACTS_CSV_FILE_PATH = "data/pse-notion-contacts-dir-export-240130.csv"
DEFAULT_VCF_FILE_PATH = "data/PSE.vcf"
