#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys


class Abstract():
    def __init__(self):
        pass

    def lan_select():
        print('Choose your language (eng, pol): ', end='')
        select = input()
        return select

    def lan_library(lang = 'eng'):
        language = {}
        if lang == 'eng':
            language['welcome'] = '<<<<  Enter "exit" to end program.  >>>>'  # welcome
            language['instructions'] = 'Player %s - (r)ock,(p)aper,(s)cissors: '  # instructions
            language['win'] = 'The winer is '  # win
            language['selectors'] = ('p', 'r', 's')  # selectors
            language['error'] = 'Wrong chars.\nI''m gonna out of here.'  # error
            language['tie'] = 'Tie!'  # tie
            return language
        elif lang == 'pol':
            language['welcome'] = '<<<<  Wprowadź "exit" żeby zakończyć program.  >>>>'
            language['instructions'] = 'Gracz %s - (p)apier,(k)amień,(n)ożyce: '
            language['win'] = 'Wygrywa '
            language['selectors'] = ('p', 'k', 'n')
            language['error'] = 'Złe znaki.\nSpadam stąd.'
            language['tie'] = 'Remis!'
            return language
        else:
            language['welcome'] = '<<<<  Enter "exit" to end program.  >>>>'  # welcome
            language['instructions'] = 'Player %s - (r)ock,(p)aper,(s)cissors: '  # instructions
            language['win'] = 'The winer is '  # win
            language['selectors'] = ('p', 'r', 's')  # selectors
            language['error'] = 'Wrong chars.\nI''m gonna out of here.'  # error
            language['tie'] = 'Tie!'  # tie
            return language

    def inputs(user_name = 'Player', i=1):
        lang = Abstract.lan_select()
        lang_pack = Abstract.lan_library(lang)
        os.system("clear")
        player = []
        while i < 3:
            print(lang_pack['welcome'])
            user = input(lang_pack['instructions' % i])
            if not user in lang_pack['selectors'] and user == 'exit':
                quit()
            player.append((user_name + ' ' + str(i), user))
            i += 1
            os.system("clear")
        return player

    def rules():
        lang = Abstract.lan_select()
        lang_pack = Abstract.lan_library(lang)
        t = Abstract.inputs()
        p1 = t[0][1]
        p1_name = t[0][0]
        p2 = t[1][1]
        p2_name = t[1][0]
        p = lang_pack['selectors'][0]
        k = lang_pack['selectors'][1]
        n = lang_pack['selectors'][2]
        win = lang_pack['win']
        if (p1 not in lang_pack['selectors']) or (p2 not in lang_pack['selectors']):
            print(lang_pack['error'])
            quit()
        if (p1 == p and p2 == k) \
                or (p1 == k and p2 == n) \
                or (p1 == n and p2 == p):
            print(win + p1_name)
        if (p1 == p and p2 == n) \
                or (p1 == k and p2 == p) \
                or (p1 == n and p2 == k):
            print(win + p2_name)


Abstract.rules()
