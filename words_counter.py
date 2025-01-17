import operator
from os import remove

full_text = '''
Oh, woah
Oh, woah
Oh, woah

You know you love me, I know you care
Just shout whenever, and I'll be there
You are my love, you are my heart
And we will never, ever, ever be apart

Are we an item? Girl, quit playing!
We're just friends? What are you saying?
Said there's another and looked right in my eyes
My first love broke my heart for the first time
And I was like

Baby, baby, baby, ooh, like
Baby, baby, baby, no, like
Baby, baby, baby, ooh
Thought you'd always be mine, mine

Baby, baby, baby, ooh, like
Baby, baby, baby, no, like
Baby, baby, baby, ooh
Thought you'd always be mine, mine

Oh, for you, I would have done whatever
And I just can't believe we ain't together
And I wanna play it cool, but I'm losing you
I'll buy you anything, I'll buy you any ring

And I'm in pieces, baby, fix me
And just shake me till you wake me from this bad dream
I'm going down, down, down, down
And I just can't believe my first love won't be around
And I'm like

Baby, baby, baby, ooh, like
Baby, baby, baby, no, like
Baby, baby, baby, ooh
Thought you'd always be mine, mine

Baby, baby, baby, ooh, like
Baby, baby, baby, no, like
Baby, baby, baby, ooh
Thought you'd always be mine, mine

Luda!
When I was thirteen, I had my first love
There was nobody that compared to my baby
And nobody came to between us or could ever come above
She had me going crazy, oh, I was starstruck
She woke me up daily, don't need no Starbucks
She make my heart pound
I skip a beat when I see her in the street and
At school, on the playground
But I really wanna see her on the weekend
She knows she got me dazing
'Cause she was so amazing
And now my heart is breaking
But I just keep on saying

Baby, baby, baby, ooh,like
Baby, baby, baby, no, like
Baby, baby, baby, ooh
Thought you'd always be mine, mine

Baby, baby, baby, ooh, like
Baby, baby, baby, no, like
Baby, baby, baby, ooh
Thought you'd always be mine, mine

I'm gone
(Yeah, yeah, yeah)
(Yeah, yeah, yeah)
Now I'm all gone
(Yeah, yeah, yeah)
(Yeah, yeah, yeah)
Now I'm all gone
(Yeah, yeah, yeah)
(Yeah, yeah, yeah)
Now I'm all gone (gone, gone, gone)
I'm gone
'''

remove_these = [',', '(', ')', '\'ll', '\'d', '\'m', '-']

for thing in remove_these:
    full_text = full_text.replace(thing, '')

words_list = full_text.lower().split()

word_count = {}

for word in words_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=False)

for word_info in sorted_count:
    print(f'{word_info[0].capitalize()} - {word_info[1]}')

print(f'\nThere are {len(sorted_count)} unique words')
