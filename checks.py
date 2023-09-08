from discord import Interaction
from settings import ModerRoles, logging

async def can_manage_access(interaction: Interaction):
    user = interaction.user
    
    if user.guild_permissions.administrator:
        return True
    else:
        flag = False
        moder_roles_id = ModerRoles.values()
        for role in user.roles:
            if role.id in moder_roles_id:
                flag = True
                break
        return flag
