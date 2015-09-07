__author__ = "The Artha Group"

import bot_constants as bot_const
from bot_intelligence import action
import global_functions as g_func


class Switch(object):

    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


def bot_call(err):
    bot_log(0, -1, "[conversation log for "+bot_const.bot_name+" @ "+bot_const.bot_init+"]\n")
    for f in bot_const.must_files:
        if not open(bot_const.bot_base+f+".artha"):
            err = -1
    bot_output("Welcome! Please begin.")
    return err


def bot_input(opt):
    cmd = ""
    if opt == 1:
        cmd = raw_input("Me: " + cmd)
    elif opt == 2:
        cmd = raw_input("Me: ")
    return cmd


def bot_output(x):
    print(bot_const.bot_name+": "+x)
    bot_log(0, 0, x)


def bot_control():
    while 1:
        cmd = bot_input(2)
        action(cmd)


def bot_log(opt=0, agent=0, buff=None, lfn=None):
    if bot_log is False:
        return
    """
    Format: DAY-MNTH-MTH-HH-MM-SS-YYYY.log
    :param opt: [0 = save; 1 = read]
    :param agent: [-1 = nobody, 0 = bot, 1 = user]
    :param buff: [the log body]
    :param lfn: [log filename (optional)]
    :return: nothing
    """
    if lfn is None:
        bot_ini = bot_const.bot_init.replace(":", "-")
        bot_ini = bot_ini.replace(" ", "-")
        lfn = bot_const.bot_log_base+bot_ini+".log"
    else:
        lfn = bot_const.bot_log_base+lfn
    if agent == 0:
        buff = bot_const.bot_name+": "+buff
    elif agent == 1:
        buff = "Me: "+buff
    if agent != -1:
        buff = "["+bot_const.cur_time+"] :: "+buff
    if opt == 0 and buff is not None and lfn is not None:
        g_func.write_local_file(lfn, buff+"\n", "a")
    elif opt == 0 and buff is not None and lfn is None:
        g_func.write_local_file(lfn, "["+bot_const.cur_time+"] :: "+buff+"\n", "a")
