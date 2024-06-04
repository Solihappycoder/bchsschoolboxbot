import discord
from discord import app_commands
import requests
import random
from rblxopencloud import Experience
import configparser

config = configparser.ConfigParser()
config.read('config.py')
token = config.get('token')
print(token)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

choices = ["sarahjharris", "juliarwilson", "val.9111", "westy3444"]

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1198877667638923334))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the timetable"))
    print("Soli!")
    
@tree.command(name="canteenbalance", description="Check your canteen balance", guild=discord.Object(id=1198877667638923334))
async def canteen(interaction):
    response = requests.get(f'https://api.blox.link/v4/public/guilds/1198877667638923334/discord-to-roblox/{interaction.user.id}',  headers={"Authorization" : "9dab7da4-a98a-4383-9798-b8639484ca7f"})
    r = response.json()
    experience = Experience(3963042649, "AZKtagN8JkC2JbbTqqGaDBmNldIlEPOApLXJZ4d4C3PrxGIn")
    datastore = experience.get_data_store("CaboltDataStore", scope="global")
    value, info = datastore.get(r["robloxID"])
    embed = discord.Embed(title="Canteen Balance", description="The balance below is your canteen balance, which can be used at the canteen at any of our sessions to buy food and drinks. To add value to your balance, ask the canteen staff or use the machine at the canteen.")
    embed.add_field(name="Balance", value=f"${value}", inline=True)
    await interaction.response.send_message(embed=embed)

@tree.command(name="smartriderbalance", description="Check your Smartrider balance", guild=discord.Object(id=1198877667638923334))
async def canteen(interaction):
    response = requests.get(f'https://api.blox.link/v4/public/guilds/1198877667638923334/discord-to-roblox/{interaction.user.id}',  headers={"Authorization" : "9dab7da4-a98a-4383-9798-b8639484ca7f"})
    r = response.json()
    experience = Experience(3963042649, "LN7Q9KFWtEyI3w+dpYI/FAq1LJWGc57noxSCnBe2afV630Wp")
    datastore = experience.get_data_store("PlayerBusMoneyStoreUpdated", scope="global")
    value1 = r["robloxID"]
    value, info = datastore.get(f"Player_{value1}")
    embed = discord.Embed(title="<:transperth:1243827021180829717> Smartrider Balance", description="The balance below is your Smartrider Balance to be used on busses after school. To add value to your card, use your in-game phone or see a student services staff.", color=discord.Color.from_rgb(0, 134, 53))
    embed.add_field(name="Balance", value=f"${value}", inline=True)
    await interaction.response.send_message(embed=embed)

@tree.command(name="updatetimetable", description="Update the timetable, for SLT and Site Managers only", guild=discord.Object(id=1198877667638923334))
async def update_cmd(interaction, year: str, period1: str, period2: str, period3: str):
    role = discord.utils.get(interaction.guild.roles, name="SchoolboxAdmin")
    if role in interaction.user.roles:
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/year{year}/period_1'
        data = {'subject': period1}
        requests.put(url, json=data)    
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/year{year}/period_2'
        data = {'subject': period2}
        requests.put(url, json=data)
        await interaction.response.send_message("Sent to the API, one more period needs to be completed before it is fully complete", ephemeral=True)
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/year{year}/period_3'
        data = {'subject': period3}
        requests.put(url, json=data)
    else:
        await interaction.response.send_message("You do not have the authorised role", ephemeral=True)

@tree.command(name="updaterooms", description="Update the timetable rooms", guild=discord.Object(id=1198877667638923334))
async def update_cmd(interaction, year: str, period1: str, period2: str, period3: str):
    role = discord.utils.get(interaction.guild.roles, name="SchoolboxAdmin")
    if role in interaction.user.roles:
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/rooms/year{year}/period_1'
        data = {'subject': period1}
        requests.put(url, json=data)    
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/rooms/year{year}/period_2'
        data = {'subject': period2}
        requests.put(url, json=data)
        await interaction.response.send_message("Sent to the API, one more period needs to be completed before it is fully complete", ephemeral=True)
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/rooms/year{year}/period_3'
        data = {'subject': period3}
        requests.put(url, json=data)
    else:
        await interaction.response.send_message("You do not have the authorised role", ephemeral=True)

@tree.command(name="updatenotices", description="Update the notices on schoolbox", guild=discord.Object(id=1198877667638923334))
async def update_cmd(interaction, id: str, title: str, body: str, imageid: str):
    role = discord.utils.get(interaction.guild.roles, name="SchoolboxAdmin")
    if role in interaction.user.roles:
        url = f'https://solidavisbchs.pythonanywhere.com/notices/notice{id}/title'
        data = {'title': title}
        requests.put(url, json=data)
        await interaction.response.send_message("Sent to the API, one more period needs to be completed before it is fully sent", ephemeral=True)
        url = f'https://solidavisbchs.pythonanywhere.com/notices/notice{id}/body'
        data = {'title': body}
        requests.put(url, json=data)
        url = f'https://solidavisbchs.pythonanywhere.com/notices/notice{id}/imageid'
        data = {'title': imageid}
        requests.put(url, json=data)        
    else:
        await interaction.response.send_message("You do not have the authorised role", ephemeral=True)


@tree.command(name="cleartimetable", description="Clears the timetable", guild=discord.Object(id=1198877667638923334))
async def clear_cmd(interaction, year: str):
    role = discord.utils.get(interaction.guild.roles, name="SchoolboxAdmin")
    if role in interaction.user.roles:
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/year{year}/period_1'
        data = {'subject': ""}
        response = requests.put(url, json=data)
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/year{year}/period_2'
        data = {'subject': ""}
        response = requests.put(url, json=data)
        url = f'https://solidavisbchs.pythonanywhere.com/timetable/year{year}/period_3'
        data = {'subject': ""}
        response = requests.put(url, json=data)
        await interaction.response.send_message(f"Cleared the timetable for year {year}", ephemeral=True)
    else:
        await interaction.response.send_message("You do not have the authorised role", ephemeral=True)

    

@tree.command(name="viewtimetable", description="View the timetable", guild=discord.Object(id=1198877667638923334))
async def view_cmd(interaction):
    r = requests.get('https://solidavisbchs.pythonanywhere.com/timetable')
    data = r.json()
    data1 = data["timetable"]
    ## Years
    data7 = data1["year7"]
    data8 = data1["year8"]
    data9 = data1["year9"]
    data12 = data1["year12"]
    ## Periods
    p17 = data7["period_1"]
    p27 = data7["period_2"]
    p37 = data7["period_3"]
    p18 = data8["period_1"]
    p28 = data8["period_2"]
    p38 = data8["period_3"]
    p19 = data9["period_1"]
    p29 = data9["period_2"]
    p39 = data9["period_3"]
    p112 = data12["period_1"]
    p212 = data12["period_2"]
    p312 = data12["period_3"]
    
    embed = discord.Embed(title="Timetable", description="You can find the most recent timetable below.")
    embed.add_field(name="Period 1", value=f"Year 7 - {p17}\nYear 8 - {p18}\nYear 9 - {p19}\nYear 12 - {p112}", inline=True)
    embed.add_field(name="Period 2", value=f"Year 7 - {p27}\nYear 8 - {p28}\nYear 9 - {p29}\nYear 12 - {p212}", inline=True)
    embed.add_field(name="Period 3", value=f"Year 7 - {p37}\nYear 8 - {p38}\nYear 9 - {p39}\nYear 12 - {p312}", inline=True)
    choice = random.choice(choices)
    if choice == "juliarwilson":
        embed.set_footer(text="juliarwilson", icon_url="https://cdn.discordapp.com/avatars/1142551750923001956/6e3fcdc770a900f66ed182ed1a426799.webp?size=80")
    elif choice == "sarahjharris":
        embed.set_footer(text="Edited by sarahjharris", icon_url="https://cdn.discordapp.com/avatars/755022149760188476/0b2c58364fc68ccf3d8050d6f8c75603.webp?size=80")
    elif choice == "val.9111":
        embed.set_footer(text="Edited by val.9111", icon_url="https://cdn.discordapp.com/avatars/728532835945676821/a_d5718328f828882da3191dceb87240fe.webp?size=80")
    elif choice == "westy3444":
        embed.set_footer(text="Edited by westy3444", icon_url="https://cdn.discordapp.com/avatars/1003810834201448549/88f808307b4fdd191d39ee65840c760b.webp?size=80")

    await interaction.response.send_message(embed=embed, ephemeral=True)

@tree.command(name="updatestatus", description="Updates the status of the bot", guild=discord.Object(id=1198877667638923334))
@app_commands.choices(presencetype=[
    app_commands.Choice(name='Watching', value=1),
    app_commands.Choice(name='Playing', value=2),
    app_commands.Choice(name='Listening', value=3)
])
async def hello(interaction, presencetype: app_commands.Choice[int], presencetext: str):
    role = discord.utils.get(interaction.guild.roles, name="SchoolboxAdmin")
    yes = discord.ActivityType.watching
    if role in interaction.user.roles:
        if presencetype.value == 1:
            yes = discord.ActivityType.watching
        elif presencetype.value == 2:
            yes = discord.ActivityType.playing
        elif presencetype.value == 3:
            yes = discord.ActivityType.listening
        await client.change_presence(activity=discord.Activity(type=yes, name=presencetext))
        await interaction.response.send_message(f"Changed the Presence to {yes}", ephemeral=True)
    else:
        await interaction.response.send_message("You do not have the authorised role", ephemeral=True)



client.run(token)
