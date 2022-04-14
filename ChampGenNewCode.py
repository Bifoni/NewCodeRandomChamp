import random

lane_champs = dict(
    Toplane=['Lillia', 'Gwen', 'Yone', 'Sett', 'Neeko', 'Sylas', 'Ornn', 'Illaoi', 'Aatrox', 'Kled', 'Tahm Kench',
             'Camille',
             'Akshan', 'Yasuo', 'Gnar', 'Aurelion Sol', 'Quinn', 'Jayce', 'Darius', 'Fiora', 'Sejuani', 'Rengar',
             'Volibear',
             'Graves', 'Shen', 'Riven', 'Garen', 'Kennen', 'Akali', 'Yorick', 'Mordekaiser', 'Pantheon', 'Gragas',
             'Poppy',
             'Udyr', 'Nasus', 'Heimerdinger', 'Rumble', 'Vayne', 'Lee Sin', 'Wukong', 'Renekton', 'Maokai', 'Nocturne',
             'Malphite', 'Trundle', 'Gangplank', 'Irelia', 'Dr. Mundo', "Cho'Gath", 'Singed', 'Jax', 'Tryndamere',
             'Warwick',
             'Tristana', 'Teemo', 'Sion', 'Ryze', 'Kayle', 'Vladimir', 'Urgot', 'Olaf'],
    Jungle=['Lillia', 'Gwen', 'Ivern', "Rek'Sai", 'Vi', 'Qiyana', 'Ekko', 'Zed', 'Viego', 'Kindred', 'Taliyah', 'Zac',
            'Kayn',
            'Diana', "Kha'Zix", 'Hecarim', 'Sejuani', 'Rengar', 'Volibear', 'Graves', 'Shyvana', 'Talon',
            'Mordekaiser',
            'Gragas', 'Poppy', 'Udyr', 'Nidalee', 'Skarner', 'Rumble', 'Lee Sin', 'Elise', 'Jarvan IV', 'Nocturne',
            'Trundle', 'Shaco', 'Rammus', 'Amumu', "Cho'Gath", 'Karthus', 'Twitch', 'Evelynn', 'Jax', 'Tryndamere',
            'Nunu & Willump', 'Warwick', 'Master Yi', 'Fiddlesticks', 'Xin Zhao', 'Olaf'],
    Midlane=['Lillia', 'Yone', 'Vex', 'Pyke', 'Neeko', 'Sylas', 'Bard', 'Azir', 'Qiyana', 'Ekko', 'Zed', 'Lucian',
             'Akshan',
             'Taliyah', "Vel'Koz", 'Yasuo', 'Seraphine', "Kai'sa", 'Zyra', 'Zoe', 'Aurelion Sol', 'Syndra', 'Diana',
             'Lissandra', 'Jayce', 'Ziggs', 'Viktor', 'Fizz', 'Ahri', 'Xerath', 'Lux', "Kog'Maw", 'Talon', 'Malzahar',
             'Akali',
             'Ezreal', 'Pantheon', 'Gragas', 'Heimerdinger', 'Cassiopeia', 'Rumble', 'Brand', 'Orianna', 'Nocturne',
             'Katarina',
             'Malphite', 'Swain', 'Caitlyn', 'Veigar', 'Corki', 'Irelia', 'Kassadin', 'Anivia', "Cho'Gath", 'Karthus',
             'Zilean', 'Morgana', 'Teemo', 'Ryze', 'Vladimir', 'LeBlanc', 'Urgot', 'Twisted Fate', 'Galio', 'Annie'],
    ADC=['Aphelios', 'Xayah', 'Kalista', 'Samira', 'Lucian', 'Jinx', 'Jhin', 'Akshan', 'Yasuo', 'Seraphine',
         "Kai'sa",
         'Quinn', 'Draven', 'Ziggs', 'Varus', "Kog'Maw", 'Ezreal', 'Heimerdinger', 'Vayne', 'Brand', 'Caitlyn',
         'Swain',
         'Veigar', 'Corki', 'Twitch', 'Morgana', 'Ashe', 'Miss Fortune', 'Tristana', 'Sivir', 'Twisted Fate'],
    Support=['Renata Glasc', 'Vex', 'Sett', 'Pyke', 'Neeko', 'Rell', 'Rakan', 'Bard', 'Thresh', 'Yuumi', 'Nami',
             'Senna',
             'Tahm Kench', 'Braum', "Vel'Koz", 'Zac', 'Seraphine', 'Zyra', 'Lulu', 'Nautilus', 'Xerath', 'Lux', 'Shen',
             'Leona', 'Pantheon', 'Brand', 'Maokai', 'Malphite', 'Blitzcrank', 'Swain', 'Taric', 'Karma', 'Janna',
             'Sona',
             'Anivia', 'Amumu', 'Zilean', 'Morgana', 'Soraka', 'Alistar', 'Galio'])


while True:
    nome = input('Digite o nome do jogador: ')
    nome = nome.upper()
    qst_lane = input('Deseja escolher sua lane?(s/n)')
    if qst_lane == 'n':
        lane = random.choice(list(lane_champs.keys()))
        champ = random.choice(lane_champs[lane])
        print(f'----------------\n{nome}\nLane: {lane}\nChampion: {champ}\n----------------')
    elif qst_lane == 's':
        choose_lane = input('Escolha sua lane(Toplane, Midlane, Support, Jungle, ADC): ')
        if choose_lane in lane_champs.keys():
            lane_champ = random.choice(lane_champs[choose_lane])
            print(f'----------------\n{nome}\nLane: {choose_lane}\nChampion: {lane_champ}\n----------------')
        else:
            nova_lane = input('Digite o nome da lane corretamente.(Toplane, Midlane, Support, Jungle, ADC): ')
            lane_champ = random.choice(lane_champs[nova_lane])
            print(f'----------------\n{nome}\nLane: {nova_lane}\nChampion: {lane_champ}\n----------------')
    novo_nome = input('Deseja digitar um nome nome?(s/n) ')
    if novo_nome == 'n':
        break

