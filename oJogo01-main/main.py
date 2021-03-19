import pygame
import sys
import keyword
import pygame.mixer
pygame.init()

altura = 600
largura = 1230
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((largura, altura), 0, 32)

font = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 70)
font3 = pygame.font.Font("Gameplay.ttf", 150)
font4 = pygame.font.SysFont(None, 40)

spritePer = 'boy'

vidaPossivel = 1000000
vidaAtual =  7

nivel = 0

dinheiro = 0

def draw_text(text, fonte, color, surface, x, y):
    textobj = fonte.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


valoresRangeEpyCCHNpcs = {
    'game': {
        'cch': [
            {'orange': range(100, 125), 'py': 150},

        ],
        'cev': [
            {'orange': range(120, 140), 'px': 130},
        ],
        'cdv': [

        ],
        'cbh': [
            {'orange': range(90, 125), 'py': 90},
        ],
    }
}

valoresRangeEpyCCHMudardeLocal = {
    'game': {
        'cch': [
            {'orange': range(310, 360), 'py': 90},

        ],
        'cev': [
        ],
        'cdv': [

        ],
        'cbh': [
        ],
    },
    'carto': {
        'cch': [

        ],
        'cev': [
            {'orange': range(410, 460), 'px': 520},
        ],
        'cdv': [

        ],
        'cbh': [
        ],
    }
}

valoresRangeEpyCCH = {
    'game': {

        'cch': [
            {'orange': range(30, 310), 'py': 330},
            {'orange': range(200, 250), 'py': 360},
            {'orange': range(250, 310), 'py': 190},
            {'orange': range(380, 450), 'py': 190},
            {'orange': range(30, 80), 'py': 190},
            {'orange': range(30, 90), 'py': 160},
            {'orange': range(180, 250), 'py': 190},
            {'orange': range(180, 250), 'py': 160},
            {'orange': range(500, 650), 'py': 90},
            {'orange': range(530, 610), 'py': 130},
            {'orange': range(470, 540), 'py': 320},
            {'orange': range(600, 650), 'py': 350},
            {'orange': range(460, 650), 'py': 300},
            {'orange': range(30, 90), 'py': 380},
            {'orange': range(80, 130), 'py': 350},
            {'orange': range(160, 200), 'py': 380},
            {'orange': range(-20, 640), 'py': 80},
            {'orange': range(90, 115), 'py': 140},

        ],
        'cev': [
            {'orange': range(340, 380), 'px': 210},
            {'orange': range(240, 330), 'px': 310},
            {'orange': range(340, 360), 'px': 250},
            {'orange': range(80, 190), 'px': 310},
            {'orange': range(80, 195), 'px': 440},
            {'orange': range(80, 160), 'px': 90},
            {'orange': range(160, 200), 'px': 80},
            {'orange': range(80, 140), 'px': 590},
            {'orange': range(240, 440), 'px': 440},
            {'orange': range(300, 330), 'px': 540},
            {'orange': range(340, 390), 'px': 80},
            {'orange': range(340, 360), 'px': 130},
            {'orange': range(-20, 460), 'px': 30},
            {'orange': range(120, 140), 'px': 120},
        ],
        'cdv': [
            {'orange': range(340, 390), 'px': 150},
            {'orange': range(80, 170), 'px': 170},
            {'orange': range(170, 200), 'px': 170},
            {'orange': range(80, 100), 'px': 480},
            {'orange': range(100, 140), 'px': 520},
            {'orange': range(80, 200), 'px': 360},
            {'orange': range(190, 330), 'px': 460},
            {'orange': range(310, 360), 'px': 580},
            {'orange': range(230, 440), 'px': 360},
            {'orange': range(70, 450), 'px': 640},

        ],
        'cbh': [
            {'orange': range(310, 40), 'py': 240},
            {'orange': range(-20, 310), 'py': 230},
            {'orange': range(365, 450), 'py': 230},
            {'orange': range(450, 650), 'py': 200},
            {'orange': range(-20, 670), 'py': 420}, 
            {'orange': range(90, 125), 'py': 100},

        ],
    },

    'carto': {

        'cch': [
            

        ],
        'cev': [
            {'orange': range(340, 380), 'px': 210},
            
        ],
        'cdv': [
            
            {'orange': range(70, 450), 'px': 640},

        ],
        'cbh': [
           
            {'orange': range(90, 125), 'py': 100},

        ],
    }
}

sobreporPesonagem = {
    'npcs': {
        'home': [
            {'y': range( 150, 190), 'x': range(90, 115)},
        ],
    },
}

falas = {
    'npcs': {
        'home': {
            'personagem1':[
                'fala ai',
                'sabia que para ativar o menu é só clicar m',
                '...',
                '....',
                'você não tem coisa melhor pra fazer? -_-'
            ]
        }
    },
}


spritesCenario = {
    'home': pygame.image.load("images\home.png")

}

sprites = {
    'boy': {
        'IdleDonw': pygame.image.load("images\spritesTestes\imagem_1.png"),
        'IdleLeft': pygame.image.load("images\spritesTestes\imagem_4.png"),
        'IdleUp': pygame.image.load("images\spritesTestes\imagem_7.png"),
        'IdleRigth': pygame.image.load("images\spritesTestes\imagem_10.png"),
        'animImgDonw': ["images\spritesTestes\imagem_1.png", "images\spritesTestes\imagem_2.png",
                        "images\spritesTestes\imagem_1.png", "images\spritesTestes\imagem_3.png"],
        'animImgLeft': ["images\spritesTestes\imagem_4.png", "images\spritesTestes\imagem_5.png",
                        "images\spritesTestes\imagem_4.png", "images\spritesTestes\imagem_6.png"],
        'animImgUP': ["images\spritesTestes\imagem_7.png", "images\spritesTestes\imagem_8.png",
                      "images\spritesTestes\imagem_7.png", "images\spritesTestes\imagem_9.png"],
        'animImgRight': ["images\spritesTestes\imagem_10.png", "images\spritesTestes\imagem_11.png",
                         "images\spritesTestes\imagem_10.png", "images\spritesTestes\imagem_12.png"],
    },
    'girl': {
        'IdleDonw': pygame.image.load("images\sprites\imagem_1.png"),
        'IdleLeft': pygame.image.load("images\sprites\imagem_4.png"),
        'IdleUp': pygame.image.load("images\sprites\imagem_7.png"),
        'IdleRigth': pygame.image.load("images\sprites\imagem_10.png"),
        'animImgDonw': ["images\sprites\imagem_1.png", "images\sprites\imagem_2.png",
                        "images\sprites\imagem_3.png", "images\sprites\imagem_4.png"],
        'animImgLeft': ["images\sprites\imagem_5.png", "images\sprites\imagem_6.png",
                        "images\sprites\imagem_7.png", "images\sprites\imagem_8.png"],
        'animImgUP': ["images\sprites\imagem_13.png", "images\sprites\imagem_14.png",
                      "images\sprites\imagem_15.png", "images\sprites\imagem_16.png"],
        'animImgRight': ["images\sprites\imagem_9.png", "images\sprites\imagem_10.png",
                         "images\sprites\imagem_11.png", "images\sprites\imagem_12.png"],
    },
    'cara1':{
        'IdleDonw': pygame.image.load("images/npcs/cara2.png"),
        'IdleRigth': pygame.image.load("images/npcs/cara1.png"),
    },
}
funcoesEnomesDeSelecao = {
    'mainMenu': [
        {'nome': 'start'},
        {'nome': 'options'},
    ],
    'GUIpt1Esq': [
        {'nome': 'Personagens'},
        {'nome': 'Mochila'},
    ],
    'GUIpt1D': [
        {'nome': 'Vida: {} / {}'.format(vidaAtual, vidaPossivel)},
        {'nome': 'Nivel: {}'.format(nivel)},
        {'nome': 'Dinheiro: {} '.format(dinheiro)},
    ],
    'person': [
        {'nome': 'Jao'},
        {'nome': 'leila'},
    ],
}

characterComeçaNaSalaNaPos = {
    'home': [
        {'posx': 340, 'posy': 130},
    ],
}


def animarNpc(acontecerAlgo):
    if acontecerAlgo == True:
        return sprites['cara1']['IdleRigth']
    else:
        return sprites['cara1'][ 'IdleDonw']

npcsPos = {
    'home': [
        {'x': 100, 'y': 140, 'sprite': sprites['cara1']['IdleRigth']},
    ],
}

clique = pygame.mixer.Sound("clique_2.wav")
seta = pygame.image.load("seta-removebg-preview.png")


def collisaEsquerdaParedeVertical(vel, bd, pos_x, pos_y):
    for a in range(len(valoresRangeEpyCCH[bd]['cev'])):
        for i in valoresRangeEpyCCH[bd]['cev'][a]['orange']:
            if pos_x == valoresRangeEpyCCH[bd]['cev'][a]['px'] and pos_y == i:
                pos_x += vel
    return pos_x


def collisaDireitaVertical(vel, bd, pos_x, pos_y):
    for a in range(len(valoresRangeEpyCCH[bd]['cdv'])):
        for i in valoresRangeEpyCCH[bd]['cdv'][a]['orange']:
            if pos_x == valoresRangeEpyCCH[bd]['cdv'][a]['px'] and pos_y == i:
                pos_x -= vel
    return pos_x


def collisaCimaHorizontal(vel, bd, pos_x, pos_y):
    for a in range(len(valoresRangeEpyCCH[bd]['cch'])):
        for i in valoresRangeEpyCCH[bd]['cch'][a]['orange']:
            if pos_x == i and pos_y == valoresRangeEpyCCH[bd]['cch'][a]['py']:
                pos_y += vel
    return pos_y


def collisaBaixoHorizontal(vel, bd, pos_x, pos_y):
    for a in range(len(valoresRangeEpyCCH[bd]['cbh'])):
        for i in valoresRangeEpyCCH[bd]['cbh'][a]['orange']:
            if pos_x == i and pos_y == valoresRangeEpyCCH[bd]['cbh'][a]['py']:
                pos_y -= vel
    return pos_y


def collisaEsquerdaParedeVerticalBooleano(bd, pos_x, pos_y,valoresDe):
    for a in range(len(valoresDe[bd]['cev'])):
        for i in valoresDe[bd]['cev'][a]['orange']:
            if pos_x == valoresDe[bd]['cev'][a]['px'] and pos_y == i:
                return True


def collisaDireitaVerticalBooleano(bd, pos_x, pos_y, valoresDe):
    for a in range(len(valoresDe[bd]['cdv'])):
        for i in valoresDe[bd]['cdv'][a]['orange']:
            if pos_x == valoresDe[bd]['cdv'][a]['px'] and pos_y == i:
                return True


def collisaCimaHorizontalBooleano(bd, pos_x, pos_y, valoresDe):
    for a in range(len(valoresDe[bd]['cch'])):
        for i in valoresDe[bd]['cch'][a]['orange']:
            if pos_x == i and pos_y == valoresDe[bd]['cch'][a]['py']:
                return True


def collisaBaixoHorizontalBooleano(bd, pos_x, pos_y, valoresDe):
    for a in range(len(valoresDe[bd]['cbh'])):
        for i in valoresDe[bd]['cbh'][a]['orange']:
            if pos_x == i and pos_y == valoresDe[bd]['cbh'][a]['py']:
                return True


def main_menu():
    seta_px = 190
    seta_py = 300
    sera = False
    while True:

        keys = pygame.key.get_pressed()

        screen.fill((5, 0, 205))

        escreverLista(265, 300, 'mainMenu', 120, font2, (225,225,225), screen)
        draw_text("O Jogo", font3, (225, 225, 225), screen, 70, 50)

        for event in pygame.event.get():
            fechartela(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                setaAtivarFuncao(event, pygame.K_e, 'game', 190,300, seta_px, seta_py)
                setaAtivarFuncao(event, pygame.K_e, 'options', 190,420, seta_px, seta_py)
                seta_py = moverSeta(event, seta_py, 300, 420, 120)

        escreverLista(265, 300, 'mainMenu', 120, font2, (225,225,225), screen)
        screen.blit(seta, (seta_px, seta_py))
        pygame.display.update()
        mainClock.tick(60)

def setaAtivarFuncao(event, tecla, e, posx, posY, seta_px, seta_py ):
    if event.key == tecla:
        if seta_px == posx and seta_py == posY:
            qualAfuncao(e)

def moverX(keys, pos_x, vel):
    if keys[pygame.K_LEFT]:
        pos_x -= vel

    if keys[pygame.K_RIGHT]:
        pos_x += vel

    return pos_x


def moverY(keys, pos_y, vel):

    if keys[pygame.K_UP]:
        pos_y -= vel

    if keys[pygame.K_DOWN]:
        pos_y += vel

    return pos_y


def voltar(keys, çao):
    if keys[pygame.K_LEFT]:

        çao = 1

    if keys[pygame.K_RIGHT]:

        çao = 2

    if keys[pygame.K_UP]:

        çao = 3

    if keys[pygame.K_DOWN]:

        çao = 0
    return çao


def animacao(keys, anim, character, bd):

    if keys[pygame.K_LEFT]:
        anim += 1
        if anim == len(sprites[bd]['animImgLeft']):
            anim = 0
        character = pygame.image.load(sprites[bd]['animImgLeft'][anim])

    if keys[pygame.K_RIGHT]:
        anim += 1
        if anim == len(sprites[bd]['animImgRight']):
            anim = 0
        character = pygame.image.load(sprites[bd]['animImgRight'][anim])

    if keys[pygame.K_UP]:
        anim += 1
        if anim == len(sprites[bd]['animImgUP']):
            anim = 0

        character = pygame.image.load(sprites[bd]['animImgUP'][anim])

    if keys[pygame.K_DOWN]:
        anim += 1
        if anim == len(sprites[bd]['animImgDonw']):
            anim = 0
        character = pygame.image.load(sprites[bd]['animImgDonw'][anim])

    return character


def retornarAnim(anim, keys):
    if keys[pygame.K_LEFT]:
        anim += 1
        if anim == 4:
            anim = 0
    if keys[pygame.K_RIGHT]:
        anim += 1
        if anim == 4:
            anim = 0

    if keys[pygame.K_UP]:
        anim += 1
        if anim == 4:
            anim = 0

    if keys[pygame.K_DOWN]:
        anim += 1
        if anim == 4:
            anim = 0
    return anim


def moverSeta(event, seta_py, posLimitCima, posLimitbaixo, intervalo):
    if seta_py < posLimitCima+intervalo:
        seta_py = seta_py + intervalo

    if event.key == pygame.K_DOWN:
        seta_py = seta_py + intervalo

    if seta_py > posLimitbaixo:
        seta_py = seta_py - intervalo

    if event.key == pygame.K_UP:
        seta_py = seta_py - intervalo

    return seta_py


def fechartela(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def carto():
    vel = 10
    anim = 0
    pos_x = characterComeçaNaSalaNaPos['carto'][0]['posx']
    pos_y = characterComeçaNaSalaNaPos['carto'][0]['posy']
    dire = [sprites[spritePer]['animImgDonw'], sprites[spritePer]['animImgLeft'],
            sprites[spritePer]['animImgRight'], sprites[spritePer]['animImgUP']]
    çao = 0
    euQueroConversar = False
    vezes = 0
    character = sprites[spritePer]['IdleDonw']
    terrp = npcsPos['home'][0]['sprite']
    screen.blit(terrp, (100, 100))
    screen.blit(spritesCenario['home'], (0, 0))
    screen.blit(character, (pos_x, pos_y))
    running = True
    while running:

        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        character = pygame.image.load(dire[çao][0])
        terrp = npcsPos['home'][0]['sprite']
        for event in pygame.event.get():
            fechartela(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                ativarFuncao(event, pygame.K_m, 'menu')
                vezes = contarVezesqueClicouATecla(event, pygame.K_c, vezes)

        pos_x = moverX(keys, pos_x, vel)
        pos_y = moverY(keys, pos_y, vel)
        character = animacao(keys, anim, character, spritePer)
        çao = voltar(keys, çao)
        anim = retornarAnim(anim, keys)
        character = pygame.transform.scale(character, (55, 75))
        pos_y = collisaBaixoHorizontal(vel, 'carto', pos_x, pos_y)
        pos_y = collisaCimaHorizontal(vel, 'carto', pos_x, pos_y)
        pos_x = collisaEsquerdaParedeVertical(vel, 'carto', pos_x, pos_y)
        pos_x = collisaDireitaVertical(vel, 'carto', pos_x, pos_y)
        mudarDeLugar(collisaCimaHorizontalBooleano('carto', pos_x, pos_y, valoresRangeEpyCCHMudardeLocal), 'carto')
        seraqestaporcima = sobreposicao(pos_x, pos_y, 'npcs', 'cartos')
        desenharSobre(seraqestaporcima, character, terrp, pos_x, pos_y, 'carto')
        escreverFalas(pos_x, pos_y, euQueroConversar, vezes-1)
        mainClock.tick(10)
        print(pos_y, pos_x)
        pygame.display.flip()
    


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text("options", font, (255, 255, 255), screen, 40, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)


def battle():
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(10)



def game():
    vel = 10
    anim = 0
    pos_x = characterComeçaNaSalaNaPos['home'][0]['posx']
    pos_y = characterComeçaNaSalaNaPos['home'][0]['posy']
    dire = [sprites[spritePer]['animImgDonw'], sprites[spritePer]['animImgLeft'],
            sprites[spritePer]['animImgRight'], sprites[spritePer]['animImgUP']]
    çao = 0
    euQueroConversar = False
    vezes = 0
    character = sprites[spritePer]['IdleDonw']
    terrp = npcsPos['home'][0]['sprite']
    screen.blit(terrp, (100, 100))
    screen.blit(spritesCenario['home'], (0, 0))
    screen.blit(character, (pos_x, pos_y))
    running = True
    while running:

        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        character = pygame.image.load(dire[çao][0])
        terrp = npcsPos['home'][0]['sprite']
        for event in pygame.event.get():
            fechartela(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                ativarFuncao(event, pygame.K_m, 'menu')
                euQueroConversar = ativarConversa(event, pygame.K_c)
                vezes = contarVezesqueClicouATecla(event, pygame.K_c, vezes)

        pos_x = moverX(keys, pos_x, vel)
        pos_y = moverY(keys, pos_y, vel)
        character = animacao(keys, anim, character, spritePer)
        çao = voltar(keys, çao)
        anim = retornarAnim(anim, keys)
        character = pygame.transform.scale(character, (55, 75))
        pos_y = collisaBaixoHorizontal(vel, 'game', pos_x, pos_y)
        pos_y = collisaCimaHorizontal(vel, 'game', pos_x, pos_y)
        pos_x = collisaEsquerdaParedeVertical(vel, 'game', pos_x, pos_y)
        pos_x = collisaDireitaVertical(vel, 'game', pos_x, pos_y)
        mudarDeLugar(collisaCimaHorizontalBooleano('game', pos_x, pos_y, valoresRangeEpyCCHMudardeLocal), 'carto')
        seraqestaporcima = sobreposicao(pos_x, pos_y, 'npcs', 'home')
        desenharSobre(seraqestaporcima, character, terrp, pos_x, pos_y, 'home')
        escreverFalas(pos_x, pos_y, euQueroConversar, vezes-1)
        mainClock.tick(10)
        print(pos_y, pos_x)
        pygame.display.flip()

def mudarDeLugar(colidiu, s):
    if colidiu == True:
        qualAfuncao(s)

def ativarFuncao(event, tecla, e):
    if event.key == tecla:
        qualAfuncao(e)

def qualAfuncao(s):
    if s == 'game':
        game()
    if s == 'options':
        options()
    if s == 'menu':
        GUI()
    if s == 'person':
        personagens()
    if s == 'bag':
        mochila()
    if s == 'carto':
        carto()

def escreverFalas(pos_x, pos_y, euQueroConversar, contador):
    desenharBox(porPerto(pos_x, pos_y, 'game'),
                euQueroConversar, falas['npcs']['home']['personagem1'][contador])    

def contarVezesqueClicouATecla(event, tecla, quantidadeAtual):
    if event.key == tecla:
        quantidadeAtual = quantidadeAtual + 1
    if quantidadeAtual >= len(falas['npcs']['home']['personagem1'])+1:
        quantidadeAtual = 0
    return quantidadeAtual

def porPerto(pos_x, pos_y, bd):
    if collisaBaixoHorizontalBooleano(bd, pos_x, pos_y, valoresRangeEpyCCHNpcs) == True:
        return True
    if collisaCimaHorizontalBooleano(bd, pos_x, pos_y, valoresRangeEpyCCHNpcs) == True:
        return True
    if collisaDireitaVerticalBooleano(bd, pos_x, pos_y, valoresRangeEpyCCHNpcs) == True:
        return True
    if collisaEsquerdaParedeVerticalBooleano(bd, pos_x, pos_y, valoresRangeEpyCCHNpcs) == True:
        return True
    else:
        return False


def desenharNpcs(bd):

    for i in range(len(npcsPos[bd])):
        screen.blit(npcsPos[bd][i]['sprite'],
                    (npcsPos[bd][i]['x'], npcsPos[bd][i]['y']))


def desenharSobre(sobreposicao, character, terrp, pos_x, pos_y, bd):
    if sobreposicao == True:
        screen.blit(spritesCenario[bd], (0, 0))
        desenharNpcs(bd)
        screen.blit(character, (pos_x, pos_y))
    else:
        screen.blit(spritesCenario[bd], (0, 0))
        screen.blit(character, (pos_x, pos_y))
        desenharNpcs(bd)


def ativarConversa(event, tecla):
    if event.key == tecla:
        return True


def sobreposicao(pos_x, pos_y, bd1, bd2):
    for e in range(len(sobreporPesonagem[bd1][bd2])):
        for i in sobreporPesonagem[bd1][bd2][e]['y']:
            for a in sobreporPesonagem[bd1][bd2][e]['x']:
                if pos_x == a and pos_y == i:
                    return True
    return False


def desenharBox(perto, querConversar, texto):
    if querConversar == True and perto == True:
        box = pygame.Surface((largura - 200, altura/3))
        box.fill((5, 0, 205))
        screen.blit(box, (30, altura - altura/3 - 30))
        draw_text(texto,
                  font4, (225, 225, 225), screen, 40, altura - altura/3)



def personagens():
    o = True
    while o:
        screen.fill((5, 0, 205))
        for event in pygame.event.get():
            fechartela(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    o = False
        escreverLista(44, 56, 'person', 76, font2,(225,225,225), screen)
        print('cheetos')
        pygame.display.update()
        mainClock.tick(60)

def mochila():
    o = True
    while o:
        screen.fill((5, 0, 205))
        
        for event in pygame.event.get():
            fechartela(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    o = False
        
        pygame.display.update()
        mainClock.tick(60)

def GUI():
    o = True
    setax = 544
    setay = 56
    while o:
        screen.fill((5, 0, 205))
        escreverLista(44, 56, 'GUIpt1D', 76, font2,(225,225,225), screen)
        escreverLista(644, 56,'GUIpt1Esq', 120, font2,(225,225,225), screen)
        for event in pygame.event.get():
            fechartela(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    o = False
                setaAtivarFuncao(event, pygame.K_e, 'person', 544,56, setax, setay)
                setaAtivarFuncao(event, pygame.K_e, 'bag', 544,176, setax, setay)
                setay=moverSeta(event, setay, 53, 180, 120)
        screen.blit(seta, (setax, setay))
        pygame.display.flip()
        mainClock.tick(60)

def escreverLista(posx, posyInicial, bd, intervalo, font, cor, superficie):
    for i in range(len(funcoesEnomesDeSelecao[bd])):
        draw_text(funcoesEnomesDeSelecao[bd][i]['nome'],
                  font, cor, superficie, posx, posyInicial)
        posyInicial = posyInicial + intervalo

main_menu()
