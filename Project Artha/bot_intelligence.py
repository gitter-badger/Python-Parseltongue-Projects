__author__ = "The Artha Group"

import random
import re
import global_functions as g_func
import bot_activity as bot_act
import bot_constants as bot_const


def action(x):
    react = ""
    bot_act.bot_log(0, 1, x)
    x = x.replace('\'', '')
    x = re.sub(r'[^\w]', ' ', x)
    x = re.sub('\s+', ' ', x)
    x = x.lower()
    x = x.strip()
    if x == "":
        x = -1
    elif g_func.find_words(x.lower(), 'define '):
        bot_act.bot_output(bot_define(x.replace("define ", "", 1)))
        x = -2
    else:
        x.decode('utf-8')
        x = x.lower()
    bot_name_x = bot_const.bot_name.lower()
    for case in bot_act.Switch(x):
        if case('hello '+bot_name_x):
            react = "Hello there!"
            break
        if case('ok') or case('okay'):
            react = "Alright then."
            break
        if case(-1):
            react = "Say something."
            break
        if case(-2):
            react = -1
            break
        if case():  # default reply, omit possible 'if True'
            react = bot_interpret(x)
    if react != -1:
        bot_act.bot_output(react)


def bot_define(term):
    lines = [line.rstrip('\n') for line in open(bot_const.bot_base+'definition_keys.artha')]
    term2 = term.replace("a ", "", 1)
    if term in lines:
        ln = lines.index(term)
        lines_x = [line.rstrip('\n') for line in open(bot_const.bot_base+'definition_values.artha')]
        return lines_x[ln]
    elif term2 in lines:
        ln = lines.index(term2)
        lines_x = [line.rstrip('\n') for line in open(bot_const.bot_base+'definition_values.artha')]
        return lines_x[ln]
    else:
        return bot_def_down()


def bot_interpret(term):
    lines = [line.rstrip('\n') for line in open(bot_const.bot_base+'intellect_keys.artha')]
    if term in lines:
        ln = lines.index(term)
        lines_x = [line.rstrip('\n') for line in open(bot_const.bot_base+'intellect_values.artha')]
        return lines_x[ln]
    else:
        return bot_down()


def bot_down():
    lines = [line.rstrip('\n') for line in open(bot_const.bot_base+'confused.artha')]
    return random.choice(lines)


def bot_def_down():
    lines = [line.rstrip('\n') for line in open(bot_const.bot_base+'lost.artha')]
    return random.choice(lines)
