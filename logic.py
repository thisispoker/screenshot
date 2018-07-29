import error_log
import postgresql
import db_conf

def getDecision(hand):
    try:
        if pocketBroadway(hand) == 1 or pocketPair(hand) == 1 or anyAce(hand) == 1 or suitedConnectors(hand) == 1:
            return 1
        else:
            return 0
    except Exception as e:
        error_log.errorLog('getDecision',e)


def pocketBroadway(hand):
    val = ''
    broadway = ['A', 'K', 'Q', 'J', 'T']
    for value in hand:
        if value.isupper():
            val += value
    try:
        if val[0] in broadway and val[1] in broadway:
            return 1
        else:
            return 0
    except:
        return 0

def pocketPair(hand):
    val = ''
    for c in hand:
        if c.isupper() or c.isdigit():
            val += c
    if val[0] == val[1]:
        return 1
    else:
        return 0

def anyAce(hand):
    val = ''
    for c in hand:
        if c.isupper() or c.isdigit():
            val += c
    if val[0] == 'A' or val[1] == 'A':
        return 1
    else:
        return 0

def suitedConnectors(hand):
    arr = ['K', 'Q', 'J', 'T', '9', '8', '7']
    if hand[1] == hand[3]:
        if hand[0] in arr and hand[2] in arr:
            return 1

def getIterationTimer(ui_element):
    db = postgresql.open(db_conf.connectionString())
    data = db.query("select round(extract(epoch from now() - created_at)) as seconds_left from iteration_timer where ui_element = '" + ui_element + "'")
    return data[0]['seconds_left']

def updateIterationTimer(ui_element):
    db = postgresql.open(db_conf.connectionString())
    db.query("UPDATE iteration_timer SET created_at = now() where ui_element = '" + ui_element + "'")