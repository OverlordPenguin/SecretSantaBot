import copy

from sopel.module import commands, require_privmsg, require_chanmsg
import random

def newGame(bot):
    bot.memory['secretSanta'] = { 'players':[],
                                  'elfToElf':{},
                                  'santaToSanta':{},
                                  'playerLocations':{},
                                  'playerPreferences':{},
                                  'setupReady':False,
                                  'christmasPhase':False

    }



@require_privmsg
@commands('load')
def loadSheet(bot, trigger):
    


@require_chanmsg
@commands('start')
def startSanta(bot, trigger):
    if bot.memory['secretSanta']['setupReady'] == True:
        
    else:
        bot.say("No sheet has been loaded.") 