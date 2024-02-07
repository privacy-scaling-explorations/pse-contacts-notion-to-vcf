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
   
## Disclaimer
PSE members have access to a [notion contacts table](https://www.notion.so/pse-team/e86dfd0a581a43419c7052534b272502?v=6dfe68e736734b38a2e28cd139cada62) that contains personal information shared by the members themselves on a voluntary basis.   
This script just converts the information available there to a vcf file that can be used to import the contacts into 3rd party applications.  
It is not bug-free and will break as soon as the structure of the notion table changes.  
The output vcf file should be used responsibly: just like the information on notion, it should not be shared with non-members.

