import time

bot_name = "Artha 1.0"  # global name for the bot
bot_version = "1.0.1"
bot_name_lower = bot_name.lower()
bot_log = True  # enable logging (True/Fales)
bot_log_base = "logs/conversations/"  # Artha's log Base
bot_base = "knowledge-base/"  # Artha's Knowledge Base
bot_sense_base = "knowledge-base/sensitive/"  # Artha's Sensitive Knowledge Base
bot_error_base = "logs/e-log/"  # Artha's Knowledge Base
must_files = ["greetings", "lost", "confused", "intellect_keys", "intellect_values"]
bot_parsing = {'#bot_name#': bot_name, '#bot_version#': bot_version}
cmd = ""  # initialize command variable
bot_init = time.ctime(time.time())  # startup time
cur_time = time.ctime(time.time())  # curent time
