from bots.strbot import strbot
from bots.calcbot import calcbot

def getBots():
    return(
    {
        "strbot": strbot,
        "calcbot": calcbot,
    })
