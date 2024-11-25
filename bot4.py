import discord
import os
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send("Hola, soy un perro pelao bot !")
@bot.command()
async def servergtag(ctx):
    await ctx.send("el server es ushehajd!")
@bot.command()
async def modoterror(ctx):
    await ctx.send("seguro ?!")
@bot.command()
async def si(ctx):
    await ctx.send("")

@bot.command()
async def meme(ctx):
    imagen = random.choice(os.listdir("image"))
    with open('image/'+imagen, 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)



def get_duck_image_url():    
    url = " https://pokeapi.co"
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def contaminacionmar(ctx):
    await ctx.send("Hola, soy un perro pelao bot te contare sobre la contaminacion del mar que probocan los humanos o quizas algun perro que lleve un plastico al mar imagina que cada plastico en el mar es un virus en tu juego cada vez que alguien tire algo al mar es un virus en tu juego ¿supongo que a ti no te gustaria que tu juego, programa o ect se llene de virus no? bueno algo parecido pasa en  el mar y los plasticos si no uvieran plasticos en el mar seria como que tu programa no tuviera virus ¿no? exacto en  el mar es parecido  es recomendable no tirar basura al mar y mejor llevar tu basura a un contenedor de la playa o guardarla y ponerla en donde corresponde varios animales marinos mueren por petroleo plasticos ect Se estima que cada año mueren 100.000 especies marinas a causa de la contaminación por plásticos ")

@bot.command()
async def manualidad(ctx):
    await ctx.send("Hola una manualidad es Macetas Decorativas Reutiliza botellas plásticas cortándolas a la mitad y pintándolas con colores vibrantes. Puedes decorarlas con cintas o pegatinas la sigente url es un ejemplo: https://www.youtube.com/watch?v=yc_HsLrl6lY ")
     
@bot.command()
async def canalyt(ctx):
    await ctx.send("con que quieres saber de mi canal de youtube eh bueno no hay problema esta es la url para ingresar a mi canal https://www.youtube.com/@El_perro_pelao  !")

@bot.command()
async def epedance(ctx):
    await ctx.send(" https://www.youtube.com/watch?v=UJWr_PzLeQc !")




bot.run("MTMwMzUwNTUzMjYwNjQ4MDQwNA.G2iwnV.kJYw36hnKhcPuOO03ajr0tZRu5Ae59DAr0t9vg")


