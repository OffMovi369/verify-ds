from discord import Interaction
from settings import ModerRoles

async def can_manage_access(interaction: Interaction):
    user = interaction.user
    user_roles_id = [role.id for role in user.roles]
    user_has_any_role = set([ModerRoles.values, *user_roles_id])
    return bool(user_has_any_role)
