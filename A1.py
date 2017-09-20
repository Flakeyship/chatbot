from chatterbot import  ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#Allows the chat bot to be trained using data from the ChatterBot dialog corpus.



bot = ChatBot(
    'A1',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./database.sqlite3'
)

"""logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],"""

bot.set_trainer(ChatterBotCorpusTrainer)

# Train based on the english corpus
bot.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.portuguese"
    )

# Train based on english greetings corpus
#bot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
#bot.train("chatterbot.corpus.english.conversations")

while True:
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
