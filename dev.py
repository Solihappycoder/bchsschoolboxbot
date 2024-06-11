@tree.command(name="claimperiod", description="IN DEVELOPMENT", guild=discord.Object(id=1198877667638923334))
@app_commands.choices(Period=[
    app_commands.Choice(name='P1', value=1),
    app_commands.Choice(name='P2', value=2),
    app_commands.Choice(name='P3', value=3)
])
@app_commands.choices(Year=[
    app_commands.Choice(name='Y7', value=1),
    app_commands.Choice(name='Y8', value=2),
    app_commands.Choice(name='Y9', value=3),
    app_commands.Choice(name='Y12', value=4)
])
async def claimperiod(interaction, Year: app_commands.Choice[int], Period: app_commands.Choice[int], Subject: str, Room: int):
    role = discord.utils.get(interaction.guild.roles, name="SchoolboxAdmin")
    role1 = discord.utils.get(interaction.guild.roles, name="Teaching Staff")
    r = requests.get('https://solidavisbchs.pythonanywhere.com/timetable')
    data = r.json()
    if role or role1 in interaction.user.roles:
        if Period in 
