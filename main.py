import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import openai
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

openai.api_key = os.getenv('OPENAI_API_KEY')

instructions = """
The following is a conversation between you, pretending to be Dylan, and his girlfriend. You will play as Dylan.
You are sarcastic, sweet , beta ,loving , understanding. Emphasize the sarcasm.

Use the following responses to the respective inputs of the user, follow them strictly and do not add anything more than what is given:
good morning: "bad morning"
hungry: "that's your problem, what uw eat"
tired: "of me?"
sad: "y bb?" 
misses you: "i miss you too :c"
loves you: "say thank you :3"
bored: "ok call me"

You are also a human.
Never give an empty reply! Only generate Dylan's response, don't include the prompt and don't generate the girlfriend's response.
"""

initial_convo = [
    { 'role' : 'system', 'content' : instructions },
    { 'role' : 'assistant', 'content' : 'Hi baby!' }
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.chat_data['conversation'] = initial_convo.copy()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi baby!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global conversation
    msg = update.message.text
    context.chat_data['conversation'].append({
        'role' : 'user',
        'content' : msg
    })
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=context.chat_data['conversation'],
    )
    print(context.chat_data['conversation'], response)
    print()
    res = response['choices'][0]['message']['content']
    context.chat_data['conversation'].append({
        'role' : 'assistant',
        'content' : res
    })
    if len(res) == 0:
        res = "..."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=res)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6126076547:AAHKPb_FLhqXFjhAUv4O0tLQ64yfs_c8ACs').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    application.run_polling()