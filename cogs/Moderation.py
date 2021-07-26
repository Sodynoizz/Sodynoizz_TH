import discord
from discord.ext import commands
from discord.ext.commands import Cog
import asyncio
class Moderation(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cancelled = False

    class DurationConverter(commands.Converter):
        async def convert(self, ctx, argument):
            amount = argument[:-1]
            unit = argument[-1]

            if amount.isdigit() and unit in ['s', 'n']:
                return (int(amount), unit)

            raise commands.BadArgument(message='Not a valid duration')

    @commands.command(brief="Ban member")
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')

    @commands.command(brief="Unban member")
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(f"Unbanned: {user.mention}")

    @commands.command(brief="Tempban member")
    @commands.has_permissions(manage_roles=True)
    async def tempban(self,ctx, member: commands.MemberConverter, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60}
        amount, unit = duration

        await ctx.guild.ban(member)
        await ctx.send(f"{member} has been banned for {amount}{unit}.")
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

    @commands.command(brief="Kick member")
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kick')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self,ctx, member: discord.Member, *, arg):
        logsChannel = self.bot.get_channel(843050417666916372)
        user = member.mention
        guild = ctx.guild
        embed = discord.Embed(title="Warning issued: ", color=0xf40000)
        embed.add_field(name="Warning: ", value=f'Reason: {arg}', inline=False)
        embed.add_field(name="User warned: ", value=f'{member.mention}', inline=False)
        embed.add_field(name="Warned by: ", value=f'{ctx.author}', inline=False)

        embed2 = discord.Embed(title="Warning issued: ", color=0xf40000)
        embed2.add_field(name="Warning: ", value=f'Reason: {arg}', inline=False)
        embed2.add_field(name="User warned: ", value=f'{member.mention}', inline=False)
        embed2.add_field(name="Warned by: ", value=f'{ctx.author}', inline=False)

        await logsChannel.send(embed=embed2)
        await member.send(f'You have been warned in {guild.name} for **{arg}**!')
        message = await ctx.send(embed=embed)

    @commands.command(pass_context=True, brief="Give @mention a role")
    async def giverole(self,ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

    @commands.command(name="deleterole", pass_context=True, brief="Delete a role")
    async def delete_role(self,ctx, role_name):
        # find role object
        role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
        # delete role
        await role_object.delete()

    @commands.command(aliases=['make_role'], brief="Create a role")
    @commands.has_permissions(manage_roles=True)
    async def createrole(self,ctx, *, name):
        guild = ctx.guild
        await guild.create_role(name=name)
        await ctx.send(f'Role `{name}` has been created')

    @commands.command(brief="Order the role")
    @commands.has_permissions(manage_roles=True)
    async def moverole(self,ctx, role: discord.Role, pos: int):
        try:
            await role.edit(position=pos)
            await ctx.send("Role moved.")
        except discord.Forbidden:
            await ctx.send("You do not have permission to do that")
        except discord.HTTPException:
            await ctx.send("Failed to move role")
        except discord.InvalidArgument:
            await ctx.send("Invalid argument")

    @commands.command(name='createchannel', brief="Create New Channel")
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def create_channel(self,ctx, channel_name='Sodynoizz'):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)
        await ctx.send(f"You have create channel name {channel_name}")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Moderation is ready")

def setup(bot):
    bot.add_cog(Moderation(bot))