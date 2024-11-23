import replicate, os, io, sys
from dotenv import load_dotenv

def chatApi(prompt):
    first_item_skipped = False
    api_token = os.getenv("REPLICATE_API_TOKEN")
    replicate.Client(api_token=api_token)

    with open("conversation.txt", "r", encoding="utf-8") as conversation:
        conversationText = conversation.read()

    output = io.StringIO()
    sys.stdout = output
    for event in replicate.stream(
        "meta/meta-llama-3-8b-instruct",
        input={
            "prompt": prompt,
            "system_prompt": "You are a helpful assistant and you can recognize images by their URL (to do that user should type '0' and send it, after that user should provide image URL), this is the conversation with user: " + conversationText,
            "length_penalty": 1
        },
    ):
        if not first_item_skipped:
            first_item_skipped = True
            continue
        print(event, end="")
    sys.stdout = sys.__stdout__
    return output.getvalue().strip()

def imageApi(imageUrl, prompt):
    output = io.StringIO()
    sys.stdout = output
    for event in replicate.stream(
        "yorickvp/llava-13b:80537f9eead1a5bfa72d5ac6ea6414379be41d4d4f6679fd776e9535d1eb58bb",
        input={
            "image": imageUrl,
            "prompt": prompt
        }
    ):
        print(event, end="")
    sys.stdout = sys.__stdout__
    return output.getvalue().strip()