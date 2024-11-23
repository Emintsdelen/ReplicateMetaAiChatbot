from api import Api

def ReplicateMetaAiChatbot():
    prompt = str(input("\n--> "))
    Api(prompt)

while True:
    if __name__ == "__main__":
        ReplicateMetaAiChatbot()