import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
pg.display.set_caption('pygametest')

x = 250
posx = 350
y = posy = 300

running = True
while running:
    pg.time.delay(25)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    comando = pg.key.get_pressed()
    # comandos circulo vermelho
    if comando[ord('w')]:
        y -= 5
    if comando[ord('s')]:
        y += 5
    if comando[ord('a')]:
        x -= 5
    if comando[ord('d')]:
        x += 5

    # comandos circulo verde
    if comando[pg.K_UP]:
        posy -= 5
    if comando[pg.K_DOWN]:
        posy += 5
    if comando[pg.K_LEFT]:
        posx -= 5
    if comando[pg.K_RIGHT]:
        posx += 5

    if comando[pg.K_ESCAPE]:
        running = False

    # bordas do mapa
    if x < 0: x = 10
    if posx < 0: posx = 10
    if x > 600: x = 590
    if posx > 600: posx = 590
    if y < 0: y = 10
    if posy < 0: posy = 10
    if y > 600: y = 590
    if posy > 600: posy = 590

    if (posy-5) <= y <= (posy+5):
        if (posx+5) == (x-5) and comando[ord('a')]:
            posx -= 5
        if (posx-5) == (x+5) and comando[ord('d')]:
            posx += 5
    if (posx-5) <= x <= (posx+5):
        if (posy+5) == (y-5) and comando[ord('s')]:
            posy += 5
        if (posy-5) == (y+5) and comando[ord('w')]:
            posy -= 5

    if (y-5) <= posy <= (y+5):
        if (x+5) == (posx-5) and comando[pg.K_LEFT]:
            x -= 5
        if (x-5) == (posx+5) and comando[pg.K_RIGHT]:
            x += 5
    if (x-5) <= posx <= (x+5):
        if (y+5) == (posy-5) and comando[pg.K_DOWN]:
            y += 5
        if (y-5) == (posy+5) and comando[pg.K_UP]:
            y -= 5

    pg.draw.circle(screen, (255, 0, 0), (x, y), 10)
    pg.draw.circle(screen, (0, 255, 0), (posx, posy), 10)
    pg.display.update()
    screen.fill((0, 0, 0))

pg.quit()
