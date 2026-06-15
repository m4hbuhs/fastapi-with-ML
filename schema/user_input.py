from pydantic import BaseModel,Field , computed_field
from typing import Literal,Annotated

class UserInput(BaseModel):
    education: Annotated[Literal["Graduate", "Not Graduate"],Field(..., description='Grauated or Not Graduated')]
    self_employed: Annotated[Literal['Yes','No'],Field(..., description='Yes or No')]
    income_annum: Annotated[int , Field(...,gt=0,description ='Annum income ')]
    loan_amount:  Annotated[int , Field(...,gt=0,description ='Amount of loan')]
    loan_term:  Annotated[int , Field(...,gt=0,description ='term of loan')]
    cibil_score:  Annotated[int , Field(...,ge=300,le=900,description ='cibil Score')]
    residential_assets_value:  Annotated[int , Field(...,ge=0, description ='value of the residential assets')]
    commercial_assets_value:  Annotated[int , Field(...,ge=0, description ='Value of commercial assets ')]
    luxury_assets_value:  Annotated[int , Field(..., ge=0,description ='Value of luxury assets value')]
    bank_asset_value:  Annotated[int , Field(..., ge=0,description ='Value of bank assert')]