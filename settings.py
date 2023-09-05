import logging
import os
import pathlib
import enum
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MAIN_GUILD = int(os.getenv("MAIN_GUILD"))
BASE_DIR = pathlib.Path(__file__).parent

# ENUMS
class ModerRoles(enum.IntEnum):
    control = 1147634588894629938
    moderator = 1147634588030607420
    administrator = 1147634586369658971

    @property
    def values(self):
        return [e.value for e in list(ModerRoles)]

class AccessRoles(enum.IntEnum):
    member = 1135360362720534669
    lock = 1147634609887117322
    male = 1147634608993730600
    female = 1147634608041623592

access_roles = {}

logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s] %(levelname)s(%(name)s) > %(message)s', 
                    datefmt='%H:%M:%S %d-%m-%Y'
)

