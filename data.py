# -*- coding: utf-8 -*-

"""
This file contains the data for the 64 hexagrams of the I Ching.
Each hexagram is represented as a dictionary with the following structure:
- num: The hexagram number (1-64).
- binary: A tuple of 6 elements (0 for Yin, 1 for Yang) representing the lines from bottom to top.
- name_ch: The name in Chinese (Pinyin).
- name_en: The name in English.
- image: The description of the Image.
- judgement: The description of the Judgment.
"""

HEXAGRAM_DATA = [
    {
        "num": 1, "binary": (1, 1, 1, 1, 1, 1), "name_ch": "Qian", "name_en": "The Creative",
        "image": "The movement of heaven is powerful. Thus the superior man makes himself strong and untiring.",
        "judgement": "The Creative works sublime success, furthering through perseverance.",
        "lines": [
            "Nine at the beginning: Hidden dragon. Do not act.",
            "Nine in the second place: Dragon appearing in the field. It furthers one to see the great man.",
            "Nine in the third place: All day long the superior man is creatively active. At nightfall his mind is still beset with cares. Danger. No blame.",
            "Nine in the fourth place: Wavering flight over the depths. No blame.",
            "Nine in the fifth place: Flying dragon in the heavens. It furthers one to see the great man.",
            "Nine at the top: Arrogant dragon will have cause to repent."
        ]
    },
    {
        "num": 2, "binary": (0, 0, 0, 0, 0, 0), "name_ch": "Kun", "name_en": "The Receptive",
        "image": "The earth's condition is receptive devotion. Thus the superior man of broad character carries the outer world.",
        "judgement": "The Receptive brings about sublime success, furthering through the perseverance of a mare. If the superior man undertakes something and tries to lead, he goes astray; but if he follows, he finds guidance.",
        "lines": [
            "Six at the beginning: When there is hoarfrost underfoot, solid ice is not far off.",
            "Six in the second place: Straight, square, great. Without purpose, yet everything is furthered.",
            "Six in the third place: Hidden lines. One is able to remain persevering. If in the service of a king, seek not works, but bring to completion.",
            "Six in the fourth place: A tied-up sack. No blame, no praise.",
            "Six in the fifth place: A yellow undergarment. Sublime good fortune.",
            "Six at the top: Dragons fight in the meadow. Their blood is black and yellow."
        ]
    },
    {
        "num": 3, "binary": (0, 1, 0, 0, 0, 1), "name_ch": "Zhun", "name_en": "Difficulty at the Beginning",
        "image": "Clouds and thunder: the image of Difficulty at the Beginning. Thus the superior man brings order out of confusion.",
        "judgement": "Difficulty at the Beginning works sublime success, furthering through perseverance. Nothing should be undertaken. It furthers one to appoint helpers.",
        "lines": [
            "Nine at the beginning: Hindrance and hesitation. It furthers one to remain persevering. It furthers one to appoint helpers.",
            "Six in the second place: Difficulties pile up. Horse and wagon part. He is not a robber; he will woo her in due time. The maiden is chaste, does not pledge herself. Ten years—then she pledges herself.",
            "Six in the third place: Whoever hunts deer without a forester only loses his way in the forest. The superior man, foreseeing the signs of the time, prefers to desist. To go on brings humiliation.",
            "Six in the fourth place: Horse and wagon part. Strive for union. To go brings good fortune. Everything acts to further.",
            "Nine in the fifth place: Difficulties in blessing. A little perseverance brings good fortune. Great perseverance brings misfortune.",
            "Six at the top: Horse and wagon part. Bloody tears flow."
        ]
    },
    {
        "num": 4, "binary": (1, 0, 0, 0, 1, 0), "name_ch": "Meng", "name_en": "Youthful Folly",
        "image": "A spring wells up at the foot of the mountain: the image of Youth. Thus the superior man fosters his character by thoroughness in all that he does.",
        "judgement": "Youthful Folly has success. It is not I who seek the young fool; the young fool seeks me. At the first oracle I inform him. If he asks two or three times, it is importunity. If he importunes, I give him no information. Perseverance furthers.",
        "lines": [
            "Six at the beginning: To make a fool develop it is useful to use punishments. Removing the fetters brings humiliation.",
            "Nine in the second place: To bear with fools in kindliness brings good fortune. To know how to take women brings good fortune. The son is capable of taking charge of the household.",
            "Six in the third place: Do not take a maiden who, when she sees a man of bronze, loses possession of herself. Nothing furthers.",
            "Six in the fourth place: Entangled folly brings humiliation.",
            "Six in the fifth place: Childlike folly brings good fortune.",
            "Nine at the top: In punishing folly it does not further one to commit transgressions. The only thing that furthers is to prevent transgressions."
        ]
    },
    {
        "num": 5, "binary": (0, 1, 0, 1, 1, 1), "name_ch": "Xu", "name_en": "Waiting (Nourishment)",
        "image": "Clouds rise up to heaven: the image of Waiting. Thus the superior man eats and drinks, is joyous and of good cheer.",
        "judgement": "Waiting. If you are sincere, you have light and success. Perseverance brings good fortune. It furthers one to cross the great water.",
        "lines": [
            "Nine at the beginning: Waiting in the meadow. It furthers one to abide in what is lasting. No blame.",
            "Nine in the second place: Waiting on the sand. There is some gossip. The end brings good fortune.",
            "Nine in the third place: Waiting in the mud brings about the arrival of the enemy.",
            "Six in the fourth place: Waiting in blood. Get out of the pit.",
            "Nine in the fifth place: Waiting at meat and drink. Perseverance brings good fortune.",
            "Six at the top: One falls into the pit. Three uninvited guests arrive. Honor them, and in the end there will be good fortune."
        ]
    },
    {
        "num": 6, "binary": (1, 1, 1, 0, 1, 0), "name_ch": "Song", "name_en": "Conflict",
        "image": "Heaven and water go their opposite ways: the image of Conflict. Thus in all his transactions the superior man carefully considers the beginning.",
        "judgement": "Conflict. You are sincere and are being obstructed. A cautious halt halfway brings good fortune. Going through to the end brings misfortune. It furthers one to see the great man. It does not further one to cross the great water.",
        "lines": [
            "Six at the beginning: If one does not perpetuate the affair, there is a little gossip. In the end, good fortune comes.",
            "Nine in the second place: One cannot engage in conflict; one returns home, gives way. The people of his town, three hundred households, remain free of guilt.",
            "Six in the third place: To nourish oneself on ancient virtue induces perseverance. Danger. In the end, good fortune comes. If you are in the service of a king, seek not works.",
            "Nine in the fourth place: One cannot engage in conflict. One turns back and submits to fate, changes one's attitude, and finds peace in perseverance. Good fortune.",
            "Nine in the fifth place: To contend before him brings sublime good fortune.",
            "Nine at the top: Even if by chance a leather belt is bestowed on one, by the end of a morning it will have been snatched away three times."
        ]
    },
    {
        "num": 7, "binary": (0, 0, 0, 0, 1, 0), "name_ch": "Shi", "name_en": "The Army",
        "image": "In the middle of the earth is water: the image of the Army. Thus the superior man increases his masses by generosity toward the people.",
        "judgement": "The Army. The army needs perseverance and a strong man. Good fortune without blame.",
        "lines": [
            "Six at the beginning: An army must set forth in proper order. If the order is not good, misfortune is certain.",
            "Nine in the second place: In the midst of the army. Good fortune. No blame. The king bestows a triple decoration.",
            "Six in the third place: The army may possibly carry corpses in the wagon. Misfortune.",
            "Six in the fourth place: The army retreats. No blame.",
            "Six in the fifth place: There is game in the field. It is favorable to catch it. Without blame. Let the eldest lead the army. The younger transports corpses; then perseverance brings misfortune.",
            "Six at the top: The great prince issues commands, founds states, vests families with fiefs. Inferior people should not be employed."
        ]
    },
    {
        "num": 8, "binary": (0, 1, 0, 0, 0, 0), "name_ch": "Bi", "name_en": "Holding Together (Union)",
        "image": "On the earth is water: the image of Holding Together. Thus the kings of antiquity bestowed the different states as fiefs and cultivated friendly relations with the feudal lords.",
        "judgement": "Holding Together brings good fortune. Inquire of the oracle once more whether you possess sublimity, constancy, and perseverance; then there is no blame. The uncertain come to join. Whoever comes too late meets with misfortune.",
        "lines": [
            "Six at the beginning: Hold to him in truth and loyalty; this is without blame. Truth, like a full earthen bowl: thus in the end good fortune comes from elsewhere.",
            "Six in the second place: Hold to him inwardly. Perseverance brings good fortune.",
            "Six in the third place: You hold together with the wrong people.",
            "Six in the fourth place: Hold to him outwardly also. Perseverance brings good fortune.",
            "Nine in the fifth place: Manifestation of holding together. In the hunt the king uses beaters on three sides only and foregoes the game that runs off in front. The citizens need no warning. Good fortune.",
            "Six at the top: He finds no head for holding together. Misfortune."
        ]
    },
    {
        "num": 9, "binary": (1, 1, 1, 0, 1, 1), "name_ch": "Xiao Chu", "name_en": "The Taming Power of the Small",
        "image": "The wind drives across heaven: the image of the Taming Power of the Small. Thus the superior man refines the outward aspect of his nature.",
        "judgement": "The Taming Power of the Small has success. Dense clouds, no rain from our western region.",
        "lines": [
            "Nine at the beginning: Return to the way. How could that be a blame? Good fortune.",
            "Nine in the second place: He lets himself be drawn back. Good fortune.",
            "Nine in the third place: The spokes of the wagon wheel break. Man and wife look at each other with averted eyes.",
            "Six in the fourth place: If you are sincere, blood vanishes and fear gives way. No blame.",
            "Nine in the fifth place: If you are sincere and loyally attached, you are rich in your neighbor.",
            "Nine at the top: The rain comes, the resting-place comes. The virtue of the woman is loaded. Perseverance brings danger to the woman. The moon is nearly full. If the superior man perseveres, misfortune comes."
        ]
    },
    {
        "num": 10, "binary": (1, 1, 0, 1, 1, 1), "name_ch": "Lü", "name_en": "Treading (Conduct)",
        "image": "Heaven above, the lake below: the image of Treading. Thus the superior man discriminates between high and low, and thereby fortifies the thinking of the people.",
        "judgement": "Treading upon the tail of the tiger. It does not bite the man. Success.",
        "lines": [
            "Nine at the beginning: Simple conduct. Progress without blame.",
            "Nine in the second place: Treading a smooth, level course. The perseverance of a dark man brings good fortune.",
            "Six in the third place: A one-eyed man is able to see, a lame man is able to tread. He treads on the tail of the tiger. The tiger bites the man. Misfortune. Thus does a warrior act on behalf of his great prince.",
            "Nine in the fourth place: He treads on the tail of the tiger. Caution and circumspection lead ultimately to good fortune.",
            "Nine in the fifth place: Resolute conduct. Perseverance with awareness of danger.",
            "Nine at the top: Look to your conduct and weigh the favorable signs. If all is complete, sublime good fortune comes."
        ]
    },
    {
        "num": 11, "binary": (0, 0, 0, 1, 1, 1), "name_ch": "Tai", "name_en": "Peace",
        "image": "Heaven and earth unite: the image of Peace. Thus the ruler divides and completes the course of heaven and earth; he furthers and regulates the gifts of heaven and earth, and so aids the people.",
        "judgement": "Peace. The small departs, the great approaches. Good fortune. Success.",
        "lines": [
            "Nine at the beginning: When ribbon grass is pulled up, the sod comes with it. Each according to his kind. Undertakings bring good fortune.",
            "Nine in the second place: Bearing with the uncultured in gentleness, fording the river with resolution, not neglecting what is distant, and not regarding one's companions. Thus one may manage to walk in the middle.",
            "Nine in the third place: No plain not followed by a slope. No going not followed by a return. He who remains persevering in danger is without blame. Do not complain about this truth; enjoy the good fortune you still possess.",
            "Six in the fourth place: He flutters down, not boasting of his wealth, together with his neighbor, guileless and sincere.",
            "Six in the fifth place: The sovereign I gives his daughter in marriage. This brings blessing and sublime good fortune.",
            "Six at the top: The wall falls back into the moat. Use no army now. Make your commands known in your own city. Perseverance brings humiliation."
        ]
    },
    {
        "num": 12, "binary": (1, 1, 1, 0, 0, 0), "name_ch": "Pi", "name_en": "Standstill (Stagnation)",
        "image": "Heaven and earth do not unite: the image of Standstill. Thus the superior man falls back upon his inner worth in order to escape the difficulties. He does not permit himself to be honored with revenue.",
        "judgement": "Standstill. Evil people do not further the perseverance of the superior man. The great departs; the small approaches.",
        "lines": [
            "Six at the beginning: When ribbon grass is pulled up, the sod comes with it. Each according to his kind. Perseverance brings good fortune and success.",
            "Six in the second place: They bear and endure; this means good fortune for inferior people. The standstill serves to help the great man to attain success.",
            "Six in the third place: They bear shame.",
            "Nine in the fourth place: He who acts at the command of the highest remains without blame. Those of like mind partake of the blessing.",
            "Nine in the fifth place: Standstill is giving way. Good fortune for the great man. 'What if it should fail, what if it should fail?' In this way he ties it to a cluster of mulberry shoots.",
            "Nine at the top: The standstill comes to an end. First standstill, then good fortune."
        ]
    },
    {
        "num": 13, "binary": (1, 1, 1, 1, 0, 1), "name_ch": "Tong Ren", "name_en": "Fellowship with Men",
        "image": "Heaven, and fire below: the image of Fellowship with Men. Thus the superior man organizes the clans and distinguishes things.",
        "judgement": "Fellowship with men in the open. Success. It furthers one to cross the great water. The perseverance of the superior man furthers.",
        "lines": [
            "Nine at the beginning: Fellowship with men at the gate. No blame.",
            "Six in the second place: Fellowship with men in the clan. Humiliation.",
            "Nine in the third place: He hides weapons in the thicket. He climbs the high hill in front of it. For three years he does not rise up.",
            "Nine in the fourth place: He climbs up on his wall; he cannot attack. Good fortune.",
            "Nine in the fifth place: Men bound in fellowship first weep and lament, but afterward they laugh. After great struggles they succeed in meeting.",
            "Nine at the top: Fellowship with men in the meadow. No remorse."
        ]
    },
    {
        "num": 14, "binary": (1, 0, 1, 1, 1, 1), "name_ch": "Da You", "name_en": "Possession in Great Measure",
        "image": "Fire in heaven above: the image of Possession in Great Measure. Thus the superior man curbs evil and furthers good, and thereby obeys the benevolent will of heaven.",
        "judgement": "Possession in Great Measure. Supreme success.",
        "lines": [
            "Nine at the beginning: No relationship with what is harmful. There is no blame in this. If one remains conscious of difficulty, one remains without blame.",
            "Nine in the second place: A big wagon for loading. One may undertake something. No blame.",
            "Nine in the third place: A prince offers it to the Son of Heaven. A small man cannot do this.",
            "Nine in the fourth place: He makes a difference between himself and his neighbor. No blame.",
            "Six in the fifth place: He whose truth is accessible, yet dignified, has good fortune.",
            "Nine at the top: He is blessed by heaven. Good fortune. Nothing that does not further."
        ]
    },
    {
        "num": 15, "binary": (0, 0, 1, 0, 0, 0), "name_ch": "Qian", "name_en": "Modesty",
        "image": "Within the earth, a mountain: the image of Modesty. Thus the superior man reduces that which is too much, and augments that which is too little. He weighs things and makes them equal.",
        "judgement": "Modesty creates success. The superior man carries things through.",
        "lines": [
            "Six at the beginning: A superior man modest in his modesty may cross the great water. Good fortune.",
            "Six in the second place: Modesty that comes to expression. Perseverance brings good fortune.",
            "Nine in the third place: A superior man of merit and modesty carries things through to the end. Good fortune.",
            "Six in the fourth place: Nothing that would not be furthered by modesty in movement.",
            "Six in the fifth place: Not boasting of one's riches in front of one's neighbor. It is favorable to attack with force. Nothing that would not be furthered.",
            "Six at the top: Modesty that comes to expression. It is favorable to set armies marching to chastise one's own city and country."
        ]
    },
    {
        "num": 16, "binary": (0, 0, 0, 1, 0, 0), "name_ch": "Yu", "name_en": "Enthusiasm",
        "image": "Thunder comes resounding out of the earth: the image of Enthusiasm. Thus the ancient kings made music in order to honor merit, and offered it with splendor to the Supreme Deity, inviting their ancestors to be present.",
        "judgement": "Enthusiasm. It furthers one to install helpers and to set armies marching.",
        "lines": [
            "Six at the beginning: Enthusiasm that expresses itself brings misfortune.",
            "Six in the second place: Firm as a rock. Not a whole day. Perseverance brings good fortune.",
            "Six in the third place: Enthusiasm that looks upward brings remorse. Hesitation brings remorse.",
            "Nine in the fourth place: The source of enthusiasm. He achieves great things. Do not doubt. You gather friends around you as a hair clasp gathers the hair.",
            "Six in the fifth place: Persistently ill, but still does not die.",
            "Six at the top: Deluded enthusiasm. But if one changes when the deed is done, there is no blame."
        ]
    },
    {
        "num": 17, "binary": (1, 0, 0, 1, 1, 0), "name_ch": "Sui", "name_en": "Following",
        "image": "Thunder in the middle of the lake: the image of Following. Thus the superior man at nightfall goes indoors for rest and recuperation.",
        "judgement": "Following has supreme success. Perseverance furthers. No blame.",
        "lines": [
            "Nine at the beginning: The standard is changing. Perseverance brings good fortune. To go out of the door in company produces deeds.",
            "Six in the second place: If one clings to the little boy, one loses the strong man.",
            "Six in the third place: If one clings to the strong man, one loses the little boy. Through following one finds what one seeks. It is favorable to remain persevering.",
            "Nine in the fourth place: Following creates success. Perseverance brings misfortune. To be sincere in the way brings clarity. How could this be a fault?",
            "Nine in the fifth place: Sincere in the good. Good fortune.",
            "Six at the top: He meets with firm allegiance and is still further bound. The king introduces him to the Western Mountain."
        ]
    },
    {
        "num": 18, "binary": (0, 1, 1, 0, 0, 1), "name_ch": "Gu", "name_en": "Work on What Has Been Spoiled",
        "image": "The wind blows low on the mountain: the image of Decay. Thus the superior man stirs up the people and strengthens their spirit.",
        "judgement": "Work on what has been spoiled has supreme success. It furthers one to cross the great water. Before the starting point, three days. After the starting point, three days.",
        "lines": [
            "Six at the beginning: Setting right what has been spoiled by the father. If there is a son, no blame rests upon the departed father. Danger. In the end good fortune.",
            "Nine in the second place: Setting right what has been spoiled by the mother. One must not be too persevering.",
            "Nine in the third place: Setting right what has been spoiled by the father. There will be a little remorse. No great blame.",
            "Six in the fourth place: Tolerating what has been spoiled by the father. In continuing one sees humiliation.",
            "Six in the fifth place: Setting right what has been spoiled by the father. One meets with praise.",
            "Nine at the top: He does not serve kings and princes, sets himself higher goals."
        ]
    },
    {
        "num": 19, "binary": (0, 0, 1, 1, 0, 0), "name_ch": "Lin", "name_en": "Approach",
        "image": "The earth above the lake: the image of Approach. Thus the superior man is inexhaustible in his will to teach, and without limits in his tolerance and protection of the people.",
        "judgement": "Approach has supreme success. Perseverance furthers. When the eighth month comes, there will be misfortune.",
        "lines": [
            "Nine at the beginning: Joint approach. Perseverance brings good fortune.",
            "Nine in the second place: Joint approach. Good fortune. Everything furthers.",
            "Six in the third place: Comfortable approach. Nothing that would further. If one becomes concerned about it, no blame.",
            "Six in the fourth place: Complete approach. No blame.",
            "Six in the fifth place: Wise approach. This is right for a great prince. Good fortune.",
            "Six at the top: Magnanimous approach. Good fortune. No blame."
        ]
    },
    {
        "num": 20, "binary": (0, 0, 1, 1, 1, 0), "name_ch": "Guan", "name_en": "Contemplation (View)",
        "image": "The wind blows over the earth: the image of Contemplation. Thus the kings of old visited the regions of the world, contemplated the people, and gave them instruction.",
        "judgement": "Contemplation. The ablution has been made, but not yet the offering. Full of trust they look up to him.",
        "lines": [
            "Six at the beginning: Boy-like contemplation. For an inferior man, no blame. For a superior man, humiliation.",
            "Six in the second place: Contemplation through the crack of the door. Furthers the perseverance of a woman.",
            "Six in the third place: Contemplation of my own life decides the advance or retreat.",
            "Six in the fourth place: Contemplation of the light of the kingdom. It furthers one to be the guest of a king.",
            "Nine in the fifth place: Contemplation of my life. The superior man is without blame.",
            "Nine at the top: Contemplation of his character. The superior man is without blame."
        ]
    },
    {
        "num": 21, "binary": (1, 0, 0, 1, 0, 1), "name_ch": "Shi He", "name_en": "Biting Through",
        "image": "Thunder and lightning: the image of Biting Through. Thus the kings of old laid down penalties with clarity and enforced the laws.",
        "judgement": "Biting Through has success. It is favorable to let justice be administered.",
        "lines": [
            "Nine at the beginning: His feet are in the stocks, so that his toes disappear. No blame.",
            "Six in the second place: Bites through soft flesh, so that his nose disappears. No blame.",
            "Six in the third place: Bites on old dried meat and strikes on something poisonous. Slight humiliation. No blame.",
            "Nine in the fourth place: Bites on dried gristly meat. Receives metal arrows. It furthers one to be mindful of difficulties and to be persevering. Good fortune.",
            "Six in the fifth place: Bites on dried lean meat. Receives yellow gold. Perseveringly aware of danger. No blame.",
            "Nine at the top: His neck is in the wooden cangue, so that his ears disappear. Misfortune."
        ]
    },
    {
        "num": 22, "binary": (1, 0, 1, 0, 0, 1), "name_ch": "Bi", "name_en": "Grace",
        "image": "Fire at the foot of the mountain: the image of Grace. Thus does the superior man proceed when clearing up current affairs. But he does not dare to decide controversial issues in this way.",
        "judgement": "Grace has success. In small matters it is favorable to undertake something.",
        "lines": [
            "Nine at the beginning: He lends grace to his toes, leaves the carriage, and walks.",
            "Six in the second place: Lends grace to the beard on his chin.",
            "Nine in the third place: Graceful and moist. Constant perseverance brings good fortune.",
            "Six in the fourth place: Grace or simplicity? A white horse comes as if on wings. He is not a robber, he will woo at the right time.",
            "Six in the fifth place: Grace in hills and gardens. The roll of silk is meager and small. Humiliation, but in the end good fortune.",
            "Nine at the top: Simple grace. No blame."
        ]
    },
    {
        "num": 23, "binary": (0, 0, 0, 0, 0, 1), "name_ch": "Bo", "name_en": "Splitting Apart",
        "image": "The mountain rests on the earth: the image of Splitting Apart. Thus those above can ensure their position only by giving generously to those below.",
        "judgement": "Splitting Apart. It does not further one to go anywhere.",
        "lines": [
            "Six at the beginning: The leg of the bed splits. Those who persevere are destroyed. Misfortune.",
            "Six in the second place: The bed splits at the edge. Those who persevere are destroyed. Misfortune.",
            "Six in the third place: He splits with them. No blame.",
            "Six in the fourth place: The bed splits up to the skin. Misfortune.",
            "Six in the fifth place: A shoal of fishes. Favor comes through the court ladies. Everything is favorable.",
            "Nine at the top: There is a large fruit still uneaten. The superior man receives a carriage. The house of the inferior man is split apart."
        ]
    },
    {
        "num": 24, "binary": (1, 0, 0, 0, 0, 0), "name_ch": "Fu", "name_en": "Return (The Turning Point)",
        "image": "Thunder within the earth: the image of the Turning Point. Thus the ancient kings closed the passes at the time of the solstice. Merchants and strangers did not go about, and the ruler did not travel through the provinces.",
        "judgement": "Return. Success. Going out and coming in without error. Friends come without blame. To and fro goes the way. On the seventh day comes return. It is favorable to have somewhere to go.",
        "lines": [
            "Nine at the beginning: Return from a short distance. No need for remorse. Great good fortune.",
            "Six in the second place: Quiet return. Good fortune.",
            "Six in the third place: Repeated return. Danger. No blame.",
            "Six in the fourth place: Walking in the midst of others, one returns alone.",
            "Six in the fifth place: Noble-hearted return. No remorse.",
            "Six at the top: Missing the return. Misfortune. Misfortune from within and without. If armies are set marching in this way, one will in the end suffer a great defeat, disastrous for the ruler of the country. For ten years it will not be possible to attack again."
        ]
    },
    {
        "num": 25, "binary": (1, 1, 1, 1, 0, 0), "name_ch": "Wu Wang", "name_en": "Innocence (The Unexpected)",
        "image": "Under heaven thunder rolls: all things attain the natural state of innocence. Thus the ancient kings, rich in virtue and in harmony with the time, fostered and nourished all beings.",
        "judgement": "Innocence. Supreme success. Perseverance furthers. If someone is not as he should be, he has misfortune, and it does not further him to undertake anything.",
        "lines": [
            "Nine at the beginning: Innocent behavior brings good fortune.",
            "Six in the second place: If one does not count on the harvest while plowing, nor on the use of the ground while clearing it, it is favorable to undertake something.",
            "Six in the third place: Undeserved misfortune. The cow that was tethered by someone is the wanderer's gain, the citizen's loss.",
            "Nine in the fourth place: He who can be persevering remains without blame.",
            "Nine in the fifth place: Use no medicine in an illness incurred through no fault of your own. It will pass of itself.",
            "Nine at the top: Innocent action brings misfortune. Nothing furthers."
        ]
    },
    {
        "num": 26, "binary": (1, 1, 1, 0, 0, 1), "name_ch": "Da Chu", "name_en": "The Taming Power of the Great",
        "image": "Heaven within the mountain: the image of the Taming Power of the Great. Thus the superior man acquaints himself with many sayings of antiquity and many deeds of the past, in order to strengthen his character thereby.",
        "judgement": "The Taming Power of the Great. Perseverance furthers. Not eating at home brings good fortune. It furthers one to cross the great water.",
        "lines": [
            "Nine at the beginning: Danger is at hand. It is favorable to desist.",
            "Nine in the second place: The spokes of the wagon wheel are taken out.",
            "Nine in the third place: A good horse that follows others. Awareness of danger, with perseverance, furthers. Practice chariot driving and armed defense daily. It is favorable to have somewhere to go.",
            "Six in the fourth place: The headboard of a young bull. Great good fortune.",
            "Six in the fifth place: The tusk of a gelded boar. Good fortune.",
            "Nine at the top: One attains the way of heaven. Success."
        ]
    },
    {
        "num": 27, "binary": (1, 0, 0, 0, 0, 1), "name_ch": "Yi", "name_en": "The Corners of the Mouth (Providing Nourishment)",
        "image": "At the foot of the mountain, thunder: the image of Providing Nourishment. Thus the superior man is careful of his words and temperate in eating and drinking.",
        "judgement": "The Corners of the Mouth. Perseverance brings good fortune. Pay heed to the providing of nourishment and to what a man seeks to fill his own mouth with.",
        "lines": [
            "Nine at the beginning: You let your magic tortoise go and look at me with the corners of your mouth drooping. Misfortune.",
            "Six in the second place: Turning to the summit for nourishment, deviating from the path to seek nourishment from the hill. Continuing to do this brings misfortune.",
            "Six in the third place: Turning away from nourishment. Perseverance brings misfortune. Do not act thus for ten years. Nothing furthers.",
            "Six in the fourth place: Turning to the summit for provision of nourishment. Good fortune. Spying about with the sharpness of a tiger with an insatiable appetite. No blame.",
            "Six in the fifth place: Turning away from the path. To remain persevering brings good fortune. One should not cross the great water.",
            "Nine at the top: The source of nourishment. Awareness of danger brings good fortune. It furthers one to cross the great water."
        ]
    },
    {
        "num": 28, "binary": (0, 1, 1, 1, 1, 0), "name_ch": "Da Guo", "name_en": "Preponderance of the Great",
        "image": "The lake rises above the trees: the image of Preponderance of the Great. Thus the superior man, when he stands alone, is unconcerned, and if he has to renounce the world, he is undaunted.",
        "judgement": "Preponderance of the Great. The ridgepole sags to the breaking point. It furthers one to have somewhere to go. Success.",
        "lines": [
            "Six at the beginning: To place the matter on white rushes. No blame.",
            "Nine in the second place: A dry poplar sprouts at the root. An older man takes a young wife. Everything furthers.",
            "Nine in the third place: The ridgepole sags to the breaking point. Misfortune.",
            "Nine in the fourth place: The ridgepole is braced. Good fortune. If there are ulterior motives, it is humiliating.",
            "Nine in the fifth place: A withered poplar puts forth flowers. An older woman takes a husband. No blame. No praise.",
            "Six at the top: One must go through the water. It goes over one's head. Misfortune. No blame."
        ]
    },
    {
        "num": 29, "binary": (0, 1, 0, 0, 1, 0), "name_ch": "Kan", "name_en": "The Abysmal (Water)",
        "image": "Water flows on uninterruptedly: the image of the Abysmal repeated. Thus the superior man walks in lasting virtue and carries on the business of teaching.",
        "judgement": "The Abysmal repeated. If you are sincere, you have success in your heart, and whatever you do succeeds.",
        "lines": [
            "Six at the beginning: Repetition of the Abysmal. In the abyss one falls into a pit. Misfortune.",
            "Nine in the second place: The abyss is dangerous. One should strive to attain small things only.",
            "Six in the third place: Forward and backward, abyss on abyss. In danger like this, pause for a while, otherwise you will fall into a pit in the abyss. Do not act.",
            "Six in the fourth place: A jug of wine, a bowl of rice with it; earthen vessels, simply handed in through the window. There is certainly no blame in this.",
            "Nine in the fifth place: The abyss is not filled to overflowing, it is filled only to the rim. No blame.",
            "Six at the top: Bound with cords and ropes, shut in between thorn-hedged prison walls. For three years one does not find the way. Misfortune."
        ]
    },
    {
        "num": 30, "binary": (1, 0, 1, 1, 0, 1), "name_ch": "Li", "name_en": "The Clinging, Fire",
        "image": "That which is bright rises twice: the image of Fire. Thus the great man, by perpetuating this brightness, illuminates the four quarters of the world.",
        "judgement": "The Clinging. Perseverance furthers. It brings success. Care of the cow brings good fortune.",
        "lines": [
            "Nine at the beginning: The footprints are confused. Be serious. Then there is no blame.",
            "Six in the second place: Yellow light. Supreme good fortune.",
            "Nine in the third place: In the light of the setting sun, men either beat the pot and sing or loudly bewail the approach of old age. Misfortune.",
            "Nine in the fourth place: Its coming is sudden; it flames up, dies down, is thrown away.",
            "Six in the fifth place: Tears in floods, sighing and lamenting. Good fortune.",
            "Nine at the top: The king uses him to march forth and chastise. Then it is best to kill the leaders and take captive the followers. No blame."
        ]
    },
    {
        "num": 31, "binary": (0, 0, 1, 1, 1, 0), "name_ch": "Xian", "name_en": "Influence (Wooing)",
        "image": "A lake on the mountain: the image of Influence. Thus the superior man encourages people to approach him by his readiness to receive them.",
        "judgement": "Influence. Success. Perseverance furthers. To take a maiden to wife brings good fortune.",
        "lines": [
            "Six at the beginning: The influence shows itself in the big toe.",
            "Six in the second place: The influence shows itself in the calves of the legs. Misfortune. Tarrying brings good fortune.",
            "Nine in the third place: The influence shows itself in the thighs. Holds to that which follows it. To continue is humiliating.",
            "Nine in the fourth place: Perseverance brings good fortune. Remorse disappears. If a man is agitated in his mind, and his thoughts go hither and thither, only those friends on whom he fixes his conscious thoughts will follow.",
            "Nine in the fifth place: The influence shows itself in the back of the neck. No remorse.",
            "Six at the top: The influence shows itself in the jaws, cheeks, and tongue."
        ]
    },
    {
        "num": 32, "binary": (0, 1, 1, 1, 0, 0), "name_ch": "Heng", "name_en": "Duration",
        "image": "Thunder and wind: the image of Duration. Thus the superior man stands firm and does not change his direction.",
        "judgement": "Duration. Success. No blame. Perseverance furthers. It is favorable to have somewhere to go.",
        "lines": [
            "Six at the beginning: Seeking duration too hastily brings misfortune persistently. Nothing that would further.",
            "Nine in the second place: Remorse disappears.",
            "Nine in the third place: He who does not give duration to his character meets with disgrace. Persistent humiliation.",
            "Nine in the fourth place: No game in the field.",
            "Six in the fifth place: Giving duration to one's character through perseverance. This is good fortune for a woman, misfortune for a man.",
            "Six at the top: Duration in restlessness. Misfortune."
        ]
    },
    {
        "num": 33, "binary": (1, 1, 1, 1, 0, 0), "name_ch": "Dun", "name_en": "Retreat",
        "image": "Mountain under heaven: the image of Retreat. Thus the superior man keeps the inferior man at a distance, not in anger but with reserve.",
        "judgement": "Retreat. Success. In what is small, perseverance furthers.",
        "lines": [
            "Six at the beginning: At the tail in retreat. This is dangerous. One must not wish to undertake anything.",
            "Six in the second place: He holds him fast with yellow oxhide. No one can tear him loose.",
            "Nine in the third place: A halted retreat is nerve-wracking and dangerous. To retain people as men- and maidservants brings good fortune.",
            "Nine in the fourth place: Voluntary retreat brings good fortune to the superior man and downfall to the inferior man.",
            "Nine in the fifth place: Friendly retreat. Perseverance brings good fortune.",
            "Nine at the top: Cheerful retreat. Everything serves to further."
        ]
    },
    {
        "num": 34, "binary": (0, 0, 0, 1, 1, 1), "name_ch": "Da Zhuang", "name_en": "The Power of the Great",
        "image": "Thunder in heaven above: the image of the Power of the Great. Thus the superior man does not tread upon paths that do not accord with established order.",
        "judgement": "The Power of the Great. Perseverance furthers.",
        "lines": [
            "Nine at the beginning: Power in the toes. Continuing brings misfortune. This is certainly true.",
            "Nine in the second place: Perseverance brings good fortune.",
            "Nine in the third place: The inferior man uses power. The superior man does not use it. Perseverance is dangerous. A ram butts against a hedge and gets its horns entangled.",
            "Nine in the fourth place: Perseverance brings good fortune. Remorse disappears. The hedge opens; there is no entanglement. Power depends upon the axle of a big cart.",
            "Six in the fifth place: Loses the ram with ease. No remorse.",
            "Six at the top: A ram butts against a hedge. It cannot go backward, it cannot go forward. Nothing serves to further. If one notes the difficulty, this brings good fortune."
        ]
    },
    {
        "num": 35, "binary": (1, 0, 1, 0, 0, 0), "name_ch": "Jin", "name_en": "Progress",
        "image": "The sun rises over the earth: the image of Progress. Thus the superior man himself brightens his bright virtue.",
        "judgement": "Progress. The powerful prince is honored with horses in large numbers. In a single day he is granted audience three times.",
        "lines": [
            "Six at the beginning: Progressing, but turned back. Perseverance brings good fortune. If one meets with no confidence, one should remain calm. No blame.",
            "Six in the second place: Progressing, but in sorrow. Perseverance brings good fortune. One receives this great happiness from one's ancestress.",
            "Six in the third place: All are in accord. Remorse disappears.",
            "Nine in the fourth place: Progressing like a hamster. Perseverance brings danger.",
            "Six in the fifth place: Remorse disappears. Take not to heart gain and loss. Undertakings bring good fortune. Everything serves to further.",
            "Nine at the top: Making progress with lowered horns. Used only for chastising one's own city. To be conscious of danger brings good fortune. No blame. Perseverance brings humiliation."
        ]
    },
    {
        "num": 36, "binary": (0, 0, 0, 1, 0, 1), "name_ch": "Ming Yi", "name_en": "Darkening of the Light",
        "image": "The light has sunk into the earth: the image of Darkening of the Light. Thus does the superior man live with the great mass: he veils his light, yet still shines.",
        "judgement": "Darkening of the Light. In adversity it furthers one to be persevering.",
        "lines": [
            "Nine at the beginning: Darkening of the light during flight. He lowers his wings. The superior man is on a journey and for three days does not eat. He has somewhere to go. The host has occasion to gossip about him.",
            "Six in the second place: Darkening of the light, injured in the left thigh. He gives aid with the strength of a horse. Good fortune.",
            "Nine in the third place: Darkening of the light during the hunt in the south. Their great leader is captured. One must not expect perseverance too soon.",
            "Six in the fourth place: He penetrates into the left side of the belly. One gets at the heart and mind of the darkening of the light, and leaves gate and courtyard.",
            "Six in the fifth place: Darkening of the light as with Prince Chi. Perseverance furthers.",
            "Six at the top: Not light but darkness. First he climbed up to heaven, then he plunged into the depths of the earth."
        ]
    },
    {
        "num": 37, "binary": (1, 0, 1, 0, 1, 1), "name_ch": "Jia Ren", "name_en": "The Family (The Clan)",
        "image": "Wind comes forth from fire: the image of the Family. Thus the superior man has substance in his words and duration in his way of life.",
        "judgement": "The Family. The perseverance of the woman furthers.",
        "lines": [
            "Nine at the beginning: Firm seclusion within the family. Remorse disappears.",
            "Six in the second place: She should not follow her whims. She must attend within to the food. Perseverance brings good fortune.",
            "Nine in the third place: When tempers flare up in the family, too great severity brings remorse. Good fortune nevertheless. When woman and child dally and laugh, it leads in the end to humiliation.",
            "Six in the fourth place: She is the treasure of the house. Great good fortune.",
            "Nine in the fifth place: As a king he approaches his family. Fear not. Good fortune.",
            "Nine at the top: His work commands respect. In the end good fortune comes."
        ]
    },
    {
        "num": 38, "binary": (1, 1, 0, 1, 0, 1), "name_ch": "Kui", "name_en": "Opposition",
        "image": "Above, fire; below, the lake: the image of Opposition. Thus amid all fellowship the superior man retains his individuality.",
        "judgement": "Opposition. In small matters, good fortune.",
        "lines": [
            "Nine at the beginning: Remorse disappears. If you lose your horse, do not run after it; it will come back of its own accord. When you see evil people, avoid them. No blame.",
            "Nine in the second place: One meets one's lord in a narrow street. No blame.",
            "Six in the third place: One sees the wagon dragged back, the oxen halted, a man's hair and nose cut off. Not a good beginning, but a good end.",
            "Nine in the fourth place: Isolated through opposition, one meets a like-minded man with whom one can associate in good faith. Despite the danger, no blame.",
            "Six in the fifth place: Remorse disappears. The companion bites his way through the wrappings. If one goes to him, how could it be a mistake?",
            "Nine at the top: Isolated through opposition, one sees one's companion as a pig covered with dirt, as a wagon full of devils. First one draws a bow against him, then one lays the bow aside. He is not a robber; he will woo at the right time. As one goes, rain falls; then good fortune comes."
        ]
    },
    {
        "num": 39, "binary": (0, 0, 1, 0, 1, 0), "name_ch": "Jian", "name_en": "Obstruction",
        "image": "Water on the mountain: the image of Obstruction. Thus the superior man turns his attention to himself and molds his character.",
        "judgement": "Obstruction. The southwest furthers. The northeast does not further. It furthers one to see the great man. Perseverance brings good fortune.",
        "lines": [
            "Six at the beginning: Going leads to obstructions, coming meets with praise.",
            "Six in the second place: The king's servant is beset by obstruction upon obstruction, but it is not his own fault.",
            "Nine in the third place: Going leads to obstructions; hence he comes back.",
            "Six in the fourth place: Going leads to obstructions, coming leads to union.",
            "Nine in the fifth place: In the midst of the greatest obstructions, friends come.",
            "Six at the top: Going leads to obstructions, coming brings great good fortune. It furthers one to see the great man."
        ]
    },
    {
        "num": 40, "binary": (0, 1, 0, 1, 0, 0), "name_ch": "Jie", "name_en": "Deliverance",
        "image": "Thunder and rain set in: the image of Deliverance. Thus the superior man pardons mistakes and forgives guilt.",
        "judgement": "Deliverance. The southwest furthers. If there is no longer anything where one has to go, return brings good fortune. If there is still something where one has to go, haste brings good fortune.",
        "lines": [
            "Six at the beginning: Without blame.",
            "Nine in the second place: One kills three foxes in the field and receives a yellow arrow. Perseverance brings good fortune.",
            "Six in the third place: If a man carries a burden on his back and nevertheless rides in a carriage, he thereby encourages robbers to draw near. Perseverance brings humiliation.",
            "Nine in the fourth place: Deliver yourself from your big toe. Then the companion comes, and him you can trust.",
            "Six in the fifth place: If only the superior man can deliver himself, it brings good fortune. He proves his sincerity to the inferior man.",
            "Six at the top: The prince shoots at a hawk on a high wall. He kills it. Everything serves to further."
        ]
    },
    {
        "num": 41, "binary": (1, 1, 0, 0, 0, 1), "name_ch": "Sun", "name_en": "Decrease",
        "image": "At the foot of the mountain, the lake: the image of Decrease. Thus the superior man controls his anger and restrains his instincts.",
        "judgement": "Decrease combined with sincerity brings sublime good fortune without blame. One may be persevering in this. It furthers one to undertake something. How is this to be carried out? Two small bowls may be used for the sacrifice.",
        "lines": [
            "Nine at the beginning: Going quickly when one's tasks are finished is without blame. But one must reflect on how much one may decrease others.",
            "Nine in the second place: Perseverance furthers. To undertake something brings misfortune. Without decreasing oneself, one is able to bring increase to others.",
            "Six in the third place: When three people journey together, their number decreases by one. When one man journeys alone, he finds a companion.",
            "Six in the fourth place: If a man decreases his faults, it makes the other hasten to rejoice. No blame.",
            "Six in the fifth place: Someone is sure to increase him. Ten pairs of tortoises cannot oppose it. Sublime good fortune.",
            "Nine at the top: If one increases without decreasing others, there is no blame. Perseverance brings good fortune. It furthers one to undertake something. One obtains servants, but no longer has a separate home."
        ]
    },
    {
        "num": 42, "binary": (1, 0, 0, 0, 1, 1), "name_ch": "Yi", "name_en": "Increase",
        "image": "Wind and thunder: the image of Increase. Thus the superior man: if he sees good, he imitates it; if he has faults, he rids himself of them.",
        "judgement": "Increase. It furthers one to undertake something. It furthers one to cross the great water.",
        "lines": [
            "Nine at the beginning: It is favorable to perform great deeds. Sublime good fortune. No blame.",
            "Six in the second place: Someone is sure to increase him. Ten pairs of tortoises cannot oppose it. Constant perseverance brings good fortune. The king presents him before God. Good fortune.",
            "Six in the third place: One is enriched through unfortunate events. No blame, if you are sincere and walk in the middle and report with a seal to the prince.",
            "Six in the fourth place: If you walk in the middle and report to the prince, he will follow. It is favorable to be used in moving the capital.",
            "Nine in the fifth place: If in truth you have a kind heart, ask not. Sublime good fortune. Truly, kindness will be recognized as your virtue.",
            "Nine at the top: He brings increase to no one. Indeed, someone is sure to strike him. He does not keep his heart constantly steady. Misfortune."
        ]
    },
    {
        "num": 43, "binary": (0, 1, 1, 1, 1, 1), "name_ch": "Guai", "name_en": "Breakthrough (Resoluteness)",
        "image": "The lake has risen up to heaven: the image of Breakthrough. Thus the superior man dispenses riches downward and refrains from resting on his virtue.",
        "judgement": "Breakthrough. One must resolutely make the matter known at the court of the king. It must be announced in truth. Danger. It is necessary to notify one's own city. It does not further to resort to arms. It furthers one to undertake something.",
        "lines": [
            "Nine at the beginning: Mighty in the forward-striding toes. When one goes and is not equal to the task, one makes a mistake.",
            "Nine in the second place: A cry of alarm. Arms at evening and at night. Fear nothing.",
            "Nine in the third place: To be powerful in the cheekbones brings misfortune. The superior man is firmly resolved. He walks alone and is caught in the rain. He is bespattered, and people murmur against him. No blame.",
            "Nine in the fourth place: There is no skin on his thighs, and walking is difficult. If one lets oneself be led like a sheep, remorse disappears. But if these words are heard, they will not be believed.",
            "Nine in the fifth place: In dealing with weeds, firm resolution is necessary. Walking in the middle remains free of blame.",
            "Six at the top: No cry. In the end misfortune comes."
        ]
    },
    {
        "num": 44, "binary": (1, 1, 1, 1, 1, 0), "name_ch": "Gou", "name_en": "Coming to Meet",
        "image": "Under heaven, wind: the image of Coming to Meet. Thus the prince issues his commands and proclaims them to the four quarters of heaven.",
        "judgement": "Coming to Meet. The maiden is powerful. One should not marry such a maiden.",
        "lines": [
            "Six at the beginning: It must be checked with a brake of bronze. Perseverance brings good fortune. If one lets it take its course, one experiences misfortune. Even a lean pig has it in him to rage around.",
            "Nine in the second place: There is a fish in the tank. No blame. Does not further guests.",
            "Nine in the third place: There is no skin on his thighs, and walking is difficult. If one is mindful of the danger, no great mistake is made.",
            "Nine in the fourth place: No fish in the tank. This leads to misfortune.",
            "Nine in the fifth place: A melon covered with willow leaves. Hidden lines. Then it drops down to one from heaven.",
            "Nine at the top: He comes to meet with his horns. Humiliation. No blame."
        ]
    },
    {
        "num": 45, "binary": (0, 0, 0, 1, 1, 0), "name_ch": "Cui", "name_en": "Gathering Together (Massing)",
        "image": "Over the earth, the lake: the image of Gathering Together. Thus the superior man renews his weapons in order to meet the unforeseen.",
        "judgement": "Gathering Together. Success. The king approaches his temple. It furthers one to see the great man. This brings success. Perseverance furthers. To make great offerings creates good fortune. It furthers one to undertake something.",
        "lines": [
            "Six at the beginning: If you are sincere, but not to the end, there will sometimes be confusion, sometimes gathering. If you cry out, then after a grasp of the hand you can laugh again. Regret not. To go is without blame.",
            "Six in the second place: Letting oneself be drawn brings good fortune and remains blameless. If one is sincere, it is favorable to make even a small offering.",
            "Six in the third place: Gathering together amid sighs. Nothing that would further. To go is without blame. Slight humiliation.",
            "Nine in the fourth place: Great good fortune. No blame.",
            "Nine in the fifth place: If in gathering together one has position, this brings no blame. If there are some who are not yet sincere in the work, sublime and enduring perseverance is needed. Then remorse disappears.",
            "Six at the top: Lamenting and sighing, floods of tears. No blame."
        ]
    },
    {
        "num": 46, "binary": (0, 1, 1, 0, 0, 0), "name_ch": "Sheng", "name_en": "Pushing Upward",
        "image": "Within the earth, wood grows: the image of Pushing Upward. Thus the superior man of devoted character heaps up small things in order to achieve something high and great.",
        "judgement": "Pushing Upward has supreme success. One must see the great man. Fear not. Departure toward the south brings good fortune.",
        "lines": [
            "Six at the beginning: Pushing upward that meets with confidence. Great good fortune.",
            "Nine in the second place: If one is sincere, it is favorable to make even a small offering. No blame.",
            "Nine in the third place: One pushes upward into an empty city.",
            "Six in the fourth place: The king offers him sacrifices on Mount Ch'i. Good fortune. No blame.",
            "Six in the fifth place: Perseverance brings good fortune. One pushes upward by steps.",
            "Six at the top: Pushing upward in darkness. It is favorable to be unremittingly persevering."
        ]
    },
    {
        "num": 47, "binary": (0, 1, 0, 1, 1, 0), "name_ch": "Kun", "name_en": "Oppression (Exhaustion)",
        "image": "No water in the lake: the image of Exhaustion. Thus the superior man stakes his life on following his will.",
        "judgement": "Oppression. Success. Perseverance. The great man brings about good fortune. No blame. When one has something to say, it is not believed.",
        "lines": [
            "Six at the beginning: One sits oppressed under a bare tree and strays into a gloomy valley. For three years one sees nothing.",
            "Nine in the second place: One is oppressed while at meat and drink. The man with the scarlet knee bands is just coming. It is favorable to make offerings. To set forth brings misfortune. No blame.",
            "Six in the third place: A man is oppressed by stone, and leans on thorns and thistles. He enters his house and does not see his wife. Misfortune.",
            "Nine in the fourth place: He comes very quietly, oppressed in a golden carriage. Humiliation, but the end is not his fault.",
            "Nine in the fifth place: His nose and feet are cut off. Oppression at the hands of the man with the purple knee bands. It is favorable to make libations with gladness.",
            "Six at the top: He is oppressed by creeping vines. He moves uncertainly and says, 'Movement brings remorse.' If one repents of this and sets forth, good fortune comes."
        ]
    },
    {
        "num": 48, "binary": (0, 1, 1, 0, 1, 0), "name_ch": "Jing", "name_en": "The Well",
        "image": "Water over wood: the image of the Well. Thus the superior man encourages the people at their work and exhorts them to help one another.",
        "judgement": "The Well. The town may be changed, but the well cannot be changed. It neither decreases nor increases. They come and go and draw from the well. If one gets down almost to the water and the rope does not go all the way, or the jug breaks, it brings misfortune.",
        "lines": [
            "Six at the beginning: One does not drink the mud of the well. No animals come to an old well.",
            "Nine in the second place: At the well hole one shoots fishes. The jug is broken and leaks.",
            "Nine in the third place: The well is cleaned, but no one drinks from it. This is the sorrow of my heart, for this one might draw from it. If the king were clear-minded, good fortune might be enjoyed in common.",
            "Six in the fourth place: The well is being lined. No blame.",
            "Nine in the fifth place: In the well there is a clear, cold spring from which one can drink.",
            "Six at the top: One draws from the well without hindrance. It is dependable. Supreme good fortune."
        ]
    },
    {
        "num": 49, "binary": (1, 0, 1, 1, 1, 0), "name_ch": "Ge", "name_en": "Revolution (Molting)",
        "image": "Fire in the lake: the image of Revolution. Thus the superior man sets the calendar in order and makes the seasons clear.",
        "judgement": "Revolution. On your own day you are believed. Supreme success, furthering through perseverance. Remorse disappears.",
        "lines": [
            "Nine at the beginning: Wrapped in the hide of a yellow cow.",
            "Six in the second place: When one's own day comes, one may create revolution. Starting brings good fortune. No blame.",
            "Nine in the third place: Starting brings misfortune. Perseverance brings danger. When the talk of revolution has gone the rounds three times, one may commit himself, and people will believe him.",
            "Nine in the fourth place: Remorse disappears. Men believe him. Changing the form of government brings good fortune.",
            "Nine in the fifth place: The great man changes like a tiger. Even before he questions the oracle, he is believed.",
            "Six at the top: The superior man changes like a panther. The inferior man molts in the face. Starting brings misfortune. To remain persevering brings good fortune."
        ]
    },
    {
        "num": 50, "binary": (0, 1, 1, 1, 0, 1), "name_ch": "Ding", "name_en": "The Cauldron",
        "image": "Fire over wood: the image of the Cauldron. Thus the superior man consolidates his fate by making his position correct.",
        "judgement": "The Cauldron. Supreme good fortune. Success.",
        "lines": [
            "Six at the beginning: A cauldron with legs upturned. Furthers removal of stagnating stuff. One takes a concubine for the sake of her son. No blame.",
            "Nine in the second place: There is food in the cauldron. My comrades are envious, but they cannot harm me. Good fortune.",
            "Nine in the third place: The handle of the cauldron is altered. One is impeded in his way of life. The fat of the pheasant is not eaten. Once rain falls, remorse is spent. Good fortune comes in the end.",
            "Nine in the fourth place: The legs of the cauldron are broken. The prince's meal is spilled and his person is soiled. Misfortune.",
            "Six in the fifth place: The cauldron has yellow handles, golden carrying rings. Perseverance furthers.",
            "Nine at the top: The cauldron has rings of jade. Great good fortune. Nothing that would not act to further."
        ]
    },
    {
        "num": 51, "binary": (1, 0, 0, 1, 0, 0), "name_ch": "Zhen", "name_en": "The Arousing (Shock, Thunder)",
        "image": "Thunder repeated: the image of Shock. Thus in fear and trembling the superior man sets his life in order and examines himself.",
        "judgement": "Shock brings success. Shock comes—oh, oh! Laughing words—ha, ha! The shock terrifies for a hundred miles, and he does not let fall the sacrificial spoon and chalice.",
        "lines": [
            "Nine at the beginning: Shock comes—oh, oh! Then follow laughing words—ha, ha! Good fortune.",
            "Six in the second place: Shock comes bringing danger. A hundred thousand times you lose your treasures and must climb the nine hills. Do not go in pursuit of them. After seven days you will get them back.",
            "Six in the third place: Shock comes and makes one distraught. If shock spurs to action, one remains free of misfortune.",
            "Nine in the fourth place: Shock is mired.",
            "Six in the fifth place: Shock goes hither and thither. Danger. However, nothing at all is lost. There are things to be done.",
            "Six at the top: Shock brings ruin and terrified gazing around. Going ahead brings misfortune. If it has not yet touched one's own body but has reached one's neighbor, there is no blame. One's comrades have something to talk about."
        ]
    },
    {
        "num": 52, "binary": (0, 0, 1, 0, 0, 1), "name_ch": "Gen", "name_en": "Keeping Still, Mountain",
        "image": "Mountains standing close together: the image of Keeping Still. Thus the superior man does not permit his thoughts to go beyond his situation.",
        "judgement": "Keeping Still. Keeping his back still so that he no longer feels his body. He goes into his courtyard and does not see his people. No blame.",
        "lines": [
            "Six at the beginning: Keeping his toes still. No blame. Continued perseverance furthers.",
            "Six in the second place: Keeping his calves still. He cannot rescue him whom he follows. His heart is not glad.",
            "Nine in the third place: Keeping his hips still. Making his sacrum rigid. Dangerous. The heart suffocates.",
            "Six in the fourth place: Keeping his trunk still. No blame.",
            "Six in the fifth place: Keeping his jaws still. The words have order. Remorse disappears.",
            "Nine at the top: Noble-hearted keeping still. Good fortune."
        ]
    },
    {
        "num": 53, "binary": (0, 0, 1, 0, 1, 1), "name_ch": "Jian", "name_en": "Development (Gradual Progress)",
        "image": "On the mountain, a tree: the image of Development. Thus the superior man abides in dignified virtue in order to improve the mores.",
        "judgement": "Development. The maiden is given in marriage. Good fortune. Perseverance furthers.",
        "lines": [
            "Six at the beginning: The wild goose gradually draws near the shore. The young son is in danger. There is talk. No blame.",
            "Six in the second place: The wild goose gradually draws near the cliff. Eating and drinking in peace and concord. Good fortune.",
            "Nine in the third place: The wild goose gradually draws near the plateau. The husband goes forth and does not return. The wife is pregnant but does not give birth. Misfortune. It is favorable to fight off robbers.",
            "Six in the fourth place: The wild goose gradually draws near the tree. Perhaps it will find a flat branch. No blame.",
            "Nine in the fifth place: The wild goose gradually draws near the summit. For three years the wife has no child. In the end nothing can hinder her. Good fortune.",
            "Nine at the top: The wild goose gradually draws near the cloud heights. Its feathers can be used for the sacred dance. Good fortune."
        ]
    },
    {
        "num": 54, "binary": (0, 1, 1, 1, 0, 0), "name_ch": "Gui Mei", "name_en": "The Marrying Maiden",
        "image": "Thunder over the lake: the image of the Marrying Maiden. Thus the superior man understands the transitory in the light of the eternity of the end.",
        "judgement": "The Marrying Maiden. Undertakings bring misfortune. Nothing that would further.",
        "lines": [
            "Nine at the beginning: The marrying maiden as a concubine. A lame man who is able to tread. Undertakings bring good fortune.",
            "Nine in the second place: A one-eyed man who is able to see. It furthers the perseverance of a solitary man.",
            "Six in the third place: The marrying maiden as a slave. She marries as a concubine.",
            "Nine in the fourth place: The marrying maiden draws out the time. A late marriage comes in due course.",
            "Six in the fifth place: The sovereign I gives his daughter in marriage. The embroidered sleeves of the princess were not as splendid as those of the serving-maid. The moon that is nearly full brings good fortune.",
            "Six at the top: The woman holds the basket, but there are no fruits in it. The man stabs the sheep, but no blood flows. Nothing that would further."
        ]
    },
    {
        "num": 55, "binary": (1, 0, 1, 1, 0, 0), "name_ch": "Feng", "name_en": "Abundance (Fullness)",
        "image": "Both thunder and lightning come: the image of Abundance. Thus the superior man decides lawsuits and carries out punishments.",
        "judgement": "Abundance has success. The king attains abundance. Be not sad. Be like the sun at midday.",
        "lines": [
            "Nine at the beginning: When a man meets his destined ruler, they can be together ten days, and it is not a mistake. To go brings honor.",
            "Six in the second place: The screen is of such abundance that the polestars can be seen at noon. Through going one meets with mistrust and hate. If one rouses him through truth, good fortune comes.",
            "Nine in the third place: The underbrush is of such abundance that the small stars can be seen at noon. He breaks his right arm. No blame.",
            "Nine in the fourth place: The screen is of such abundance that the polestars can be seen at noon. He meets his ruler, who is of like kind. Good fortune.",
            "Six in the fifth place: He brings grace, which means blessing and praise. Good fortune.",
            "Six at the top: His house is in a state of abundance. He screens off his family. He peers through the gate and no longer perceives anyone. For three years he sees nothing. Misfortune."
        ]
    },
    {
        "num": 56, "binary": (1, 0, 0, 1, 0, 1), "name_ch": "Lü", "name_en": "The Wanderer",
        "image": "Fire on the mountain: the image of the Wanderer. Thus the superior man is clear-minded and cautious in imposing penalties, and protracts no lawsuits.",
        "judgement": "The Wanderer. Success through smallness. Perseverance brings good fortune to the wanderer.",
        "lines": [
            "Six at the beginning: If the wanderer busies himself with trivial things, he draws down misfortune.",
            "Six in the second place: The wanderer comes to an inn. He has his property with him. He wins the steadfastness of a young servant.",
            "Nine in the third place: The wanderer's inn burns down. He loses the steadfastness of his young servant. Danger.",
            "Nine in the fourth place: The wanderer rests in a shelter. He obtains his property and an ax. My heart is not glad.",
            "Six in the fifth place: He shoots a pheasant. It drops with the first arrow. In the end this brings him praise and office.",
            "Nine at the top: The bird's nest burns up. The wanderer laughs at first, then must lament and weep. He loses his cow too easily. Misfortune."
        ]
    },
    {
        "num": 57, "binary": (0, 1, 1, 0, 1, 1), "name_ch": "Xun", "name_en": "The Gentle (The Penetrating, Wind)",
        "image": "Winds following one upon the other: the image of the Gentle. Thus the superior man spreads his commands and carries out his undertakings.",
        "judgement": "The Gentle. Success through what is small. It is favorable to have somewhere to go. It is favorable to see the great man.",
        "lines": [
            "Six at the beginning: In advancing and in retreating, the perseverance of a warrior furthers.",
            "Nine in the second place: Penetration under the bed. Priests and magicians are used in great number. Good fortune. No blame.",
            "Nine in the third place: Repeated penetration. Humiliation.",
            "Six in the fourth place: Remorse vanishes. In the hunt three kinds of game are caught.",
            "Nine in the fifth place: Perseverance brings good fortune. Remorse vanishes. Nothing that does not further. No beginning, but an end. Before the change, three days. After the change, three days. Good fortune.",
            "Nine at the top: Penetration under the bed. He loses his property and his ax. Perseverance brings misfortune."
        ]
    },
    {
        "num": 58, "binary": (0, 1, 0, 1, 1, 0), "name_ch": "Dui", "name_en": "The Joyous, Lake",
        "image": "Lakes resting one on the other: the image of the Joyous. Thus the superior man joins with his friends for discussion and practice.",
        "judgement": "The Joyous. Success. Perseverance is favorable.",
        "lines": [
            "Nine at the beginning: Contented joyousness. Good fortune.",
            "Nine in the second place: Sincere joyousness. Good fortune. Remorse disappears.",
            "Six in the third place: Coming joyousness. Misfortune.",
            "Nine in the fourth place: Joyousness that is weighed is not at peace. After ridding himself of his mistakes, a man has joy.",
            "Nine in the fifth place: Sincerity toward disintegrating influences is dangerous.",
            "Six at the top: Seductive joyousness."
        ]
    },
    {
        "num": 59, "binary": (0, 1, 0, 0, 1, 1), "name_ch": "Huan", "name_en": "Dispersion (Dissolution)",
        "image": "The wind drives over the water: the image of Dispersion. Thus the kings of old sacrificed to the Lord and built temples.",
        "judgement": "Dispersion. Success. The king approaches his temple. It furthers one to cross the great water. Perseverance furthers.",
        "lines": [
            "Six at the beginning: He brings help with the strength of a horse. Good fortune.",
            "Nine in the second place: At the dissolution he hurries to his support. Remorse disappears.",
            "Six in the third place: He dissolves his self. No remorse.",
            "Six in the fourth place: He dissolves his bond with his group. Supreme good fortune. Dispersion leads in turn to accumulation. This is something that ordinary men do not think of.",
            "Nine in the fifth place: His loud cries are like sweat. Dissolution. A king abides without blame.",
            "Nine at the top: He dissolves his blood. He departs, remains at a distance, goes away. This is without blame."
        ]
    },
    {
        "num": 60, "binary": (1, 1, 0, 0, 1, 0), "name_ch": "Jie", "name_en": "Limitation",
        "image": "Water over lake: the image of Limitation. Thus the superior man creates number and measure, and examines the nature of virtue and correct conduct.",
        "judgement": "Limitation. Success. Galling limitation must not be persevered in.",
        "lines": [
            "Nine at the beginning: Not going out of the door and the courtyard is without blame.",
            "Nine in the second place: Not going out of the gate and the courtyard brings misfortune.",
            "Six in the third place: He who knows no limitation will have cause to lament. No blame.",
            "Six in the fourth place: Contented limitation. Success.",
            "Nine in the fifth place: Sweet limitation brings good fortune. Going brings esteem.",
            "Six at the top: Galling limitation. Perseverance brings misfortune. Remorse disappears."
        ]
    },
    {
        "num": 61, "binary": (1, 1, 0, 0, 1, 1), "name_ch": "Zhong Fu", "name_en": "Inner Truth",
        "image": "Wind over lake: the image of Inner Truth. Thus the superior man discusses criminal cases in order to delay executions.",
        "judgement": "Inner Truth. Pigs and fishes. Good fortune. It furthers one to cross the great water. Perseverance furthers.",
        "lines": [
            "Nine at the beginning: Being prepared brings good fortune. If there are secret designs, it is disquieting.",
            "Nine in the second place: A crane calling in the shade. Its young answers it. I have a good goblet. I will share it with you.",
            "Six in the third place: He finds a comrade. Now he beats the drum, now he stops. Now he weeps, now he sings.",
            "Six in the fourth place: The moon is nearly full. The team horse goes astray. No blame.",
            "Nine in the fifth place: He possesses truth, which links together. No blame.",
            "Nine at the top: The crowing of a cock penetrates to heaven. Perseverance brings misfortune."
        ]
    },
    {
        "num": 62, "binary": (0, 0, 1, 1, 0, 0), "name_ch": "Xiao Guo", "name_en": "Preponderance of the Small",
        "image": "Thunder on the mountain: the image of Preponderance of the Small. Thus in his conduct the superior man gives preponderance to reverence. In bereavement he gives preponderance to grief. In his expenditures he gives preponderance to thrift.",
        "judgement": "Preponderance of the Small. Success. Perseverance furthers. Small things may be done; great things should not be done. The flying bird brings the message: It is not well to strive upward, it is well to remain below. Great good fortune.",
        "lines": [
            "Six at the beginning: The bird meets with misfortune through flying.",
            "Six in the second place: She passes by her ancestor and meets her ancestress. He does not reach his prince and meets the official. No blame.",
            "Nine in the third place: If one is not extremely careful, somebody may come from behind and strike him. Misfortune.",
            "Nine in the fourth place: No blame. He meets him without passing by. Going brings danger. One must be on guard. Do not act. Be constantly persevering.",
            "Six in the fifth place: Dense clouds, no rain from our western region. The prince shoots and hits him who is in the cave.",
            "Six at the top: He passes him by, not meeting him. The flying bird leaves him. Misfortune. This means bad luck and injury."
        ]
    },
    {
        "num": 63, "binary": (1, 0, 1, 0, 1, 0), "name_ch": "Ji Ji", "name_en": "After Completion",
        "image": "Water over fire: the image of the condition after completion. Thus the superior man takes thought of misfortune and arms himself against it in advance.",
        "judgement": "After Completion. Success in small matters. Perseverance furthers. At the beginning good fortune, at the end disorder.",
        "lines": [
            "Nine at the beginning: He brakes his wheels. He gets his tail in the water. No blame.",
            "Six in the second place: The woman loses the curtain of her carriage. Do not run after it; on the seventh day you will get it.",
            "Nine in the third place: The Illustrious Ancestor chastises the Devil's Country. After three years he conquers it. Inferior people must not be employed.",
            "Six in the fourth place: The finest clothes turn to rags. Be careful all day long.",
            "Nine in the fifth place: The neighbor in the east who slaughters an ox does not attain as much real blessing as the neighbor in the west with his small offering.",
            "Six at the top: He gets his head in the water. Danger."
        ]
    },
    {
        "num": 64, "binary": (0, 1, 0, 1, 0, 1), "name_ch": "Wei Ji", "name_en": "Before Completion",
        "image": "Fire over water: the image of the condition before transition. Thus the superior man is careful in the differentiation of things, so that each finds its place.",
        "judgement": "Before Completion. Success. But if the little fox, after nearly completing the crossing, gets his tail in the water, there is nothing that would further.",
        "lines": [
            "Six at the beginning: He gets his tail in the water. Humiliating.",
            "Nine in the second place: He brakes his wheels. Perseverance brings good fortune.",
            "Six in the third place: Before completion, attack brings misfortune. It is favorable to cross the great water.",
            "Nine in the fourth place: Perseverance brings good fortune. Remorse disappears. Shock, in order to chastise the Devil's Country. For three years, great realms are given as reward.",
            "Six in the fifth place: Perseverance brings good fortune. No remorse. The light of the superior man is true. Good fortune.",
            "Nine at the top: He drinks wine in genuine confidence. No blame. But if he wets his head, he loses it, in truth."
        ]
    }
]
