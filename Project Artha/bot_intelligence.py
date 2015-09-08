__author__ = "The Artha Group"

import os
import random
import global_functions as g_func
import bot_constants as bot_const


def bot_process(term):
    senses = bot_senses()
    for sense in senses:
        if sense in term:
            lines = [line.rstrip('\n') for line in open(bot_const.bot_sense_base+sense+'_keys.artha')]
            if g_func.clean_for_artha(term.replace(sense, "", 1)) in lines:
                ln = lines.index(g_func.clean_for_artha(term.replace(sense, "", 1)))
                lines_x = [line.rstrip('\n') for line in open(bot_const.bot_sense_base+sense+'_replies.artha')]
                return lines_x[ln]
            elif g_func.clean_for_artha(term.replace(sense+" a", "", 1)) in lines:
                ln = lines.index(g_func.clean_for_artha(term.replace(sense+" a", "", 1)))
                lines_x = [line.rstrip('\n') for line in open(bot_const.bot_sense_base+sense+'_replies.artha')]
                return lines_x[ln]
            else:
                return bot_down()
        else:
                return bot_def_down()


def bot_senses():
    true_senses = []
    raw_sense = [x for x in os.listdir(bot_const.bot_sense_base) if os.path.isfile(bot_const.bot_sense_base+x)]
    for s in raw_sense:
        if '_replies.artha' not in s:
            true_senses.append(s.replace('_keys.artha', ''))
    return true_senses


def bot_interpret(term):
    lines = [line.rstrip('\n') for line in open(bot_const.bot_base+'intellect_keys.artha')]

    if term in lines:
        ln = lines.index(term)
        lines_x = [line.rstrip('\n') for line in open(bot_const.bot_base+'intellect_values.artha')]
        return lines_x[ln]
    else:
        return bot_process(term)


def bot_greeting():
    lines = [line.rstrip('\n') for line in open(bot_const.bot_base+'greetings.artha')]
    return random.choice(lines)


def bot_down():
    lines = [line.rstrip('\n') for line in open(bot_const.bot_base+'confused.artha')]
    return random.choice(lines)


def bot_def_down():
    lines = [line.rstrip('\n') for line in open(bot_const.bot_base+'lost.artha')]
    return random.choice(lines)
