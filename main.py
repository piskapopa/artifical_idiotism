import pygame as pg
import isskustvennyj_idiotism as ii
import time
pg.init()
clock = pg.time.Clock()
class App:
    def main(self):
        self.pukpuk = time.time() + 0.2
        self._, self.ppp_shirina, self.ppp_vysota = ii.funktsiya("file")
        self.scx = 20
        self.scy = 20
        self.screen = pg.display.set_mode((20*self.ppp_shirina,20*self.ppp_vysota))
        self.dt = clock.tick(60) / 1000.0
        self.running = True
        for i in range(10):
            ii.main()
        while self.running: 
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    self.running = False
            if time.time() >= self.pukpuk:
                self.pukpuk = time.time() + 0.2
                napravlenie = ii.idiot_two(tuple(ii.sostoyanie["koordinaty"]), self.ppp_shirina, self.ppp_vysota, self._)
                ii.sostoyanie["koordinaty"] = list(ii.konstanty(napravlenie, ii.sostoyanie, self.ppp_shirina, self.ppp_vysota, self._)[0]["koordinaty"])
            self.draw()
            pg.display.flip()


    def draw(self):
        self.screen.fill("black")
        for i in range(self.ppp_vysota):
            for j in range(self.ppp_shirina):
                if self._[i][j] == '1':
                    pg.draw.rect(self.screen, "grey", (self.scx*j, self.scy*i, self.scx+1, self.scy+1))
                if self._[i][j] == '2':
                    pg.draw.rect(self.screen, "red", (self.scx*j, self.scy*i, self.scx+1, self.scy+1))
                if self._[i][j] == '3':
                    pg.draw.rect(self.screen, "green", (self.scx*j, self.scy*i, self.scx+1, self.scy+1))

        pg.draw.rect(self.screen, "blue", (self.scx*ii.sostoyanie["koordinaty"][1], self.scy*ii.sostoyanie["koordinaty"][0], self.scx+1, self.scy+1))

app = App()
app.main()