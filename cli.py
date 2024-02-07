import argparse

from config import DEFAULT_NOTION_CONTACTS_CSV_FILE_PATH, DEFAULT_VCF_FILE_PATH


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert PSE Notion csv contacts to vcf format"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default=DEFAULT_NOTION_CONTACTS_CSV_FILE_PATH,
        help="Notion contacts csv file path",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=DEFAULT_VCF_FILE_PATH,
        help="VCF output file path",
    )
    return parser.parse_args()
