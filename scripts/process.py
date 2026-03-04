import io

import pandas as pd
import requests

header = [
    "Code value",
    "Character name",
    "General category",
    "Canonical combining classes",
    "Bidirectional category",
    "Character decomposition mapping",
    "Decimal digit value",
    "Digit value",
    "Numeric value",
    "Mirrored",
    "Unicode 1.0 Name",
    "10646 comment field",
    "Uppercase mapping",
    "Lowercase mapping",
    "Titlecase mapping",
]

source_url = "https://www.unicode.org/Public/UNIDATA/UnicodeData.txt"
response = requests.get(source_url, timeout=60)
response.raise_for_status()

raw_data = response.text
df = pd.read_csv(io.StringIO(raw_data), delimiter=";", keep_default_na=False)
df_modified = pd.read_csv(
    io.StringIO(raw_data), delimiter=";", names=header, keep_default_na=False
)


df.to_csv("archive/source.csv", index=False)

df_modified.to_csv("data/unicode-characters.csv", index=False)
