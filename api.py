import replicate
import os
from dotenv import load_dotenv

def Api(prompt):
    first_item_skipped = False
    api_token = os.getenv("REPLICATE_API_TOKEN")
    replicate.Client(api_token=api_token)
    model_name = "meta/meta-llama-3-8b-instruct"

    print("")
    for event in replicate.stream(
        model_name,
        input={
            "prompt": prompt,
            "system_prompt": "You are a helpful assistant",
            "length_penalty": 1
        },
    ):
        if not first_item_skipped:
            first_item_skipped = True
            continue
        print(event, end="")
    print("")