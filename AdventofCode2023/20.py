fiji1 = 0
fiji2 = 0

data = []

with open("input/20.txt", "r") as file:
    for zeile in file:
        vorderteil, stringzu = zeile.split(" -> ")
        zu = stringzu.split(',')
        zu = [element.strip() for element in zu]
        if len(zu) == 1:
            zu = zu[0]
        if vorderteil == "broadcaster":
            von = "broadcaster"
            art = "broadcaster"
        else:
            art = vorderteil[0]
            von = vorderteil[1:]
        entry = {
            "m": von,
            "t": art,
            "z": zu
        }
        data.append(entry)

stati = []
for x in data:
    if x["t"] == "%":
        modul = x["m"]
        status = {
            "m": modul,
            "s": 0
        }
        stati.append(status)
    elif x["t"] == "&":
        modul = x["m"]
        status = {
            "m": modul,
            "s": 0
        }
        stati.append(status)

cons = []
for x in data:
    if x["t"] == "&":
        modul = x["m"]
        watchlist = []
        for y in data:
            #print("Y",y,"modul",modul)
            if modul in y["z"]:
                #print("istdrin")
                watchlist.append(y["m"])
        cons.append([modul, watchlist])
        #hier ein assoz. array erstellen, dass checkstatecon aufgreifen kann, mit:
        #eintrag[modul] = watchlist


def main(signaleundempfänger):
    stillstand = False
    lowpulscount = 0
    highpulscount = 0
    while not stillstand:
        #print("Signale & Empfänger",signaleundempfänger)
        #print("Stati",stati)
        new_signaleundempfänger = []
        filtered_signaleundempfänger = [item for item in signaleundempfänger if item['s'] is not None]
        if not filtered_signaleundempfänger:
            stillstand = True
            break
        else:
            for x in filtered_signaleundempfänger:
                signal = x["s"]
                empfängers = x["z"]
                #print("Signal",signal)
                #print("Empfänger",empfängers)
                for empfänger in empfängers:
                    #print("Innerer Main Loop:","Signal",signal,"Empfänger",empfänger,)
                    einneues_signalundempfänger = kategorisieren(signal,empfänger)      
                    new_signaleundempfänger.append(einneues_signalundempfänger) 
                    #print("Signal",signal)
                    #print("Empfänger",empfänger)
                    if signal == "high":
                        highpulscount += 1
                        #print("Highpuls",highpulscount)
                    elif signal == "low":
                        lowpulscount += 1
                        #print("Lowpuls",lowpulscount)
        signaleundempfänger = new_signaleundempfänger
        #print( )
    returnval = (highpulscount, lowpulscount)
    return returnval

def checkstate(modul):
    for status in stati:
        if status["m"] in modul:
            state = status["s"]
            return state


def kategorisieren(signal,modul,buttoncount = None):
    for eintrag in data:
        if eintrag["m"] == modul:
            n_modul = eintrag["z"]
            #print("Eintrag",eintrag)
            #print("Anfang Kategorisierung",eintrag["m"],modul)
            #print("Neues Modul",n_modul)

            if eintrag["t"] == "broadcaster":
                n_signal = "low"
            elif eintrag["t"] == "button":
                n_signal = "low"
            else:
                if eintrag["t"] == "%":
                    state = checkstate(modul)
                    n_signal = flipflop(signal,state,modul)
                elif eintrag["t"] == "&":
                    #print("Kategorie Modul",modul)
                    n_signal = conjunction(modul,buttoncount)

            if not isinstance(n_modul, list):
                n_modul = [n_modul]

            n_pair = {
                "s": n_signal,
                "z": n_modul
            }

            return n_pair

    leer_pair = {
        "s": None,
        "z": None
    }
    return leer_pair
            

def flipflop(signal,state,modul):
    if signal == "high":
        #print("Signal None")
        return None
    elif signal == "low":
        #print("Lowsignal flipflop State:",state)
        if state == 0:
            for i,x in enumerate(stati):
                if x["m"] == modul:
                    stati[i]["s"] = 1
            #print("Signal high")
            return "high"
        elif state == 1:
            for i,x in enumerate(stati):
                if x["m"] == modul:
                    stati[i]["s"] = 0
            #print("Signal low")
            return "low"

def conjunction(modul,buttoncount=None):
    #print(cons)
    for x in cons:
        #print("X",x,"modul",modul)
        if x[0] == modul:
            watchlist = x[1]
            #print("Modul",modul,"Watchlist",watchlist)
            allwatchliston = True
            for flipmodul in watchlist:
                state = checkstate(flipmodul)
                if modul in ["dh","db","lm","sg"] and state == 0:
                    print("Flipstate",modul,state,"Count",buttoncount)
                    if buttoncount > 5000:
                        rx[modul] = buttoncount - rx[modul]
                    else:
                        rx[modul] = buttoncount
                if state == 0:
                    allwatchliston = False
            if allwatchliston:
                #print("Low conj")
                for i,x in enumerate(stati):
                    if x["m"] == modul:
                        stati[i]["s"] = 0
                return "low"
            else:
                for i,x in enumerate(stati):
                    if x["m"] == modul:
                        stati[i]["s"] = 1
                return "high"

    
#print("Stati:",stati)
#print("Cons:",cons)
#print("Data",data)
                    

startsignal = [{
    "s": "low",
    "z": ["broadcaster"]
}]
lowcount = 0
highcount = 0
buttoncount = 0
for i in range(1000):
    buttoncount += 1
    highcountx, lowcountx = main(startsignal)
    lowcount += lowcountx
    highcount += highcountx
    #print("Low Nummer",lowcount,"High Nummer",highcount)

fiji1 = lowcount * highcount

def main2(signaleundempfänger,buttoncount):
    stillstand = False
    lowpulscount = 0
    highpulscount = 0
    while not stillstand:
        #print("Signale & Empfänger",signaleundempfänger)
        #print("Stati",stati)
        new_signaleundempfänger = []
        filtered_signaleundempfänger = [item for item in signaleundempfänger if item['s'] is not None]
        if not filtered_signaleundempfänger:
            stillstand = True
            break
        else:
            for x in filtered_signaleundempfänger:
                signal = x["s"]
                empfängers = x["z"]
                #print("Signal",signal)
                #print("Empfänger",empfängers)
                for empfänger in empfängers:
                    #print("Innerer Main Loop:","Signal",signal,"Empfänger",empfänger,)
                    einneues_signalundempfänger = kategorisieren(signal,empfänger,buttoncount)      
                    new_signaleundempfänger.append(einneues_signalundempfänger) 
                    #print("Signal",signal)
                    #print("Empfänger",empfänger)
                    if signal == "high":
                        highpulscount += 1
                        #print("Highpuls",highpulscount)
                    elif signal == "low":
                        lowpulscount += 1
                        #print("Lowpuls",lowpulscount)
        signaleundempfänger = new_signaleundempfänger
        #print( )

buttoncount = 0
rx = {}
for i in range(10000):
    buttoncount += 1
    on = main2(startsignal,buttoncount)

# aus den prints LCM vals nehmen
import math
print(rx)
rx_values = list(rx.values())
fiji2 = math.lcm(*rx_values)

print("Lösung Aufgabe 20.1: " + str(fiji1))
print("Lösung Aufgabe 20.2: " + str(fiji2))
print("Grüße von Fiji :^)")