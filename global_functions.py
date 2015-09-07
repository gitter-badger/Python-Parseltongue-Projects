__author__ = "The Artha Group"

import urllib
import os

def find_words(text, search):
   """ @Gurkirpal Singh
   searches for text in given string

   text:    string in which search is to
            be done
   search:  text to find

   returns: boolean
   """
   text_words = [ x for x in text.lower().split() ]
   search_words = [ x for x in search.lower().split() ]

   found = [ word in text_words  for word in search_words ]

   return all( found )

#######################################################################

def get_remote_file(url, opt = 0, filename = None):
    """Grab a file form the given url.
    fname is optional
    opt 0 for no local file (return only); 1 for local save
    """
    resp = urllib.urlopen(url)
    c = resp.read()
    if opt==1 and filename:
        with open(filename, "w") as file_handler:
            file_handler.write(c)
    elif opt==1 and not filename:
        filename = url.split('/')[-1]
        with open(filename, "w") as file_handler:
            file_handler.write(c)
    else:
        return c

#######################################################################

def write_local_file(fn, fc, m):
    fs = open(fn, m)
    fs.write(fc)
    fs.close()
    return  True

#######################################################################

def include(filename):
    if os.path.exists(filename):
        execfile(filename)