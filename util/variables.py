#Instances in util/instances.py, trauma in entities/traum.py

#Sample location
locations = {
  "Home": {
    "time": 0,
  },
  "Woods": {
    "time": 0,
  }
}

party = []
inventory = [["Money", 0]]

def add_party_member(party_member):
  party.append(party_member)
def add_item(name, data):
  party.append([name, data])

long = 0.025 #These 3 may get moved to where delay_print is defined
punc_delays = {',': 3, '(': 4, ')': 4, ';': 4, ':': 5, '.': 5, '?': 5, '!': 5}
punc_pause = True
