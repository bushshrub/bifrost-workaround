"""Download the Bifrost model-parameters datasheet and add the rows in overrides.json."""
import json
import os
import sys
import urllib.request

SOURCE_URL = "https://getbifrost.ai/datasheet/model-parameters"
OUTPUT_DIR = "site"

request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "bifrost-workaround"})
with urllib.request.urlopen(request, timeout=120) as response:
    datasheet = json.load(response)
if not isinstance(datasheet, dict) or len(datasheet) < 1000:
    sys.exit(f"datasheet looks wrong: {type(datasheet).__name__} with {len(datasheet)} entries")

with open("overrides.json") as file:
    overrides = json.load(file)
datasheet.update(overrides)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "model-parameters.json"), "w") as file:
    json.dump(datasheet, file, separators=(",", ":"))
print(f"wrote {len(datasheet)} models ({len(overrides)} overrides)")
