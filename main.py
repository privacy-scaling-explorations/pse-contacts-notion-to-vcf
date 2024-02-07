from cli import parse_args
from parse_notion_csv import parse_notion_csv
from create_vcards import create_vcards

if __name__ == "__main__":
    args = parse_args()
    notion_csv_file_path = args.input
    vcf_file_path = args.output

    with open(vcf_file_path, "w") as f:
        for vcard in create_vcards(parse_notion_csv(notion_csv_file_path)):
            f.write(vcard)
