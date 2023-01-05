# Thiago Novinski Machado - 155476
# Vinicius Anselmo Rodrigues - 155466


from graphics import *
import random
import time
from math import trunc


tela = GraphWin("PokePega", 1200, 700, autoflush=False)

meninoBaixo = ["baixo_1.gif", "baixo_2.gif", "baixo_3.gif", "baixo_4.gif"]

meninoCima = ["cima_1.gif", "cima_2.gif", "cima_3.gif", "cima_4.gif"]

meninoEsquerda = ["esquerda_1.gif", "esquerda_2.gif",
                  "esquerda_3.gif", "esquerda_4.gif"]

meninoDireita = ["direita_1.gif", "direita_2.gif",
                 "direita_3.gif", "direita_4.gif"]


blastoiseSprite = ["blastoise.gif", "blastoise_Shiny.gif"]
watergunSprites = ["watergun_1.gif", "watergun_2.gif", "watergun_3.gif"]
watergunShinySprites = ["watergunShiny_1.gif",
                        "watergunShiny_2.gif", "watergunShiny_3.gif"]
watergunAtual = []
# É Shiny?
shinyChanceB = random.randrange(1, 81)
if shinyChanceB == 1:
    spriteBlastoise = blastoiseSprite[1]
    watergunAtual = watergunShinySprites
else:
    spriteBlastoise = blastoiseSprite[0]
    watergunAtual = watergunSprites


charizardSprite = ["charizard.Gif", "charizard_Shiny.gif"]
fireballSprites = ["fireball_1.gif", "fireball_2.gif",
                   "fireball_3.gif"]
fireballShinySprites = ["fireballShiny_1.gif",
                        "fireballShiny_2.gif", "fireballShiny_3.gif"]
fireballAtual = []

shinyChanceC = random.randrange(1, 81)
if shinyChanceC == 1:
    spriteCharizard = charizardSprite[1]
    fireballAtual = fireballShinySprites
else:
    spriteCharizard = charizardSprite[0]
    fireballAtual = fireballSprites


pikachuFinal = ["pikachu_1.gif", "pikachu_2.gif", "pikachu_3.gif"]

# cenário/menino posição inicial
fundo = Image(Point(600, 400), "cenário_Final.gif")
fundo.draw(tela)
menino = Image(Point(600, 400), "baixo_1.gif")
i = 0
menino.draw(tela)
posiçãoY = 400
posiçãoX = 600
velocidade = 15
velocidadeUpdate = 24
# pokebola
pokeY = (random.randrange(8, 19)*30)
pokeX = (random.randrange(1, 40)*30)
pokebola = Image(Point(pokeX, pokeY), "pokebola.png")
pokebola.draw(tela)

# hud
bordaTempo = Image(Point(100, 50), "bordaTempo.gif")
bordaTempo.draw(tela)
bordaPokebola = Image(Point(700, 50), "bordaPokebolas.gif")
bordaPokebola.draw(tela)
pokebola1 = Image(Point(250, 50), "pokebolaCinza.gif")
pokebola1.draw(tela)
pokebola2 = Image(Point(350, 50), "pokebolaCinza.gif")
pokebola2.draw(tela)
pokebola3 = Image(Point(450, 50), "pokebolaCinza.gif")
pokebola3.draw(tela)
pokebola4 = Image(Point(550, 50), "pokebolaCinza.gif")
pokebola4.draw(tela)
pokebola5 = Image(Point(650, 50), "pokebolaCinza.gif")
pokebola5.draw(tela)
pokebola6 = Image(Point(750, 50), "pokebolaCinza.gif")
pokebola6.draw(tela)
pokebola7 = Image(Point(850, 50), "pokebolaCinza.gif")
pokebola7.draw(tela)
pokebola8 = Image(Point(950, 50), "pokebolaCinza.gif")
pokebola8.draw(tela)
pokebola9 = Image(Point(1050, 50), "pokebolaCinza.gif")
pokebola9.draw(tela)
pokebola10 = Image(Point(1150, 50), "pokebolaCinza.gif")
pokebola10.draw(tela)


# timer
timeStart = time.time()
timer = Text(Point(100, 200), "0")
timer.draw(tela)
tempoRecord = 0

# contador
pokePegas = 0
contador = Text(Point(100, 100), pokePegas)
contadorAtual = 0

# inimigo1:charizard
inicialCharizard = (random.randrange(1, 11)*100)
charizard = Image(Point(inicialCharizard, 640), spriteCharizard)
charizard.draw(tela)
velCharizard = 10

# ataque charizard
c = 0
fireball = Image(Point((inicialCharizard+60), 580), fireballSprites[c])
fireball.draw(tela)

# inimigo2:blastoise
inicialBlastoise = (random.randrange(1, 11)*100)
blastoise = Image(Point(inicialBlastoise, 125), spriteBlastoise)
blastoise.draw(tela)
velBlastoise = -5

# ataque blastoise
b = 0
watergun = Image(Point(inicialBlastoise, 125), watergunAtual[b])
watergun.draw(tela)


key = tela.checkKey()
while key != "Escape":
    # movimentação do personagem/animações
    if key == "Right":
        if posiçãoX < 1170:
            menino.move(velocidade, 0)
            posiçãoX = menino.getAnchor().getX()
            menino.undraw()
            menino = meninoDireita[i]
            menino = Image(Point(posiçãoX, posiçãoY), menino)
            menino.draw(tela)
            i += 1
            if i >= len(meninoDireita):
                i = 0

    elif key == "Left":
        if posiçãoX > 30:
            menino.move(-1*velocidade, 0)
            posiçãoX = menino.getAnchor().getX()
            menino.undraw()
            menino = meninoEsquerda[i]
            menino = Image(Point(posiçãoX, posiçãoY), menino)
            menino.draw(tela)
            i += 1
            if i >= len(meninoEsquerda):
                i = 0

    elif key == "Up":
        if posiçãoY > 190:
            menino.move(0, -1*velocidade)
            posiçãoY = menino.getAnchor().getY()
            menino.undraw()
            menino = meninoCima[i]
            menino = Image(Point(posiçãoX, posiçãoY), menino)
            menino.draw(tela)
            i += 1
            if i >= len(meninoCima):
                i = 0

    elif key == "Down":
        if posiçãoY < 550:
            menino.move(0, velocidade)
            posiçãoY = menino.getAnchor().getY()
            menino.undraw()
            menino = meninoBaixo[i]
            menino = Image(Point(posiçãoX, posiçãoY), menino)
            menino.draw(tela)
            i += 1
            if i >= len(meninoBaixo):
                i = 0

    # pega a pokebola
    if posiçãoX < (pokeX+25) and posiçãoX > (pokeX-25) and posiçãoY < (pokeY+25) and posiçãoY > (pokeY-50):
        pokebola.undraw()
        pokeY = (random.randrange(8, 19)*30)
        pokeX = (random.randrange(1, 40)*30)
        pokebola = Image(Point(pokeX, pokeY), "pokebola.png")
        pokebola.draw(tela)
        pokePegas = pokePegas + 1

    # atualiza o contador

    if pokePegas == 1:
        pokebola1.undraw()
        pokebola1 = Image(Point(250, 50), "pokebola.png")
        pokebola1.draw(tela)
    elif pokePegas == 2:
        pokebola2.undraw()
        pokebola2 = Image(Point(350, 50), "pokebola.png")
        pokebola2.draw(tela)
    elif pokePegas == 3:
        pokebola3.undraw()
        pokebola3 = Image(Point(450, 50), "pokebola.png")
        pokebola3.draw(tela)
    elif pokePegas == 4:
        pokebola4.undraw()
        pokebola4 = Image(Point(550, 50), "pokebola.png")
        pokebola4.draw(tela)
    elif pokePegas == 5:
        pokebola5.undraw()
        pokebola5 = Image(Point(650, 50), "pokebola.png")
        pokebola5.draw(tela)
    elif pokePegas == 6:
        pokebola6.undraw()
        pokebola6 = Image(Point(750, 50), "pokebola.png")
        pokebola6.draw(tela)
    elif pokePegas == 7:
        pokebola7.undraw()
        pokebola7 = Image(Point(850, 50), "pokebola.png")
        pokebola7.draw(tela)
    elif pokePegas == 8:
        pokebola8.undraw()
        pokebola8 = Image(Point(950, 50), "pokebola.png")
        pokebola8.draw(tela)
    elif pokePegas == 9:
        pokebola9.undraw()
        pokebola9 = Image(Point(1050, 50), "pokebola.png")
        pokebola9.draw(tela)
    elif pokePegas == 10:
        pokebola10.undraw()
        pokebola10 = Image(Point(1150, 50), "pokebola.png")
        pokebola10.draw(tela)

    # movimentação charizard
    charizard.move(velCharizard, 0)
    charizardX = charizard.getAnchor().getX()
    charizardY = charizard.getAnchor().getY()
    if charizardX >= 1100 or charizardX <= 90:
        velCharizard = velCharizard*-1

    # movimentação fireball
    fireball.move(0, -10)
    fireballY = fireball.getAnchor().getY()
    fireballX = fireball.getAnchor().getX()
    fireball.undraw()
    fireball = Image(Point(fireballX, fireballY), fireballAtual[c])
    fireball.draw(tela)
    c += 1
    if c >= len(fireballAtual):
        c = 0

    if fireball.getAnchor().getY() <= 110:
        fireball.undraw()
        fireball = Image(Point(charizardX+60, charizardY-60),
                         fireballAtual[c])
        fireball.draw(tela)

    # movimentação blastoise
    blastoise.move(velBlastoise, 0)
    blastoiseX = blastoise.getAnchor().getX()
    blastoiseY = blastoise.getAnchor().getY()
    if blastoise.getAnchor().getX() >= 1100 or blastoise.getAnchor().getX() <= 90:
        velBlastoise = velBlastoise*-1

    # movimentação watergun
    watergun.move(0, 16)
    watergunY = watergun.getAnchor().getY()
    watergunX = watergun.getAnchor().getX()
    watergun.undraw()
    watergun = Image(Point(watergunX, watergunY), watergunAtual[b])
    watergun.draw(tela)
    if watergun.getAnchor().getY() >= 730:
        watergun.undraw()
        watergun = Image(Point(blastoiseX, blastoiseY), watergunAtual[b])
        watergun.draw(tela)
    b += 1
    if b >= len(watergunAtual):
        b = 0

    # colisão fireball
    if posiçãoX > fireballX-25 and posiçãoX < fireballX+25 and posiçãoY < fireballY+30 and posiçãoY > fireballY-30:
        imagemPerdeu = Image(Point(600, 200), "telaPerdeu.gif")
        imagemPerdeu.draw(tela)
        textoPerdeu1 = Text(Point(600, 300), "Você perdeu!")
        textoPerdeu1.setSize(20)
        textoPerdeu1.setTextColor("yellow")
        textoPerdeu1.draw(tela)

        textoPerdeu2 = Text(
            Point(600, 330), "Aperte ESC para sair ou R para resetar")
        textoPerdeu2.setSize(15)
        textoPerdeu2.setTextColor("red")
        textoPerdeu2.draw(tela)

        while key != "r":

            if key == "Escape":
                tela.close()

            key = tela.checkKey()

    # colisão watergun
    if posiçãoX > watergunX-45 and posiçãoX < watergunX+45 and posiçãoY < watergunY+35 and posiçãoY > watergunY-35:
        imagemPerdeu = Image(Point(600, 200), "telaPerdeu.gif")
        imagemPerdeu.draw(tela)
        textoPerdeu1 = Text(Point(600, 300), "Você perdeu!")
        textoPerdeu1.setSize(20)
        textoPerdeu1.setTextColor("yellow")
        textoPerdeu1.draw(tela)
        textoPerdeu2 = Text(
            Point(600, 330), "Aperte ESC para sair ou R para resetar")
        textoPerdeu2.setSize(15)
        textoPerdeu2.setTextColor("red")
        textoPerdeu2.draw(tela)
        while key != "r":
            if key == "Escape":
                tela.close()

            key = tela.checkKey()

        # mensagem/gif tela final
    if pokePegas == 10:
        textoFinal1 = Text(Point(600, 300), "Parabéns! Você venceu!")
        textoFinal1.setSize(20)
        textoFinal1.setTextColor("yellow")
        textoFinal1.draw(tela)

        textoFinal2 = Text(
            Point(600, 330), "Aperte ESC para sair ou R para resetar")
        textoFinal2.setSize(15)
        textoFinal2.setTextColor("red")
        textoFinal2.draw(tela)
        if tempoS < tempoRecord or tempoRecord == 0:
            tempoRecord = trunc(tempoS)
            textoRecord = Text(
                Point(600, 370), "Você estabeleceu um novo recorde de " + str(tempoRecord)+" segundos")
            textoRecord.setTextColor("white")
            textoRecord.setSize(20)
            textoRecord.draw(tela)
        else:
            textoRecord = Text(
                Point(600, 370), "Tempo recorde: " + str(tempoRecord))
            textoRecord.setTextColor("white")
            textoRecord.setSize(20)
            textoRecord.draw(tela)

        i = 0
        while i < len(pikachuFinal):
            if 'pikachu' in locals():
                pikachu.undraw()
            pikachu = pikachuFinal[i]
            pikachu = Image(Point(600, 200), pikachu)
            pikachu.draw(tela)
            i += 1

            if i == len(pikachuFinal):
                i = 0
            update(8)

            key = tela.checkKey()
            if key == "Escape":
                tela.close()
            elif key == "r":
                break

    # timer
    timer.undraw()
    tempoS = time.time() - timeStart
    timeTrunc = trunc(tempoS)
    timer = Text(Point(100, 50), timeTrunc)
    timer.setSize(30)
    timer.setTextColor("black")
    timer.draw(tela)

    update(velocidadeUpdate)

    # função reset
    if key == "r" or key == "R":

        pokebola1.undraw()
        pokebola2.undraw()
        pokebola3.undraw()
        pokebola4.undraw()
        pokebola5.undraw()
        pokebola6.undraw()
        pokebola7.undraw()
        pokebola8.undraw()
        pokebola9.undraw()
        pokebola10.undraw()
        pokebola1 = Image(Point(250, 50), "pokebolaCinza.gif")
        pokebola1.draw(tela)
        pokebola2 = Image(Point(350, 50), "pokebolaCinza.gif")
        pokebola2.draw(tela)
        pokebola3 = Image(Point(450, 50), "pokebolaCinza.gif")
        pokebola3.draw(tela)
        pokebola4 = Image(Point(550, 50), "pokebolaCinza.gif")
        pokebola4.draw(tela)
        pokebola5 = Image(Point(650, 50), "pokebolaCinza.gif")
        pokebola5.draw(tela)
        pokebola6 = Image(Point(750, 50), "pokebolaCinza.gif")
        pokebola6.draw(tela)
        pokebola7 = Image(Point(850, 50), "pokebolaCinza.gif")
        pokebola7.draw(tela)
        pokebola8 = Image(Point(950, 50), "pokebolaCinza.gif")
        pokebola8.draw(tela)
        pokebola9 = Image(Point(1050, 50), "pokebolaCinza.gif")
        pokebola9.draw(tela)
        pokebola10 = Image(Point(1150, 50), "pokebolaCinza.gif")
        pokebola10.draw(tela)
        blastoise.undraw()
        watergun.undraw()
        charizard.undraw()
        fireball.undraw()
        menino.undraw()
        posiçãoY = 400
        posiçãoX = 600
        menino = Image(Point(600, 400), "baixo_1.gif")
        menino.draw(tela)
        pokebola.undraw()
        pokeY = (random.randrange(8, 19)*30)
        pokeX = (random.randrange(1, 40)*30)
        pokebola = Image(Point(pokeX, pokeY), "pokebola.png")
        pokebola.draw(tela)
        pokePegas = 0
        shinyChanceB = random.randrange(1, 81)
        if shinyChanceB == 1:
            spriteBlastoise = blastoiseSprite[1]
            watergunAtual = watergunShinySprites
        else:
            spriteBlastoise = blastoiseSprite[0]
            watergunAtual = watergunSprites
        inicialBlastoise = (random.randrange(1, 11)*100)
        blastoise = Image(Point(inicialBlastoise, 125), spriteBlastoise)
        blastoise.draw(tela)
        velBlastoise = -5
        watergun = Image(Point(inicialBlastoise, 125), watergunAtual[b])
        watergun.draw(tela)
        shinyChanceC = random.randrange(1, 81)
        if shinyChanceC == 1:
            spriteCharizard = charizardSprite[1]
            fireballAtual = fireballShinySprites
        else:
            spriteCharizard = charizardSprite[0]
            fireballAtual = fireballSprites

        inicialCharizard = (random.randrange(1, 11)*100)
        charizard = Image(Point(inicialCharizard, 640), spriteCharizard)
        charizard.draw(tela)
        velCharizard = 10
        fireball = Image(Point((inicialCharizard+60), 580), fireballAtual[c])
        fireball.draw(tela)
        if 'textoPerdeu1' in locals():
            textoPerdeu1.undraw()
        if 'textoPerdeu2' in locals():
            textoPerdeu2.undraw()
        if 'imagemPerdeu' in locals():
            imagemPerdeu.undraw()
        if 'pikachu' in locals():
            pikachu.undraw()
        if 'textoFinal1' in locals():
            textoFinal1.undraw()
        if 'textoFinal2' in locals():
            textoFinal2.undraw()
        if 'textoRecord' in locals():
            textoRecord.undraw()
        timeStart = time.time()
    key = tela.checkKey()
