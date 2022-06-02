from app.characters.api_v1_0.schemas import CrewSchema
from app.characters.models import Crew

class AppErrorBaseClass(Exception):
    pass


class ObjectNotFound(AppErrorBaseClass):
    pass