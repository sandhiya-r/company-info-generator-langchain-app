from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List


#defining the desired data structure
class CompanyIntel(BaseModel):
    summary: str = Field(description="Summary of the company")
    skills: List[str] = Field(description="List of skills needed to work at the company")

    def to_dict(self): #will be used when server responds with serialized info
        return {'summary':self.summary,'skills':self.skills}

parser = PydanticOutputParser(pydantic_object=CompanyIntel)
