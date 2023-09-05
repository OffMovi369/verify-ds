import discord
from discord import SelectOption
from settings import AccessRoles, access_roles

class AccessView(discord.ui.View):

    def __init__(self, member: discord.Member, timeout: int = 180):
        self.member = member
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Выдать доступ", style=discord.ButtonStyle.green)
    async def access(self, interaction: discord.Interaction, button: discord.ui.Button):
        if access_roles['member'] in self.member.roles:
            await interaction.response.send_message(f"{self.member.mention} уже имеет доступ", ephemeral=True)
        else:
            await self.member.remove_roles(access_roles['lock'])
            await self.member.add_roles(access_roles['member'])
            await interaction.response.send_message(f"{self.member.mention} получил доступ", ephemeral=True)
        
        self.member = interaction.guild.get_member(self.member.id)
    
    @discord.ui.button(label="Запретить доступ", style=discord.ButtonStyle.red)
    async def not_access(self, interaction: discord.Interaction, button: discord.ui.Button):
        if access_roles['lock'] in self.member.roles:
            await interaction.response.send_message(f"{self.member.mention} уже с запрещённым доступом", ephemeral=True)
        else:
            await self.member.remove_roles(access_roles['member'])
            await self.member.add_roles(access_roles['lock'])
            await interaction.response.send_message(f"Для {self.member.mention} доступ успешно запрещён", ephemeral=True)
        self.member = interaction.guild.get_member(self.member.id)
    
    @discord.ui.button(label="Мужчина", style=discord.ButtonStyle.gray)
    async def male(self, interaction: discord.Interaction, button: discord.ui.Button):
        if access_roles['male'] in self.member.roles:
            await self.member.remove_roles(access_roles['male'])
            await interaction.response.send_message(f"{self.member.mention} больше не мужчина", ephemeral=True)
        else:
            await self.member.remove_roles(access_roles['female'])
            await self.member.add_roles(access_roles['male'])
            await interaction.response.send_message(f"{self.member.mention} теперь мужчина", ephemeral=True)
        self.member = interaction.guild.get_member(self.member.id)

    
    @discord.ui.button(label="Женщина", style=discord.ButtonStyle.gray)
    async def female(self, interaction: discord.Interaction, button: discord.ui.Button):
        if access_roles['female'] in self.member.roles:
            await self.member.remove_roles(access_roles['female'])
            await interaction.response.send_message(f"{self.member.mention} больше не женщина", ephemeral=True)
        else:
            await self.member.remove_roles(access_roles['male'])
            await self.member.add_roles(access_roles['female'])
            await interaction.response.send_message(f"{self.member.mention} теперь женщина", ephemeral=True)
        self.member = interaction.guild.get_member(self.member.id)


class FormView(discord.ui.View):
    #TODO
    @discord.ui.select(options=[
        SelectOption(label="Модератор (чат/войс)", description="Легкий входной порог с последующей оплатой", value=""),
        SelectOption(label="Инвентёр", description="Мудак без денег", value=""),
        SelectOption(label="Креативщик", description="Высокий входной порог, оплата сразу", value=""),
    ])
    async def asd(self):
        ...

    # @discord.ui.button(label="Ответить", style=discord.ButtonStyle.green)
    # async def answer(self, interaction : discord.Interaction, button: discord.ui.Button):
    #     answer_modal = AnswerModal(title = self.question)
    #     answer_modal.answer.placeholder = self.placeholder

    #     try:
    #         answer = Answer.get(question=self.question)
    #     except Exception as e:
    #         await interaction.response.send_modal(answer_modal)
    #     else:
    #         if not(answer):
    #             await interaction.response.send_modal(answer_modal)
    #         else:
    #             await interaction.response.send_message("Вы уже отвечали на этот вопрос", ephemeral=True)