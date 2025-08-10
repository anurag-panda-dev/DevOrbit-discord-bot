# DevOrbit_BOT - Discord Bot for DevOrbit Study Server
# Fill in your bot token below before running.

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DEVORBIT_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    channel = discord.utils.get(bot.get_all_channels(), name='general')
    if channel:
        await channel.send('DevOrbit_BOT is now online! Ready to help you study 🚀')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="🚀 DevOrbit_BOT Help",
        description="**Here are all the things I can do for you!**",
        color=0x2d2d7a
    )
    embed.set_author(name="DevOrbit_BOT", icon_url="https://cdn-icons-png.flaticon.com/512/3135/3135768.png")
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3135/3135768.png")
    embed.add_field(name="🆘 !help", value="Show this help message.", inline=False)
    embed.add_field(name="📚 !resources", value="Get useful study resources.", inline=False)
    embed.add_field(name="📅 !schedule", value="Show upcoming study sessions.", inline=False)
    embed.add_field(name="💡 !motivate", value="Get a motivational quote.", inline=False)
    embed.add_field(name="📜 !rules", value="Show the server rules.", inline=False)
    embed.add_field(name="ℹ️ !about", value="About DevOrbit_BOT.", inline=False)
    embed.add_field(name="🏓 !ping", value="Check bot latency.", inline=False)
    embed.add_field(name="📊 !poll", value="Create a quick poll.", inline=False)
    embed.add_field(name="⏰ !remind", value="Set a reminder.", inline=False)
    embed.add_field(name="🙋 !introduce", value="Introduce yourself to the server.", inline=False)
    embed.add_field(name="🏆 !leaderboard", value="Show the leaderboard.", inline=False)
    embed.add_field(name="👤 !user_info [@member]", value="Show info about a user (mention or leave blank for yourself).", inline=False)
    embed.add_field(name="🌐 !server_info", value="Show info about the server.", inline=False)
    embed.set_footer(text="DevOrbit Study Server • Stay curious! ✨")
    await ctx.send(embed=embed)

@bot.command()
async def resources(ctx):
    embed = discord.Embed(title="📚 Study Resources", color=0x2d2d7a)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3135/3135768.png")
    embed.add_field(name="🐍 Python", value="[Python Docs](https://docs.python.org/3/)", inline=False)
    embed.add_field(name="🌐 JavaScript", value="[MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)", inline=False)
    embed.add_field(name="📖 Data Structures & Algorithms", value="[GeeksforGeeks](https://www.geeksforgeeks.org/data-structures/)", inline=False)
    embed.add_field(name="🧩 LeetCode", value="[LeetCode](https://leetcode.com/)", inline=False)
    embed.add_field(name="🎓 FreeCodeCamp", value="[FreeCodeCamp](https://www.freecodecamp.org/)", inline=False)
    embed.set_footer(text="DevOrbit Study Server • Share your favorite resources!")
    await ctx.send(embed=embed)

@bot.command()
async def schedule(ctx):
    embed = discord.Embed(title="📅 Upcoming Study Sessions", color=0x2d2d7a)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3135/3135768.png")
    embed.add_field(name="Monday 7PM IST", value="🐍 Python Practice", inline=False)
    embed.add_field(name="Wednesday 7PM IST", value="🧮 DSA Workshop", inline=False)
    embed.add_field(name="Friday 7PM IST", value="🤝 Project Collaboration", inline=False)
    embed.set_footer(text="DevOrbit Study Server • Join the sessions and level up!")
    await ctx.send(embed=embed)

@bot.command()
async def motivate(ctx):
    import random
    quotes = [
        "🌟 Success is not the key to happiness. Happiness is the key to success.",
        "🚀 The secret of getting ahead is getting started.",
        "⏳ Don’t watch the clock; do what it does. Keep going.",
        "🔮 The future depends on what you do today.",
        "🔥 Push yourself, because no one else is going to do it for you."
    ]
    embed = discord.Embed(
        title="💡 Motivation Boost!",
        description=random.choice(quotes),
        color=0x2d2d7a
    )
    embed.set_footer(text="DevOrbit Study Server • You got this! 💪")
    await ctx.send(embed=embed)

@bot.command()
async def rules(ctx):
    embed = discord.Embed(title="📜 DevOrbit Server Rules", color=0xe74c3c)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3135/3135768.png")
    embed.add_field(name="1️⃣ Be Respectful", value="Treat everyone with respect. No harassment or hate speech.", inline=False)
    embed.add_field(name="2️⃣ Stay On Topic", value="Keep discussions relevant to study and tech.", inline=False)
    embed.add_field(name="3️⃣ No Spam", value="Avoid spamming messages or links.", inline=False)
    embed.add_field(name="4️⃣ Help Each Other", value="Support your fellow members!", inline=False)
    embed.set_footer(text="DevOrbit Study Server • Let’s keep it friendly and productive!")
    await ctx.send(embed=embed)

@bot.command()
async def about(ctx):
    embed = discord.Embed(
        title="🤖 About DevOrbit_BOT",
        description="I'm **DevOrbit_BOT**, your friendly study companion for the DevOrbit server!\n\nUse `!help` to see what I can do.\n\nLet's learn and grow together! 🚀",
        color=0x2d2d7a
    )
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3135/3135768.png")
    embed.set_footer(text="DevOrbit Study Server • Powered by Discord.py")
    await ctx.send(embed=embed)

# --- Additional Commands ---

@bot.command()
async def user_info(ctx, member: discord.Member = None):
    """Show info about a user. Usage: !user_info [@member]"""
    member = member or ctx.author
    embed = discord.Embed(
        title=f"👤 User Info: {member.display_name}",
        color=0x2d2d7a,
        timestamp=ctx.message.created_at
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.add_field(name="Username", value=str(member), inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime('%Y-%m-%d %H:%M'), inline=False)
    embed.add_field(name="Account Created", value=member.created_at.strftime('%Y-%m-%d %H:%M'), inline=False)
    embed.add_field(name="Top Role", value=member.top_role.mention, inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.display_name}")
    await ctx.send(embed=embed)

@bot.command()
async def server_info(ctx):
    """Show info about the server."""
    guild = ctx.guild
    embed = discord.Embed(
        title=f"🌐 Server Info: {guild.name}",
        color=0x2d2d7a,
        timestamp=ctx.message.created_at
    )
    embed.set_thumbnail(url=guild.icon.url if guild.icon else discord.Embed.Empty)
    embed.add_field(name="Server ID", value=guild.id, inline=True)
    embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="Created On", value=guild.created_at.strftime('%Y-%m-%d %H:%M'), inline=False)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.display_name}")
    await ctx.send(embed=embed)

# --- Welcome New Members ---
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='introductions')
    if channel is None:
        channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        embed = discord.Embed(
            title="🙋 Introduce Yourself!",
            description=f"👋 Welcome, {member.mention}!\n\nShare your interests, what you're learning, and your goals with the community!",
            color=0x2d2d7a
        )
        embed.set_footer(text="DevOrbit Study Server • We love meeting new members!")
        await channel.send(embed=embed)

@bot.command()
async def ping(ctx):
    """Check bot latency."""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Latency: `{latency}ms`",
        color=0x2d2d7a
    )
    embed.set_footer(text="DevOrbit_BOT • Always here for you!")
    await ctx.send(embed=embed)

@bot.command()
async def poll(ctx, *, question_and_options: str):
    """Create a quick poll. Usage: !poll Question | Option1 | Option2 | ..."""
    parts = [p.strip() for p in question_and_options.split('|')]
    if len(parts) < 3:
        await ctx.send('Usage: !poll Question | Option1 | Option2 | ...')
        return
    question = parts[0]
    options = parts[1:]
    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    if len(options) > len(emojis):
        await ctx.send('Max 10 options allowed.')
        return
    desc = '\n'.join(f'{emojis[i]} {opt}' for i, opt in enumerate(options))
    embed = discord.Embed(
        title=f'📊 {question}',
        description=desc,
        color=0x2d2d7a
    )
    embed.set_footer(text="DevOrbit Poll • Vote by reacting below!")
    msg = await ctx.send(embed=embed)
    for i in range(len(options)):
        await msg.add_reaction(emojis[i])

@bot.command()
async def remind(ctx, time: int, *, reminder: str):
    """Set a reminder. Usage: !remind <minutes> <reminder>"""
    embed = discord.Embed(
        title="⏰ Reminder Set!",
        description=f"I will remind you in **{time} minutes**: {reminder}",
        color=0x2d2d7a
    )
    embed.set_footer(text="DevOrbit_BOT • Stay on track!")
    await ctx.send(embed=embed)
    await discord.utils.sleep_until(discord.utils.utcnow() + discord.timedelta(minutes=time))
    await ctx.send(f'🔔 Reminder: {reminder} (set by {ctx.author.mention})')

@bot.command()
async def introduce(ctx):
    """Introduce yourself to the server."""
    embed = discord.Embed(
        title="🙋 Introduce Yourself!",
        description=f"👋 Welcome, {ctx.author.mention}!\n\nShare your interests, what you're learning, and your goals with the community!",
        color=0x2d2d7a
    )
    embed.set_footer(text="DevOrbit Study Server • We love meeting new members!")
    await ctx.send(embed=embed)

@bot.command()
async def leaderboard(ctx):
    """Show a mock leaderboard (customize for real data)."""
    embed = discord.Embed(title="🏆 DevOrbit Leaderboard", color=0x2d2d7a)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3135/3135768.png")
    embed.add_field(name="🥇 1. Alice", value="150 points", inline=False)
    embed.add_field(name="🥈 2. Bob", value="120 points", inline=False)
    embed.add_field(name="🥉 3. Charlie", value="100 points", inline=False)
    embed.set_footer(text="Participate in events to climb the leaderboard!")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    if not TOKEN:
        print("Please set your Discord bot token in the 'DEVORBIT_BOT_TOKEN' environment variable.")
    else:
        bot.run(TOKEN)
