import discord
from discord.ext import commands
import random
import asyncio
import randoms
import os
import io
import re
import time
import youtube_dll
import discord.ext.commands
import requests
import .json
import datetime
from io import BytsIO
from PIL import Image, ImageDraw, ImageFont, ImageOps

players = {}
config = None

DEIN_USERNAME = "DEINE_USER_ID"

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto

    token = secreto.seu_token()

verde = 0x00FF00
azul = 0x0000FF
vermelho = 0xFF0000
amarelo = 0xFFFF00
roxo = 0x690FC3
msg_id = None
msg_user = None


@client.event
async def on_ready():
    print('BOT ONLINE')
    print(client.user.name)
    print(client.user.id)
    print('https://discord.gg/CmszJUV')

async def up_time():
    await client.wait_until_ready()
    global days
    days = 0
    global minutes
    minutes = 0
    global hour
    hour = 0
    global seconds
    seconds = 0
    while client._is_ready:
        await asyncio.sleep(1)
        seconds += 1
        if hour == 24:
            hour = 0
            days += 1
        if minutes == 60:
            minutes = 0
            hour += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
client.loop.create_task(up_time())



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith("zhelp"):
        if message.author.id in blacklist:
                await client.send_message(message.channel, "{}, Você foi banido da minha vida\nNunca mais poderá usar meus comandos ;-;".format(message.author.mention))
                return
    if message.author.id in blacklist:
        return

    user_id = message.author.id

 #   if message.content.lower().startswith('zzueiro-logs'):
  #      server = message.server
   #     await client.create_channel(server, 'zueiro-logs', type=discord.ChannelType.text)

    if message.content.startswith('zpresence') and message.author.id == "320339126601777152":
        game = message.content[9:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Cóe criador, mudei minha presence para:\n **Jogando** " + game + "")

    if message.content.startswith('zlistadevips'):
        if not message.author.id == '320339126601777152':
            return await client.send_message(message.channel, '**Permissão insuficiente**')
        try:
            mencionar = []
            for ids in listadevips:
                member = '<@{}>'.format(ids)
                mencionar.append(member)
            await client.send_message(message.channel, ' '.join(mencionar))
        except:
            await client.send_message(message.channel, "Deu erro, filhão")

    if message.content.lower().startswith('zss'):
        user = message.author.mention
        sserro1 = message.content[4:]
        fraseerross = "\n**Não foi encontrado uma resposta para** `{}`**,** \npor favor adicione uma com o comando abaixo: \n `zADDss <pergunta>`".format(sserro1)
        try:
            simsimi1 = message.content[:]
            simsimiapi = requests.get(
                'https://dogewebsite.glitch.me/api/v1/responses/get-question&question=' + simsimi1 + '')
            simsimiapi1 = json.loads(simsimiapi.text)
            statussimsimi = simsimiapi1['code']
            respostasimsimi = simsimiapi1['response']
            xxxsimsimi = "{}, {}".format(user, respostasimsimi)
            await client.send_message(messagechannel, xxxsimsimi.replace("Não encontrado!", fraseerross))
        except:
            simsimierro = await client.send_message(message.channel, "Buguei")

    if message.content.lower().startswith('zaddss'):
        user = message.author.mention
        try:
            addquestss = message.content[7:]
            def check(msg):
                return msg.content.startswith('')
            await client.send_message(message.channel, "O que eu devo responder quando disserem:\n `{}` ?".format(addquestss))
            message = await client.wait_for_message(author=message.author, check=check)
            addrespss = message.content[len(''):].strip()
            addsimsimiapi = requests.get(
                'https://dogewebsite.glitch.me/api/v1/responses/set-response&question=' + addquestss + '&answer=' + addrespss + '')
            addsimsimiapi1 = json.loads(addsimsimiapi.text)
            addrespostasimsimi = addsimsimiapi1['response']
            simsimiaddsucess = "Sucesso <3 Agora quando me disserem `{}`, eu direi `{}`".format(addquestss, addrespss)
            xxxsimsimi = "{}, {}".format(user, addrespostasimsimi)
            await client.send_message(message.channel, xxxsimsimi.replace("Sucesso!", simsimiaddsucess))
        except:
            await client.send_message(message.channel, "Buguei")

    if message.content.lower().startswith("z?eval"):
         if not message.author.id == '320339126601777152':
            return await client.send_message(message.channel, '**Permissão insuficiente**')
         try:
            embedeval1 = discord.Embed(title='\n', description='\n')
            embedeval1.add_field(name='**:inbox_tray: Entrada**', value='```py\n' + message.content[7:] + '```')
            embedeval1.add_field(name='**:outbox_tray: Saída**', value='```py\n' + str(eval(message.content[7:])) + '```')
            eval1 = await client.send_message(message.channel, embed=embedeval1)
            await client.add_reaction(eval1, "☑")
            await client.add_reaction(eval1, "🗑")
            await client.wait_for_reaction(message=eval1, user=message.author, emoji="🗑")
            await client.delete_message(eval1)
            await client.delete_message(message)

         except Exception as e:
            embedeval = discord.Embed(title='\n', description='\n')
            embedeval.add_field(name='**:inbox_tray: Entrada**', value='```py\n' + message.content[7:] + '```')
            embedeval.add_field(name='**:outbox_tray: Saída**', value='```py\n' + repr(e) + '```')
            eval2 = await client.send_message(message.channel, embed=embedeval)
            await client.add_reaction(eval2, "❎")
            await client.add_reaction(eval2, "🗑")
            await client.wait_for_reaction(message=eval2, user=message.author, emoji="🗑")
            await client.delete_message(eval2)
            await client.delete_message(message)

    if message.content.lower().startswith("z!eval"):
         if not message.author.id == '320339126601777152':
            return await client.send_message(message.channel, '**Permissão insuficiente**')
         try:
            embedeval1 = '' + str(eval(message.content[7:])) + ''
            eval1 = await client.send_message(message.channel, embedeval1)
            await client.add_reaction(eval1, "☑")
            await client.add_reaction(eval1, "🗑")
            await client.wait_for_reaction(message=eval1, user=message.author, emoji="🗑")
            await client.delete_message(eval1)
            await client.delete_message(message)

         except Exception as e:
            embedeval = '' + repr(e) + ''
            eval2 = await client.send_message(message.channel, embedeval)
            await client.add_reaction(eval2, "❎")
            await client.add_reaction(eval2, "🗑")
            await client.wait_for_reaction(message=eval2, user=message.author, emoji="🗑")
            await client.delete_message(eval2)
            await client.delete_message(message)

    if message.content.lower().startswith("zconvite"):
        invitelinknew = await client.create_invite(destination = message.channel, unique = True)
        embedMsginv=diord.Embed(color=message.author.color)
        embedMsginv.add_field(name="Convite para o servidor {}".format(message.server.name), value=invitelinknew)
        embedMsginv.set_footer(text="#Convide seus amigos")
        await client.send_message(message.channel, embed=embedMsginv)

    if message.content.lower().startswith('zban'):
        if not message.author.server_permissions.ban_members:
            user = message.mentions[0
            author = message.author
            embkickx = discord.Embed(color=amarelo)
            embkickx.add_field(name="Alá `{}`, o `{}` tentu te banir sem ser ADM".format(user, author), value="<a:zueiroanonimobotemoji:440504316613230592>")
            embkickx.set_image(url='https://media.discordapp.net/attachments/440679680530710560/442450061004111874/unknown.png?width=459&height=248')
            embkickx.set_footer(text='Vacilão morre cedo')
            return await client.send_message(message.channel, embed=embkickx)
        try
            author = message.author
            user = message.mentions[0]
            embkickx = discord.Embd(color=author.color)
            embkick2x.add_field(name="<a:zueiroanonimobotemoji:440504316613230592> **EXPULSÃO**",
                              value="**Usuário bando:** {} \n"
                                    "**Comando realizado por:** {} \n"
                                    ".format(user, author)
                              )
            embkick2x.set_thumbnail(url=user.avatar_url)
            embkick2x.se_footer(text="ID = {}".format(user.id))
            await clent.ban(membr=user)
            return await client.send_message(message.channel,embed=embkick2x)
        except discord.errors.Forbidden:
            author = message.auho
            embkick3x= discord.Embed(color=amarelo)
            embkck3x.add_field(name=Eu bair alguém de cargo mais alto que o meu ? kkk tu sonha demais {}".format(author), value="<a:zueiroanonimobotemoji:440504316613230592>")
            embkick3x.set_image(url='https://pbs.twim.com/media/C4aWOX8XAAI9MX7.jpg')
            embkick3x.set_footr(text='PS: Assim tu me fode mano')
            return await client.send_mesage(message.cannel, embed=embkick3x)
        except:
            return await client.send_message(message.channel, "Você deve especificar um usuário para banir, baby")

    if message.content.lower().startswith('zkick'):
        if not message.author.server_permissions.kick_members:
            user = message.mentions[0]
            author = message.author
            embkick = discord.Embed(color=amarelo)
            embkick.add_field(name="Alá `{}`, o `{}` tentou te kikar sem ser ADM".format(user, author), value="<a:zueiroanonimobotemoji:440504316613230592>")
            embkick.set_image(url='https://media.discordapp.net/attachments/440679680530710560/442450061004111874/unknown.png?width=459&height=248')
            embkick.set_footer(text='Vacilão morre cedo')
            return await client.send_message(message.channel, embed=embkick)
        try:
            author = message.author
            user = message.mentions[0]
            embkick2 = discord.Embed(color=author.color)
            embkick2.add_field(name="<a:zueiroanonimobotemoji:440504316613230592> **EXPULSÃO**",
                              value="**Usuário expulso:** {} \n"
                                    "**Comando realizado por:** {} \n"
                                    "".format(user, author)
                              )
            embkick2.set_thumbnail(url=user.avatar_url)
            embkick2.set_footer(text="ID = {}".format(user.id))
            await client.kick(member=user)
            return await client.send_message(message.channel,embed=embkick2)
        except discord.errors.Forbidden:
            author = message.author
            embkick3 = discord.Embed(color=amarelo)
            embkick3.add_field(name="Eu expulsar alguém de cargo mais alto que o meu ? kkk tu sonha demais {}".format(author), value="<a:zueiroanonimobotemoji:440504316613230592>")
            embkick3.set_image(url='https://pbs.twimg.com/media/C4aWOX8XAAI9MX7.jpg')
            embkick3.set_footer(text='PS: Assim tu me fode mano')
            return await client.send_message(message.channel, embed=embkick3)
        except:
            return await client.send_message(message.channel, "Você deve especificar um usuário para expulsar, baby")

    if message.content.lower().startswith('zsugestao'):
        try:
            inviteforsup = await client.create_invite(destination=message.channel, unique=True)
            canalsuges = discord.utils.get(client.get_all_channels(), id='437736462843248651')
            shaiderwow = dage.content[9:]
            user = message.author
            emb title='Nova sgestão de {}'.format(
                    user.name),
                color=user.colrname='<:zueiroanonimosafadinho:438472983942660097>  Sugestão proposta:', value=sugestao1)
            embsuges.add_field(name="<a:zueiroanonimobotemoji:440504316613230592> Informações do usuário que enviou a sugestão <a:zueiroanonimobotemoji:440504316613230592>",
                            value="**Nome**: {} \n"
                            "**Apelido no seu server**: {} \n"
                            "**Seu ID**: {} \n"
                            "**Tag**: {} \n"
                            "**Enviada através do server**: {
 sobre o BOT! nada mais")
            await client.send_message(shaiderwow, embed=embsuges)
            await client.send_messagee(message.channel, 'Sua sugestão foi enviada para o servidor de suporte :3')
            await client.send_message(canalsuges, embed=embsuges)
        except:
            await client.send_message(message.channel, 'Desculpe, não entendi')

    if message.content.lower().startswith('zcsgo'):
        user = message.author
        try:
            csgo1 = message.content[6:]
            csgoname = requests.get(
                'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamids=' + csgo1 + '&format=json')
            csgo2 = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamid=' + csgo1 + '&l=br')
            csgoloads1 = json.loads(csgo2.text)
            csgoloads2 = json.loads(csgoname.text)
            namecsgo = csgoloads2['response']['players'][0]['personaname']
            killscsgo = csgoloads1['playerstats']['stats'][0]['value']#['total_kills']
            deathcsgo = csgoloads1['playerstats']['stats'][1]['value']#['total_deaths']
            plantacsgo = csgoloads1['playerstats']['stats'][3]['value']#['total_planted_bombs']
            defusecsgo = csgoloads1['playerstats']['stats'][4]['value']#['total_defused_bombs']
            tempocsgo = csgoloads1['playerstats']['stats'][2]['value']#['total_time_played']
            win

            embedcsgo = discord.Embed(color=user.color)
            embedcsgo.add_field(name='<:prsoncs:439190430924668939> Informações da conta <:personcs:439190430924668939>',
                                value="<:globalcsgo:439190468337598474> **Nick Atual:** {} <:globalcsgo:439190468337598474>\n"
                                      "<:miracsgo:439190488780898315> **Total de Kills:** {}           <:armacsgo:439190272413532160> **Total de mortes:** {} \n"
                                      "<:trcsgo:439190365980065792> **Bombas plantadas:** {}           <:ctcsgo:439190338364768256> **Bombas defusadas:** {} \n"
                                      "<:a_csgo:43919038710956544> **Money ganho em partidas:** ${} \n"
                                      "<:x_csgo:439190408686469120> **Total de tempo jogado:** `Estamos com problemas nesta parte ainda` \n"
                                      "".format(namecsgo, killscsgo, deathcsgo, plantacsgo, defusecsgo, winscsgo, moneycsgo)
                                )
            embedcsgo.set_thumbnail(url=thumbcsgo)
            embedcsgo.set_footer(text="Seus Frags ultrapassam a barreira do -4")
            await                   "Exemplo: `zCSGO 76561198168296588`\n"
                                                  "Não sabe sua ID ? Acesse: `steamidfinder.com`\n"
                                                  "`Obs. Seu ID será o steamID64`\n"
                                                  "**Clique na lixeira para excluir esta mensagem**")
            await client.add_reaction(zzsteamid, "🗑")
            await client.delete_message(zzsteamid)
    if message.content.lnse']['players'][0]['profileurl']
            avatarste = steesponse']['games'][2]['name']
          #  recent4ste = steamload3['response']['games'][3]['name']

            embedsteam = discord.Embed(color=user.color)
            embedsteam.add_field(
                name='<a:zueiroanonimobotemoji:440504
                      "format(nomeste, jogosste, time.strftime("%d/%m/%Y às %H:%M", time.localtime(temposte)), time.strftime("%d/%m/%Y às %H:%M", time.localtime(ulonlineste)), recent1ste, linkste)
            )
            embedsteam.set_thumbnail(url=avatarste)
            embedsteam.set_footer(text='#ZueiroAnonimoJogaNaSteam')
            await client.send_message(message.channel, embed=embedsteam)
        except KeyError:
            steam1priv = message.content[7:
            steam2priv = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamids=' + steam1 + '&format=json')
            steamload1priv = json.loads(steam2priv.text)
            nomestepriv = steamload1priv['response']['players'][0]['personaname']
        #    idstepriv = steamload1priv['response']['players'][0]['steamid']
            linkstepriv = steamload1priv['response']['players'][0]['profileurl']
            avatarstepriv = steamload1priv['response']['players'][0]['avatarfull']

            embedsteampriv = discord.Embed(color=user.color)
            embedsteampriv.add_field(
                name=' Aqui está a conta Steam que pediu, {}'.format(user.name),
                value="**Nick:** {} \n"
                      "**Link do perfil:** \n {} \n"
                      "`Este perfil possui áreas privadas, não consigo mostrar mais informações`"
                      "".format(nomestepriv, linkstepriv)
            )
            embeddsteampriv.set_footer(text='#ZueiroAnonimoJogaNaSteam')
            await client.send_message(message.channel, embed=embedsteampriv)
        except json.decoder.JSONDecodeError:
            await asyncio.sleep(1)
            zzsteamid = await client.send_message(message.channel,
                                                  "Olá, os comandos `zSteam` e `zCSGO` funcionam somente com o seu ID Steam\n"
                                               "`Obs. Seu ID será o steamID64`\n"
                                                  "**Clique na lixeira para excluir esta mensagem**")
            await client.add_reaction(zzsteamid, "🗑")
            await client.wait_for_reaction(message=zzsteamid, user=message.author, emoji="🗑")
            await client.delete_message(zzsteamid)

        try:
            movie1 = message.content[7:]
            movie2 = requests.get('https://api.themoviedb.org/3/search/movie?apa196865d5&language=pt-br&query=' + movie1 + '/')
            movie = json.loads(movie2.text)
            nomemovie = (movie['results'][0]['title'])
            nomeorigmovie = (movie['results'][0]['original_title'])
            sinopsemovie = (movie['results'][0]['overview'])
            datamovie = (movie['results'][0]['release_date'])
            languagemvie = (mesults'][0]['vote_average'])
            postermovie = (movie['results'][0]['poster_path'])


            embedfilm = discord.Embed(color=user.color)
            embedfilm.add_field(name='<a:zueiroanonimobotemoji:440504316613230592> Aqui está o filme 10 barra 10 que pediu, {}'.format(user.name),
                               value="🎬 **Filme:** {} \n"
                                     "** Nome Original:** {} 🎬\n"
                                     "📆 nguagem original:** {} \n
                                     "🔢 **Nota:** {} \n"
                                     "🌍 **Sinopse:** {} \n" 
                                     "".format(nomemovie, nomeorigmovie, datamovie, languagemovie, imdbmovie, sinopsemovie)
                               )/p/w600_and_h900_bestv2' + postermovie)
            embedfilm.set_footer(text="#ZueiroAninomoVirouCinéfolo")
            await client.send_message(message.channel, embed=embedfilm)
        except
            await client.send_message(message.channel, "Putz grila Nilce, não consegui encontrar o filme!  :C")

    if message.content.lower().startswith('zserie'):
        user = message.author
        try:
            serie1 = message.content[7:]
            serie2 = requests.get('https://api.themoviedb.org/3/search/tv?api_key=d9f2dc02f23bb44860dbb5fa196865d5&language=pt-br&query=' + serie1 + '/')
            serie = json.loads(serie2.text)
            nomeserie = (serie['results'][0]['name'])
            nomeorigserie = (serie['results'][0]['original_name'])
            sinopseserie = (serie['results'][0]['overview'])
            dataserie = (serie['results'][0]['first_air_date'])
            langageserie = (serie['results'][0]['original_language'])
            imdb = discord.Embed(color=user.color)
            embedserie.add_field(name='<a:zueiroanonimobotemoji:440504316613230592> Aqui está a série 10 barra 10 que pediu, {}'.format(user.name),
                               value="🎬 **Série:** {} \n"
                                     "** Nome Original:** {} 🎬\n"
                                     "📆 **Data do 1° episódio:** {} \n"
                                     "👅 **Linguagem original:** {} \n"
                                     "🔢 **Nota:** {} \n
                                     "🌍 **Sinopse:** {} \n" 
                     ed=embedserie)
        except:
            await client.send_message(message.channel, "Putz grila Nilce, no
    if message.content.lower().startswith('zzztoc4r'):
        #role = discord.utils.get(message.server.roles, name='DJ')
        #if not role in message.author.roles:
        #    return await client.send_message(message.channel, "💽``É necessário o cargo DJ para executar este comando!``")
        link = message.content[9:]
        voice = client.voice_client_in(message.server)
        player = await voice.create_ytdl_player("ytsearch:{}".format(link))
        player.start()
        await client.send_message(message.channel, "💽``Tocando agora: {}``".format(player.title))

    if message.content.startswith('ztist'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('zsleep'):
        await asyncio.sleep(5)
        await client.send_mess
##############################BOT MUSIC##################################
    if message.content.startswith('zzzentr4r'):
      try:
        canal = message.author.voicgument:
             await client.send_message(message.channel, "Tu acha que eu vou advinhar em qual canal de voz entrar ? entra nele primeiro, depois me chama!")

    if message.content.startswith('zzzs4ir'):
      try:
      except AttributeError:
          await client.send_message(message.channel,"Tu ta me vendo eu algum canal de voz ???? ENTÃO NÃO ME PEDE PRA SAIR!")
    #if message.content.startswith('zplay ')
     #   yt_url = message.content[6:]
      #  channel = message.author.voice.voice_channel
       # voice = await client.join_voice_channel(channel)
        #await voice.create_ytdl_player(yt_url)
    if message.contnt.startswith('zzzpl4y'):
            link = message.content[8:]
            canal = message.author.voice.voice_channel
            voice = await client.join_voice_channel(canal)
            player = await voice.create_ytdl_player(link)
            player.start()bed(
                title=":headphones: Tocando agora : {0}".format(player.title),
                colour=azul,
                descripition='\n'/i.pinimg.com/originals/a7/28/a7/a728a76e57ef17416040dd45a6548845.png%27')
            embedmusic.add_field(name='Duração', value='{} segundos'.format(player.duration))
            embedmusic.add_field(name="Música requisitada por", value='{}'.format(message.author.name))
            await client.send_message(message.channel, edmusic)
######
    if message.content.lower().startswith('zbotslabnegro'):
        user = message.author
        emblabneg1 = discord.Embed(
            title='{}, aqui estão algumas info de nossos BOTS em Python'.format(message.author.name),
            color=user.color,
            description='✅ = Informações completas\n❌ = Informações incompletas\n \n'
                        '✅**Nome do bot:** Deku#5579, '
                '**Id do bot:** 426889239318364170, '
                '**Dono do bot:** Diego#8505, '
                '**Id do dono:** 348920758623272960, '
                '**Link pra invite:** https://goo.gl/u28a1h, '
                '**LP:** Python, '
                '**Prefixo:** `-` \n'
               '**Dono do bot:** Diego#8505, '
                '**Id do dono:** 348920758623272960, '
                '**Link pra invite:** http://swifttopia.com/6870268/botepjack, '
                '**LP:** Python, '
                '**Prefixo:** `&` \n'
                '✅**Nome do bot:** Pythozinho#0053, '
                '**Id dobot:** 420703371918442499, '
                '**Dono do bot:** Vagner#1735, '
                '**Id do dono:** 232309115865661440, '
                '**Link pra invite:** https:/
                '**Prefixo:** `?` \n'
                '✅**Nome do bot:** LoriS#9246, '
                '**Id do dono:** 369962464613367811, '
                '**Link pra invite:** bit.ly/LoriSBOT, '
                '**LP:** Python, '
                '**Prefixo:** `L!` \n'
                '✅**Nome do bot:** Zueiro Anonimo#9641, '
                '**Id do bot:** 421862224454221824, '
                '**Dono do bot:** SHAIDERWOW#6701, '
                '**Id do dono:** 320339126601777152, '
                '**Link pra invite:** http://swifttopia.com/6870268/zueiroanonimo, '
                '**LP:** Python, '
                '**Prefixo:** `z` \n'
        )
        emblabneg2 = discord.Embed(
            title=None,
            color=user.color,
            description='✅**Nome do bot:** Beagle!#3110, '
                '**Id do bot:** 431517427147472936, '
                '**Dono do bot:** oCyberBR#5963 , '
                '**Id do dono:** 409318688895008768, '
                '**Link pra invite:** http://swifttopia.com/6870268/botbeagle, '
                '**LP:** Python, '
                '**Prefixo:** `b?` \n' 
                '✅**Nome do bot:** Joder#7480, '
                '**Id do bot:** 416669469050404865, '
                '**Dono do bot:** Kaigo#5682, '
                '**Id do dono:** 380441229416071170, '
                '**Link pra invite:** https://bit.ly/Joder, '
                '**LP:** Python, '
                '**Prefixo:** `jd_` \n' 
                '❌**Nome do bot:** Sesshomaru#9401, '
                '**Id do bot:** 425670256741187604, '
                '**Dono do bot:** Vagner#1735, '
                '**Id do dono:** 232309115865661440, '
                '**Link pra invite:** ?????, '
                '**LP:** Python, '
                '**Prefixo:** `s!` \n' 
                '✅**Nome do bot:** Hullo!!#2613, '
                '**Id do bot:** 431800868585865219, '
                '**Dono do bot:** Ph4#3931, '
                '**Id do dono:** 369962464613367811, '
                '**Link pra invite:** bit.ly/HulloBOT, '
                '**LP:** Python, '
                '**Prefixo:** `!!` \n' 
                '✅**Nome do bot:** Wanted#6346, '
                '**Id do bot:** 429376853162197002, '
                '**Dono do bot:** IamEduardo#6790, '
                '**Id do dono:** 319253966586118146, '
                '**Link pra invite:** http://swifttopia.com/6870268/botwanted, '
                '**LP:** Python, '
                '**Prefixo:** `w!` \n'
        )
        emblabneg3 = discord.Embed(
            title=None,
            color=user.color,
            description='✅**Nome do bot:** Zero#0561, '
                '**Id do bot:** 410173139084115968, '
                '**Dono do bot:** ◤LUCAS◥#5146, '
                '**Id do dono:** 302148993688010752, '
                '**Link pra invite:** https://goo.gl/9nECqp, '
                '**LP:** Python, '
                '**Prefixo:** `.` \n' 
                '✅**Nome do bot:** Shelect#7633, '
                '**Id do bot:** 414639245932756992, '
                '**Dono do bot:** yNerdSz.py 🔥#2937, '
                '**Id do dono:** 326513443693920266, '
                '**Link pra invite:** http://swifttopia.com/6870268/botshelect, '
                '**LP:** Python, '
                '**Prefixo:** `sh!` \n' 
                '❌**Nome do bot:** GeniusesBot#4849, '
                '**Id do bot:** 429022581614444553, '
                '**Dono do bot:** Dono#1090, '
                '**Id do dono:** ?????, '
                '**Link pra invite:** http://swifttopia.com/6870268/botgenuis, '
                '**LP:** Python, '
                '**Prefixo:** `?` \n' 
                '✅**Nome do bot:** Rafaela#2740, '
                '**Id do bot:** 428321055539462145, '
                '**Dono do bot:** yFunnyBr Lira#3629, '
                '**Id do dono:** 264101569333559297, '
                '**Link pra invite:** http://swifttopia.com/6870268/botrafaela, '
                '**LP:** Python, '
                '**Prefixo:** `.` \n'
        )
        emblabneg3.set_footer(text="Todas as informações foram pegas em: https://h4rt3ck.wixsite.com/apocryphos/forum/programacao/_bots")
        await client.send_message(message.channel, embed=emblabneg1)
        await client.send_message(message.channel, embed=emblabneg2)
        await clint.send_message(message.channel, embed=emblabneg3)
    ##################################################################################
    ###################################BOTS DO LAB###########################################
    #LoriShor
        embtestmarc = discord.Embed(
            title='<:python:419662789997756419> Reação da LoriS ao ver sua marcação, {}'.format(message.author.name),
            color=user.color,
            descriptino="VACILÃO MORRE CEDO",
        )end_message(message.channel, embed=embtestmarc)
    #ZERO
    if message.content.lower().startswith('<@410173139084115968>'):
        user = message.author
        embtestmarc1 = discord.Embed(O",
        )
        embtestmarc1.set_image(
            url='https://media.discordapp.net/attachments/425866379921719297/428576974005338117/Izuku_Midoriya.png?width=589&height=431')
        testmarc11 = await client.send_message(message.channel, embed=embtestmarc1)

    if message.content.lower().startswith('<@426745809833295872>')
        user = message.author
        embtestmarc2 = discord.Embed(
        color=user.color,
            descriptino="VACILÃO MORRE CEDO",
        )
        embtestmarc.set_image(
            url='https://i.pinimg.com/originals/d0/e0/1c/d0e01cae1613414eff5e5091ac09b934.jpg')
        testmarc1 = await client.send_message(message.channel, embed=embtestmarc2)
    ###############################
    if message.content.lower().startswith('z.py'):
        usermsgcod = message.content[4:]
        try:
            await client.send_message(message.channel,'<:python:426890674256740384> {} enviou o segunte código:\n```python\n{} \n```'.format(message.author.mention, usermsgcod))
            await client.delete_message(message
        except:
            await client.send_message(message.channel, 'Esqueceu de por o código, bb.')

    if message.content.lower().startswith('zhelp'):
            embhelp3 = discord.Embed(title="Não tema! Sua ajuda chegou", color=user.color,
                                     description="Não se preocupe, não somos igual a Correios, a lista de comandos já foi entregue em seu privado."
                                    )
            embhelp3.add_field(name="Abaixo está meu site, sinta-se livre em compartilha-lo para sua família ❤",
                               value="https://zueiro-anonimo.glitch.me \n `breve mais coisas no site`")
            embhelp3.set_thumbnail(url="https://cdn.discordapp.com/emojis/440504316613230592.gif")
            embhelp3.set_footer(icon_url=user.avatar_url, text="Comando utilizado por {}".format(user.name))
            #ed(title='<a:zueiroanonimobotemoji:440504316613230592> Olá, {}. <a:zueiroanonimobotemoji:440504316613230592>'.format(message.author.name), color=user.color,
                                  description='No momento ainda não estou pronto, porém, posso lhe servir em algumas coisas.\n'
                                              '\n'
                                              '<a:zueiroanonimobotemoji:440504316613230592>**Comandos públicos**<a:zueiroanonimobotemoji:440504316613230592>\n'
                                              '\n'
                                              '**zHel`<mensagem>` :** Faz uma votação por reactions.\n'
                                              '**zAvatar :** Mostra o avatar do usuário mencionado ou do seu.\n'
                                              '**zServerinfo :** Mostra as informações do servidor.\n'
                                              '**zBotinfo :** Mostra algumas informações sobre mim.\n'
                                              '**zUserinfo :** Mostra asformações do usuário mencionado ou as suas.\n'
                                              '**zGpsteam : **Mostra o meu grupo da Stem.\n'
                                              '**zSteam `<ID da conta>`:** **Eu lhe mostro informações sobre a conta Steam.** \n'
                                              '**zCsgo `<ID da Steam>`:** **Eu lhe mostro as informações sobre a conta de CS:GO**\n'
                                              '**zFlipcoin :** Me faz reagir com cara(😀) ou coroa(👑).\n'
                                              '**zFilme `<nome do filme>`:** Eu te mostro informações do filme escolhido.\n'
                                              '**zSerie `<nome da serie>`:** Eu te mostro informações da serie escolhida.\n'
                                              '**zGames :** Te dá o cargo do jogo caso você reaja com o emoji relativo ao mesmo.\n'
                                              '**zPing :** Exibe meu tempo de resposta.\n'
                                              '**zSugestao `<mensagem>`:** Envia sua sugestão diretamente pro meu dono.\n'
                                              '**zConvite:** Gera um link para convidar outros à este servidor. \n'
                                              '**zSS `<mensagem>`:** **SimSimi do Zueiro Anonimo** S2 \n'
                                              '**zADDss `<mensagem>`:** **Adiciona questões novas à SimSimi** \n'
                                              '\n'
                                              '<a:zueiroanonimobotemoji:440504316613230592>**Comandos que requerem permissões de administrador.**<a:zueiroanonimobotemoji:440504316613230592>\n'
                                              '\n'
                                              '**zAviso `<menção>` `<mensagem>` :** Envia uma mensagem ao usuário mencionado através de mim.\n'
                                              '**zBan `<menção>` :** Bane o usuário mencionado do servidor. \n'
                                              '**zKick `<menção>` :** Kika o usuário mencionado do servidor. \n'
                                              '\n'
                                              '<a:zueiroanonimobotemoji:440504316613230592>**Obrigado**<a:zueiroanonimobotemoji:440504316613230592>\n'
                                                                                                        '\n'
                                               'Obs. **descrição em negrito** = O comando é NOVO, ou foi ATUALIZADO')
            await client.send_message(message.author, embed=embhelp2)
            await client.send_message(message.channel, embed=embhelp3)
        except:
            await client.send_message(message.channel, "Olha, você deve ter bloqueado mensagens no seu privado... infelizmente não poderei mandar meus comando para você enquanto estiver me bloqueando ;-;")

    if message.content.lower().startswith('zzhelpantigasso'):
        user = message.author
        embhelp = discord.Embed(
            title='<:python:419660191244484609> Olá, {}'.format(message.author.name),
            color=user.color,
            descriptino='No momento ainda não estou pronto, porem posso lhe servir em algumas coisas...\nVou deixar algumas infos abaixo para lhe ajudar',
        )
        embhelp.add_field(name='<:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> ' ,value='No momento ainda não estou pronto, porem posso lhe servir em algumas coisas...\nVou deixar algumas infos abaixo para lhe ajudar')
        embhelp.add_field(name='Meu servidor oficial',value='http://discord.me/zueirosanonimous')
        embhelp.add_field(name='Me adicione em seu servidor',value='http://swifttopia.com/6870268/zueiroanonimo')
        await client.send_message(message.channel, embed=embhelp)
       user = message.author
        embhelp1 = discord.Embed(
            title='<:phon:419660191244484609> COMANDOS',
            coloruser.color,
            descriptino=None,
        )
        embhelp1.add_field(e='zVotar + (mensagem)', value='Faz uma votação de ✅ ou ❌ na sua mensagem')
        embhelp1.add_field(name='zAvatar + (usuário)', value='Mostra o avatar do usuário mencionado, junto com reações')
        embhelp1.add_field(name='zServerinfo', value='Mostra informações do servidor em que o BOT está')
        embhelp1.add_field(name='zBotinfo', value='Mostra minhas informações, ou seja, as informações do Zueiro Anonimo')
        embhelp1.add_field(name='zUser', value='Famoso "cara ou coroa", o BOT reagirá se for cara(😀) ou coroa(👑)')
        embhelp1.add_field(name='zGames', value='Aparece uma lista de jogos e se você clicar em um dos emotes você ganha o cargo dele, entretando só ganhará o cargo se o servidor tiver os seguintes cargos: `CS:GO, League of Legends, Gartic, VRCHAT, Brawlhalla, GTA V, PUBG, Roblox` (Obs. os cargos (roles) devem estar escritos igual ao que está acima)')
        embhelp1.add_field(name='zPing', value='Quantos segundos o BOT demora pra responder ? Teste de velocidade da internet do BOT')
        embhelp1.add_field(name='z.Py + (código)', value='Envia o código do formato Python formatado devolta')
        await client.send_message(message.channel, embed=embhelp1)
        embhelp2 = discord.Embed
            title='<:python:419660191244484609> COMANDOS PARA ADMs',
            color=amarelo,
            descriptino=None,
        )
        embhelp2.add_field(name='zAviso (usuário) (mensagem)', value='Manda uma mensagem para o usuário mencionado através do BOT')
        await client.send_message(message.channel, embed=embhelp2)
        embhelp99 = discord.Embed(
            title='<:python:419660191244484609> BREVE MAIS...',
            color=azul,
            descriptino=None,
        )
        embhelp9ent.send_message(message.channel, embed=embhelp99)
e.content.lower().startswith('<@421862224454221824>'):
        if message.author.id in [y.id for y in message.server.members if y.bot]:
            retur
        else:iroanonimobotemoji:440504316613230592> Falou comigo, {}? <a:zueiroanonimobotemoji:440504316613230592>'.format(message.author.name),
                color=user.color,
                descriptino="VACILÃO MORRE CEDO",
            )
            embpapaco.set_image
                url='https://images-ext-2.discordapp.net/external/UuIdfaTGI15OWrW9tZnlXD-rjkhVSzsuQXhUh7463Pg/https/i.imgur.com/T8auOavh.jpg?width=764&height=430')
            embpapaco.set_footer(text="Para ver meus comandos utilize zHelp")
            papaco = await client.send_message(message.channel, embed=embpapaco)
            #   🇧 🇺  🇳  🇩  🇦  ➖   aco, '🇦')
            await client.add_reaction(papaco, '➖')
            awaitclient.add_reaction(papaco, '🇲')
            await client.add_reaction(papaco, '🇴')
            await cli
            author = message.author
            user = message.mentions[0]
            msgg = message.content[6:]
            await client.send_message(message.channel, 'Escreva algo para eu envi
       ping = os.popen('ping 157.240.12.35 -n 1')
       result = ping.readlines()
       texto = msLine[28:].replace("M¡nimo = ", "").replace(" ximo = ", " ").replace(" Max ", "").replace(" M‚dia = ", " ").replace(",", " ").replace(" ", "").replace("ms", "")+"ms"
       timepx = time.time(
       emb = discord.Embed(title='Aguarde...', color=0x565656)
       pingmx0 = await client.send_me
       embedping = discord.Embed(description="<a:zueiroanonimobotemoji:440504316613230592> - **PING:** " + texto +"\n**Tempo de resposta:** %.01f segs" % pingx,
                             color=0xff0080

    if message.content.lower().startswith('zdiga'):
        if message.author.id == '320339126601777152':
            await client.send_message(message.channel, message.content[5:])
            await client.delete_message(message)

    if message.content.lower().startswith('zuserinfo'):
        try:
            member_id = message.mentions[0].id
            member = message.mentions[0]
            vipstatus = member.id in listadevips
            statusgamememb = str(member.game)
            stusu.add_field(name="<a:nyancat:450290566802964480> Seu ID", value="`{}`".format(member.id))
            embedusu.add_field(name="<a:nyancat:450290566802964480> Status",value=statusonmemb.replace("online", "<:online:438399398808911882>").replace("offline","<:offline:438399398762905600>").replace("dnd", "<:dnd:438399396548313091>").replace("idle","<:idle:438399398796460032>").replace("stream", "<:stream:438399396963418131>"))
            embedusu.add_field(name='<a:nyancat:
        except:
            user = message.author
            vipstatus2 = user.id in listadevips
            statusgameuse = str(message.author.game)
            statusnickuse = str(message.author.nick)
           statusonuse = str(message.author.status)
            rolesuse = ([role.name for role in user.roles if role.name != "@everyone"])
            tbedusu1 = discord.Embed(
                title='<a:zueiroanonimobotemoji:440504316613230592> Informações de: {} <a:zueiroanonimobotemoji:440504316613230592>'.format(
                    user.name),
                color=user.color,
                de
            embedus embedusu1.finame="<a:nyancat:450290566802964480> Status",value=statusonuse.replace("online", "<:online:438399398808911882>").replace("offline","<:offline:438399398762905600>").replace("dnd", "<:dnd:438399396548313091>").replace("idle","<:idle:438399398796460032>").replace("stream", "<:stream:438399396963418131>"))
            embedusu1.add_field(nme='<a:nyancat:450290566802964480> Jogando:',value=statusgameuse.replace('None', 'Nada ;-;'))
            embedusu1.ad_field(name="<a:nyancat:450290566802964480> Criado em:",value=user.created_at.strftime("%d/%m/%Y às %H:%M"))
            embedusu1.add_field(nahannel, embed=embedusu1)
",eld(name='<a:zueiroanonimobotemoji:440504316613230592> Discord BOT Básico', value='Um botizinho com o programa HUEBR injetado na veia')
        embedbotin.add_field(name='<a:n02964480> Ultima atualização:', value='`13/06/2018`')
        embedbotin.add_field(namea:nyancat:450290566802964480> Zueiro VIP's",value="Tenho `{}` usuários vips no momento\n`Sistema VIP ainda está em BETA`".format(numlistadevips))
        embedbotin.set_footer(text="Criado por SHAIDERWOW#6701 - Copyright © 2018 - Quer saber mais ? digite zHelp", icon_url="https://images-ext-1.discordapp.net/external/OMP4WooSTGR7TMyMtuRSyDPApIIB3f2POTZV6PPLBgM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/320339126601777152/6044af07c657f2d82a2b5bcfbed01d3d.webp")
        await client.send_message(message.channel, embed=embedbotin)

    if message.content.lower().startswith('zvip')
        #cargo = mesage.content[5:]
        if not message.author.id in listadevips:
            return await client.send_message(message.channel, "O VIP atual custa 1000 Reais, para tê-lo fale com o meu criador, e somente com ele \n Obs. não aconselho a comprar nada, (ainda) não existem comandos para VIP's.... ou será que existem... :3")
        try:
            return await client.send_message(message.channel, "Vc é VIP  :3 Uau")
        except:
            return await client.send_message(message.channel, "Vc é um VIP mt foda S2")

            member = message.mentions[0]
            embed = discord.Embed(
                title='<a:zueiroanonimobotemoji:440504316613230592> Avatar de: {} <a:zueiroanonimobotemoji:440504316613230592>'.format(member.name),
                color=member.color,
            embed.set_image(url=member.avatar_url)
            avatar = await client.send_message(message.channel, embed=embed)
            await client.add_reaction(avatar, '👍')
            await client.add_reaction(avatar, '💩')

        except:
            user = message.author
            embedavata = discord.Embed(
                title='<a:zueiroanonimobotemoji:440504316613230592> Avatar de: {} <a:zueiroanonimobotemoji:440504316613230592>'.format(user.name),
                color=user.color,
                reaction(avatar2, '❤')
            await client.add_if message.content.lower().startswith('zserverinfo'):s
                          if m.status == discord.Status.online])
            offline = len([m.status for m i
            server = essage.server
            online = len([m.status for m in message.server.membern message.server.members
                           if m.status == discord.Status.offline])
            dnd = len([m.status for m in message.server.members
                       if m.status == discord.Status.dnd])
            idle = len([m.status for m in message.server.members
                        if m.status == discord.Status.idle])
            bots = len([member.bot for member in message.server.members if member.bot])
            cargosserv = [role.name for role in message.server.roles if role.name != "@everyone"]

            embed3 = discord.Embed(
                title="Informações do server <a:zueiroanonimobotemoji:440504316613230592> ",
                descriptino=None,
            
            embed3.add_field(name="<a:nyancat:450290566802964480> Nome do server", value=message.server.name, inline=True)
            embe_field(name="<a:nyancat:450290566802964480> Dono", value=message.server.owner.mention)
            embed3.add_field(na=str(message.server.region).title())
            embed3.add_field(name="<a:nyancat:450290566802964480> Emojis", value=f"{len(message.server.emojis)}/100")
            embed3.add_field(name="<a:nyancat:450290566802964480> Membros ({}):".format(len(message.server.members)),
                             value=  ".join(cargosser1 - Copyright © 2018 - Quer saber mais ? digite zHelp",
                              icon_url="https://images-ext-1.discordapp.net/external
        exceptstatus for m in message.server.members
                          ifer.bot for member in message.server.members if member.bot])
            cargosserv = [role.name for role in message.server.roles if role.name != "@everyone"]

            )
            embed33.add_field(name="<a:nyancat:450290566802964480> Nome do server", value=message.server.name,
                             inline=True
            embed33.add_field(name="<a:nyancat:450290566802964480> Criado em",
                             value=message.server.created_at.strftime("%d/%m/%Y às %H:%M"))
            embed3.ad_field(name="<a:nyancat:450290566802964480> Dono", value=message.server.owner.mention)
            embed33.f"**{online}<:online:438399398808911882> {offline}<:offline:438399398762905600> \n{dnd}<:dnd:438399396548313091> {idle}<:idle:438399398796460032> \n{bots}<:bot:437248340724416514>**")
            embed33.add_field(name="<a:nyancat:450290566802964480> Cargos:",
                             value="{} cargos ? uau".format(len(message.server.roles)))
            embed33.set_thumbnail(url=messa por SHAIDERWOW#6701 - Copyright © 2018 - Quer saber mais ? digite zHelp",
                              icon_url="https://images-ext-1.discordapp.net/external/OMP4WooSTGR7TMyMtuRSyDPApIIB3f2POTZV6PPLBgM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/320339126601777152/6044af07c657f2d82a2b5bcfbed01d3d.webp")
            a
            linkdogif = "https://media.t/giphy.gif"

        embgif.set_image(url=linkdogif)
        await client.send_message(message.channel, embed=embgif)

    if message.content.lower().startswith('zflipcoin'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '😀')
        if choice == 2:
            await client.add_reaction(message, '👑')

    if message.content.lower().startswith('zvotar'):
        try:
            user  message.author
            phrase = message.content[6:]
            ield(name="{} Opinou...".format(message.author.name), value="{}".format(phrase),
                     inline=False)
                       )
        embed1.add_field(name="<a:zueiroanonimobotemoji:440504316613230592>",
                         value="**Minecraft =** <:minecraft:442757343646580757>\n"
                        "**Rainbow Six  =**  <:r6:442757819926577152> \n"
                        "**Overwatch  =** <:overwatch:442758257799462913>\n"
                        "**Paladins =** <:paladins:442823168810549249>\n"
                        "**Warframe =** <:warframe:442758505816915980>\n"
                        "**Black Squad =** <:blacksquad:442822965718024201>\n"
                        "*gtav:442822601295790080")
        await client.add_reaction(botmsg, "pubg:442758461810409482")
        await client.add_reaction(botmsg, "brawlhalla:442757169675370497")
        await client.add_reaction(botmsg, "vrchat:442758209585807361")
        await client.add_reaction(botmsg, "lol:442758156850823168")
        await client.add_reaction(botmsg, "roblox:442757513939648522")
        await client.add_reaction(botmsg, "minecraft:442757343646580757")
        await client.add_reaction(botmsg, "r6:442757819926577152")
        await client.add_reaction(botmsg, "overwatch:442758257799462913")
        await client.add_reaction(botmsg, "paladins:442823168810549249")
        await client.add_reaction(botmsg, "warframe:442758505816915980")
        await client.add_reaction(botmsg, "blacksquad:442822965718024201")
        await client.add_reaction(botmsg, "rocketleague:442822713195757569")
        await client.add_reaction(botmsg, "fortnite:442823029278638080")

        gsts.get(member.avatar_url)
        avatar = Image.open(BytesIO(url.content))
        #avatar = Image.open('avatar.png')
        avatar = avatar
    if message.content.startswith("shvideo"):
        try:
            member = message.mentions[0]
            url = requests
            fundomyvid = Image.open('myvideo.png')
            fontemyv, 12), text="Novo de " + member.name, fill=(0, 0, 0), font=fontemyvid2)
                fundomyvid.paste(avatar, (0, 0))fill=(0, 0, 0), font=fontemyvid)
                escrevermyvid.text(xy=(122, 12), text="Novo de " + member.name, fill=(0, 0, 0), font=fontemyvid2)
                fundomyvid.paste(avatar, (0, 0))
                fundomyvid.save('myvideo1.png')
            #fundovid.show()
            await client.send_file(message.channel, 'myvideo1.png')
        except:
            member = message.author
            url = requests.get(member.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            #avatar = Image.open('avatar.png')
            avatar = avatar.resize((100, 100))

            #notificação = message.content[8:]
            fueDraw.Draw(fundomyvid)
            if len(message.content) <= 50:
                notificação = message.content[8:]
                escrevermvid.text(xy=(120, 40), text=notificação, fill=(0, 0, 0), font=fontemyvid)
                escrevermyvd.text(xy=(122, 12), text="Novo de " + member.name, fill=(0, 0, 0), font=fontemyvid2)
                fundomyvmageFont.truetype('A            fundoverine = Image.open('verine.png')
            frenteverine = Image.open('verine.png')
            fundoverine.paste(avatar, (131, 385))
            fundoverine.paste(frenteverine, (0, 0), frenteverine)rial.ttf', 15)
            fontemyvid2 = ImageFont.truetype('Arial.ttf', 18)
            escrevermyvid = Imgg'
            member = message.mentions[0]
            url = requests.get(member.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            avatar = avatar.resize((280, 300))#;

            fundoverine.save('verine1.png')
            frenteverine = Image.open('verine.png')
            fundoverine.paste(avatar, (131, 385))
            fundoverine.paste(frenteverine, (0, 0), frenteverine)
            fundov
            url = requests.get(member.avatar_url)
            avatar ('nando1.png')l=(0, 0, 0), font=fontebarry)
        if len(message.content) >= 69:
            x1 = message.content[8:38]
            x2 = message.content[38:68]
            x3 = message.content[68:]
            escreverbarry.text(xy=(3, 3), text=x1, fill=(0, 0, 0), font=fontebarry)
            escreverbarry.text(xy=(3, 30), text=x2, fill=(0, 0, 0), font=fontebarry)
            escreverbarry.text(xy=(3, 58), text=x3, fill=(0, 0, 0), font=fontebarry)
        fundobarry.save('barryal1.png')
        # fundovid.show()
        await client.send_file(message.channel, 'barryal1.png')

    if message.content.startswith("shbobsp"):

            x1a = message.content[8:]
            x1 = x1a.split(", ")
            fundobobspon= Image.open('bobspon.png')
            #txt = Image.new('L', (500, 50))
            fontebobspon = ImageFont.truetype('Arial.ttf', 15)
            fontebobspon2 = ImageFont.truety
    if reaction.emoji.id == "442758461810409482" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "PUBG", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="PUBG")
            print("create")

    if reaction.emoji.id == "442757169675370497" and msg.id == msg_id and not user == msg_user:
        try:
necraft", msg.server.roles)
await client.create_role(msg_user.server, name="Overwatch")
            print("create")

    if reaction.emoji.id == "442823168810549249" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Paladins", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Paladins")
            print("create")

    if reaction.emoji.id == "442758505816915980" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Warframe", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Warframe")
            print("create")

    if reaction.emoji.id == "442822965718024201" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Black Squad", msg.server.roles)
            await client.add_roles(user, role)
