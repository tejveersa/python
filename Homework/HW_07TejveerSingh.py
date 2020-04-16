''' Tejveer Singh
    10/13/15'''

theBells = '''
HEAR the sledges with the bells,
Silver bells!
What a world of merriment their melody foretells!
How they tinkle, tinkle, tinkle,
In the icy air of night!
While the stars, that oversprinkle
All the heavens, seem to twinkle
With a crystalline delight;
Keeping time, time, time,
In a sort of Runic rhyme,
To the tintinnabulation that so musically wells
From the bells, bells, bells, bells,
Bells, bells, bells—
From the jingling and the tinkling of the bells.

Hear the mellow wedding bells,
Golden bells!
What a world of happiness their harmony foretells!
Through the balmy air of night
How they ring out their delight!
From the molten-golden notes,
And all in tune,
What a liquid ditty floats
To the turtle-dove that listens, while she gloats
On the moon!
Oh, from out the sounding cells,
What a gush of euphony voluminously wells!
How it swells!
How it dwells
On the Future! how it tells
Of the rapture that impels
To the swinging and the ringing
Of the bells, bells, bells,
Of the bells, bells, bells, bells,
Bells, bells, bells—
To the rhyming and the chiming of the bells!

Hear the loud alarum bells,
Brazen bells!
What a tale of terror, now, their turbulency tells!
In the startled ear of night
How they scream out their affright!
Too much horrified to speak,
They can only shriek, shriek,
Out of tune,
In a clamorous appealing to the mercy of the fire,
In a mad expostulation with the deaf and frantic fire,
Leaping higher, higher, higher,
With a desperate desire,
And a resolute endeavor
Now—now to sit or never,
By the side of the pale-faced moon.
Oh, the bells, bells, bells!
What a tale their terror tells
Of Despair!

How they clang, and clash, and roar!
What a horror they outpour
On the bosom of the palpitating air!
Yet the ear it fully knows,
By the twanging
And the clanging,
How the danger ebbs and flows;
Yet the ear distinctly tells,
In the jangling
And the wrangling,
How the danger sinks and swells,—
By the sinking or the swelling in the anger of the bells,
Of the bells,
Of the bells, bells, bells, bells,
Bells, bells, bells—
In the clamor and the clangor of the bells!

Hear the tolling of the bells,
Iron bells!
What a world of solemn thought their monody compels!
In the silence of the night
How we shiver with affright
At the melancholy menace of their tone!
For every sound that floats
From the rust within their throats
Is a groan.
And the people—ah, the people,
They that dwell up in the steeple,
All alone,
And who tolling, tolling, tolling,
In that muffled monotone,
Feel a glory in so rolling
On the human heart a stone—
They are neither man nor woman,
They are neither brute nor human,
They are Ghouls:
And their king it is who tolls;
And he rolls, rolls, rolls,
Rolls
A pæan from the bells;
And his merry bosom swells
With the pæan of the bells,
And he dances, and he yells:
Keeping time, time, time,
In a sort of Runic rhyme,
To the pæan of the bells,
Of the bells:
Keeping time, time, time,
In a sort of Runic rhyme,
To the throbbing of the bells,
Of the bells, bells, bells—
To the sobbing of the bells;
Keeping time, time, time,
As he knells, knells, knells,
In a happy Runic rhyme,
To the rolling of the bells,
Of the bells, bells, bells:
To the tolling of the bells,
Of the bells, bells, bells, bells,
Bells, bells, bells—
To the moaning and the groaning of the bells.
'''

cantoXII = '''
Arise to birth with me, my brother.
Give me your hand out of the depths
sown by your sorrows.
You will not return from these stone fastnesses.
You will not emerge from subterranean time.
Your rasping voice will not come back,
nor your pierced eyes rise from their sockets.

Look at me from the depths of the earth,
tiller of fields, weaver, reticent shepherd,
groom of totemic guanacos,
mason high on your treacherous scaffolding,
iceman of Andean tears,
jeweler with crushed fingers,
farmer anxious among his seedlings,
potter wasted among his clays--
bring to the cup of this new life
your ancient buried sorrows.
Show me your blood and your furrow;
say to me: here I was scourged
because a gem was dull or because the earth
failed to give up in time its tithe of corn or stone.
Point out to me the rock on which you stumbled,
the wood they used to crucify your body.
Strike the old flints
to kindle ancient lamps, light up the whips
glued to your wounds throughout the centuries
and light the axes gleaming with your blood.

I come to speak for your dead mouths.

Throughout the earth
let dead lips congregate,
out of the depths spin this long night to me
as if I rode at anchor here with you.

And tell me everything, tell chain by chain,
and link by link, and step by step;
sharpen the knives you kept hidden away,
thrust them into my breast, into my hands,
like a torrent of sunbursts,
an Amazon of buried jaguars,
and leave me cry: hours, days and years,
blind ages, stellar centuries.

And give me silence, give me water, hope.

Give me the struggle, the iron, the volcanoes.

Let bodies cling like magnets to my body.

Come quickly to my veins and to my mouth.

Speak through my speech, and through my blood. 
'''

import string

def litCricFriend(wordList, text):
    text = text.lower()
    text = text.replace('-', ' ')
    text = text.split()
    newWordList = []
    for word in text:
        newWordList.append(word.strip(string.punctuation))
    wordList = [word.lower() for word in wordList]
    counter = 0
    for word in wordList:
        word = word.lower()
        counter+= newWordList.count(word)
    return(counter/len(newWordList))


print(litCricFriend(['a', 'an'], theBells))
print(litCricFriend(['the'], theBells))
print(litCricFriend(['a', 'an'], cantoXII))
print(litCricFriend(['the'], cantoXII))

'''
0.0347682119205298 'a' and 'an' in theBells
0.1357615894039735 'the' in theBells
0.009615384615384616 'a' and 'an' in cantoXII
0.05448717948717949 the' in cantoXII

Poe and Neruda use "a" and "an" at different rates as shown by the outputs above.
Poe and Neruda use "the" at different rates as shown by the outputs above.
'a', 'an', and 'the' are used more in theBells than cantoXII.
'''
