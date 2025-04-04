from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Optional, List
import datetime


class Risk(BaseModel):
    name: str = Field(..., title="Risk Name", description="Name of the risk.")
    impact: int = Field(
        ...,
        title="Impact",
        description="Impact assessment of the risk, represented as an integer between 1 (low) and 5 (high).",
    )
    likelihood: int = Field(
        ...,
        title="Likelihood",
        description="Likelihood assessment of the risk, represented as an integer between 1 (low) and 5 (high).",
    )

    @field_validator("name")
    def validate_non_empty(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name} must be a non-empty string.")
        return v

    @field_validator("impact", "likelihood")
    def validate_impact_likelihood(cls, v, info):
        if v < 1 or v > 5 or not isinstance(v, int):
            raise ValueError(f"{info.field_name} must be an integer between 1 and 5.")
        return v

    @computed_field(return_type=float)
    @property
    def impact_level(self):
        """
        Impact level as a decimal percentage.
        """
        return max(0.05, min(self.impact / 5, 0.95))

    @computed_field(return_type=float)
    @property
    def likelihood_level(self):
        """
        Likelihood level as a decimal percentage.
        """
        return max(0.01, min(self.likelihood / 5, 0.99))


class RiskSection(BaseModel):
    risks: List[Risk] = Field(
        ..., title="Risk", description="List of risks associated with the project"
    )
    content: str = Field(
        ..., title="Risk Description", description="The content of the risk section."
    )

    @field_validator("content")
    def validate_non_empty(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name} must be a non-empty string")
        return v


class Budget(BaseModel):
    name: str = Field(..., title="Budget Name", description="Name of the budget item")
    amount: float = Field(
        ..., title="Budget Amount", description="Amount allocated for the budget item"
    )

    @field_validator("name")
    def validate_non_empty(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name} must be a non-empty string")
        return v

    @field_validator("amount")
    def validate_positive(cls, v, info):
        if v <= 0:
            raise ValueError(f"{info.field_name} must be a positive number")
        return v


class BudgetSection(BaseModel):
    budget: List[Budget] = Field(
        ...,
        title="Budget",
        description="List of budget items associated with the project",
    )
    content: str = Field(
        ...,
        title="Budget Description",
        description="The content of the budget section.",
    )

    @field_validator("content")
    def validate_non_empty(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name} must be a non-empty string")
        return v

    @field_validator("budget")
    def validate_non_empty_list(cls, v, info):
        if not isinstance(v, list) or len(v) == 0:
            raise ValueError(f"{info.field_name} must be a non-empty list")
        return v


class Objective(BaseModel):
    name: str = Field(..., title="Objective Name", description="Name of the objective")
    start_date: str = Field(
        ...,
        title="Start Date",
        description="Start date of the objective. Must be in YYYY-MM-DD format",
    )
    end_date: str = Field(
        ...,
        title="End Date",
        description="End date of the objective. Must be in YYYY-MM-DD format",
    )

    @computed_field(return_type=int)
    @property
    def duration(self):
        # Convert start_date and end_date to datetime objects and calculate duration in days
        start_date = datetime.datetime.strptime(self.start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(self.end_date, "%Y-%m-%d")
        duration = (end_date - start_date).days
        return duration

    @field_validator("start_date", "end_date")
    def validate_date_format(cls, v, info):
        try:
            datetime.datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"{info.field_name} must be in YYYY-MM-DD format")
        return v

    @field_validator("name")
    def validate_non_empty(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name} must be a non-empty string")
        return v

    @field_validator("duration")
    def validate_duration(cls, v):
        if v < 0:
            raise ValueError(f"Duration must be a non-negative integer")
        return v


class ObjectiveSection(BaseModel):
    objectives: List[Objective] = Field(
        ...,
        title="Objectives",
        description="List of objectives associated with the project",
    )
    content: str = Field(
        ...,
        title="Objective Description",
        description="The content of the objective section.",
    )

    @field_validator("content")
    def validate_non_empty(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name} must be a non-empty string")
        return v

    @field_validator("objectives")
    def validate_non_empty_list(cls, v, info):
        if not isinstance(v, list) or len(v) == 0:
            raise ValueError(f"{info.field_name} must be a non-empty list")
        return v


class ProjectDescriptionSection(BaseModel):
    project_name: str = Field(
        ..., title="Project Name", description="Name of the project"
    )
    content: str = Field(
        ..., title="Project Description", description="Description of the project"
    )

    @field_validator("project_name", "content")
    def validate_non_empty(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name} must be a non-empty string")
        return v


class ProjectDescription(BaseModel):
    project: ProjectDescriptionSection = Field(
        ..., title="Project Description", description="Description of the project"
    )
    start_date: str = Field(
        ..., title="Start Date", description="Start date of the project"
    )
    end_date: str = Field(..., title="End Date", description="End date of the project")
    stakeholders: List[str] = Field(
        ...,
        title="Stakeholders",
        description="List of stakeholders involved in the project",
    )
    budget: BudgetSection = Field(
        ..., title="Budget", description="Estimated budget for the project"
    )
    objectives: Optional[ObjectiveSection] = Field(
        ...,
        title="Objectives",
        description="List of objectives for the project. This is optional.",
    )
    risks: Optional[RiskSection] = Field(
        ...,
        title="Risks",
        description="List of potential risks associated with the project. This is optional.",
    )

    @field_validator("start_date", "end_date")
    def validate_date_format(cls, v, info):
        try:
            datetime.datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"{info.field_name} must be in YYYY-MM-DD format")
        return v

    @field_validator("stakeholders")
    def validate_non_empty_list(cls, v, info):
        if not isinstance(v, list) or len(v) == 0:
            raise ValueError(f"{info.field_name} must be a non-empty list")
        return v
