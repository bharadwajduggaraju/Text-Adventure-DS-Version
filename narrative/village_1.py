#In progress
from narrative.nodes.node import Node
from util.colors import *
from util.colors import RESET, DARK_RED, WHITE
#Current format: areaname_varStates
village_1_variables = {
  "QUEST_COMPLETE": ["BOOL", False],
  "MINU_VISITS": ["INT", 0],
  "STOLE_SOMETHING": ["BOOL", False],
  "MINU_MAD": ["BOOL", False],
  "SQUARE_VISITS": ["INT", 0],
  "BALLIYA_COAT": ["BOOL", False]
}

noblehouse_questCompleteF = Node("noblehouse_quCoF", [], WHITE + "The door is locked!{TIME:1}{CLEAR}{ENTER:village_1}", [])
noblehouse_questCompleteT = Node("noblehouse_quCoT", [], WHITE + "The knocker thumps hollowly against the door.\nYou hear frantic footsteps scuttling in your direction.\nThe door creaks open, revealing a stout old butler in a tuxedo.\n'Stay out of this house!' he whines. 'The master is not expecting visitors!'\nYou were shoved out of the house!{TIME:1}{CLEAR}{ENTER:village_1}", [])

noblehouse = Node("noblehouse", [noblehouse_questCompleteF, noblehouse_questCompleteT], DARK_RED + "NOBLE HOUSE{TIME:0.25}", [])

ch_carpenter_breakfastF = Node("ch_carpenter_breakfastF", [], "'That's all right,' the carpenter says, slightly disappointed. 'Don't forget to come back another time!'{TIME:1}{CLEAR}{ENTER:village_1", [])
ch_carpenter_breakfastT = Node("ch_carpenter_breakfastT", [], "'Wonderful!' He grins and proffers a bowl of steaming hot rice\nYou much on the food you were offered. It's delicious!{CHARACTER:Esteri:HP:=MAX}{TIME:1}{ENTER:carpenterhouse}", [])
ch_carpenter = Node("ch_carpenter", [ch_carpenter_breakfastT, ch_carpenter_breakfastT, ch_carpenter_breakfastF, ch_carpenter_breakfastF], "The carpenter glances up at you with a bit of confusion. His eyes crinkle kindly when he recognizes you.\n'Hello, hero!' he says, standing frantically and bowing. 'I greatly appreciate your help. Thank you for saving my wife, my daughter, and I!'\nHe looks down at his daughter for a second, expression soft and proud. 'I would never forgive myself if I let her be hurt.'\n{TIME:0.25}You're hit by a pang of jealousy.\n{TIME:0.25}He looks back at you, slightly disoriented. 'Where was I? Ah, yes. We're eating breakfast right now. All we have is rice, but it may be able to help you replenish your energy. Would you like to eat some?'", ["yes", "y", "no", "n"])

ch_carpenterwife = Node("ch_carpenterwife", [], "The carpenter's wife gnaws on rice. She seems distracted.\n'Mmmmm... such good rice...'{TIME:1}{ENTER:carpenterhouse}", [])

ch_minu_takeAmulet1 = Node("ch_minu_taAm1", [], "You sneak the stone into your bag. No one notices.{ADD_ITEM:Minu's Amulet:An amulet containing the power to harm others.}You decide to sneak out of the carpenter's house before anyone can catch you.{CHANGE:STOLE_SOMETHING:TRUE}{CHANGE:MINU_VISITS:1}{TIME:1}{CLEAR}{ENTER:village_1}", [])
ch_minu_takeAmulet2 = Node("ch_minu_taAm2", [], "You rescind your hand and smile stiffly.{TIME:1}{CLEAR}{ENTER:carpenterhouse}", [])

ch_minu_minuSecret1_carpenterDisappointed1 = Node("ch_minu_miSe1_caDi1", [], "'Thank you!' Minu's face brightens. 'That makes me feel a lot more confident.'\nShe looks down for a second. 'It's been a while since I'd had a good friend...'{TIME:0.5}The moment of silence passes, and Minu smiles awkwardly.{TIME:0.5}She holds out her palm. In it is a small purple stone, pusling with blue light.\nShe grins. 'I'd like you to have this as thanks.'\nYou take the amulet and slip it into your bag.{ADD_ITEM:Minu's Amulet:An amulet containing a mysterious healing power.}{CHANGE:MINU_VISITS:1}{TIME:1}{CLEAR}{ENTER:carpenterhouse}", [])
ch_minu_minuSecret1_carpenterDisappointed2 = Node("ch_minu_miSe1_caDi2", [ch_minu_takeAmulet1, ch_minu_takeAmulet2], "'Oh...' Minu looks concerned. 'I suppose you're right. Thank you for your time, Esteri.'\nShe turns away, looking disheartened.\nYou notice a stone next to her plate, bright red and pulsing with fiery orange streaks.\nDo you take it?\n 1. Yes\n 2. No", [1, 2])

ch_minu_minuSecret1 = Node("ch_minu_miSe1", [ch_minu_minuSecret1_carpenterDisappointed1, ch_minu_minuSecret1_carpenterDisappointed2], "She furtively flicks her gaze to her father.\n'I'm afraid that my dad is disappointed that I'm not a carpenter,' she confesses.\nShe looks sheepish. 'I wish I could be a good carpenter, I really do. But I enjoy taking care of animals more.'\nShe looks down at her lap. 'Do you think he's mad at me?'\nWhat will you say?\n 1. I'm sure he loves you a lot. He isn't angry.\n 2. I think he is... he seems angry.", [1, 2])
ch_minu_minuSecret2 = Node("ch_minu_miSe2", [], "Minu smiles softly. 'That's all right. Maybe you can come back another time to hear my secret!'{TIME:1}{CLEAR}{ENTER:carpenterhouse}", [])

ch_minu_minuVisits0_EsteriDescription1 = Node("ch_minu_miVi0_EsDe1", [ch_minu_minuSecret1, ch_minu_minuSecret2], "'Nice to meet you, Esteri!'\nThe girl bows slightly. 'My name is Minu.'\nHer expression becomes one of trepidation. 'Can I trust you with a secret?'\nChoose your response.\n 1. Sure!\n 2. No way.", [1, 2])
ch_minu_minuVisits0_EsteriDescription2 = Node("ch_minu_miVi0_EsDe2", [], "'Well, that was rude!' She looks slightly offended.{CHANGE:MINU_MAD:TRUE}{TIME:1}{CLEAR}{ENTER:carpenterhouse}", [])
ch_minu_minuVisits0_EsteriDescription3 = Node("ch_minu_miVi0_EsDe3", [], "'Oh... maybe I picked the wrong person. Sorry!' She looks slightly uncomfortable.{TIME:1}{CLEAR}{ENTER:carpenterhouse}", [])

ch_minu_minuVisits0 = Node("ch_minu_miVi0", [ch_minu_minuVisits0_EsteriDescription1, ch_minu_minuVisits0_EsteriDescription2, ch_minu_minuVisits0_EsteriDescription3], "The carpenter's daughter looks downcast. She picks at her rice.\nShe glances up at you.\n'Oh, you're the village hero!' she says, recognizing you immediately.\nShe kneads her hands. 'What's your name?'\nWhat will you say?\n 1. I'm Esteri! I'm the heir to the chiefdom of Elyria!\n 2. You don't deserve to know.\n 3. Who's the village hero?", [1, 2, 3])
ch_minu_minuVisits1 = Node("ch_minu_miVi1+", [], "'This rice is delicious!{EXIT}'", [])

ch_minu_minuMadF = Node("ch_minu_miMaF", [ch_minu_minuVisits0, ch_minu_minuVisits1], "", "MINU_MAD")
ch_minu_minuMadT = Node("ch_minu_miMaT", [], "You shouldn't go over to her! She's angry!{TIME:1}{CLEAR}{ENTER:carpenterhouse}", [])
ch_minu = Node("ch_minu", [ch_minu_minuMadF, ch_minu_minuMadT], "", "MINU_MAD")

ch_none = Node("ch_none", [], "{TIME:0.5}{CLEAR}{ENTER:village_1}", [])

ch_questCompleteF = Node("ch_QuCoF", [], "The door is locked!{TIME:1}{CLEAR}", [])
ch_questCompleteT = Node("ch_QuCoT", [ch_carpenter, ch_carpenterwife, ch_minu, ch_none], WHITE + "{TIME:0.25}Who would you like to talk to?\n 1. Carpenter\n 2. Carpenter's Wife\n 3. Carpenter's Daughter\n 4. Exit House", [1, 2, 3, 4])

ch_stoleSomethingF = Node("ch_StSoF", [ch_questCompleteF, ch_questCompleteT], "{CLEAR}" + DARK_RED + "CARPENTER'S HOUSE{TIME:0.25}" + RESET, "QUEST_COMPLETE")
ch_stoleSomethingT = Node("ch_StSoT", [], "You can't enter! They might find out that you stole Minu's amulet!" + "{TIME:1.0}{CLEAR}{ENTER:village_1}", [])

carpenterhouse = Node("carpenterhouse", [ch_stoleSomethingF, ch_stoleSomethingT], "", "STOLE_SOMETHING")

cobblerhouse = Node("cobblerhouse", [], "[Entering a store unavabile]", [])

tailorhouse_questCompleteF = Node("tailorhouse_quCoF", [], WHITE + "The door is locked!{TIME:1}{CLEAR}{ENTER:village_1}", [])
tailorhouse_questCompleteT = Node("tailorhouse_quCoT", [], WHITE + "You fiddle with the doorknob and the door squeaks open, scuffing the dirt floor.\nThe inside of the house is filthy. Do you still want to go in?{EXIT}", [])
tailorhouse = Node("tailorhouse", [tailorhouse_questCompleteF, tailorhouse_questCompleteT], "{CLEAR}" + DARK_RED + "TAILOR'S HOUSE{TIME:0.25}" + RESET, "QUEST_COMPLETE")

kurigaluhouse_letter = Node("kurgalu_le", [], "{TIME:1}{CLEAR}Kurigalu pores over the letter. 'Interesting...' she mumbles.\nShe looks up after a few seconds of incoherent mumbling. 'Aviveki sent you?'\nNo longer able to contain himself, Kosu nods. 'Yes.'\nKurigalu frowns. 'Aviveki and I are not on the best of terms.'\nYou wonder what she's talking about.\nBehind you, Kosu shifts nervously on his feet. 'We don't necessarily like her much either,' he lies, lacking conviction.\n'But we don't have much of a choice. We'd like to find Chief Amaliyah and restore her to her position.'{TIME:1}{CLEAR}Kurigalu folds the letter into a small square and drops it into the fire.\nShe gives you a long, hard look, and sighs with exhaustion.\n'I'm an old lady,' she tells you. 'I no longer have as much energy as I did years ago. I can't offer you much help myself.'\n'On the other hand,' she continues, 'Amaliyah was one of my best students...'\nShe meets your eyes. 'And you seem to take after your mother.'{TIME:1}{CLEAR}She pulls out a piece of aged charcoal and a sheet of pulpy wood paper.\nAfter spending a few seconds scribbling frantically in Oi'nan, she folds the letter and hands it to you.\n'Here,' she tells you. 'Take this letter to Nagara and find a man named Hukosu. He may be able to help you.'\nYou nod.\nKosu clears his throat. 'Do we have to go to Nagara?'\nHe sounds uncharacteristically scared.\nKurigalu looks up at him, expression suddenly sharp. 'Yes,' she says slowly. 'You must go to Nagara.'{EXIT}", [])
kurigaluhouse_AmaliyahDeath = Node("kurigalu_AmDe", [kurigaluhouse_letter, kurigaluhouse_letter], "Kurigalu inclines her head. 'Mmm.'\nWill you give Kurigalu the letter?", ["y", "yes"], err_message="You'd better give the letter to her!")
kurigaluhouse_EsteriIntroDone = Node("kurigaluhouse_EsInDo", [kurigaluhouse_AmaliyahDeath, kurigaluhouse_AmaliyahDeath], "Kurigalu inclines her head. 'I heard that Amaliyah died years ago.'\nWhat will you say?\n 1. We're not sure. I'm hoping to find her.\n 2. I don't think she died. That's why I'm looking for her.", [1, 2], err_message="Kurigalu waits patiently for an answer.")
# kurigaluhouse_EsteriIntro1 = Node("kurigaluhouse_EsIn1")

kurigaluhouse_questCompleteF = Node("kurigaluhouse_quCoF", [], "The door is locked!{TIME:1}{CLEAR}{ENTER:village_1}", [])
# kurigaluhouse_questCompleteT = Node("kurigaluhouse_quCoT", )
# kurigaluhouse = Node("kurigaluhouse", )

# village1_questCompleteF = Node("village1_questIncomplete")

