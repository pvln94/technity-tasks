import os
import telebot
import requests
import csv
import tempfile

# TODO: 1.1 Get your environment variables 
yourkey = "c5006214"
bot_id = "6465455369:AAGdmuNXj4LK5EWkb3HX0DNJraEf4jS6su4"

bot = telebot.TeleBot(bot_id)

movies_data = []  # to store movie data

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    bot.reply_to(message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')

@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    bot.reply_to(message, 'Bye!\nHave a good time')

@bot.message_handler(commands=['help'])
def helpProvider(message):
    bot.reply_to(message, ('1.0 You can use "/movie MOVIE_NAME" command to get the details of a particular movie.'
                           '\n2.0. You can use "/export" command to export all the movie data in CSV format.'
                           '\n3.0. You can use "/stop" or the command "/bye" to stop the bot.'))

@bot.message_handler(commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    movie_name = ' '.join(message.text.split()[1:])  # get the movie name from the message
    response = requests.get(f'http://www.omdbapi.com/?t={movie_name}&apikey={yourkey}')
    data = response.json()

    if data['Response'] == 'True':
        # extract relevant info
        title = data['Title']
        year = data['Year']
        imdbRating = data['imdbRating']

        movies_data.append([title, year, imdbRating])
        bot.reply_to(message, f"Title: {title}\nYear: {year}\nimdbRating: {imdbRating}")
    else:
        bot.reply_to(message, "Couldn't find the movie.")

@bot.message_handler(commands=['export'])
def export_to_csv(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    if not movies_data:
        bot.reply_to(message, "No movie data to export.")
        return

    with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Year', 'imdbRating'])  # header
        writer.writerows(movies_data)
        
        file_name = file.name
    with open(file_name, 'rb') as file:
        bot.send_document(message.chat.id, file, caption="Here's your movie data in CSV format!")

    os.remove(file_name)

@bot.message_handler(func=lambda m: True)  # default handler for any other text
def default(message):
    bot.reply_to(message, 'I did not understand \N{confused face}')

bot.infinity_polling()
