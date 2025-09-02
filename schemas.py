from typing import List
from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema For Source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema For AgentResponse with answers and source urls"""

    answer: str = Field(description="The agent answer's to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answers"
    )
