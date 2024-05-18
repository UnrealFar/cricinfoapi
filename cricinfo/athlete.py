from __future__ import annotations

from typing import List, overload, TYPE_CHECKING
from datetime import datetime

from .base import BaseModel

if TYPE_CHECKING:
    from .team import Team

class Athlete[Q: str | int | None](BaseModel):


    @overload
    def __init__(
        self,
        *,
        id: int,
    ) -> None:
        pass

    @overload
    def __init__(
        self,
        *,
        player_url: str,
        team: Team | None = None
    ) -> None:
        pass

    def __init__(
        self,
        *,
        player_url: Q = None,
        id: Q = None,
        team: Team | None = None,
    ):
        if id:
            self.json_url = f"http://core.espnuk.org/v2/sports/cricket/athletes/{id}/"
        else:
            self.json_url = player_url
        self.json = j = self.get_json(self.json_url)

        self.id = j['id']
        self.name = j['name']
        self.first_name = j['firstName']
        self.middle_name = j['middleName']
        self.last_name = j['lastName']
        self.short_name = j['shortName']
        self.full_name = j['fullName']
        self.display_name = j['displayName']    
        self.batting_name = j['battingName']
        self.fielding_name = j['fieldingName']
        self.captain = None
        self.keeper = None
        self.weight = j['weight']
        self.height = j['height']
        self.age = j['age']
        dob_str = j['dateOfBirth']
        self.date_of_birth = None
        if len(dob_str):
            self.date_of_birth = datetime.strptime(dob_str, "%Y-%m-%dT%H:%M%Z")
        dod_str = j['dateOfDeath']
        self.date_of_death = None
        if len(dod_str):
            self.date_of_death = datetime.strptime(dod_str, "%Y-%m-%dT%H:%M%Z")
        self.is_active = j['isActive']
        self.active = j['active']
        self.gender = j['gender']
        self.debut_year = j['debutYear']
        self.birth_place = j['birthPlace']
        self.jersey = j['jersey']

        if 'league' in j['$ref']:
            self.captain = j['captain']
            self.keeper = j['keeper']

        if team:
            self.team = team

    @property
    def major_teams(self) -> List[Team]:
        t_cls = self.models['Team']
        return [t_cls(team_url=t['$ref']) for t in self.json['majorTeams']]

