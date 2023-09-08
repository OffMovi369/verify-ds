import discord
from discord import app_commands
from discord.ext import commands

from mylibs.Views import AccessView

from settings import logging, BOT_TOKEN, MAIN_GUILD, access_roles, AccessRoles
from checks import can_manage_access

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())
client.remove_command('help')

# ignored_cogs = [] # Коги, которые не нужно импортировать. Example^ ['AdminCommands', 'GodDamns', ...]

# # Импорт всех когов
# async def load_cogs():
# 	for cog_file in COGS_DIR.glob("*.py"):
# 		if cog_file.name != "__init__.py":
# 			await client.load_extension(f'cogs.{cog_file.name[:-3]}')
# 			logging.info(f"Cog <{cog_file.name}> added")
		
# Проверка на бота, client не будет отвечать боту
# @client.event
# async def on_message(message):
# 	if not(message.author.bot):
# 		await client.process_commands(message)

# @client.tree.command(description="Отправка сообщения с селектором и формой на набор модераторов")
# async def form(interaction: discord.Interaction):
# 	emb = discord.Embed(
# 		title="Набор в модераторы",
# 		description="Выберите категорию модерирования и заполните анкету",
# 		color=discord.Color.dark_blue()
# 	)
# 	await interaction.response.send_message(embed=emb)

@client.tree.context_menu(name="Доступ")
@app_commands.check(can_manage_access)
async def access(interaction: discord.Interaction, member: discord.Member):
	await interaction.response.send_message(
		content=f"Настройка доступа для {member.mention}",
		view=AccessView(member=member,timeout=300),
		ephemeral=True
	)

@client.tree.error
async def on_contex_menu(interaction: discord.Interaction, error):
	match type(error):
		case app_commands.errors.CheckFailure:
			await interaction.response.send_message("У вас недостаточно прав!", ephemeral=True)
		case _:
			await interaction.response.send_message("Извините, произошла необработанная ошибка, сообщите о ней разработчику", ephemeral=True)
			logging.error(f"app_commands error: {type(error)}")


@client.event
async def on_ready():
	await client.tree.sync()
	main_guild = client.get_guild(MAIN_GUILD)
	for role in AccessRoles:
		access_roles[role.name] = main_guild.get_role(role.value)

	logging.info(f"The bot {client.user} has been started!")

# форма
# имя, возраст
# часовой пояс
# прйм тайм
# время на сервер уделять готовы сколько
# опыт
# расскажите о себе

if __name__ == "__main__":
	client.run(BOT_TOKEN)