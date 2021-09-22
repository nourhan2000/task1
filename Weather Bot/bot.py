from rivescript import RiveScript
import os.path #to be able to run on multiplatform 
file = os.path.dirname(__file__) #gets absolute path 
brain = os.path.join(file, 'brain') #joins brain with the absolute path 
# then loads it 
bot = RiveScript()
bot.load_directory(brain)
bot.sort_replies()

# we have to be in a infinite loop to get responses contiously
def chat(msg,user):
    if msg=='q':
        return "quitting"
    else:
        return bot.reply(user, msg)
      