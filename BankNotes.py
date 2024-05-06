## To "post" the 4 parameters of our dataset:
#   - variance
#   - skewness
#   - curtosis
#   - entropy

from pydantic import BaseModel

# This class describes bank note measurements.
class BankNote(BaseModel):
    variance : float
    skewness : float
    curtosis : float
    entropy : float