import discord
from discord import app_commands
import requests
import random
from rblxopencloud import Experience
import os
from dotenv import load_dotenv
from discord.ui import Button, View


load_dotenv()

token = os.getenv("TOKEN")
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

choices = ["sarahjharris", "juliarwilson", "val.9111"]

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1198877667638923334))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the timetable"))
    print("Ready!")
    
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

@tree.command(name="updatetimetable", description="Update the timetable", guild=discord.Object(id=1198877667638923334))
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
        embed = discord.Embed(title="An error occured", description="Error 409 occured when trying to execute this command. `Error 409 = You don't have the correct permissions.`")
        await interaction.response.send_message(Embed=embed, ephemeral=True)

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
        embed = discord.Embed(title="An error occured", description="Error 409 occured when trying to execute this command. `Error 409 = You don't have the correct permissions.`")
        await interaction.response.send_message(Embed=embed, ephemeral=True)

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
        embed = discord.Embed(title="An error occured", description="Error 409 occured when trying to execute this command. `Error 409 = You don't have the correct permissions.`")
        await interaction.response.send_message(Embed=embed, ephemeral=True)


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
        embed = discord.Embed(title="An error occured", description="Error 409 occured when trying to execute this command. `Error 409 = You don't have the correct permissions.`")
        await interaction.response.send_message(Embed=embed, ephemeral=True)

    

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
        embed.set_footer(text="Edited by juliarwilson", icon_url="https://cdn.discordapp.com/avatars/1142551750923001956/6e3fcdc770a900f66ed182ed1a426799.webp?size=80")
    elif choice == "sarahjharris":
        embed.set_footer(text="Edited by sarahjharris", icon_url="https://cdn.discordapp.com/avatars/755022149760188476/0b2c58364fc68ccf3d8050d6f8c75603.webp?size=80")
    elif choice == "val.9111":
        embed.set_footer(text="Edited by val.9111", icon_url="https://cdn.discordapp.com/avatars/728532835945676821/a_d5718328f828882da3191dceb87240fe.webp?size=80")

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
        await interaction.response.send_message(f"Changed the Presence to {presencetype} {yes}", ephemeral=True)
    else:
        embed = discord.Embed(title="An error occured", description="Error 409 occured when trying to execute this command. `Error 409 = You don't have the correct permissions.`")
        await interaction.response.send_message(Embed=embed, ephemeral=True)

@tree.command(name="updatelinkssite", description="Updates the campus beating", guild=discord.Object(id=1198877667638923334))
@app_commands.choices(beatingstatus=[
    app_commands.Choice(name='Beating (In Session)', value=1),
    app_commands.Choice(name='Not Beating (Not in Session)', value=2)
])
async def updateslinks(interaction, beatingstatus: app_commands.Choice[int]):
    role = discord.utils.get(interaction.guild.roles, name="SchoolboxAdmin")
    if role in interaction.user.roles:
        if beatingstatus.value == 1:
            requests.put('https://scintillating-youth-production.up.railway.app/update/boolean', json={'value': True})
        else:
            requests.put('https://scintillating-youth-production.up.railway.app/update/boolean', json={'value': False})
    else:
        embed = discord.Embed(title="An error occured", description="Error 409 occured when trying to execute this command. `Error 409 = You don't have the correct permissions.`")
        await interaction.response.send_message(Embed=embed, ephemeral=True)            

class RequestView(View):
    def __init__(self, user: discord.User, date: str, linemanager: discord.User):
        super().__init__()
        self.user = user
        self.date = date
        self.linemanager = linemanager

    @discord.ui.button(label="Approve", style=discord.ButtonStyle.green, custom_id="approve_button")
    async def approve_button(self, button: Button, interaction: discord.Interaction):
        # Create an embed for the user
        user_embed = discord.Embed(
            title="Request Approved",
            description=f"Hello {self.user.mention},\n\nYour request has been approved.",
            color=discord.Color.green()
        )

        linemanager_embed = discord.Embed(
            title="LOA Request Approved",
            description=(
                f"Username: {interaction.user} ({interaction.user.id})\n"
                f"Date: {self.date}\n"
                f"Line Manager: {self.linemanager.name} ({self.linemanager.id})\n"
                "Please press the buttons below to approve or decline this request."
            ),
            color=discord.Color.blue()
        )
        
        try:
            usertosend = client.get_member(444660512983089156)
            await client.send_message(usertosend, embed=linemanager_embed)
        except discord.Forbidden:
            await interaction.response.send_message("I can't send a DM to the line manager. They might have DMs disabled.", ephemeral=True)
            return

        # Send approval message to the original user
        await self.user.send(embed=user_embed)
        await interaction.response.send_message("Request approved and message sent to the user and line manager!", ephemeral=True)

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.red, custom_id="deny_button")
    async def deny_button(self, button: Button, interaction: discord.Interaction):
        deny_embed = discord.Embed(
            title="Request Denied",
            description=f"Hello {self.user.mention},\n\nUnfortunately, your request has been denied.",
            color=discord.Color.red()
        )
        await self.user.send(embed=deny_embed)
        await interaction.response.send_message("Request denied!", ephemeral=True)
        
@tree.command(name="loa-request", description="Sends in a LOA Request", guild=discord.Object(id=1198877667638923334))
async def loarequest(interaction, date: str, reason: str, linemanager: discord.User):
    view = RequestView(user = interaction.user, linemanager = linemanager, date = date)
    channel = client.get_channel(1246366616435032136)
    embed = discord.Embed(title = "LOA Request Received", description=f"Username: {interaction.user} ({interaction.user.id})\nReason: {reason}\nDate: {date}\n Line Manager: {linemanager.name} ({linemanager.id})\n Please press the buttons below to approve or decline this request")
    await channel.send(f"{linemanager.mention}, received from {interaction.user}", embed=embed, view=view)
    await interaction.response.send_message("Sent the LOA Request to your Line Manager", ephemeral=True)
    
@tree.command(name="generatesetmessages", description="Generates Set Messages for Session Hosts", guild=discord.Object(id=1198877667638923334))
async def generate_cmd(interaction):
    role = discord.utils.get(interaction.guild.roles, name="SchoolboxAdmin")
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
    
    rr = requests.get('https://solidavisbchs.pythonanywhere.com/timetable/rooms')
    datar = rr.json()
    data1r = datar["rooms"]
    ## Years
    data7r = data1r["year7"]
    data8r = data1r["year8"]
    data9r = data1r["year9"]
    data12r = data1r["year12"]
    ## Periods
    p17r = data7r["period_1"]
    p27r = data7r["period_2"]
    p37r = data7r["period_3"]
    p18r = data8r["period_1"]
    p28r = data8r["period_2"]
    p38r = data8r["period_3"]
    p19r = data9r["period_1"]
    p29r = data9r["period_2"]
    p39r = data9r["period_3"]
    p112r = data12r["period_1"]
    p212r = data12r["period_2"]
    p312r = data12r["period_3"]

    if role in interaction.user.roles:
        await interaction.response.send_message(f":setmessage HOMEROOM - Year 7 go to 2A - Year 8 go to 1A - Year 9 go to 1A - Year 12 go to 7A | :lesson\n:setmessage PERIOD 1- Year 7: {p17} - {p17r} - Year 8: {p18} - {p18r} - Year 9: {p19} - {p19r} - Year 12: {p112} - {p112r} | :lesson\n:setmessage RECESS- Canteen is open | :music 11153244661\n:setmessage PERIOD 2 - Year 7: {p27} - {p27r} - Year 8: {p28} - {p28r} - Year 9: {p29} - {p29r} - Year 12: {p212} - {p212r}  | :lesson\n:setmessage LUNCH - Canteen is open | :music 11153244661\n:setmessage PERIOD 3-  Year 7: {p37} - {p37r} - Year 8: {p38} - {p38r} - Year 9: {p39} - {p39r} - Year 12 - {p312} - {p312r} | :lesson\n:setmessage END OF DAY - If you're not in our group join today as well as our communications server to keep updated | :music 11153244661")
    else:
        embed = discord.Embed(title="An error occured", description="Error 409 occured when trying to execute this command. `Error 409 = You don't have the correct permissions.`")
        await interaction.response.send_message(Embed=embed, ephemeral=True)
        
client.run(token)
