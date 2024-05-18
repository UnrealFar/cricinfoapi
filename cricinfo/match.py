from typing import List, TYPE_CHECKING

from .base import BaseModel
from .team import Team

if TYPE_CHECKING:
    from .series import Series

class Match(BaseModel):

    def __inti__(
        self,
        id: int,
    ):
        self.id = id
        self.json_url = f"https://www.espncricinfo.com/matches/engine/match/{id}.json"
        self.json = j = self.get_json(self.json_url)

        self.descrpition = j['description']
        self.innings = j['innings']
