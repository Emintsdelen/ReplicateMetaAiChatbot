from api import chatApi, imageRecognitionApi, imageGenerationApi

with open("conversation.txt", "w", encoding="utf-8") as conversation:
    conversation.write("")
def ReplicateMetaAiChatbot():
    print("\nTo upload an image type '0'")
    print("To generate an image type '1'")
    prompt = str(input("--> "))
    if prompt == "0":
        imageUrl = input("\nImage url --> ")
        prompt = input("Prompt for image (You can leave this blank) --> ")
        with open("conversation.txt", "a", encoding="utf-8") as conversation:
            conversation.write("'User: " + imageUrl + " " + prompt + "', ")
        if prompt == "":
            prompt = "explain this image."
        output = imageRecognitionApi(imageUrl, "Explain this image.")
        output = chatApi("'" + output + "', " + prompt)
        print("\n" + output)
        with open("conversation.txt", "a", encoding="utf-8") as conversation:
            conversation.write("'Chatbot: " + output + "', ")
    elif prompt == "1":
        prompt = input("\nPrompt for image --> ")
        with open("conversation.txt", "a", encoding="utf-8") as conversation:
            conversation.write("'User: '" + prompt + "' this is a prompt for image generation', ")
        imageUrlOutputList = imageGenerationApi(prompt)
        imageUrlOutput = str(imageUrlOutputList[0])
        output = chatApi("You generated an image, send this url to user '" + imageUrlOutput + "'")
        print("\n" + output)
        with open("conversation.txt", "a", encoding="utf-8") as conversation:
            conversation.write("'Chatbot: " + output + "', ")
    else:
        with open("conversation.txt", "a", encoding="utf-8") as conversation:
            conversation.write("'User: " + prompt + "', ")
        output = chatApi(prompt)
        print("\n" + output)
        with open("conversation.txt", "a", encoding="utf-8") as conversation:
            conversation.write("'Chatbot: " + output + "', ")

while True:
    if __name__ == "__main__":
        ReplicateMetaAiChatbot()