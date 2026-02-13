from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import List


class CrewRanks(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        ranks_present = {m.rank for m in self.crew}
        required_ranks = {CrewRanks.commander, CrewRanks.captain}
        if not required_ranks.intersection(ranks_present):
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            exp_count = sum(1 for m in self.crew if m.years_experience >= 5)
            if exp_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions require at least 50% experienced crew")

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        crew = [
            CrewMember(
                member_id="CM001", name="Sarah Connor",
                rank=CrewRanks.commander,
                age=35, specialization="Mission Command", years_experience=10
            ),
            CrewMember(
                member_id="CM002", name="John Smith",
                rank=CrewRanks.lieutenant,
                age=40, specialization="Navigation", years_experience=15
            ),
            CrewMember(
                member_id="CM003", name="Alice Johnson",
                rank=CrewRanks.officer,
                age=30, specialization="Engineering", years_experience=5
            )
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-07-01T09:00:00",
            duration_days=900,
            crew=crew,
            mission_status="active",
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Validation Error: {e}")

    print("=========================================")
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Fail",
            destination="Moon",
            launch_date="2026-01-01T12:00:00",
            duration_days=10,
            crew=[
                CrewMember(
                    member_id="CM999", name="Red Shirt", rank=CrewRanks.cadet,
                    age=19, specialization="Security", years_experience=0
                )
            ],
            budget_millions=100.0
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
