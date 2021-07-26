import json
async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('data/levels.json', 'r') as g:
        levels = json.load(g)
        experience = users[f'{user.id}']['experience']
        lvl_start = users[f'{user.id}']['level']
        lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up!!! **LEVEL => {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end