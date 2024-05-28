import requests
from typing import Any, Dict


def call_api(input_json: Dict[str, Any]) -> Dict[str, Any]:
    response = requests.get("https://rising-analogy-387407.uc.r.appspot.com/.well-known/ai-plugin.json")

    if response.status_code == 200:
        return response.json()
    else:
        return {"status_code": response.status_code, "text": response.text}
