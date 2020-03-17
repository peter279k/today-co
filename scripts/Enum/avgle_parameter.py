from enum import Enum
 
class AvgleTimeType(Enum):
    TODAY = 't'
    WEEK = 'w'
    MONTH = 'm'
    FOREVER = 'a'

class AvgleSeachType(Enum):
    LastViewed = 'bw'
    Latest = 'mr'
    MostViewed = 'mv'
    TopRated = 'tr'
    MostFavoured = 'tf'
    Longest = 'lg'