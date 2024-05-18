from __future__ import annotations

from typing import List, Literal, NamedTuple, overload, TYPE_CHECKING
from datetime import datetime

from .base import BaseModel

if TYPE_CHECKING:
    from .team import Team

class Position(NamedTuple):
    """Position of an athlete."""
    id: str
    name: str
    abbreviation: str
    leaf: bool

    def __repr__(self) -> str:
        return f"<Position {self.name}>"

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

        self.id = int(j['id'])

        self.captain = None
        self.keeper = None

        self.age = j['age']
        dob_str = j['dateOfBirth']
        self.date_of_birth = None
        if len(dob_str):
            self.date_of_birth = datetime.strptime(dob_str, "%Y-%m-%dT%H:%MZ")
        dod_str = j['dateOfDeath']
        self.date_of_death = None
        if len(dod_str):
            self.date_of_death = datetime.strptime(dod_str, "%Y-%m-%dT%H:%MZ")


        if team:
            self.team = team
            self.captain = j['captain']
            self.keeper = j['keeper']

    @property
    def name(self) -> str:
        """Returns the name of the athlete."""
        return self.json['name']

    @property
    def first_name(self) -> str | None:
        """Returns the first name of the athlete."""
        return self.json.get('firstName')

    @property
    def middle_name(self) -> str | None:
        """Returns the middle name of the athlete."""
        return self.json.get('middleName')

    @property
    def last_name(self) -> str | None:
        """Returns the last name of the athlete."""
        return self.json.get('lastName')

    @property
    def short_name(self) -> str | None:
        """Returns the short name of the athlete."""
        return self.json.get('shortName')

    @property
    def full_name(self) -> str | None:
        """Returns the full name of the athlete."""
        return self.json.get('fullName')

    @property
    def display_name(self) -> str | None:
        """Returns the display name of the athlete."""
        return self.json.get('displayName')

    @property
    def batting_name(self) -> str | None:
        """Returns the batting name of the athlete."""
        return self.json.get('battingName')

    @property
    def fielding_name(self) -> str | None:
        """Returns the fielding name of the athlete."""
        return self.json.get('fieldingName')

    @property
    def weight(self) -> float | None:
        """Returns the weight of the athlete."""
        return self.json.get('weight')

    @property
    def height(self) -> float | None:
        """Returns the height of the athlete."""
        return self.json.get('height')

    @property
    def is_active(self) -> bool:
        """Returns the active status of the athlete."""
        return self.json['isActive']

    @property
    def active(self):
        """Returns the active status of the athlete."""
        return self.json['active']

    @property
    def gender(self) -> Literal['M', 'F'] | None:
        """Returns the gender of the athlete."""
        return self.json['gender']

    @property
    def debut_year(self) -> int:
        """Returns the debut year of the athlete."""
        return self.json['debutYear']

    @property
    def birth_place(self) -> str:
        """Returns the birth place of the athlete."""
        return self.json['birthPlace']

    @property
    def jersey(self) -> str:
        """Returns the jersey number of the athlete."""
        return self.json['jersey']

    @property
    def position(self) -> Position:
        """Returns the position of the athlete."""
        return Position(**self.json['position'])

    @property
    def major_teams(self) -> List[Team]:
        t_cls = self.models['Team']
        return [t_cls(team_url=t['$ref']) for t in self.json['majorTeams']]

