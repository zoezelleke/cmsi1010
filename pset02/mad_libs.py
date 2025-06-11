# ----------------------------------------------------------------------
# This is the file mad_libs.py

# The intent is to give you practice writing a complete, interactive
# Python program using a lot of Python data types, especially lists,
# sets, and dictionaries.

# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
# ----------------------------------------------------------------------

# Things to do:

# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!

# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.

# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.

# Here are some constraints:

#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.

import random
templates = [
    {
        "text": "The :color :flower :verb on the :adjective :object.",
        "author": "Lucy Dacus"
    },
    {
        "text": "The :adjective :band is :verb at the :place.",
        "author": "Pheobe Bridgers"
    },
    {
        "text": "Even the :color :animal loves to :verb with a :adjective :object.",
        "author": "Julian Baker"
    },
    {
        "text": "The :noun goes to the :adjective :person.",
        "author": "Lorde"
    },
    {
        "text": "The :adjective :person :verb over a :color :object.",
        "author": "Dora Jar"
    },
    {
        "text": ":verb like a :adjective :animal trying to :verb at the :place.",
        "author": "Mitski"
    },
    {
        "text": ":noun and :noun are best friends in the :place.",
        "author": "Grace"
    },
    {
        "text": "The :person :verb under the :adjective sky:",
        "author": "Imogen Heap"
    },
    {
        "text": ":On :day :person is :verb at the :adjective :place.",
        "author": "SZA"
    },
    {
        "text": ":pronoun :verb for her :person to :verb :pronoun to the :place.", 
        "author": "Ariana Grande"
    

    }
]

yes_answers = {"yes", "oui", "si" "yeah"}

current_template = random.choice(templates)
word = {}
for word in current_template["text"].split():
    if word 

