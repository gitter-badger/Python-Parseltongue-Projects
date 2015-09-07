import time

bot_name = "Artha X"  # global name for the bot
bot_log = True  # enable logging (True/Fales)
bot_log_base = "logs/conversations/"  # Artha's log Base
bot_base = "knowledge-base/"  # Artha's Knowledge Base
bot_error_base = "logs/e-log/"  # Artha's Knowledge Base
must_files = ["lost", "confused", "intellect_keys", "intellect_values", "definition_keys", "definition_values"]
cmd = ""  # initialize command variable
bot_init = time.ctime(time.time())  # startup time
cur_time = time.ctime(time.time())  # curent time
