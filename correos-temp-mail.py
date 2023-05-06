import telebot
import random
import re

# Inserta aquí el token de tu bot de Telegram
TOKEN = '6220571791:AAHhs_nNb98_eSZUWihRvbTHiGUiwDnOihA'

# Lista de números para usar en los correos temporales
NUMEROS_TEMPORALES = ['eczbk56a4f', 'upmeu1jlgt', 'et0h53tdp2', 'en2zmj53gn', '915vg81m0w', '8p4whet73g', 'cnl48rgupt', 'sanghofj5i', '0ag369ab5x', 'nyxgvugonw', '9u05vlipak', 'pfdvxojyk1']

# Inicializa el bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.reply_to(message, "Hola. Usa /mail para generar un correo temporal ☂️.")

# Función para crear correos temporales
def generar_correo_temporal(nombre):
    numero_temporal = random.choice(NUMEROS_TEMPORALES)
    return nombre + '+' + numero_temporal + '@gmail.com'

# Manejador de comando "/tempmail" o ".tempmail"
@bot.message_handler(commands=['mail'])
def handle_tempmail_command(message):
    # Extrae el nombre del correo temporal a partir del mensaje
    nombre = re.findall(r'/mail\s(\w+)', message.text)

    if nombre:
        # Genera el correo temporal y lo envía al usuario
        correo_temporal = generar_correo_temporal(nombre[0])
        # Construye el mensaje con el enlace
        mensaje = f"""
𝗖𝗼𝗿𝗿𝗲𝗼 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗹 𝗴𝗲𝗻𝗲𝗿𝗮𝗱𝗼 ✅
╭══════════ ♤ ══════════╮

`{correo_temporal}`.

╰══════════ ♤ ══════════╯
*Creator* [𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱](https://t.me/hackerismyname)       _enjoy!_ 😄
"""
        bot.reply_to(message, mensaje, parse_mode='Markdown', disable_web_page_preview=True)
    else:
        # Si no se proporciona un nombre, envía un mensaje de error
        bot.reply_to(message, 'Debes proporcionar un nombre para el correo temporal.')

bot.polling()