# Notion contacts csv table to vcf

## Getting started

1. Export [PSE notion contacts page](https://www.notion.so/pse-team/e86dfd0a581a43419c7052534b272502?v=6dfe68e736734b38a2e28cd139cada62&pvs=13)
to csv.
2. Install deps: `poetry install`
3. Run the script with the path to the csv file as an argument
    ```commandline
    python main.py [-i /path/to/notion.csv] [-o /path/to/output.vcf]
    ```
   OR
   ```commandline
   poe exec [-i /path/to/notion.csv] [-o /path/to/output.vcf]
   ```