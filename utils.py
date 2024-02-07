import re


def clean_projects_teams_col(input_str):
    if isinstance(input_str, str):
        # Use regular expression to remove content within brackets
        cleaned_str = re.sub(
            r"\(.*?\)",
            "",
            input_str.replace("  ", " ")
            .replace(" (", "(")
            .replace(" / ", "/")
            .replace(" - ", "-"),
        )

        # Trim the resulting string
        cleaned_str = cleaned_str.strip()
        return ["PSE", cleaned_str]
    else:
        return ["PSE"]


def clean_name_col(input_str):
    cleaned_str = re.sub(r"\(.*?\)", "", input_str)
    return cleaned_str.strip()
