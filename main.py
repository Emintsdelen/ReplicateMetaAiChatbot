from api import Api

with open("conversation.txt", "w", encoding="utf-8") as conversation:
    conversation.write("")
def ReplicateMetaAiChatbot():
    prompt = str(input("\n--> "))
    with open("conversation.txt", "a", encoding="utf-8") as conversation:
        conversation.write("'User: " + prompt + "', ")
    output = Api(prompt)
    print("\n" + output)
    with open("conversation.txt", "a", encoding="utf-8") as conversation:
        conversation.write("'Chatbot: " + output + "', ")

while True:
    if __name__ == "__main__":
        ReplicateMetaAiChatbot()