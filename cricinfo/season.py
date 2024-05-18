from typing import List, TYPE_CHECKING

from .base import BaseModel
from .team import Team

if TYPE_CHECKING:
    from .series import Series

class Season[S: Series, U: str](BaseModel):

    if TYPE_CHECKING:
        series: S
        id: int
        name: str
        alt_name: str
        description: str
        short_name: str
        short_alt_name: str
        year: int
        start_date: str
        end_date: str
        slug: str
        teams_url: str
        events_url: str
        notes_url: str
        groups_url: str

    def __init__(
        self,
        series: S,
        season_url: U,
    ):
        self.series = series
        self.id = series.id
        self.json_url = season_url
        self.json = j = self.get_json(self.json_url)

        self.teams_url = j['teams']["$ref"]
        self.events_url = j['events']["$ref"]
        self.notes_url = j['notes']["$ref"]
        self.groups_url = j['groups']["$ref"]

        self._teams = None

    @property
    def name(self) -> str:
        """Returns the name of the season."""
        return self.json['name']

    @property
    def alternate_name(self) -> str:
        """Returns the alternate name of the season."""
        return self.json['alternateName']

    @property
    def short_name(self) -> str:
        """Returns the short name of the season."""
        return self.json['shortName']

    @property
    def short_alternate_name(self) -> str:
        """Returns the short alternate name of the season."""
        return self.json['shortAlternateName']

    @property
    def description(self) -> str:
        """Returns the description of the season."""
        return self.json['description']

    @property
    def year(self) -> int:
        """Returns the year of the season."""
        return self.json['year']

    @property
    def start_date(self) -> str:
        """Returns the start date of the season."""
        return self.json['startDate']

    @property
    def end_date(self) -> str:
        """Returns the end date of the season."""
        return self.json['endDate']

    @property
    def slug(self) -> str:
        """Returns the slug of the season."""
        return self.json['slug']

    @property
    def teams(self) -> List[Team]:
        """Returns a list of teams in the season."""
        if self._teams is None:
            tms = self.get_json(self.teams_url)["items"]
            self._teams = [Team(team_url=tm["$ref"]) for tm in tms]
        return self._teams


