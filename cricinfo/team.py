from __future__ import annotations

from typing import List, overload
from datetime import datetime

from .base import BaseModel

from .athlete import Athlete



class Team[Q: str | int | None](BaseModel):

    @overload
    def __init__(
        self,
        *,
        league_id: int,
        id: int,
    ):
        pass

    @overload
    def __init__(
        self,
        *,
        team_url: str,
    ):
        pass

    def __init__(
        self,
        *,
        team_url: Q = None,
        league_id: Q = None,
        id: Q = None,
    ):
        if id and league_id:
            self.json_url = f"http://core.espnuk.org/v2/sports/cricket/leagues/{league_id}/teams/{id}/"
        else:
            self.json_url = team_url
        self.json = j = self.get_json(self.json_url)

        self.id = int(j['id'])

        self.athletes_url = j['athletes']["$ref"]
        self._athletes = []

    def __repr__(self) -> str:
        return f"<Team {self.name}>"

    @property
    def name(self) -> str:
        """Returns the name of the team."""
        return self.json['name']

    @property
    def nickname(self) -> str:
        """Returns the nickname of the team."""
        return self.json['nickname']

    @property
    def abbreviation(self) -> str:
        """Returns the abbreviation of the team."""
        return self.json['abbreviation']

    @property
    def display_name(self) -> str:
        """Returns the display name of the team."""
        return self.json['displayName']

    @property
    def short_display_name(self) -> str:
        """Returns the short display name of the team."""
        return self.json['shortDisplayName']

    @property
    def is_national(self) -> bool:
        """Returns whether the team is national."""
        return self.json['isNational']

    @property
    def is_active(self) -> bool:
        """Returns whether the team is active."""
        return self.json['isActive']

    @property
    def country_code(self) -> str:
        """Returns the country code of the team."""
        return self.json['countryCode']

    @property
    def slug(self) -> str:
        """Returns the slug of the team."""
        return self.json['slug']

    @property
    def athletes(self) -> List[Athlete[str]]:
        """Returns a list of athletes in the team."""
        if not self._athletes:
            j = self.get_json(self.athletes_url)
            for a in j['items']:
                self._athletes.append(Athlete(player_url=a['$ref']))
        return self._athletes

    def get_athlete(
        self,
        name: str,
    ) -> Athlete[str] | None:
        """Returns the athlete with the given name."""
        name = name.lower().strip()
        for a in self.athletes:
            if name in (
                a.name.lower(), a.first_name.lower(),
                a.middle_name.lower(), a.last_name.lower(),
                a.short_name.lower(), a.full_name.lower(),
                a.display_name.lower(), a.batting_name.lower(),
                a.fielding_name.lower(),
                ):
                return a
        return None
    
