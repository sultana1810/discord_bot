import discord
from discord.ext import commands
from discord import app_commands
import requests

class Client(commands.Bot) :
    async def on_ready(self) :
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(***id***)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e :
            print(f'Error syncing commands: {e}')



    async def on_message(self,message) :
        if message.author == self.user :
            return

        if message.content.startswith('hello') :
            await message.channel.send(f'Hi there {message.author}')

    async def on_reaction_add(self,reaction,user) :
        await reaction.message.channel.send('You reacted.')

    async def on_reaction_remove(self,reaction,user) :
        await reaction.message.channel.send('You removed your reaction.')

    async def on_message_edit(self,before,after) :
        await after.channel.send('You edited your message.')

    async def on_message_delete(self,message) :
        await message.channel.send('You deleted your message.')



intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)


GUILD_ID = discord.Object(id=***id****)


@client.tree.command(name="hello",description="Say hello!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction) :
    await interaction.response.send_message("Hi,there!")

@client.tree.command(name="printer", description="I will print whatever you give me!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
  await interaction.response.send_message(printer)

@client.tree.command(name="embed", description="Embed demo!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction) :
  embed = discord.Embed(title="I am a title", url="https://www.youtube.com", description="I am the description",color=discord.Color.blue())
  embed.set_thumbnail(url="https://pin.it/4G3ncs2iW")
  embed.add_field(name="Field 1 Title", value="I am Cassini!",inline=False)
  embed.add_field(name="Field 2 Title", value="Good to see you!", inline=True)
  embed.add_field(name="Field 3 Title", value="Welcome!", inline=True)
  embed.set_footer(text="This is the footer!")
  embed.set_author(name=interaction.user.name)
  await interaction.response.send_message(embed=embed)

class View(discord.ui.View) :
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.red, emoji="🔥")
    async def button_callback(self, button, interaction) :
      await button.response.send_message("You have clicked the button!")

    @discord.ui.button(label="2nd Button!", style=discord.ButtonStyle.blurple, emoji="👻")
    async def two_button_callback(self, button, interaction):
      await button.response.send_message("This is the second button!")

    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.green, emoji="😺")
    async def three_button_callback(self, button, interaction):
      await button.response.send_message("This is the third button!")

@client.tree.command(name="button", description="Displaying a button", guild=GUILD_ID)
async def myButton(interaction: discord.Interaction) :
  await interaction.response.send_message(view=View())

@client.tree.command(name="calculate",description="Calculate the sum of two numbers", guild=GUILD_ID)
async def calculate(interaction:discord.Interaction,num1:int, num2:int) :
    result = num1 + num2
    await interaction.response.send_message(f'The sum of {num1} and {num2} is {result}')

@client.tree.command(name="weather", description="Get the current weather for a city",guild=GUILD_ID)
async def weather(interaction:discord.Interaction,city : str) :
    api_key = "***api_key***"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200 :
        main = data["main"]
        wind = data["wind"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        humidity = main["humidity"]
        wind_speed = wind["speed"]

        weather_report = (f'Weather in {city} : \n'
                          f'Description : {weather_desc}\n'
                          f'Temperature : {temperature}°C\n'
                          f'Humidity : {humidity}%\n'
                          f'Wind Speed : {wind_speed} m/s')

    else :
        weather_report = f"City {city} not found."

    await interaction.response.send_message((weather_report))




client.run('*******bot_token******')



