import telebot

bot = telebot.TeleBot(token='6265514966:AAGf20rw7rZceudkN7LuAJiqTIkIoJ6W2Y4')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'SELAMAT DATANG DICHATBOT KAMI')

# Define a dictionary with the list of subjects for each day
subject_dict = {
    'senin': ['\n Jam Pertama \n Mata Kuliah : KOMPUTER GRAFIK (08.50 - 10.30) \n Dosen : DEVI DAMAYANTI','\n Jam Kedua \n Mata Kuliah : MOBILE PROGRAMMING (13.00 - 14.40) \n Dosen : DIKI RASAPTA'],
    'selasa': ['\n Jam Pertama \n  Mata Kuliah : PEMROGRAMAN WEB 2 (08.50 - 10.30) \n Dosen : MAULANA ARDIANSYAH','\n Jam Kedua \n Mata Kuliah : KECERDASAN BUATAN (13.00 - 14.40) \n Dosen : AGUNG FERDANANTO','\n Jam Ketiga \n Mata Kuliah : SISTEM INFORMASI MANAJEMEN (14.40 - 16.20) \n Dosen : INES HEIDIANI IKASARI'],
    'rabu': ['\n Jam Pertama \n Mata Kuliah : REKAYASA PERANGKAT LUNAK (08.50 - 10.30) \n Dosen : KHANIF FAOZI'],
    'jumat': ['\n Jam Pertama \n Mata Kuliah : KERJA PRAKTEK (10.30 - 12.10) \n Dosen : ROESLAN DJUTALOV','\n Jam Kedua \n Mata Kuliah : TEKNIK KOMPILASI (13.00 - 14.40) \n Dosen : ZURNAN ALFIAN'],
}

# Define the message handler for the "/makul" command
@bot.message_handler(commands=['matkul'])
def handle_makul(message):
    # Send a message asking for the day
    bot.send_message(message.chat.id, "Silahkan Masukkan Hari Yang Ingin Kamu Ketahui Mata Kuliahnya!")

    # Define a nested function to handle the day response
    @bot.message_handler(func=lambda m: True)
    def handle_day(message):
        # Get the day from the message text
        day = message.text.lower()

        # Check if the day is valid (in the subject dictionary)
        if day not in subject_dict:
            bot.send_message(message.chat.id, "Invalid day. Please enter a valid day (senin, selasa, rabu, kamis, jumat, sabtu, minggu):")
            return

        # Get the list of subjects for the day from the subject dictionary
        subjects = subject_dict[day]

        # Check if there are any subjects for the day
        if not subjects:
            bot.send_message(message.chat.id, f"Tidak Ada Mata Kuliah Pada Hari {day.capitalize()}")

        # Send a message with the list of subjects for the day
        else:
            subject_text = "\n- ".join(subjects)
            bot.send_message(message.chat.id, f"Mata Kuliah Pada Hari {day.capitalize()}:\n- {subject_text}")

        # Remove the nested message handler to avoid conflicts
       # bot.remove_message_handler(handle_day)

    # Add the nested message handler to the bot
    bot.add_message_handler(handle_day)


# Define a dictionary with absen numbers and corresponding names
absen_dict = {
    1: "\n Ahmad Fadly Fahmi \n (201011400384) \n 06TPLP007",
    2: "\n Arif Rahman Gunawan \n (201011400385) \n 06TPLP007",
    3: "\n Attaul Wahab Khasbun \n (201011400386) \n 06TPLP007",
}

# Define the message handler for the "/absen" command
@bot.message_handler(commands=['absen'])
def handle_absen(message):
    # Send a message asking for the absen number
    bot.send_message(message.chat.id, "Silahkan Masukkan Nomor Absensi Kalian !")

    # Define a nested function to handle the absen number response
    @bot.message_handler(func=lambda m: True)
    def handle_absen_number(message):
        try:
            # Try to convert the message text to an integer
            absen_number = int(message.text)

            # Check if the absen number is valid (between 1 and 33)
            if absen_number < 1 or absen_number > 10:
                bot.send_message(message.chat.id, "Invalid absen number. Please enter a number between 1 and 10:")
                return

            # Get the corresponding name from the absen dictionary
            absen_name = absen_dict[absen_number]

            # Send a message with the absen name
            bot.send_message(message.chat.id, f"Absen {absen_number} : {absen_name}")

            # Remove the nested message handler to avoid conflicts
           ## bot.remove_message_handler(handle_absen_number)

        except ValueError:
            # If the message text cannot be converted to an integer, ask again
            bot.send_message(message.chat.id, "Invalid input. Please enter a number between 1 and 10:")

    # Add the nested message handler to the bot
    bot.add_message_handler(handle_absen_number)

##@bot.message_handler(func=lambda message: True)
##def handle_message(message):
 ##   bot.send_message(message.chat.id, 'saya tidak mengerti apa yang kamu katakan')

bot.polling()