import json
def get_prefix(client, message):  ##first we define get_prefix
    with open('data/prefixes.json', 'r') as f:  ##we open and read the prefixes.json, assuming it's in the same file
        prefixes = json.load(f)  # load the json as prefixes
    return prefixes[str(message.guild.id)]  # recieve the prefix for the guild id given
