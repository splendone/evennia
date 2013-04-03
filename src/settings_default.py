"""
Master configuration file for Evennia.

NOTE: NO MODIFICATIONS SHOULD BE MADE TO THIS FILE!

All settings changes should be done by copy-pasting the variable and
its value to game/settings.py. An empty game/settings.py can be
auto-generated by running game/manage.py without any arguments.

Hint: Don't copy&paste over more from this file than you actually want
to change.  Anything you don't copy&paste will thus retain its default
value - which may change as Evennia is developed. This way you can
always be sure of what you have changed and what is default behaviour.
"""

import os

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Evennia"
# Activate telnet service
TELNET_ENABLED = True
# A list of ports the Evennia telnet server listens on
# Can be one or many.
TELNET_PORTS = [4000]
# Interface addresses to listen to. If 0.0.0.0, listen to all.
TELNET_INTERFACES = ['0.0.0.0']
# OOB (out-of-band) telnet communication allows Evennia to communicate
# special commands and data with enabled Telnet clients. This is used
# to create custom client interfaces over a telnet connection. To make
# full use of OOB, you need to prepare functions to handle the data
# server-side (see OOB_FUNC_MODULE). TELNET_ENABLED is required for this
# to work.
TELNET_OOB_ENABLED = False # OBS - currently not fully implemented - do not use!
# Start the evennia django+twisted webserver so you can
# browse the evennia website and the admin interface
# (Obs - further web configuration can be found below
# in the section  'Config for Django web features')
WEBSERVER_ENABLED = True
# A list of ports the Evennia webserver listens on
WEBSERVER_PORTS = [8000]
# Interface addresses to listen to. If 0.0.0.0, listen to all.
WEBSERVER_INTERFACES = ['0.0.0.0']
# IP addresses that may talk to the server in a reverse proxy configuration,
# like NginX.
UPSTREAM_IPS = ['127.0.0.1']
# Start the evennia ajax client on /webclient
# (the webserver must also be running)
WEBCLIENT_ENABLED = True
# Activate SSH protocol (SecureShell)
SSH_ENABLED = False
# Ports to use for SSH
SSH_PORTS = [8022]
# Interface addresses to listen to. If 0.0.0.0, listen to all.
SSH_INTERFACES = ['0.0.0.0']
# Actiave SSL protocol (SecureSocketLibrary)
SSL_ENABLED = False
# Ports to use for SSL
SSL_PORTS = [4001]
# Interface addresses to listen to. If 0.0.0.0, listen to all.
SSL_INTERFACES = ['0.0.0.0']
# The path that contains this settings.py file (no trailing slash).
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Path to the src directory containing the bulk of the codebase's code.
SRC_DIR = os.path.join(BASE_PATH, 'src')
# Path to the game directory (containing the database file if using sqlite).
GAME_DIR = os.path.join(BASE_PATH, 'game')
# Place to put log files
LOG_DIR = os.path.join(GAME_DIR, 'logs')
SERVER_LOG_FILE = os.path.join(LOG_DIR, 'server.log')
PORTAL_LOG_FILE = os.path.join(LOG_DIR, 'portal.log')
# Where to log server requests to the web server. This is VERY spammy, so this
# file should be removed at regular intervals.
HTTP_LOG_FILE = os.path.join(LOG_DIR, 'http_requests.log')
# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/8.0/interactive/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'UTC'
# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
LANGUAGE_CODE = 'en-us'
# Should the default MUX help files be imported? This might be
# interesting to developers for reference, but is frustrating to users
# since it creates a lot of help entries that has nothing to do
# with what is actually available in the game.
IMPORT_MUX_HELP = False
# How long time (in seconds) a user may idle before being logged
# out. This can be set as big as desired. A user may avoid being
# thrown off by sending the empty system command 'idle' to the server
# at regular intervals. Set <=0 to deactivate idle timout completely.
IDLE_TIMEOUT = 3600
# The idle command can be sent to keep your session active without actually
# having to spam normal commands regularly. It gives no feedback, only updates
# the idle timer.
IDLE_COMMAND = "idle"
# The set of encodings tried. A Player object may set an attribute "encoding" on
# itself to match the client used. If not set, or wrong encoding is
# given, this list is tried, in order, aborting on the first match.
# Add sets for languages/regions your players are likely to use.
# (see http://en.wikipedia.org/wiki/Character_encoding)
ENCODINGS = ["utf-8", "latin-1", "ISO-8859-1"]
# The game server opens an AMP port so that the portal can
# communicate with it. This is an internal functionality of Evennia, usually
# operating between two processes on the same machine. You usually don't need to
# change this unless you cannot use the default AMP port/host for whatever reason.
AMP_HOST = 'localhost'
AMP_PORT = 5000
AMP_INTERFACE = '127.0.0.1'
# Caching speeds up all forms of database access, often considerably. There
# are (currently) only two settings, "local" or None, the latter of which turns
# off all caching completely. Local caching stores data in the process. It's very
# fast but will go out of sync if more than one process writes to the database (such
# as when using procpool or an extensice web precense).
GAME_CACHE_TYPE = "local"
# Attributes on objects are cached aggressively for speed. If the number of
# objects is large (and their attributes are often accessed) this can use up a lot of
# memory. So every now and then Evennia checks the size of this cache and resets
# it if it's too big. This variable sets the maximum size (in MB).
ATTRIBUTE_CACHE_MAXSIZE = 100
# OOB (Out-of-band

######################################################################
# Evennia Database config
######################################################################

# Database config syntax for Django 1.2+.
# ENGINE - path to the the database backend. Possible choices are:
#            'django.db.backends.sqlite3', (default)
#            'django.db.backends.mysql',
#            'django.db.backends.'postgresql_psycopg2' (see Issue 241),
#            'django.db.backends.oracle' (untested).
# NAME - database name, or path to the db file for sqlite3
# USER - db admin (unused in sqlite3)
# PASSWORD - db admin password (unused in sqlite3)
# HOST - empty string is localhost (unused in sqlite3)
# PORT - empty string defaults to localhost (unused in sqlite3)
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':os.path.join(GAME_DIR, 'evennia.db3'),
        'USER':'',
        'PASSWORD':'',
        'HOST':'',
        'PORT':''
        }}
# Engine Config style for Django versions < 1.2 only. See above.
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(GAME_DIR, 'evennia.db3')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

######################################################################
# Evennia pluggable modules
######################################################################
# Plugin modules extend Evennia in various ways. In the cases with no
# existing default, there are examples of many of these modules
# in game/gamesrc/conf/examples.

# The command parser module to use. See the default module for which
# functions it must implement
COMMAND_PARSER = "src.commands.cmdparser.cmdparser"
# The handler that outputs errors when searching
# objects using object.search().
SEARCH_AT_RESULT = "src.commands.cmdparser.at_search_result"
# The parser used in order to separate multiple
# object matches (so you can separate between same-named
# objects without using dbrefs).
SEARCH_AT_MULTIMATCH_INPUT = "src.commands.cmdparser.at_multimatch_input"
# The module holding text strings for the connection screen.
# This module should contain one or more variables
# with strings defining the look of the screen.
CONNECTION_SCREEN_MODULE = "src.commands.connection_screen"
# An optional module that, if existing, must hold a function
# named at_initial_setup(). This hook method can be used to customize
# the server's initial setup sequence (the very first startup of the system).
# The check will fail quietly if module doesn't exist or fails to load.
AT_INITIAL_SETUP_HOOK_MODULE = ""
# Module containing your custom at_server_start(), at_server_reload() and
# at_server_stop() methods. These methods will be called every time
# the server starts, reloads and resets/stops respectively.
AT_SERVER_STARTSTOP_MODULE = ""
# List of one or more module paths to modules containing a function start_plugin_services(application). This module
# will be called with the main Evennia Server application when the Server is initiated.
# It will be called last in the startup sequence.
SERVER_SERVICES_PLUGIN_MODULES = []
# List of one or more module paths to modules containing a function start_plugin_services(application). This module
# will be called with the main Evennia Portal application when the Portal is initiated.
# It will be called last in the startup sequence.
PORTAL_SERVICES_PLUGIN_MODULES = []
# Module holding MSSP meta data. This is used by MUD-crawlers to determine
# what type of game you are running, how many players you have etc.
MSSP_META_MODULE = ""
# Module holding server-side custom functions for out-of-band protocols to call.
# Note that OOB_ENABLED must be True for this to be used.
OOB_FUNC_MODULE = "" # Not yet available in Evennia - do not use!
# Tuple of modules implementing lock functions. All callable functions
# inside these modules will be available as lock functions.
LOCK_FUNC_MODULES = ("src.locks.lockfuncs",)

######################################################################
# Default command sets
######################################################################
# Note that with the exception of the unloggedin set (which is not
# stored anywhere in the databse), changing these paths will only affect NEW created
# characters/objects, not those already in play. So if you plan to change
# this, it's recommended you do it before having created a lot of objects
# (or simply reset the database after the change for simplicity). Remember
# that you should never edit things in src/. Instead copy out the examples
# in game/gamesrc/commands/examples up one level and re-point these settings
# to point to these copies instead - these you can then change as you please
# (or copy/paste from the default modules in src/ if you prefer).

# Command set used before player has logged in
CMDSET_UNLOGGEDIN = "src.commands.default.cmdset_unloggedin.UnloggedinCmdSet"
# Default set for logged in player with characters (fallback)
CMDSET_DEFAULT = "src.commands.default.cmdset_default.DefaultCmdSet"
# Command set for players without a character (ooc)
CMDSET_OOC = "src.commands.default.cmdset_ooc.OOCCmdSet"

######################################################################
# Typeclasses
######################################################################

# Base paths for typeclassed object classes. These paths must be
# defined relative evennia's root directory. They will be searched in
# order to find relative typeclass paths.
OBJECT_TYPECLASS_PATHS = ["game.gamesrc.objects", "game.gamesrc.objects.examples", "contrib"]
SCRIPT_TYPECLASS_PATHS = ["game.gamesrc.scripts", "game.gamesrc.scripts.examples", "contrib"]
PLAYER_TYPECLASS_PATHS = ["game.gamesrc.objects", "contrib"]

# Typeclass for player objects (linked to a character) (fallback)
BASE_PLAYER_TYPECLASS = "src.players.player.Player"
# Typeclass and base for all objects (fallback)
BASE_OBJECT_TYPECLASS = "src.objects.objects.Object"
# Typeclass for character objects linked to a player (fallback)
BASE_CHARACTER_TYPECLASS = "src.objects.objects.Character"
# Typeclass for rooms (fallback)
BASE_ROOM_TYPECLASS = "src.objects.objects.Room"
# Typeclass for Exit objects (fallback).
BASE_EXIT_TYPECLASS = "src.objects.objects.Exit"
# Typeclass for Scripts (fallback). You usually don't need to change this
# but create custom variations of scripts on a per-case basis instead.
BASE_SCRIPT_TYPECLASS = "src.scripts.scripts.DoNothing"
# The home location for new characters. This must be a unique
# dbref (default is Limbo #2). If you want more advanced control over
# start locations, copy the "create" command from
# src/commands/default/unloggedin.py and customize.
CHARACTER_DEFAULT_HOME = "#2"

######################################################################
# Batch processors
######################################################################

# Python path to a directory to be searched for batch scripts
# for the batch processors (.ev and/or .py files).
BASE_BATCHPROCESS_PATHS = ['game.gamesrc.world', 'contrib']

######################################################################
# Game Time setup
######################################################################

# You don't actually have to use this, but it affects the routines in
# src.utils.gametime.py and allows for a convenient measure to
# determine the current in-game time. You can of course read "week",
# "month" etc as your own in-game time units as desired.

#The time factor dictates if the game world runs faster (timefactor>1)
# or slower (timefactor<1) than the real world.
TIME_FACTOR = 2.0
# The tick is the smallest unit of time in the game. Smallest value is 1s.
TIME_TICK = 1.0
# These measures might or might not make sense to your game world.
TIME_MIN_PER_HOUR = 60
TIME_HOUR_PER_DAY = 24
TIME_DAY_PER_WEEK = 7
TIME_WEEK_PER_MONTH = 4
TIME_MONTH_PER_YEAR = 12


######################################################################
# Default Player setup and access
######################################################################

# Different Multisession modes allow a player (=account) to connect to the game simultaneously
# with multiple clients (=sessions). In modes 0,1 there is only one character created to the same
# name as the account at first login. In modes 1,2 no default character will be created and
# the MAX_NR_CHARACTERS value (below) defines how many characters are allowed.
#  0 - single session, one player, one character, when a new session is connected, the old one is disconnected
#  1 - multiple sessions, one player, one character, each session getting the same data
#  2 - multiple sessions, one player, many characters, each session getting data from different characters
MULTISESSION_MODE = 0
# The maximum number of characters allowed for MULTISESSION_MODE 2. This is checked
# by the default ooc char-creation command. Forced to 1 for MULTISESSION_MODE 0 and 1.
MAX_NR_CHARACTERS = 1
# The access hiearchy, in climbing order. A higher permission in the
# hierarchy includes access of all levels below it. Used by the perm()/pperm() lock functions.
PERMISSION_HIERARCHY = ("Players","PlayerHelpers","Builders", "Wizards", "Immortals")
# The default permission given to all new players
PERMISSION_PLAYER_DEFAULT = "Players"

######################################################################
# In-game Channels created from server start
######################################################################

# Defines a dict with one key for each from-start
# channel. Each key points to a tuple containing
# (name, aliases, description, locks)
# where aliases may be a tuple too, and locks is
# a valid lockstring definition.
# Default user channel for communication
CHANNEL_PUBLIC = ("Public", ('ooc',), 'Public discussion',
                  "control:perm(Wizards);listen:all();send:all()")
# General info about the server
CHANNEL_MUDINFO = ("MUDinfo", '', 'Informative messages',
                   "control:perm(Immortals);listen:perm(Immortals);send:false()")
# Channel showing when new people connecting
CHANNEL_CONNECTINFO = ("MUDconnections", '', 'Connection log',
                       "control:perm(Immortals);listen:perm(Wizards);send:false()")

######################################################################
# External Channel connections
######################################################################

# Note: You do *not* have to make your MUD open to
# the public to use the external connections, they
# operate as long as you have an internet connection,
# just like stand-alone chat clients. IRC and IMC2
# requires that you have twisted.words installed.

# Evennia can connect to external IRC channels and
# echo what is said on the channel to IRC and vice
# versa. Obs - make sure the IRC network allows bots.
# When enabled, command @irc2chan will be available in-game
IRC_ENABLED = False
# IMC (Inter-MUD communication) allows to connect an Evennia channel
# to an IMC2 server. This lets them talk to people on other MUDs also
# using IMC.  Evennia's IMC2 client was developed against MudByte's
# network. You must register your MUD on the network before you can
# use it, go to http://www.mudbytes.net/imc2-intermud-join-network.
# Choose 'Other unsupported IMC2 version' from the choices and and
# enter your information there. You should enter the same 'short mud
# name' as your SERVERNAME above, then choose imc network server as
# well as client/server passwords same as below. When enabled, the
# command @imc2chan becomes available in-game and allows you to
# connect Evennia channels to IMC channels on the network. The Evennia
# discussion channel 'ievennia' is on server01.mudbytes.net:5000.
IMC2_ENABLED = False
IMC2_NETWORK = "server01.mudbytes.net"
IMC2_PORT = 5000 # this is the imc2 port, not on localhost
IMC2_CLIENT_PWD = ""
IMC2_SERVER_PWD = ""
# RSS allows to connect RSS feeds (from forum updates, blogs etc) to
# an in-game channel. The channel will be updated when the rss feed
# updates. Use @rss2chan in game to connect if this setting is
# active. OBS: RSS support requires the python-feedparser package to
# be installed (through package manager or from the website
# http://code.google.com/p/feedparser/)
RSS_ENABLED=False
RSS_UPDATE_INTERVAL = 60*10 # 10 minutes

######################################################################
# Django web features
######################################################################

# While DEBUG is False, show a regular server error page on the web
# stuff, email the traceback to the people in the ADMINS tuple
# below. If True, show a detailed traceback for the web
# browser to display. Note however that this will leak memory when
# active, so make sure to turn it off for a production server!
DEBUG = False
# While true, show "pretty" error messages for template syntax errors.
TEMPLATE_DEBUG = DEBUG
# Emails are sent to these people if the above DEBUG value is False. If you'd
# rather nobody recieve emails, leave this commented out or empty.
ADMINS = () #'Your Name', 'your_email@domain.com'),)
# These guys get broken link notifications when SEND_BROKEN_LINK_EMAILS is True.
MANAGERS = ADMINS
# Absolute path to the directory that holds media (no trailing slash).
# Example: "/home/media/media.lawrence.com"
MEDIA_ROOT = os.path.join(SRC_DIR, 'web', 'media')
# Absolute path to the directory that holds (usually links to) the
# django admin media files. If the target directory does not exist, it
# is created and linked by Evennia upon first start. Otherwise link it
# manually to django/contrib/admin/media.
ADMIN_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'admin')
# It's safe to dis-regard this, as it's a Django feature we only half use as a
# dependency, not actually what it's primarily meant for.
SITE_ID = 1
# The age for sessions.
# Default: 1209600 (2 weeks, in seconds)
SESSION_COOKIE_AGE = 1209600
# Session cookie domain
# Default: None
SESSION_COOKIE_DOMAIN = None
# The name of the cookie to use for sessions.
# Default: 'sessionid'
SESSION_COOKIE_NAME = 'sessionid'
# Should the session expire when the browser closes?
# Default: False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False
# Where to find locales (no need to change this, most likely)
LOCALE_PATHS = ["../locale/"]
# This should be turned off unless you want to do tests with Django's
# development webserver (normally Evennia runs its own server)
SERVE_MEDIA = False
# The master urlconf file that contains all of the sub-branches to the
# applications.
ROOT_URLCONF = 'src.web.urls'
# Where users are redirected after logging in via contrib.auth.login.
LOGIN_REDIRECT_URL = '/'
# Where to redirect users when using the @login_required decorator.
LOGIN_URL = '/accounts/login'
# Where to redirect users who wish to logout.
LOGOUT_URL = '/accounts/login'
# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure
# to use a trailing slash. Django1.4+ will look for admin files under
# STATIC_URL/admin.
STATIC_URL = '/media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/" # needed for backwards compatibility django < 1.4
# The name of the currently selected web template. This corresponds to the
# directory names shown in the webtemplates directory.
ACTIVE_TEMPLATE = 'prosimii'
# We setup the location of the website template as well as the admin site.
TEMPLATE_DIRS = (
    os.path.join(SRC_DIR, "web", "templates", ACTIVE_TEMPLATE),
    os.path.join(SRC_DIR, "web", "templates"),)
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',)
# MiddleWare are semi-transparent extensions to Django's functionality.
# see http://www.djangoproject.com/documentation/middleware/ for a more detailed
# explanation.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', # 1.4?
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',)
# Context processors define context variables, generally for the template
# system to use.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.debug',
    'src.web.utils.general_context.general_context',)

######################################################################
# Evennia components
######################################################################

# Global and Evennia-specific apps. This ties everything together so we can
# refer to app models and perform DB syncs.
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'src.server',
    'src.players',
    'src.objects',
    'src.comms',
    'src.help',
    'src.scripts',
    'src.web.news',
    'src.web.website',)
# The user profile extends the User object with more functionality;
# This should usually not be changed.
AUTH_PROFILE_MODULE = "players.PlayerDB"
# Use a custom test runner that just tests Evennia-specific apps.
TEST_RUNNER = 'src.utils.test_utils.EvenniaTestSuiteRunner'

######################################################################
# Django extensions
######################################################################

# Django extesions are useful third-party tools that are not
# always included in the default django distro.
try:
    import django_extensions
    INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',)
except ImportError:
    pass
# South handles automatic database scheme migrations when evennia
# updates
try:
    import south
    INSTALLED_APPS = INSTALLED_APPS + ('south',)
except ImportError:
    pass

#######################################################################
# SECRET_KEY
#######################################################################
# This is the salt for account passwords. It is a fallback for the
# SECRET_KEY setting in settings.py, which is randomly seeded when
# settings.py is first created. If copying from here, make sure to
# change it!
SECRET_KEY = 'changeme!(*#&*($&*(#*(&SDFKJJKLS*(@#KJAS'
