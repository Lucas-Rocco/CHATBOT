from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'MeuChatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
    ],
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')

def iniciar_chat():
    print("Olá! Sou o seu chatbot. Como posso ajudar?")
    while True:
        try:
            entrada = input("Você: ")
            if entrada.lower() == 'sair':
                print("Até logo!")
                break
            resposta = chatbot.get_response(entrada)
            print(f"Chatbot: {resposta}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == "__main__":
    iniciar_chat()
