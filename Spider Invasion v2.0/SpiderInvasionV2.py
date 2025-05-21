import pyxel

class Jeu:

    def __init__(self):
        pyxel.init(256,256, title = "Spider Invasion")
        pyxel.mouse_x
        pyxel.mouse_y
        self.timer = 0
        self.projectiles = []
        self.spider = []
        self.spiderSpeed = 1
        self.spiderLife = 1
        self.spawn = [0, 256]
        self.max_spiders = 10
        self.compteurSpider = 0
        self.compteurTir = 0
        self.compteurTirTouche = 0
        self.score = 0
        self.pause = False
        pyxel.load("3.pyxres")
        self.life = 5
        pyxel.run(self.update, self.draw)
        
    def ajouter_projectile(self):
        self.projectiles.append(Projectile(self.player.x + 8,self.player.y+6,self.direction))        
    def update(self):
        if self.life == 0 or self.life < 0 :
            self.life = 0
        else:
            if pyxel.btnp(pyxel.KEY_ESCAPE):
                pyxel.quit()
            if pyxel.btnp(pyxel.KEY_P):
                self.pause = not self.pause
                
            if not self.pause:
                self.timer += 0.5
                
                self.player = Player(pyxel.mouse_x, pyxel.mouse_y, self.life)
                
                if len(self.spider) < self.max_spiders and int(self.timer / 10) > 5:
                    if self.compteurSpider < 15:
                        self.spider.append(Spider(self.spawn[pyxel.rndi(0,1)], self.spawn[pyxel.rndi(0,1)], self.spiderLife, self.spiderSpeed))
                    if self.compteurSpider >= 15:
                        self.spiderSpeed = 2
                        self.spider.append(Spider(self.spawn[pyxel.rndi(0,1)], self.spawn[pyxel.rndi(0,1)], self.spiderLife, self.spiderSpeed))
                    if self.compteurSpider >= 30:
                        self.spiderSpeed = 3
                        self.spider.append(Spider(self.spawn[pyxel.rndi(0,1)], self.spawn[pyxel.rndi(0,1)], self.spiderLife, self.spiderSpeed))
                    if self.compteurSpider >= 50:
                        self.spiderLife = 2
                        self.spider.append(Spider(self.spawn[pyxel.rndi(0,1)], self.spawn[pyxel.rndi(0,1)], self.spiderLife, self.spiderSpeed))
                    if self.compteurSpider >= 100:
                        self.spiderSpeed = 5
                        self.spider.append(Spider(self.spawn[pyxel.rndi(0,1)], self.spawn[pyxel.rndi(0,1)], self.spiderLife, self.spiderSpeed))
                        
                if self.timer%20 == 0 and int(self.timer / 10) > 5 and int(self.timer / 10) <= 20:
                    self.score += 50
                if self.timer%20 == 0 and int(self.timer / 10) > 20 and int(self.timer / 10) <= 40:
                    self.score += 100
                if self.timer%20 == 0 and int(self.timer / 10) > 40 and int(self.timer / 10) <= 60:
                    self.score += 150
                if self.timer%20 == 0 and int(self.timer / 10) > 60:
                    self.score += 200
                    
                if int(self.timer / 10) >= 15:
                    self.max_spiders = 20
                if int(self.timer / 10) >= 30:
                    self.max_spiders = 30
                if int(self.timer / 10) >= 60:
                    self.max_spiders = 50
                    
                if len(self.spider)>0:
                    for s in self.spider:
                        s.deplacement(self.player.x, self.player.y)
                        if s.collision(self.player.x, self.player.y) == True:
                            if self.timer%10 == 0:
                                self.life -= 1
                                
                if pyxel.btnp(pyxel.KEY_Z) :
                    self.shooting= True
                    self.direction = "z"
                    self.ajouter_projectile()
                    self.compteurTir += 1
                else:
                    self.shooting=False
                if pyxel.btnp(pyxel.KEY_D) and pyxel.btnp(pyxel.KEY_Z) :
                    self.shooting= True
                    self.direction = "zd"
                    self.ajouter_projectile()
                    self.compteurTir += 1
                else:
                    self.shooting=False
                if pyxel.btnp(pyxel.KEY_D):
                    self.shooting= True
                    self.direction = "d" 
                    self.ajouter_projectile()
                    self.compteurTir += 1
                else:
                    self.shooting=False
                if pyxel.btnp(pyxel.KEY_D)and pyxel.btnp(pyxel.KEY_S) :
                    self.shooting= True
                    self.direction = "ds"
                    self.ajouter_projectile()
                    self.compteurTir += 1
                else:
                    self.shooting=False
                if pyxel.btnp(pyxel.KEY_S) :
                    self.shooting= True
                    self.direction = "s"
                    self.ajouter_projectile()
                    self.compteurTir += 1
                else:
                    self.shooting=False
                if pyxel.btnp(pyxel.KEY_S) and pyxel.btnp(pyxel.KEY_Q) :
                    self.shooting= True
                    self.direction = "sq"
                    self.ajouter_projectile()
                    self.compteurTir += 1
                else:
                    self.shooting=False
                if pyxel.btnp(pyxel.KEY_Q):
                    self.shooting= True
                    self.direction = "q"
                    self.ajouter_projectile()
                    self.compteurTir += 1
                else:
                    self.shooting=False 
                if pyxel.btnp(pyxel.KEY_Q)and pyxel.btnp(pyxel.KEY_Z):
                    self.shooting= True
                    self.direction = "qz"
                    self.ajouter_projectile()
                    self.compteurTir += 1
                else:
                    self.shooting=False
            
                projectile_delete = []
                for p in range(len(self.projectiles)):
                    if self.projectiles[p].collision(self.projectiles[p].x, self.projectiles[p].y):
                        projectile_delete.append(p)
                for p in range(len(self.projectiles)):
                    for s in range(len(self.spider)):
                        if self.projectiles[p].collision_projectile_spider(self.spider[s].x, self.spider[s].y):
                            self.spider[s].life -= 1
                            projectile_delete.append(p)
                            self.compteurTirTouche += 1
                for i in reversed(sorted(set(projectile_delete))):
                    del self.projectiles[i]
                projectile_delete.clear()
                
                list_spider = []
                for i, s in enumerate(self.spider):
                    if s.life < 1:
                        list_spider.append(i)
                for i in reversed(list_spider):
                    del self.spider[i]
                    self.compteurSpider += 1
                    if self.compteurSpider <= 15 :
                        self.score += 100
                    if self.compteurSpider > 15 and self.compteurSpider <= 30:
                        self.score += 150
                    if self.compteurSpider > 30 and self.compteurSpider <= 50:
                        self.score += 200
                    if self.compteurSpider > 50 and self.compteurSpider <= 100:
                        self.score += 250
                    if self.compteurSpider > 100:
                        self.score += 300

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player.x, self.player.y, (1-1), 0, 8, 16, 16, 5)
        for s in self.spider:
            pyxel.blt(s.x, s.y, (1-1), 0, 120, 16, 16, 5)
        if len(self.projectiles)>0:
            for p in self.projectiles:
                p.update_pos()
                pyxel.blt(p.x, p.y, (1-1),42,10,4,4)
                
        timer = int(self.timer / 10)
        if timer > 5:
            pyxel.text(180, 10, "Temps ecoule : " + str(timer) + "s", 10)
            pyxel.text(10, 10, "Vie : " + str(self.life), 10)
            pyxel.text(90, 10, "Score : " + str(int(self.score)), 10)
        
        if self.compteurSpider >= 15 and self.compteurSpider <= 20:
            pyxel.text(95, 20, "Vitesse spiders +1", 10)
        if self.compteurSpider >= 30 and self.compteurSpider <= 37:
            pyxel.text(95, 20, "Vitesse spiders +2", 10)
        if self.compteurSpider >= 50 and self.compteurSpider <= 60:
            pyxel.text(98, 20, "Vie spiders x2", 10)
        if self.compteurSpider == 100 and self.compteurSpider <= 110:
            pyxel.text(94, 20, "Vitesse spiders max", 10)
        if timer <= 3:
            pyxel.text(95, 10, "Spider Invasion", 11)
            pyxel.text(55, 25, "by D.D.T.L (Digital Dream Team Labs)", 11)
        if timer <= 5:
            pyxel.text(8, 55, "Survivez avec ZQSD pour tirer et la souris pour vous deplacer", 7)
        if timer <= 5:
            pyxel.text(16, 70, "Utilisez 'P' pour mettre le jeu en pause ou le reprendre", 7)
        if timer <= 7:
            pyxel.text(32, 100, "Plus vous survivez et plus vous gagnez de points", 7)
        if timer <= 7:
            pyxel.text(19, 115, "Plus vous tuez de spiders et plus vous gagnez de points", 7)
        if timer >= 15 and timer <= 18:
            pyxel.text(95, 30, "Nombre spiders +10", 10)
        if timer >= 30 and timer <= 33:
            pyxel.text(95, 30, "Nombre spiders +10", 10)
        if timer >= 60 and timer <= 63:
            pyxel.text(95, 30, "Nombre spiders max", 10)
    
        if self.life == 0 or self.life < 0 :
            pyxel.cls(0)
            pyxel.rect(0,0,256,256,7)
            pyxel.text(102, 100, "Game Over", 1)
            pyxel.text(86, 110, "Score final : " + str(self.score), 1)
            pyxel.text(92, 130, "Kill fait : " + str(self.compteurSpider), 1)
            pyxel.text(90, 140, "Nombre tirs : " + str(self.compteurTir), 1)
            pyxel.text(75, 150, "Nombre tirs touches : " + str(self.compteurTirTouche), 1)
            if self.compteurTir != 0 and self.compteurTirTouche != 0:
                pyxel.text(85, 160, "Tirs touches : " + str(int(self.compteurTirTouche / self.compteurTir * 100)) + "%", 1)
                pyxel.text(79, 170, "Survecu pendant : " + str(timer) + "s", 1)
            else:
                pyxel.text(79, 160, "Survecu pendant : " + str(timer) + "s", 1)
    
class Player:
    def __init__(self, x, y, life):
        self.x = x
        self.y = y
        self.life = life
    
class Spider:
    def __init__(self, x, y, life, speed):
        self.x = x
        self.y = y
        self.life = life
        self.speed = speed
        
    def afficherVitesse(self):
        pyxel.text(30, 10, "Speed : " + str(self.speed), 10)

    def deplacement(self, playerX, playerY):
        angle = pyxel.atan2(playerY - self.y, playerX - self.x)
        self.x += pyxel.cos(angle) * self.speed
        self.y += pyxel.sin(angle) * self.speed

    def collision(self, xTest , yTest):
        if (xTest > self.x - 13 and xTest < self.x + 13 and yTest > self.y - 13 and yTest < self.y + 13):
            return True

class Projectile:
    def __init__(self, x,y, direction) -> None:
        self.x = x
        self.y = y
        self.speed = 5
        self.sprite = pyxel.blt(self.x, self.y, (1-1),42,10,4,4,5)
        self.direction = direction

    def collision_projectile_spider(self, x,y):
        if self.x < x + 13 and self.x + 4 > x and self.y < y + 13 and self.y + 4 > y :
            return True
        
    def collision(self, xTest, yTest):
        if xTest < 0 or xTest > pyxel.width - 4 - 4:
            return True
            
        if yTest < 0 or yTest > pyxel.height - 4 - 4:
            return True
    
    def update_pos(self):
        if self.direction == "z":
            self.y-= self.speed
        if self.direction == "zd":
            self.y-= self.speed
            self.x+= self.speed
        if self.direction == "d":
            self.x+= self.speed
        if self.direction == "ds":
            self.x+= self.speed
            self.y+= self.speed
        if self.direction == "s":
            self.y+= self.speed
        if self.direction =="sq":
            self.y+= self.speed
            self.x-= self.speed
        if self.direction =="q":
            self.x-=self.speed
        if self.direction =="qz":
            self.x-=self.speed
            self.y-=self.speed
            
Jeu()
