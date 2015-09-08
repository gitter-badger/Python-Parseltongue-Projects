__author__ = "The Artha Group"

import urllib
import os
import re
import bot_constants as bot_const

class Switch(object):
    """
    Case-type switch
    """

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


def find_words(text, search):
    """
    @Gurkirpal Singh
    searches for text in given string
    text:    string in which search is to be done
    search:  text to find
    returns: boolean
    """
    text_words = [x for x in text.lower().split()]
    search_words = [x for x in search.lower().split()]
    found = [word in text_words for word in search_words]
    return all(found)


def get_remote_file(url, opt=0, filename=None):
    """
    Grab a file form the given url.
    filename is optional
    opt 0 for no local file (return only); 1 for local save
    """
    resp = urllib.urlopen(url)
    c = resp.read()
    if opt == 1 and filename:
        with open(filename, "w") as file_handler:
            file_handler.write(c)
    elif opt == 1 and not filename:
        filename = url.split('/')[-1]
        with open(filename, "w") as file_handler:
            file_handler.write(c)
    else:
        return c


def write_local_file(fn, fc, m):
    """
    Write into a local file
    :param fn: filename
    :param fc: what to write
    :param m: file open mode
    :return:
    """
    fs = open(fn, m)
    fs.write(fc)
    fs.close()
    return True


def include(filename):
    """
    File inclusion
    """
    if os.path.exists(filename):
        execfile(filename)


def clean_for_artha(x):
    """
    Remove punctuation and trim space, tabs and lines
    :param x: text in
    :return: sanitized text out
    """
    x = x.replace('\'', '')
    x = re.sub(r'[^\w]', ' ', x)
    x = re.sub('\s+', ' ', x)
    x = x.lower()
    x = x.strip()
    return x


def files_in_dir(dir_name):
    """
    Files in a folder
    :param dir_name: folder name
    :return: list of files
    """
    return [x for x in os.listdir(dir_name) if os.path.isfile(dir_name+'/'+x)]

def parse_artha_vars(x):
    """
    Parse the list bot_parsing[]
    :param x: text in
    :return: text out
    """
    for match in bot_const.bot_parsing:
        if match and bot_const.bot_parsing[match] is not None:
            return x.replace(match, bot_const.bot_parsing[match])

def upper_first_char(x):
    """
    Capitalize first letter in string.
    :param x: text in
    :return: text out
    """
    return x[0].upper() + x[1:]

