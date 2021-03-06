from random import randint
from flask import g
from poets_glossary import poets_name_glossary


def random_verse_generator(poet=None):
    if poet == None:
        return randint(1, 1384003)
    elif poet not in list(poets_name_glossary.keys()):
        return 'Error'
    else:
        select_poems = g.cur.execute('SELECT * FROM poems')
        poems = select_poems.fetchall()

        id = []
        for each_row in poems:
            if each_row[3] == '':
                continue

            url_feild = each_row[3]
            poet_name = url_feild.split('/')[3]
            if poet == poet_name:
                id.append(each_row[0])
        
        id_lenght = len(id)
        random_poemID =  randint(0, id_lenght)
        return id[random_poemID]
