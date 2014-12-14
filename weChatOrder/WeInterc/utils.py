# -*- coding: utf-8 -*-
__author__ = 'lxr0827'
import sys
import re
import random
import time
import logging
import json

try:
    import curses
    assert curses
except ImportError:
    curses = None

py3k = sys.version_info >= (3, 0, 0)

if py3k:
    basestring = unicode = str


def check_token(token):
    return re.match('^[A-Za-z0-9]{3,32}$', token)


def to_unicode(value):
    if isinstance(value, unicode):
        return value
    if isinstance(value, basestring):
        return value.decode('utf-8')
    if isinstance(value, int):
        return str(value)
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value


def isstring(value):
    return isinstance(value, basestring)


def generate_token(length=''):
    if not length:
        length = random.randint(3, 32)
    length = int(length)
    assert 3 <= length <= 32
    token = []
    letters = 'abcdefghijklmnopqrstuvwxyz' \
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
              '0123456789'
    for _ in range(length):
        token.append(random.choice(letters))
    return ''.join(token)


def enable_pretty_logging(logger, level='info'):
    """Turns on formatted logging output as configured.
    """
    logger.setLevel(getattr(logging, level.upper()))

    if not logger.handlers:
        # Set up color if we are in a tty and curses is installed
        color = False
        if curses and sys.stderr.isatty():
            try:
                curses.setupterm()
                if curses.tigetnum("colors") > 0:
                    color = True
            except:
                pass
        channel = logging.StreamHandler()
        channel.setFormatter(_LogFormatter(color=color))
        logger.addHandler(channel)


class _LogFormatter(logging.Formatter):
    def __init__(self, color, *args, **kwargs):
        logging.Formatter.__init__(self, *args, **kwargs)
        self._color = color
        if color:
            # The curses module has some str/bytes confusion in
            # python3.  Until version 3.2.3, most methods return
            # bytes, but only accept strings.  In addition, we want to
            # output these strings with the logging module, which
            # works with unicode strings.  The explicit calls to
            # unicode() below are harmless in python2 but will do the
            # right conversion in python 3.
            fg_color = (curses.tigetstr("setaf") or
                        curses.tigetstr("setf") or "")
            if (3, 0) < sys.version_info < (3, 2, 3):
                fg_color = unicode(fg_color, "ascii")
            self._colors = {
                logging.DEBUG: unicode(curses.tparm(fg_color, 4),
                                       "ascii"),  # Blue
                logging.INFO: unicode(curses.tparm(fg_color, 2),
                                      "ascii"),  # Green
                logging.WARNING: unicode(curses.tparm(fg_color, 3),
                                         "ascii"),  # Yellow
                logging.ERROR: unicode(curses.tparm(fg_color, 1),
                                       "ascii"),  # Red
            }
            self._normal = unicode(curses.tigetstr("sgr0"), "ascii")

    def format(self, record):
        try:
            record.message = record.getMessage()
        except Exception as e:
            record.message = "Bad message (%r): %r" % (e, record.__dict__)
        record.asctime = time.strftime(
            "%y%m%d %H:%M:%S", self.converter(record.created))
        prefix = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]' % \
                 record.__dict__
        if self._color:
            prefix = (self._colors.get(record.levelno, self._normal) +
                      prefix + self._normal)
        formatted = prefix + " " + record.message
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            formatted = formatted.rstrip() + "\n" + record.exc_text
        return formatted.replace("\n", "\n    ")


def json_loads(s):
    s = to_unicode(s)
    return json.loads(s)

def multi_get_letter(str_input):
    if isinstance(str_input, unicode): 
        unicode_str = str_input 
    else: 
        try: 
            unicode_str = str_input.decode('utf8') 
        except: 
            try: 
                unicode_str = str_input.decode('gbk') 
            except: 
                print('unknown coding')
                return 

    return_list = ''
    for one_unicode in unicode_str: 
        return_list+=single_get_first(one_unicode)
    return return_list 

def single_get_first(unicode1): 
    str1 = unicode1.encode('gbk') 
    try:         
        ord(str1) 
        return str1 
    except: 
        asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536 
        if asc >= -20319 and asc <= -20284: 
            return 'a' 
        if asc >= -20283 and asc <= -19776: 
            return 'b' 
        if asc >= -19775 and asc <= -19219: 
            return 'c' 
        if asc >= -19218 and asc <= -18711: 
            return 'd' 
        if asc >= -18710 and asc <= -18527: 
            return 'e' 
        if asc >= -18526 and asc <= -18240: 
            return 'f' 
        if asc >= -18239 and asc <= -17923: 
            return 'g' 
        if asc >= -17922 and asc <= -17418: 
            return 'h' 
        if asc >= -17417 and asc <= -16475: 
            return 'j' 
        if asc >= -16474 and asc <= -16213: 
            return 'k' 
        if asc >= -16212 and asc <= -15641: 
            return 'l' 
        if asc >= -15640 and asc <= -15166: 
            return 'm' 
        if asc >= -15165 and asc <= -14923: 
            return 'n' 
        if asc >= -14922 and asc <= -14915: 
            return 'o' 
        if asc >= -14914 and asc <= -14631: 
            return 'p' 
        if asc >= -14630 and asc <= -14150: 
            return 'q' 
        if asc >= -14149 and asc <= -14091: 
            return 'r' 
        if asc >= -14090 and asc <= -13119: 
            return 's' 
        if asc >= -13118 and asc <= -12839: 
            return 't' 
        if asc >= -12838 and asc <= -12557: 
            return 'w' 
        if asc >= -12556 and asc <= -11848: 
            return 'x' 
        if asc >= -11847 and asc <= -11056: 
            return 'y' 
        if asc >= -11055 and asc <= -10247: 
            return 'z' 
        return '' 

def json_dumps(d):
    return json.dumps(d)
