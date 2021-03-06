import os, random, discord, sys, getopt, time
from dotenv import load_dotenv
from urllib.request import urlopen, Request
from discord.ext.commands import Bot
from discord.ext import commands
from mcstatus import MinecraftServer


load_dotenv()


def main(argv):
    client = discord.Client()

    # intents = discord.Intents().all()

    bot = commands.Bot(command_prefix="t!")

    TOKEN = 'ODIwNDM1MDI5MTI5ODIyMjk4.YE1HqQ.0Vb-fPc_-QxXMX2dwvGqVfuUDTM'

    print(TOKEN)
  #  print('please error') (debug)

    @client.event
    async def on_ready():
      #  print('made it to client.event') (debug)
        await client.change_presence(activity=discord.Game('with kick commands lmao | t!help'))
        print("We have logged  in as {}".format(client))

    @client.event
    async def on_message(message):
       # print('made it to on_message') (for debug)


##        if message.content.startswith('t!numberguess'):
##            player = message.author
##            def check(m):
##                print('checking new message')
##                return message.content.startswith('yes') and m .author == player
##            print(player)
##            await message.channel.send('Discord, yes or no?')
##            msg = await client.wait_for('message', check = check, timeout=60)
##            await message.channel.send('poopybutt -d')
    #@bot.command()
    #async def join(ctx):
        #channel = ctx.author.voice.channel
        #await channel.connect()
    #@bot.command()
        #async def leave(ctx):
        #await ctx.voice_client.disconnect()

    #    if message.content == 't!check':
        #    for member in ctx.guild.members:
        #        id = member.id
            #    await message.channel.send(id)

    #    if message.content == 't!kick {discord.User}':
            #@client.command()
        #    @client.command.has_permissions(administrator=True)
            #async def kick(ctx, member: discord.Member):
                #await log_channel.send(f"{ctx.author.name} has kicked {member.display_name}")
                #doing respond thing when you dont have admin
##@client.command()
##elif @client.command.has_permissions(administrator=False):
    ##await message.channel.send("You need to be an admin to use this command")




        if message.content == 't!help':
            info = discord.Embed(title="Commands list:",  description="All existing commands", color=0x28e038)
            info.add_field(name=":star_struck:`t!inspiration`", value="makes you go :O", inline=False)
            info.add_field(name=":1234:`t!randommath`", value="random math. adds numbers -45000-45000", inline=True)
            info.add_field(name=":thinking:`t!randomquotes`", value="random quotes, made by yours truly", inline=True)
            info.add_field(name=":ab:`t!cvf y=mx+b`", value="replace y=mx+b with numbers (Don't make y or x a number, and don't add spaces)", inline=False)
            info.add_field(name=":ping_pong:`t!ping`", value="would send the time it takes to run the code but it doeSNT WORK", inline=False)
            info.set_footer(text='[sumbit ideas and issues](https://github.com/zTheroy/theroy-discord-bot/issues)')
            await message.channel.send(embed=info)

        if message.content == 't!randomquotes':
            response = random.choice(random_quotes)

            await message.channel.send(response)
        if message.content == 't!randommath':
            lst = ['+', '-', '*', '/']
            math_embed = discord.Embed(title="math", description="math answer", color=0x11d43b)
            x = random.randint(-45000,45000)
            y = random.randint(-45000,45000)
            random_operator=random.randint(0,len(lst)-1)
            if lst[random_operator] == '+':
                answer = x + y
                math_output = '{} + {} = {}'.format(x,y,answer)
            elif lst[random_operator] == '-':
                answer = x - y
                math_output = '{} - {} = {}'.format(x,y,answer)
            elif lst[random_operator] == '*':
                answer = x * y
                math_output = '{} * {} = {}'.format(x,y,answer)
            elif lst[random_operator] == '/':
                answer = x / y
                math_output = '{} / {} = {}'.format(x,y,answer)
            elif x < 0 and y < 0 and lst[random_operator] == '-':
                y = abs(y)
                answer = x + y
                math_output = '{} + {} = {}'.format(x,y,answer)
                print(y)
            math_embed.add_field(name="oh my god its your math answer", value=math_output, inline=False)
            await message.channel.send(embed=math_embed)

        if message.content == 't!inspiration':
            random_quote = Request('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?', headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(random_quote)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            #print(html)
            html = html.split(":")
            inspiration = html[1].split("quoteAuthor")
            inspiration = inspiration[0]
            inspiration = inspiration[:-3]
            await message.channel.send(inspiration)



        if message.content.startswith('t!cvf'):
            message_content = message.content.split()
            arg = message_content[1]
            lst = arg.split("=")
            for x in lst:
                if "+" in x:
                    y = lst[0]
                    temp=lst[1].split("+")
                    mx = temp[0]
                    answer = temp[1]
                elif "-" in x:
                    y = lst[0]
                    temp=lst[1].split("-")
                    mx = temp[0]
                    answer = temp[1]
            if "+" in arg:
                cvf_answer="Youre ansswer do be: {} - {} = {} :flushed:".format(mx, y, answer)
            else:
                cvf_answer="Youre ansssswer do be: {} + {} = {} :flushed:".format(mx, y, answer)
            await message.channel.send(cvf_answer)




        if message.content.startswith('t!ping'):
            start = time.time()
            latency = message.channel.created_at
            end = time.time()
            execution_time = end - start
            #embedding execution time and latency under
            ping_title = discord.Embed(title="pong :ping_pong:",color=0x005ef5)
            ping_title.add_field(name="Execution Time", value=(f"{execution_time} seconds"), inline=False)
            ping_title.add_field(name="Latency", value=str(round(client.latency*1000))+" ms", inline=False)
            await message.channel.send(embed=ping_title)



            server = MinecraftServer.lookup("73.72.30.138:5000")

            # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
            status = server.status()
            print(f"The server has {status.players.online} players and replied in {status.latency} ms")

            # 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
            # It is included in a 'status' call, but is also exposed separate if you do not require the additional info.
            latency = server.ping()
            print(f"The server replied in {latency} ms")

            # 'query' has to be enabled in a servers' server.properties file!
            # It may give more information than a ping, such as a full player list or mod information.
            query = server.query()
            print(f"The server has the following players online: {', '.join(query.players.names)}")

    client.run(TOKEN)
if __name__ == "__main__":
    main(sys.argv[1:])
