#Disaster simulator code
import random
import time
import pygame
import sys
import os
from pygame import mixer
        
class Game:
    def __init__(self,Upgrades):#function to initialse resources
        self.food = 0
        self.water = 0
        self.money = 0
        self.energy = 0
        self.medics = 0
        self.shelter = 0
        self.counter = 0
        self.day = 0
        self.continent_info = {}
        
    def resources(self):
        #This function will define the natural regen for resource generation
        self.counter += 1
        if self.counter == 25:
            self.day += 1
            self.counter = 0
        food_r = (self.food_u * 5) * (1 + (self.bigger_farm / 100))
        self.food += round(food_r)
                            
        water_r = (self.water_u * 10) * (1 + (self.water_station / 100))
        self.water += round(water_r)
                            
        money_r = (self.money_u * 100) * (1 + (self.bigger_bank / 100))
        self.money += round(money_r)
                            
        energy_r = (self.energy_u * 2) * (1 + (self.power_plant / 100))
        self.energy += round(energy_r)
                            
        medics_r = (self.medics_u * 1) * (1 + (self.bigger_school / 100))
        self.medics += round(medics_r)
                            
        shelter_r = (self.shelter_u * 3) * (1 + (self.bigger_factory / 100))
        self.shelter += round(shelter_r)
        
    def system(self):
        if Startup.fullscreen == True:
            screen2 = pygame.display.set_mode((1920, 1080))
            time_hud = pygame.Surface((300, 100))
            resource_hud = pygame.Surface((500,100))
            x = 1620
            y = 0
        elif Startup.fullscreen == False:
            screen2 = pygame.display.set_mode((1080,720))
            time_hud = pygame.Surface((200, 50))
            resource_hud = pygame.Surface((400,50))
            x = 880
            y = 0
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        start = 1
        last_time = pygame.time.get_ticks()
        time_hud.fill((255, 0, 0))
        resource_hud.fill((255, 0, 0))
        color = (199, 31, 12) #background colour of display
        screen2.fill(color)
        image = pygame.image.load('Mapnew.JPG') #pixel image for background
        image_rec = image.get_rect(center = screen2.get_rect().center)
        screen2.blit(image, image_rec)
        
        pygame.draw.polygon(screen2, (255, 0, 0),
                            [[500, 1070], [700, 970],
                             [700, 1070]])
        pygame.draw.polygon(screen2, (255, 0, 0),
                            [[1400, 1070], [1200, 970],
                             [1200, 1070]])
        pygame.draw.rect(screen2, color,
                         [1850, 125, 50, 50], 0)
        
        while self.play == True:
            mouse = pygame.mouse.get_pos()
            current_time = pygame.time.get_ticks()
            if current_time - last_time >= 1000:#loop for game's resources
                Defences.fastheal_system(self)
                Game.resources(self)
                last_time = current_time
                #code for resource bonus meteors go here...
                if start == 1:
                    spawned = False
                    clicked = False
                    bonus = False
                    start  = 0
                multiplier = 10
                chance = random.randint(1,10)
                bonus_image = pygame.image.load('bonus.PNG')
                if chance == 1 and spawned == False:
                    bonus = True
                    clicked = False
                    spawn_time = pygame.time.get_ticks()
                if bonus == True:
                    if Startup.fullscreen == True:#choose random co-ordinates on screen to blit image
                        x1 = random.randint(100, 1800)
                        y1 = random.randint(100, 980)
                        x2 = x1 + 50
                        y2 = y1 + 50
                        screen2.blit(bonus_image, (x1, y1))
                    elif Startup.fullscreen == False:
                        x1 = random.randint(100, 980)
                        y1 = random.randint(100, 620)
                        x2 = x1 + 50
                        y2 = y1 + 50
                        screen2.blit(bonus_image, (x1, y1))
                    spawned = True
                    bonus = False
                elif self.counter == 5 or self.counter == 10 or self.counter == 20 or self.counter == 15:
                    Game.event(self)

            time_hud.fill((255, 0, 0))
            resource_hud.fill((255, 0, 0))
            text7 = Startup.font.render(f"Time: {self.counter}:00", True, (0, 0, 0))
            textRec7 = text7.get_rect()
            textRec7.center = (100, 25)
            time_hud.blit(text7, textRec7)
            
            text8 = Startup.font.render(f"Day: {self.day}", True, (0, 0, 0))
            textRec8 = text8.get_rect()
            textRec8.center = (75, 75)
            time_hud.blit(text8, textRec8)
            
            text9_1 = Startup.font2.render("Europe", True, (0, 0, 0))#Start here: Show continent info
            text9_2 = "Population:" + str(self.Europe[1])
            text9_3 = Startup.font2.render(text9_2, True, (0, 0, 0))
            text9_4 = "Dead:" + str(self.Europe[2])
            text9_5 = Startup.font2.render(text9_4, True, (0, 0, 0))
            text9_6 = "Injured:" + str(self.Europe[3])
            text9_7 = Startup.font2.render(text9_6, True, (0, 0, 0))
            textRec9_1 = text9_1.get_rect()
            textRec9_1.center = (800, 275)
            screen2.blit(text9_1, textRec9_1)
            textRec9_3 = text9_3.get_rect()
            textRec9_3.center = (800, 300)
            screen2.blit(text9_3, textRec9_3)
            textRec9_5 = text9_5.get_rect()
            textRec9_5.center = (800, 325)
            screen2.blit(text9_5, textRec9_5)
            textRec9_7 = text9_7.get_rect()
            textRec9_7.center = (800, 350)
            screen2.blit(text9_7, textRec9_7)
            
            text10_1 = Startup.font2.render("N.America", True, (0, 0, 0))
            text10_2 = "Population:" + str(self.N_America[1])
            text10_3 = Startup.font2.render(text10_2, True, (0, 0, 0))
            text10_4 = "Dead:" + str(self.N_America[2])
            text10_5 = Startup.font2.render(text10_4, True, (0, 0, 0))
            text10_6 = "Injured:" + str(self.N_America[3])
            text10_7 = Startup.font2.render(text10_6, True, (0, 0, 0))
            textRec10_1 = text10_1.get_rect()
            textRec10_1.center = (250, 275)
            screen2.blit(text10_1, textRec10_1)
            textRec10_3 = text10_3.get_rect()
            textRec10_3.center = (250, 300)
            screen2.blit(text10_3, textRec10_3)
            textRec10_5 = text10_5.get_rect()
            textRec10_5.center = (250, 325)
            screen2.blit(text10_5, textRec10_5)
            textRec10_7 = text10_7.get_rect()
            textRec10_7.center = (250, 350)
            screen2.blit(text10_7, textRec10_7)
            
            text11_1 = Startup.font2.render("S.America", True, (0, 0, 0))
            text11_2 = "Population:" + str(self.S_America[1])
            text11_3 = Startup.font2.render(text11_2, True, (0, 0, 0))
            text11_4 = "Dead:" + str(self.S_America[2])
            text11_5 = Startup.font2.render(text11_4, True, (0, 0, 0))
            text11_6 = "Injured:" + str(self.S_America[3])
            text11_7 = Startup.font2.render(text11_6, True, (0, 0, 0))
            textRec11_1 = text11_1.get_rect()
            textRec11_1.center = (500, 675)
            screen2.blit(text11_1, textRec11_1)
            textRec11_3 = text11_3.get_rect()
            textRec11_3.center = (500, 700)
            screen2.blit(text11_3, textRec11_3)
            textRec11_5 = text11_5.get_rect()
            textRec11_5.center = (500, 725)
            screen2.blit(text11_5, textRec11_5)
            textRec11_7 = text11_7.get_rect()
            textRec11_7.center = (500, 750)
            screen2.blit(text11_7, textRec11_7)
            
            text12_1 = Startup.font2.render("Africa", True, (0, 0, 0))
            text12_2 = "Population:" + str(self.Africa[1])
            text12_3 = Startup.font2.render(text12_2, True, (0, 0, 0))
            text12_4 = "Dead:" + str(self.Africa[2])
            text12_5 = Startup.font2.render(text12_4, True, (0, 0, 0))
            text12_6 = "Injured:" + str(self.Africa[3])
            text12_7 = Startup.font2.render(text12_6, True, (0, 0, 0))
            textRec12_1 = text12_1.get_rect()
            textRec12_1.center = (900, 475)
            screen2.blit(text12_1, textRec12_1)
            textRec12_3 = text12_3.get_rect()
            textRec12_3.center = (900, 500)
            screen2.blit(text12_3, textRec12_3)
            textRec12_5 = text12_5.get_rect()
            textRec12_5.center = (900, 525)
            screen2.blit(text12_5, textRec12_5)
            textRec12_7 = text12_7.get_rect()
            textRec12_7.center = (900, 550)
            screen2.blit(text12_7, textRec12_7)
            
            text13_1 = Startup.font2.render("Asia", True, (0, 0, 0))
            text13_2 = "Population:" + str(self.Asia[1])
            text13_3 = Startup.font2.render(text13_2, True, (0, 0, 0))
            text13_4 = "Dead:" + str(self.Asia[2])
            text13_5 = Startup.font2.render(text13_4, True, (0, 0, 0))
            text13_6 = "Injured:" + str(self.Asia[3])
            text13_7 = Startup.font2.render(text13_6, True, (0, 0, 0))
            textRec13_1 = text13_1.get_rect()
            textRec13_1.center = (1300, 375)
            screen2.blit(text13_1, textRec13_1)
            textRec13_3 = text13_3.get_rect()
            textRec13_3.center = (1300, 400)
            screen2.blit(text13_3, textRec13_3)
            textRec13_5 = text13_5.get_rect()
            textRec13_5.center = (1300, 425)
            screen2.blit(text13_5, textRec13_5)
            textRec13_7 = text13_7.get_rect()
            textRec13_7.center = (1300, 450)
            screen2.blit(text13_7, textRec13_7)
            
            text14_1 = Startup.font2.render("Oceania", True, (0, 0, 0))
            text14_2 = "Population:" + str(self.Oceania[1])
            text14_3 = Startup.font2.render(text14_2, True, (0, 0, 0))
            text14_4 = "Dead:" + str(self.Oceania[2])
            text14_5 = Startup.font2.render(text14_4, True, (0, 0, 0))
            text14_6 = "Injured:" + str(self.Oceania[3])
            text14_7 = Startup.font2.render(text14_6, True, (0, 0, 0))
            textRec14_1 = text14_1.get_rect()
            textRec14_1.center = (1600, 775)
            screen2.blit(text14_1, textRec14_1)
            textRec14_3 = text14_3.get_rect()
            textRec14_3.center = (1600, 800)
            screen2.blit(text14_3, textRec14_3)
            textRec14_5 = text14_5.get_rect()
            textRec14_5.center = (1600, 825)
            screen2.blit(text14_5, textRec14_5)
            textRec14_7 = text14_7.get_rect()
            textRec14_7.center = (1600, 850)
            screen2.blit(text14_7, textRec14_7)#End here: show continent info

            upgradesimage = pygame.image.load('upgrades_m.PNG')
            screen2.blit(upgradesimage, (1860, 133))
            screen2.blit(time_hud, (x, y))
            
            defencesimage = pygame.image.load('defences_m.PNG')
            screen2.blit(defencesimage, (1860, 233))
            
            
            text1 = Startup.font.render(f'{self.food}', True, (0, 0, 0))#Will show the amount of food to the player
            textRec1 = text1.get_rect()
            textRec1.center = (75, 27)
            resource_hud.blit(text1, textRec1)
            foodimage = pygame.image.load('food_r.PNG')
            resource_hud.blit(foodimage, (0, 10))
            
            text2 = Startup.font.render(f'{self.water}', True, (0, 0, 0))#Will show the amount of water to the player
            textRec2 = text2.get_rect()
            textRec2.center = (75, 77)
            resource_hud.blit(text2, textRec2)
            waterimage = pygame.image.load('water_r.PNG')
            resource_hud.blit(waterimage, (0, 60))
        
            text3 = Startup.font.render(f'{self.money}', True, (0, 0, 0))#Will show the amount of money to the player
            textRec3 = text3.get_rect()
            textRec3.center = (225, 27)
            resource_hud.blit(text3, textRec3)
            moneyimage = pygame.image.load('money_r.PNG')
            resource_hud.blit(moneyimage, (150, 10))
        
            text4 = Startup.font.render(f'{self.energy}', True, (0, 0, 0))#Will show the amount of energy to the player
            textRec4 = text4.get_rect()
            textRec4.center = (225, 77)
            resource_hud.blit(text4, textRec4)
            energyimage = pygame.image.load('energy_r.PNG')
            resource_hud.blit(energyimage, (150, 60))
        
            text5 = Startup.font.render(f'{self.shelter}', True, (0, 0, 0))#Will show the amount of shelter to the player
            textRec5 = text5.get_rect()
            textRec5.center = (375, 27)
            resource_hud.blit(text5, textRec5)
            shelterimage = pygame.image.load('shelter_r.PNG')
            resource_hud.blit(shelterimage, (300, 10))

            text6 = Startup.font.render(f'{self.medics}', True, (0, 0, 0))#Will show the amount of medics to the player
            textRec6 = text6.get_rect()
            textRec6.center = (375, 77)
            resource_hud.blit(text6, textRec6)
            medicsimage = pygame.image.load('medics_r.PNG')
            resource_hud.blit(medicsimage, (300, 60))
            
            screen2.blit(resource_hud, (700, 970))
            pygame.display.flip()
            
            pygame.draw.rect(screen2, color,[1850, 125, 50, 50])#code to toggle upgrade menu
            if 1850 <= mouse[0] <= 1900 and 125 <= mouse[1] <= 175:
                pygame.draw.rect(screen2, (255, 128, 128),
                                 [1850, 125, 50, 50])
                pygame.draw.rect(screen2, (255, 0, 0),
                                 [1850, 125, 50, 50], 3)
            else:
                pygame.draw.rect(screen2, (255, 0, 0), [1850, 125, 50, 50], 3)
            pygame.display.update()
            
            pygame.draw.rect(screen2, color,[1850, 225, 50, 50])#code to toggle defences menu
            if 1850 <= mouse[0] <= 1900 and 225 <= mouse[1] <= 275:
                pygame.draw.rect(screen2, (255, 128, 128),
                                 [1850, 225, 50, 50])
                pygame.draw.rect(screen2, (255, 0, 0),
                                 [1850, 225, 50, 50], 3)
            else:
                pygame.draw.rect(screen2, (255, 0, 0), [1850, 225, 50, 50], 3)
            pygame.display.update()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 1850 <= mouse[0] <= 1900 and 125 <= mouse[1] <= 175:
                        Upgrades.purchase_u(self)
                    elif 1850 <= mouse[0] <= 1900 and 225 <= mouse[1] <= 275:
                        Defences.purchase_d(self)
                    elif spawned == True and clicked == False and x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
                        clicked = True
                        spawned = False
                        clicked_time = pygame.time.get_ticks()
                        live_time = spawn_time / clicked_time #variable to show difference in time between the spawn and click of the meteor
                        if live_time > 0.9:
                            multiplier = 3
                        elif live_time > 0.6 and live_time < 0.9:
                            multiplier = 2
                        elif live_time > 0.3 and live_time < 0.6:
                            multiplier = 1
                        elif live_time > 0 and live_time < 0.3:
                            multiplier = 0.5
                        resource_chance = random.randint(1,6)
                        if resource_chance == 1:
                            self.food += 70 * multiplier
                        elif resource_chance == 2:
                            self.water += 70 * multiplier
                        elif resource_chance == 3:
                            self.money += 300 * multiplier
                        elif resource_chance == 4:
                            self.energy += 20 * multiplier
                        elif resource_chance == 5:
                            self.medics += 5 * multiplier
                        elif resource_chance == 6:
                            self.shelter += 3 * multiplier
                        Game.system(self)
                        
    def disasters(self):
        #using a tuple as i do not need to change this data at any point
        self.disasters = ("Tornado", "Tsunami", "Earthquake", "Hurricane", "Wildfire", "Volcano")
        self.Tornado = ("Tornado", "Asia", "Oceania")
        self.Tsunami = ("Tsunami", "N_America", "Africa")
        self.Earthquake = ("Earthquake", "Europe", "S_America")
        self.Hurricane = ("Hurricane", "Africa", "N_America")
        self.Wildfire = ("Wildfire", "Oceania", "Europe")
        self.Volcano = ("Volcano", "S_America", "Asia")


    def event(self):
        if Startup.fullscreen == True:
            screen5 = pygame.display.set_mode((1920, 1080))
            time_hud = pygame.Surface((300, 100))
            resource_hud = pygame.Surface((500,100))
            x = 1620
            y = 0
        elif Startup.fullscreen == False:
            screen5 = pygame.display.set_mode((1080,720))
            time_hud = pygame.Surface((200, 50))
            resource_hud = pygame.Surface((400,50))
            x = 880
            y = 0
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        color = (199, 31, 12)
        old_pop = 0
        old_dead = 0
        old_injured = 0
        event_pop = 0
        event_dead = 0
        event_injured = 0
        event_total = 0
        disaster_strength = 0
        chance = random.randint(1,2)    
        if chance == 1:
            current_disaster = random.choice(self.disasters)
            current_location = random.choice(self.continents)
            if current_disaster == self.Tornado[0]:#Start here: loops to decide how impactful a disaster is
                if current_location == self.Tornado[1]:
                    disaster_strength = 2 * self.day - self.tornado_shelter
                    old_pop = self.Asia[1]
                    old_dead = self.Asia[2]
                    old_injured = self.Asia[3]
                    event_total = self.Asia[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.Asia[1] = old_pop - event_pop
                    self.Asia[2] = old_dead + event_dead
                    self.Asia[3] = old_injured + event_injured
                elif current_location == self.Tornado[2]:
                    disaster_strength = 0.5 * self.day - self.tornado_shelter
                    old_pop = self.Oceania[1]
                    old_dead = self.Oceania[2]
                    old_injured = self.Oceania[3]
                    event_total = self.Oceania[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.Oceania[1] = old_pop - event_pop
                    self.Oceania[2] = old_dead + event_dead
                    self.Oceania[3] = old_injured + event_injured
                else:
                    disaster_strength = 1 * self.day - self.tornado_shelter
                    old_pop = (getattr(self, current_location))[1]
                    old_dead = (getattr(self, current_location))[2]
                    old_injured = (getattr(self, current_location))[3]
                    event_total = (getattr(self, current_location))[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    (getattr(self, current_location))[1] = old_pop - event_pop
                    (getattr(self, current_location))[2] = old_dead + event_dead
                    (getattr(self, current_location))[3] = old_injured + event_injured

            elif current_disaster == self.Tsunami[0]:
                if current_location == self.Tsunami[1]:
                    disaster_strength = 2 * self.day - self.sea_wall
                    old_pop = self.N_America[1]
                    old_dead = self.N_America[2]
                    old_injured = self.N_America[3]
                    event_total = self.N_America[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.N_America[1] = old_pop - event_pop
                    self.N_America[2] = old_dead + event_dead
                    self.N_America[3] = old_injured + event_injured
                elif current_location == self.Tsunami[2]:
                    disaster_strength = 0.5 * self.day - self.sea_wall
                    old_pop = self.Africa[1]
                    old_dead = self.Africa[2]
                    old_injured = self.Africa[3]
                    event_total = self.Africa[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.Africa[1] = old_pop - event_pop
                    self.Africa[2] = old_dead + event_dead
                    self.Africa[3] = old_injured + event_injured
                else:
                    disaster_strength = 1 * self.day - self.sea_wall
                    old_pop = (getattr(self, current_location))[1]
                    old_dead = (getattr(self, current_location))[2]
                    old_injured = (getattr(self, current_location))[3]
                    event_total = (getattr(self, current_location))[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    (getattr(self, current_location))[1] = old_pop - event_pop
                    (getattr(self, current_location))[2] = old_dead + event_dead
                    (getattr(self, current_location))[3] = old_injured + event_injured
                    
            elif current_disaster == self.Earthquake[0]:
                if current_location == self.Earthquake[1]:
                    disaster_strength = 2 * self.day - self.shock_absorber
                    old_pop = self.Europe[1]
                    old_dead = self.Europe[2]
                    old_injured = self.Europe[3]
                    event_total = self.Europe[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.Europe[1] = old_pop - event_pop
                    self.Europe[2] = old_dead + event_dead
                    self.Europe[3] = old_injured + event_injured
                elif current_location == self.Earthquake[2]:
                    disaster_strength = 0.5 * self.day - self.shock_absorber
                    old_pop = self.S_America[1]
                    old_dead = self.S_America[2]
                    old_injured = self.S_America[3]
                    event_total = self.S_America[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.S_America[1] = old_pop - event_pop
                    self.S_America[2] = old_dead + event_dead
                    self.S_America[3] = old_injured + event_injured
                else:
                    disaster_strength = 1 * self.day - self.shock_absorber
                    old_pop = (getattr(self, current_location))[1]
                    old_dead = (getattr(self, current_location))[2]
                    old_injured = (getattr(self, current_location))[3]
                    event_total = (getattr(self, current_location))[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    (getattr(self, current_location))[1] = old_pop - event_pop
                    (getattr(self, current_location))[2] = old_dead + event_dead
                    (getattr(self, current_location))[3] = old_injured + event_injured
                    
            elif current_disaster == self.Hurricane[0]:
                if current_location == self.Hurricane[1]:
                    disaster_strength = 2 * self.day - self.stronger_house
                    old_pop = self.Africa[1]
                    old_dead = self.Africa[2]
                    old_injured = self.Africa[3]
                    event_total = self.Africa[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.Africa[1] = old_pop - event_pop
                    self.Africa[2] = old_dead + event_dead
                    self.Africa[3] = old_injured + event_injured
                elif current_location == self.Hurricane[2]:
                    disaster_strength = 0.5 * self.day - self.stronger_house
                    old_pop = self.N_America[1]
                    old_dead = self.N_America[2]
                    old_injured = self.N_America[3]
                    event_total = self.N_America[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.N_America[1] = old_pop - event_pop
                    self.N_America[2] = old_dead + event_dead
                    self.N_America[3] = old_injured + event_injured
                else:
                    disaster_strength = 1 * self.day - self.stronger_house
                    old_pop = (getattr(self, current_location))[1]
                    old_dead = (getattr(self, current_location))[2]
                    old_injured = (getattr(self, current_location))[3]
                    event_total = (getattr(self, current_location))[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    (getattr(self, current_location))[1] = old_pop - event_pop
                    (getattr(self, current_location))[2] = old_dead + event_dead
                    (getattr(self, current_location))[3] = old_injured + event_injured
                    
            elif current_disaster == self.Wildfire[0]:
                if current_location == self.Wildfire[1]:
                    disaster_strength = 2 * self.day - self.fire_station
                    old_pop = self.Oceania[1]
                    old_dead = self.Oceania[2]
                    old_injured = self.Oceania[3]
                    event_total = self.Oceania[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.Oceania[1] = old_pop - event_pop
                    self.Oceania[2] = old_dead + event_dead
                    self.Oceania[3] = old_injured + event_injured

                elif current_location == self.Wildfire[2]:
                    disaster_strength = 0.5 * self.day - self.fire_station
                    old_pop = self.Europe[1]
                    old_dead = self.Europe[2]
                    old_injured = self.Europe[3]
                    event_total = self.Europe[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.Europe[1] = old_pop - event_pop
                    self.Europe[2] = old_dead + event_dead
                    self.Europe[3] = old_injured + event_injured

                else:
                    disaster_strength = 1 * self.day - self.fire_station
                    old_pop = (getattr(self, current_location))[1]
                    old_dead = (getattr(self, current_location))[2]
                    old_injured = (getattr(self, current_location))[3]
                    event_total = (getattr(self, current_location))[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    (getattr(self, current_location))[1] = old_pop - event_pop
                    (getattr(self, current_location))[2] = old_dead + event_dead
                    (getattr(self, current_location))[3] = old_injured + event_injured
                    
            elif current_disaster == self.Volcano[0]:
                if current_location == self.Volcano[1]:
                    disaster_strength = 2 * self.day - self.tornado_shelter
                    old_pop = self.S_America[1]
                    old_dead = self.S_America[2]
                    old_injured = self.S_America[3]
                    event_total = self.S_America[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.S_America[1] = old_pop - event_pop
                    self.S_America[2] = old_dead + event_dead
                    self.S_America[3] = old_injured + event_injured
                elif current_location == self.Volcano[2]:
                    disaster_strength = 0.5 * self.day - self.tornado_shelter
                    old_pop = self.Asia[1]
                    old_dead = self.Asia[2]
                    old_injured = self.Asia[3]
                    event_total = self.Asia[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    self.Asia[1] = old_pop - event_pop
                    self.Asia[2] = old_dead + event_dead
                    self.Asia[3] = old_injured + event_injured
                else:
                    disaster_strength = 1 * self.day - self.tornado_shelter
                    old_pop = (getattr(self, current_location))[1]
                    old_dead = (getattr(self, current_location))[2]
                    old_injured = (getattr(self, current_location))[3]
                    event_total = (getattr(self, current_location))[1] * (disaster_strength/100) 
                    event_pop = (event_total / 4) * 2
                    event_dead = (event_total / 4)
                    event_injured = (event_total / 4)
                    (getattr(self, current_location))[1] = old_pop - event_pop
                    (getattr(self, current_location))[2] = old_dead + event_dead
                    (getattr(self, current_location))[3] = old_injured + event_injured
            Game.system(self)

    def world(self):
        #using a list as the data needs to be changed over time, exception of all continent names being in a tuple
        self.continents = ("Europe", "N_America", "S_America", "Africa", "Asia", "Oceania")
        self.Europe = ["Europe", 750000000, 0, 0]
        self.N_America = ["N_America", 579000000, 0, 0]
        self.S_America = ["S_America", 422000000, 0, 0]
        self.Africa = ["Africa", 1216000000, 0, 0]
        self.Asia = ["Asia", 4561000000, 0, 0]
        self.Oceania = ["Oceania", 46000000, 0, 0]

class Defences:
    def __init__(self):
        self.fast_heal = 0 #increase injured recovery speed
        self.bigger_farm = 0 #increase food production
        self.water_station = 0 #increase water production
        self.power_plant = 0 #increase energy production
        self.bigger_bank = 0 #increase money production
        self.bigger_school = 0 #increase medics production
        self.bigger_factory = 0 #increase shelter production
        self.shock_absorber = 0 #decrease earthquake damage
        self.sea_wall = 0 #decrease tsunami damage
        self.lava_barrier = 0 #decrease volcano damage
        self.tornado_shelter = 0 #decrease tornado damage
        self.fire_station = 0 #decrease wildfire damage
        self.stronger_house = 0 #decrease hurricane damage
        
    #defences functions build here e.g. fastheal ect
    
    def fastheal_system(self):#function used to replace a portion of injured with population
        current_injured = 0
        current_healed = 0
        
        current_injured = self.Europe[3]
        current_healed = round(current_injured) * (self.fast_heal / 100)
        self.Europe[3] -= round(current_healed)

        current_injured = self.N_America[3]
        current_healed = round(current_injured) * (self.fast_heal / 100)
        self.N_America[3] -= round(current_healed)
        
        current_injured = self.S_America[3]
        current_healed = round(current_injured) * (self.fast_heal / 100)
        self.S_America[3] -= round(current_healed)
        
        current_injured = self.Africa[3]
        current_healed = round(current_injured) * (self.fast_heal / 100)
        self.Africa[3] -= round(current_healed)

        current_injured = self.Asia[3]
        current_healed = round(current_injured) * (self.fast_heal / 100)
        self.Asia[3] -= round(current_healed)

        current_injured = self.Oceania[3]
        current_healed = round(current_injured) * (self.fast_heal / 100)
        self.Oceania[3] -= round(current_healed)

    def purchase_d(self):
        #In this function variables ending _c are the cost variables - how much of a resource needed to purchase and upgrade
        #Formatted as (resource being upgraded)_(resource being used in the upgrade)_c
        if Startup.fullscreen == True:
            screen4 = pygame.display.set_mode((1920, 1080))
        elif Startup.fullscreen == False:
            screen4 = pygame.display.set_mode((1080,720))
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        color = (135, 206, 235)
        screen4.fill(color)
        text16 = Startup.font.render("Purchase", True, (0, 0, 0))
        
        foodimage = pygame.image.load('food_r.PNG')
        waterimage = pygame.image.load('water_r.PNG')
        moneyimage = pygame.image.load('money_r.PNG')
        energyimage = pygame.image.load('energy_r.PNG')
        shelterimage = pygame.image.load('shelter_r.PNG')
        medicsimage = pygame.image.load('medics_r.PNG')
        
        text1 = Startup.font.render(f"Fast heal level:{self.fast_heal}", True, (0, 0, 0))
        textRec1 = text1.get_rect()
        textRec1.center = (200, 75)
        screen4.blit(text1, textRec1)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [125, 100, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [125, 300, 200, 50], 3)
        screen4.blit(medicsimage, (150, 125))
        screen4.blit(shelterimage, (150, 175))
        screen4.blit(moneyimage, (150, 225))
        
        fastheal_medics_c = (self.fast_heal + self.medics_u) *1
        fastheal_shelter_c = (self.fast_heal + self.shelter_u) *1
        fastheal_money_c = (self.money_u + self.food_u) *1
        
        text1_1 = Startup.font.render(f"{fastheal_medics_c}", True, (0, 0, 0))
        textRec1_1 = text1_1.get_rect()
        textRec1_1.center = (225, 140)
        screen4.blit(text1_1, textRec1_1)
        text1_2 = Startup.font.render(f"{fastheal_shelter_c}", True, (0, 0, 0))
        textRec1_2 = text1_2.get_rect()
        textRec1_2.center = (225, 190)
        screen4.blit(text1_2, textRec1_2)
        text1_3 = Startup.font.render(f"{fastheal_money_c}", True, (0, 0, 0))
        textRec1_3 = text1_3.get_rect()
        textRec1_3.center = (225, 240)
        screen4.blit(text1_3, textRec1_3)
        
        text2 = Startup.font.render(f"Bigger farm level:{self.bigger_farm}", True, (0, 0, 0))
        textRec2 = text2.get_rect()
        textRec2.center = (475, 75)
        screen4.blit(text2, textRec2)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [425, 100, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [425, 300, 200, 50], 3)
        screen4.blit(foodimage, (450, 125))
        screen4.blit(waterimage, (450, 175))
        screen4.blit(moneyimage, (450, 225))
        
        biggerfarm_food_c = (self.bigger_farm + self.food_u) *20
        biggerfarm_water_c = (self.bigger_farm + self.water_u) *20
        biggerfarm_money_c = (self.bigger_farm + self.money_u) *200
        
        text2_1 = Startup.font.render(f"{biggerfarm_food_c}", True, (0, 0, 0))
        textRec2_1 = text2_1.get_rect()
        textRec2_1.center = (525, 140)
        screen4.blit(text2_1, textRec2_1)
        text2_2 = Startup.font.render(f"{biggerfarm_water_c}", True, (0, 0, 0))
        textRec2_2 = text2_2.get_rect()
        textRec2_2.center = (525, 190)
        screen4.blit(text2_2, textRec2_2)
        text2_3 = Startup.font.render(f"{biggerfarm_money_c}", True, (0, 0, 0))
        textRec2_3 = text2_3.get_rect()
        textRec2_3.center = (525, 240)
        screen4.blit(text2_3, textRec2_3)
        
        text3 = Startup.font.render(f"Water station level:{self.water_station}", True, (0, 0, 0))
        textRec3 = text3.get_rect()
        textRec3.center = (775, 75)
        screen4.blit(text3, textRec3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [725, 100, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [725, 300, 200, 50], 3)
        screen4.blit(waterimage, (750, 125))
        screen4.blit(energyimage, (750, 175))
        screen4.blit(moneyimage, (750, 225))
        
        waterstation_water_c = (self.water_station + self.water_u) *50
        waterstation_energy_c = (self.water_station + self.shelter_u) *20
        waterstation_money_c = (self.water_station + self.money_u) *200
        
        text3_1 = Startup.font.render(f"{waterstation_water_c}", True, (0, 0, 0))
        textRec3_1 = text3_1.get_rect()
        textRec3_1.center = (825, 140)
        screen4.blit(text3_1, textRec3_1)
        text3_2 = Startup.font.render(f"{waterstation_energy_c}", True, (0, 0, 0))
        textRec3_2 = text3_2.get_rect()
        textRec3_2.center = (825, 190)
        screen4.blit(text3_2, textRec3_2)
        text3_3 = Startup.font.render(f"{waterstation_money_c}", True, (0, 0, 0))
        textRec3_3 = text3_3.get_rect()
        textRec3_3.center = (825, 240)
        screen4.blit(text3_3, textRec3_3)
        
        text4 = Startup.font.render(f"Power plant level:{self.water_station}", True, (0, 0, 0))
        textRec4 = text4.get_rect()
        textRec4.center = (1075, 75)
        screen4.blit(text4, textRec4)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [1025, 100, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [1025, 300, 200, 50], 3)
        screen4.blit(energyimage, (1050, 125))
        screen4.blit(shelterimage, (1050, 175))
        screen4.blit(moneyimage, (1050, 225))
        
        powerplant_energy_c = (self.power_plant + self.energy_u) *50
        powerplant_shelter_c = (self.power_plant + self.shelter_u) *20
        powerplant_money_c = (self.power_plant + self.money_u) *200
        
        text4_1 = Startup.font.render(f"{powerplant_energy_c}", True, (0, 0, 0))
        textRec4_1 = text4_1.get_rect()
        textRec4_1.center = (1125, 140)
        screen4.blit(text4_1, textRec4_1)
        text4_2 = Startup.font.render(f"{powerplant_shelter_c}", True, (0, 0, 0))
        textRec4_2 = text4_2.get_rect()
        textRec4_2.center = (1125, 190)
        screen4.blit(text4_2, textRec4_2)
        text4_3 = Startup.font.render(f"{powerplant_money_c}", True, (0, 0, 0))
        textRec4_3 = text4_3.get_rect()
        textRec4_3.center = (1125, 240)
        screen4.blit(text4_3, textRec4_3)
        
        text5 = Startup.font.render(f"Bigger bank level:{self.bigger_bank}", True, (0, 0, 0))
        textRec5 = text5.get_rect()
        textRec5.center = (1375, 75)
        screen4.blit(text5, textRec5)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [1325, 100, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [1325, 300, 200, 50], 3)
        screen4.blit(shelterimage, (1350, 105))
        screen4.blit(medicsimage, (1350, 145))
        screen4.blit(foodimage, (1350, 185))
        screen4.blit(waterimage, (1350, 225))
        screen4.blit(moneyimage, (1350, 265))
        
        biggerbank_shelter_c = (self.bigger_bank + self.shelter_u) * 20
        biggerbank_medics_c = (self.bigger_bank + self.medics_u) * 20
        biggerbank_food_c = (self.bigger_bank + self.food_u) * 50
        biggerbank_water_c = (self.bigger_bank + self.water_u) * 50
        biggerbank_money_c = (self.bigger_bank + self.money_u) * 200
        
        text5_1 = Startup.font.render(f"{biggerbank_shelter_c}", True, (0, 0, 0))
        textRec5_1 = text5_1.get_rect()
        textRec5_1.center = (1425, 120)
        screen4.blit(text5_1, textRec5_1)
        text5_2 = Startup.font.render(f"{biggerbank_medics_c}", True, (0, 0, 0))
        textRec5_2 = text5_2.get_rect()
        textRec5_2.center = (1425, 160)
        screen4.blit(text5_2, textRec5_2)
        text5_3 = Startup.font.render(f"{biggerbank_food_c}", True, (0, 0, 0))
        textRec5_3 = text5_3.get_rect()
        textRec5_3.center = (1425, 200)
        screen4.blit(text5_3, textRec5_3)
        text5_4 = Startup.font.render(f"{biggerbank_water_c}", True, (0, 0, 0))
        textRec5_4 = text5_4.get_rect()
        textRec5_4.center = (1425, 240)
        screen4.blit(text5_4, textRec5_4)
        text5_5 = Startup.font.render(f"{biggerbank_money_c}", True, (0, 0, 0))
        textRec5_5 = text5_5.get_rect()
        textRec5_5.center = (1425, 280)
        screen4.blit(text5_5, textRec5_5)
        
        text6 = Startup.font.render(f"Bigger school level:{self.bigger_school}", True, (0, 0, 0))
        textRec6 = text6.get_rect()
        textRec6.center = (175, 400)
        screen4.blit(text6, textRec6)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [125, 450, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [125, 650, 200, 50], 3)
        screen4.blit(foodimage, (150, 475))
        screen4.blit(energyimage, (150, 525))
        screen4.blit(moneyimage, (150, 575))
        
        biggerschool_food_c = (self.bigger_school + self.food_u) *50
        biggerschool_energy_c = (self.bigger_school + self.energy_u) *20
        biggerschool_money_c = (self.bigger_school + self.money_u) *200
        
        text6_1 = Startup.font.render(f"{biggerschool_food_c}", True, (0, 0, 0))
        textRec6_1 = text6_1.get_rect()
        textRec6_1.center = (225, 490)
        screen4.blit(text6_1, textRec6_1)
        text6_2 = Startup.font.render(f"{biggerschool_energy_c}", True, (0, 0, 0))
        textRec6_2 = text6_2.get_rect()
        textRec6_2.center = (225, 540)
        screen4.blit(text6_2, textRec6_2)
        text6_3 = Startup.font.render(f"{biggerschool_money_c}", True, (0, 0, 0))
        textRec6_3 = text6_3.get_rect()
        textRec6_3.center = (225, 590)
        screen4.blit(text6_3, textRec6_3)
        
        text7 = Startup.font.render(f"Bigger factory level:{self.bigger_factory}", True, (0, 0, 0))
        textRec7 = text7.get_rect()
        textRec7.center = (500, 400)
        screen4.blit(text7, textRec7)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [425, 450, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [425, 650, 200, 50], 3)
        screen4.blit(medicsimage, (450, 475))
        screen4.blit(foodimage, (450, 525))
        screen4.blit(moneyimage, (450, 575))
        
        biggerfactory_medics_c = (self.bigger_factory + self.medics_u) * 20
        biggerfactory_food_c = (self.bigger_factory + self.food_u) * 70
        biggerfactory_money_c = (self.bigger_factory + self.money_u) * 200
        
        text7_1 = Startup.font.render(f"{biggerfactory_medics_c}", True, (0, 0, 0))
        textRec7_1 = text7_1.get_rect()
        textRec7_1.center = (525, 490)
        screen4.blit(text7_1, textRec7_1)
        text7_2 = Startup.font.render(f"{biggerfactory_food_c}", True, (0, 0, 0))
        textRec7_2 = text7_2.get_rect()
        textRec7_2.center = (525, 540)
        screen4.blit(text7_2, textRec7_2)
        text7_3 = Startup.font.render(f"{biggerfactory_money_c}", True, (0, 0, 0))
        textRec7_3 = text7_3.get_rect()
        textRec7_3.center = (525, 590)
        screen4.blit(text7_3, textRec7_3)
        
        text8 = Startup.font.render(f"Shock absorber level:{self.shock_absorber}", True, (0, 0, 0))
        textRec8 = text8.get_rect()
        textRec8.center = (825, 400)
        screen4.blit(text8, textRec8)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [725, 450, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [725, 650, 200, 50], 3)
        screen4.blit(energyimage, (750, 475))
        screen4.blit(waterimage, (750, 525))
        screen4.blit(moneyimage, (750, 575))
        
        shockabsorber_energy_c = (self.shock_absorber + self.energy_u) * 20
        shockabsorber_water_c = (self.shock_absorber + self.water_u) * 80
        shockabsorber_money_c = (self.shock_absorber + self.money_u) * 200
        
        text8_1 = Startup.font.render(f"{shockabsorber_energy_c}", True, (0, 0, 0))
        textRec8_1 = text8_1.get_rect()
        textRec8_1.center = (825, 490)
        screen4.blit(text8_1, textRec8_1)
        text8_2 = Startup.font.render(f"{shockabsorber_water_c}", True, (0, 0, 0))
        textRec8_2 = text8_2.get_rect()
        textRec8_2.center = (825, 540)
        screen4.blit(text8_2, textRec8_2)
        text8_3 = Startup.font.render(f"{shockabsorber_money_c}", True, (0, 0, 0))
        textRec8_3 = text8_3.get_rect()
        textRec8_3.center = (825, 590)
        screen4.blit(text8_3, textRec8_3)
        
        text9 = Startup.font.render(f"Sea wall level:{self.sea_wall}", True, (0, 0, 0))
        textRec9 = text9.get_rect()
        textRec9.center = (1125, 400)
        screen4.blit(text9, textRec9)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [1025, 450, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [1025, 650, 200, 50], 3)
        screen4.blit(energyimage, (1050, 475))
        screen4.blit(waterimage, (1050, 525))
        screen4.blit(moneyimage, (1050, 575))
        
        seawall_medics_c = (self.sea_wall + self.medics_u) * 20
        seawall_water_c = (self.sea_wall + self.water_u) * 50
        seawall_money_c = (self.sea_wall + self.money_u) * 200
        
        text9_1 = Startup.font.render(f"{seawall_medics_c}", True, (0, 0, 0))
        textRec9_1 = text9_1.get_rect()
        textRec9_1.center = (1125, 490)
        screen4.blit(text9_1, textRec9_1)
        text9_2 = Startup.font.render(f"{seawall_water_c}", True, (0, 0, 0))
        textRec9_2 = text9_2.get_rect()
        textRec9_2.center = (1125, 540)
        screen4.blit(text9_2, textRec9_2)
        text9_3 = Startup.font.render(f"{seawall_money_c}", True, (0, 0, 0))
        textRec9_3 = text9_3.get_rect()
        textRec9_3.center = (1125, 590)
        screen4.blit(text9_3, textRec9_3)
        
        text10 = Startup.font.render(f"Lava barrier level:{self.lava_barrier}", True, (0, 0, 0))
        textRec10 = text10.get_rect()
        textRec10.center = (1400, 400)
        screen4.blit(text10, textRec10)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [1325, 450, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [1325, 650, 200, 50], 3)
        screen4.blit(medicsimage, (1350, 475))
        screen4.blit(waterimage, (1350, 525))
        screen4.blit(shelterimage, (1350, 575))
        
        lavabarrier_medics_c = (self.lava_barrier + self.medics_u) * 20
        lavabarrier_water_c = (self.lava_barrier + self.water_u) * 50
        lavabarrier_shelter_c = (self.lava_barrier + self.shelter_u) * 200
        
        text10_1 = Startup.font.render(f"{lavabarrier_medics_c}", True, (0, 0, 0))
        textRec10_1 = text10_1.get_rect()
        textRec10_1.center = (1425, 490)
        screen4.blit(text10_1, textRec10_1)
        text10_2 = Startup.font.render(f"{lavabarrier_water_c}", True, (0, 0, 0))
        textRec10_2 = text10_2.get_rect()
        textRec10_2.center = (1425, 540)
        screen4.blit(text10_2, textRec10_2)
        text10_3 = Startup.font.render(f"{lavabarrier_shelter_c}", True, (0, 0, 0))
        textRec10_3 = text10_3.get_rect()
        textRec10_3.center = (1425, 590)
        screen4.blit(text10_3, textRec10_3)
        
        text11 = Startup.font.render(f"Lava barrier level:{self.tornado_shelter}", True, (0, 0, 0))
        textRec11 = text11.get_rect()
        textRec11.center = (200, 725)
        screen4.blit(text11, textRec11)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [125, 750, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [125, 950, 200, 50], 3)
        screen4.blit(foodimage, (150, 775))
        screen4.blit(waterimage, (150, 825))
        screen4.blit(shelterimage, (150, 875))
        
        tornadoshelter_food_c = (self.tornado_shelter + self.food_u) * 20
        tornadoshelter_water_c = (self.tornado_shelter + self.water_u) * 50
        tornadoshelter_shelter_c = (self.tornado_shelter + self.shelter_u) * 200
        
        text11_1 = Startup.font.render(f"{tornadoshelter_food_c}", True, (0, 0, 0))
        textRec11_1 = text11_1.get_rect()
        textRec11_1.center = (225, 790)
        screen4.blit(text11_1, textRec11_1)
        text11_2 = Startup.font.render(f"{tornadoshelter_water_c}", True, (0, 0, 0))
        textRec11_2 = text11_2.get_rect()
        textRec11_2.center = (225, 840)
        screen4.blit(text11_2, textRec11_2)
        text11_3 = Startup.font.render(f"{tornadoshelter_shelter_c}", True, (0, 0, 0))
        textRec11_3 = text11_3.get_rect()
        textRec11_3.center = (225, 890)
        screen4.blit(text11_3, textRec11_3)
        
        text12 = Startup.font.render(f"Fire station level:{self.fire_station}", True, (0, 0, 0))
        textRec12 = text12.get_rect()
        textRec12.center = (500, 725)
        screen4.blit(text12, textRec12)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [425, 750, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [425, 950, 200, 50], 3)
        screen4.blit(medicsimage, (450, 775))
        screen4.blit(waterimage, (450, 825))
        screen4.blit(shelterimage, (450, 875))
        
        firestation_medics_c = (self.fire_station + self.medics_u) * 20
        firestation_water_c = (self.fire_station + self.water_u) * 50
        firestation_shelter_c = (self.fire_station + self.shelter_u) * 200
        
        text12_1 = Startup.font.render(f"{firestation_medics_c}", True, (0, 0, 0))
        textRec12_1 = text12_1.get_rect()
        textRec12_1.center = (525, 790)
        screen4.blit(text12_1, textRec12_1)
        text12_2 = Startup.font.render(f"{firestation_water_c}", True, (0, 0, 0))
        textRec12_2 = text12_2.get_rect()
        textRec12_2.center = (525, 840)
        screen4.blit(text12_2, textRec12_2)
        text12_3 = Startup.font.render(f"{firestation_shelter_c}", True, (0, 0, 0))
        textRec12_3 = text12_3.get_rect()
        textRec12_3.center = (525, 890)
        screen4.blit(text12_3, textRec12_3)
        
        text13 = Startup.font.render(f"Stronger house level:{self.stronger_house}", True, (0, 0, 0))
        textRec13 = text13.get_rect()
        textRec13.center = (800, 725)
        screen4.blit(text13, textRec13)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [725, 750, 200, 200], 3)
        pygame.draw.rect(screen4, (255, 0, 0),
                         [725, 950, 200, 50], 3)
        screen4.blit(energyimage, (750, 775))
        screen4.blit(shelterimage, (750, 825))
        screen4.blit(moneyimage, (750, 875))
        
        strongerhouse_energy_c = (self.stronger_house + self.energy_u) * 20
        strongerhouse_shelter_c = (self.stronger_house + self.shelter_u) * 50
        strongerhouse_money_c = (self.stronger_house + self.money_u) * 200
        
        text13_1 = Startup.font.render(f"{strongerhouse_energy_c}", True, (0, 0, 0))
        textRec13_1 = text13_1.get_rect()
        textRec13_1.center = (825, 790)
        screen4.blit(text13_1, textRec13_1)
        text13_2 = Startup.font.render(f"{strongerhouse_shelter_c}", True, (0, 0, 0))
        textRec13_2 = text13_2.get_rect()
        textRec13_2.center = (825, 840)
        screen4.blit(text13_2, textRec13_2)
        text13_3 = Startup.font.render(f"{strongerhouse_money_c}", True, (0, 0, 0))
        textRec13_3 = text13_3.get_rect()
        textRec13_3.center = (825, 890)
        screen4.blit(text13_3, textRec13_3)
        
        pygame.display.update()
        hover_sound_played = {'fastheal_b': False, 'biggerfarm_b': False, 'waterstation_b': False, 'powerplant_b': False, 'biggerbank_b': False, 'biggerschool_b': False, 'biggerfactory_b': False,
                              'shockabsorber_b' : False, 'seawall_b' : False, 'lavabarrier_b' : False, 'tornadoshelter_b' : False, 'firestation_b' : False, 'strongerhouse_b' : False, 'defence_toggle' : False}
        while self.play == True:
            defencesimage = pygame.image.load('defences_m.PNG')
            screen4.blit(defencesimage, (1860, 233))
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 125 <= mouse[0] <= 325 and 300 <= mouse[1] <= 350:
                        if self.medics >= fastheal_medics_c and self.shelter >= fastheal_shelter_c and self.money >= fastheal_shelter_c:
                            self.fast_heal += 1
                            self.medics -= fastheal_medics_c
                            self.shelter -= fastheal_shelter_c
                            self.money -= fastheal_shelter_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 425 <= mouse[0] <= 625 and 300 <= mouse[1] <= 350:
                        if self.food >= biggerfarm_food_c and self.water >= biggerfarm_water_c and self.money >= biggerfarm_money_c:
                            self.bigger_farm += 1
                            self.food -= biggerfarm_food_c
                            self.water -= biggerfarm_water_c
                            self.money -= biggerfarm_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 725 <= mouse[0] <= 925 and 300 <= mouse[1] <= 350:
                        if self.water >= waterstation_water_c and self.energy >= waterstation_energy_c and self.money >= waterstation_money_c:
                            self.water_station += 1
                            self.water -= waterstation_water_c
                            self.energy -= waterstation_energy_c
                            self.money -= waterstation_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 1025 <= mouse[0] <= 1225 and 300 <= mouse[1] <= 350:
                        if self.energy >= powerplant_energy_c and self.shelter >= powerplant_shelter_c and self.money >= powerplant_money_c:
                            self.power_plant += 1
                            self.energy -= powerplant_energy_c
                            self.shelter -= powerplant_shelter_c
                            self.money -= powerplant_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 1325 <= mouse[0] <= 1525 and 300 <= mouse[1] <= 350:
                        if self.shelter >= biggerbank_shelter_c and self.medics >= biggerbank_medics_c and self.food >= biggerbank_food_c and self.water >= biggerbank_water_c and self.money >= biggerbank_money_c:
                            self.bigger_bank += 1
                            self.shelter -= biggerbank_shelter_c
                            self.medics -= biggerbank_medics_c
                            self.food -= biggerbank_food_c
                            self.water -= biggerbank_water_c
                            self.money -= biggerbank_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 125 <= mouse[0] <= 325 and 650 <= mouse[1] <= 700:
                        if self.food >= biggerschool_food_c and self.energy >= biggerschool_energy_c and self.money >= biggerschool_money_c:
                            self.bigger_school += 1
                            self.food -= biggerschool_food_c
                            self.energy -= biggerschool_energy_c
                            self.money -= biggerschool_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    if 425 <= mouse[0] <= 625 and 650 <= mouse[1] <= 700:
                        if self.medics >= biggerfactory_medics_c and self.food >= biggerfactory_food_c and self.money >= biggerfactory_money_c:
                            self.bigger_factory += 1
                            self.medics -= biggerfactory_medics_c
                            self.food -= biggerfactory_food_c
                            self.money -= biggerfactory_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 725 <= mouse[0] <= 925 and 650 <= mouse[1] <= 700:
                        if self.energy >= shockabsorber_energy_c and self.water >= shockabsorber_water_c and self.money >= shockabsorber_money_c:
                            self.shock_absorber += 1
                            self.energy -= shockabsorber_energy_c
                            self.water -= shockabsorber_water_c
                            self.money -= shockabsorber_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 1025 <= mouse[0] <= 1225 and 650 <= mouse[1] <= 700:
                        if self.medics >= seawall_medics_c and self.water >= seawall_water_c and self.money >= seawall_money_c:
                            self.sea_wall += 1
                            self.medics -= seawall_medics_c
                            self.water -= seawall_water_c
                            self.money -= seawall_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 1325 <= mouse[0] <= 1525 and 650 <= mouse[1] <= 700:
                        if self.medics >= lavabarrier_medics_c and self.water >= lavabarrier_water_c and self.shelter >= lavabarrier_shelter_c:
                            self.lava_barrier += 1
                            self.medics -= lavabarrier_medics_c
                            self.water -= lavabarrier_water_c
                            self.shelter -= lavabarrier_shelter_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 125 <= mouse[0] <= 325 and 950 <= mouse[1] <= 1000:
                        if self.food >= tornadoshelter_food_c and self.water >= tornadoshelter_water_c and self.shelter >= tornadoshelter_shelter_c:
                            self.tornado_shelter += 1
                            self.food -= tornadoshelter_food_c
                            self.water -= tornadoshelter_water_c
                            self.shelter -= tornadoshelter_shelter_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 425 <= mouse[0] <= 625 and 950 <= mouse[1] <= 1000:
                        if self.medics >= firestation_medics_c and self.water >= firestation_water_c and self.shelter >= firestation_shelter_c:
                            self.fire_station += 1
                            self.medics -= firestation_medics_c
                            self.water -= firestation_water_c
                            self.shelter -= firestation_shelter_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 725 <= mouse[0] <= 925 and 950 <= mouse[1] <= 1000:
                        if self.energy >= strongerhouse_energy_c and self.shelter >= strongerhouse_shelter_c and self.money >= strongerhouse_money_c:
                            self.stronger_house += 1
                            self.energy -= strongerhouse_energy_c
                            self.shelter -= strongerhouse_shelter_c
                            self.money -= strongerhouse_money_c
                            Defences.purchase_d(self)
                        else:
                            Defences.purchase_d(self)
                    elif 1800 <= mouse[0] <= 1900 and 225 <= mouse[1] <= 325:
                        Game.system(self)
            
            pygame.draw.rect(screen4, color, [125, 300, 200, 50])  #Fast heal purchase button code
            if 125 <= mouse[0] <= 325 and 300 <= mouse[1] <= 350:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [125, 300, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [125, 300, 200, 50], 3)
                screen4.blit(text16, (165, 310))

                if not hover_sound_played['fastheal_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['fastheal_b'] = True
            else:
                hover_sound_played['fastheal_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [125, 300, 200, 50], 3) 
                screen4.blit(text16, (165, 310))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [425, 300, 200, 50])  #Bigger farm purchase button code
            if 425 <= mouse[0] <= 625 and 300 <= mouse[1] <= 350:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [425, 300, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [425, 300, 200, 50], 3)
                screen4.blit(text16, (465, 310))

                if not hover_sound_played['biggerfarm_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['biggerfarm_b'] = True
            else:
                hover_sound_played['biggerfarm_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [425, 300, 200, 50], 3) 
                screen4.blit(text16, (465, 310))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [725, 300, 200, 50])  #Water station purchase button code
            if 725 <= mouse[0] <= 925 and 300 <= mouse[1] <= 350:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [725, 300, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [725, 300, 200, 50], 3)
                screen4.blit(text16, (765, 310))

                if not hover_sound_played['waterstation_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['waterstation_b'] = True
            else:
                hover_sound_played['waterstation_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [725, 300, 200, 50], 3) 
                screen4.blit(text16, (765, 310))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [1025, 300, 200, 50])  #Power plant purchase button code
            if 1025 <= mouse[0] <= 1225 and 300 <= mouse[1] <= 350:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [1025, 300, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [1025, 300, 200, 50], 3)
                screen4.blit(text16, (1065, 310))

                if not hover_sound_played['powerplant_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['powerplant_b'] = True
            else:
                hover_sound_played['powerplant_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [1025, 300, 200, 50], 3) 
                screen4.blit(text16, (1065, 310))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [1325, 300, 200, 50])  #Bigger bank purchase button code
            if 1325 <= mouse[0] <= 1525 and 300 <= mouse[1] <= 350:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [1325, 300, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [1325, 300, 200, 50], 3)
                screen4.blit(text16, (1365, 310))

                if not hover_sound_played['biggerbank_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['biggerbank_b'] = True
            else:
                hover_sound_played['biggerbank_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [1325, 300, 200, 50], 3) 
                screen4.blit(text16, (1365, 310))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [125, 650, 200, 50])  #Bigger school purchase button code
            if 125 <= mouse[0] <= 325 and 650 <= mouse[1] <= 700:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [125, 650, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [125, 650, 200, 50], 3)
                screen4.blit(text16, (165, 660))

                if not hover_sound_played['biggerschool_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['biggerschool_b'] = True
            else:
                hover_sound_played['biggerschool_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [125, 650, 200, 50], 3) 
                screen4.blit(text16, (165, 660))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [425, 650, 200, 50])  #Bigger factory purchase button code
            if 425 <= mouse[0] <= 625 and 650 <= mouse[1] <= 700:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [425, 650, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [425, 650, 200, 50], 3)
                screen4.blit(text16, (465, 660))

                if not hover_sound_played['biggerfactory_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['biggerfactory_b'] = True
            else:
                hover_sound_played['biggerfactory_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [425, 650, 200, 50], 3) 
                screen4.blit(text16, (465, 660))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [725, 650, 200, 50])  #Shock absorber purchase button code
            if 725 <= mouse[0] <= 925 and 650 <= mouse[1] <= 700:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [725, 650, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [725, 650, 200, 50], 3)
                screen4.blit(text16, (765, 660))

                if not hover_sound_played['shockabsorber_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['shockabsorber_b'] = True
            else:
                hover_sound_played['shockabsorber_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [725, 650, 200, 50], 3) 
                screen4.blit(text16, (765, 660))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [1025, 650, 200, 50])  #Sea wall purchase button code
            if 1025 <= mouse[0] <= 1225 and 650 <= mouse[1] <= 700:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [1025, 650, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [1025, 650, 200, 50], 3)
                screen4.blit(text16, (1065, 660))

                if not hover_sound_played['seawall_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['seawall_b'] = True
            else:
                hover_sound_played['seawall_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [1025, 650, 200, 50], 3) 
                screen4.blit(text16, (1065, 660))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [1325, 650, 200, 50])  #Lava barrier purchase button code
            if 1325 <= mouse[0] <= 1525 and 650 <= mouse[1] <= 700:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [1325, 650, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [1325, 650, 200, 50], 3)
                screen4.blit(text16, (1365, 660))

                if not hover_sound_played['lavabarrier_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['lavabarrier_b'] = True
            else:
                hover_sound_played['lavabarrier_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [1325, 650, 200, 50], 3) 
                screen4.blit(text16, (1365, 660))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [125, 950, 200, 50])  #Tornado shelter purchase button code
            if 125 <= mouse[0] <= 325 and 950 <= mouse[1] <= 1000:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [125, 950, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [125, 950, 200, 50], 3)
                screen4.blit(text16, (165, 960))

                if not hover_sound_played['tornadoshelter_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['tornadoshelter_b'] = True
            else:
                hover_sound_played['tornadoshelter_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [125, 950, 200, 50], 3) 
                screen4.blit(text16, (165, 960))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [425, 950, 200, 50])  #Fire station purchase button code
            if 425 <= mouse[0] <= 625 and 950 <= mouse[1] <= 1000:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [425, 950, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [425, 950, 200, 50], 3)
                screen4.blit(text16, (465, 960))

                if not hover_sound_played['firestation_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['firestation_b'] = True
            else:
                hover_sound_played['firestation_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [425, 950, 200, 50], 3) 
                screen4.blit(text16, (465, 960))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [725, 950, 200, 50])  #Stronger house purchase button code
            if 725 <= mouse[0] <= 925 and 950 <= mouse[1] <= 1000:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [725, 950, 200, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [725, 950, 200, 50], 3)
                screen4.blit(text16, (765, 960))

                if not hover_sound_played['strongerhouse_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['strongerhouse_b'] = True
            else:
                hover_sound_played['strongerhouse_b'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [725, 950, 200, 50], 3) 
                screen4.blit(text16, (765, 960))
            pygame.display.update()
            
            pygame.draw.rect(screen4, color, [1860, 233, 50, 50])  #Stronger house purchase button code
            if 1850 <= mouse[0] <= 1900 and 200 <= mouse[1] <= 250:
                pygame.draw.rect(screen4, (255, 128, 128),
                                 [1860, 233, 50, 50])
                pygame.draw.rect(screen4, (255, 0, 0),
                                 [1860, 233, 50, 50], 3)

                if not hover_sound_played['defence_toggle']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['defence_toggle'] = True
            else:
                hover_sound_played['defence_toggle'] = False
                pygame.draw.rect(screen4, (255, 0, 0), [1860, 233, 50, 50], 3) 
            pygame.display.update()

class Upgrades:
    def __init__(self):
        self.food_u = 1
        self.water_u = 1
        self.money_u = 1
        self.energy_u = 1
        self.medics_u = 1
        self.shelter_u = 1

    def purchase_u(self):
        #In this function variables ending _c are the cost variables - how much of a resource needed to purchase and upgrade
        #Formatted as (resource being upgraded)_(resource being used in the upgrade)_c
        if Startup.fullscreen == True:
            screen3 = pygame.display.set_mode((1920, 1080))
        elif Startup.fullscreen == False:
            screen3 = pygame.display.set_mode((1080,720))
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        color = (135, 206, 235)
        screen3.fill(color)
        text7 = Startup.font.render("Purchase", True, (0, 0, 0))
        
        foodimage = pygame.image.load('food_r.PNG')
        waterimage = pygame.image.load('water_r.PNG')
        moneyimage = pygame.image.load('money_r.PNG')
        energyimage = pygame.image.load('energy_r.PNG')
        shelterimage = pygame.image.load('shelter_r.PNG')
        medicsimage = pygame.image.load('medics_r.PNG')
        
        text1 = Startup.font.render(f"Food level:{self.food_u}", True, (0, 0, 0))
        textRec1 = text1.get_rect()
        textRec1.center = (475, 75)
        screen3.blit(text1, textRec1)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [325, 100, 300, 300], 3)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [325, 400, 300, 50], 3)
        screen3.blit(waterimage, (350, 150))
        screen3.blit(energyimage, (350, 250))
        screen3.blit(moneyimage, (350, 350))
        
        #code to calculate food upgrade cost
        food_water_c = (self.water_u + self.food_u) *200
        food_energy_c = (self.energy_u + self.food_u) *20
        food_money_c = (self.money_u + self.food_u) *200
        
        text1_1 = Startup.font.render(f"{food_water_c}", True, (0, 0, 0))
        textRec1_1 = text1_1.get_rect()
        textRec1_1.center = (450, 165)
        screen3.blit(text1_1, textRec1_1)
        text1_2 = Startup.font.render(f"{food_energy_c}", True, (0, 0, 0))
        textRec1_2 = text1_2.get_rect()
        textRec1_2.center = (450, 265)
        screen3.blit(text1_2, textRec1_2)
        text1_3 = Startup.font.render(f"{food_money_c}", True, (0, 0, 0))
        textRec1_3 = text1_3.get_rect()
        textRec1_3.center = (450, 365)
        screen3.blit(text1_3, textRec1_3)
        
        text2 = Startup.font.render(f"Water level:{self.water_u}", True, (0, 0, 0))
        textRec2 = text2.get_rect()
        textRec2.center = (825, 75)
        screen3.blit(text2, textRec2)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [725, 100, 300, 300], 3)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [725, 400, 300, 50], 3)
        screen3.blit(moneyimage, (750, 150))
        screen3.blit(energyimage, (750, 250))
        #code to calculate water upgrade cost
        water_money_c = (self.water_u + self.money_u) * 200
        water_energy_c = (self.water_u + self.energy_u) * 50
        
        text2_1 = Startup.font.render(f"{water_money_c}", True, (0, 0, 0))
        textRec2_1 = text2_1.get_rect()
        textRec2_1.center = (850, 165)
        screen3.blit(text2_1, textRec2_1)
        text2_2 = Startup.font.render(f"{water_energy_c}", True, (0, 0, 0))
        textRec2_2 = text2_2.get_rect()
        textRec2_2.center = (850, 265)
        screen3.blit(text2_2, textRec2_2)
        
        text3 = Startup.font.render(f"Money level:{self.money_u}", True, (0, 0, 0))
        textRec3 = text3.get_rect()
        textRec3.center = (1225, 75)
        screen3.blit(text3, textRec3)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [1125, 100, 300, 300], 3)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [1125, 400, 300, 50], 3)
        screen3.blit(shelterimage, (1150, 115))
        screen3.blit(medicsimage, (1150, 185))
        screen3.blit(foodimage, (1150, 255))
        screen3.blit(waterimage, (1150, 325))
        #code to calculate money upgrade cost
        money_shelter_c = (self.money_u + self.shelter_u) * 20
        money_medics_c = (self.money_u + self.medics_u) * 10
        money_food_c = (self.money_u + self.food_u) * 100
        money_water_c = (self.money_u + self.water_u) * 50
        
        text3_1 = Startup.font.render(f"{money_shelter_c}", True, (0, 0, 0))
        textRec3_1 = text3_1.get_rect()
        textRec3_1.center = (1250, 130)
        screen3.blit(text3_1, textRec3_1)
        text3_2 = Startup.font.render(f"{money_medics_c}", True, (0, 0, 0))
        textRec3_2 = text3_2.get_rect()
        textRec3_2.center = (1250, 200)
        screen3.blit(text3_2, textRec3_2)
        text3_3 = Startup.font.render(f"{money_food_c}", True, (0, 0, 0))
        textRec3_3 = text3_3.get_rect()
        textRec3_3.center = (1250, 270)
        screen3.blit(text3_3, textRec3_3)
        text3_4 = Startup.font.render(f"{money_water_c}", True, (0, 0, 0))
        textRec3_4 = text3_4.get_rect()
        textRec3_4.center = (1250, 340)
        screen3.blit(text3_4, textRec3_4)
        
        text4 = Startup.font.render(f"Energy level:{self.energy_u}", True, (0, 0, 0))
        textRec4 = text4.get_rect()
        textRec4.center = (475, 475)
        screen3.blit(text4, textRec4)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [325, 500, 300, 300], 3)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [325, 800, 300, 50], 3)
        screen3.blit(shelterimage, (350, 530))
        screen3.blit(moneyimage, (350, 630))
        screen3.blit(waterimage, (350, 730))
        #code to calculate energy upgrade cost
        energy_shelter_c = (self.energy_u + self.shelter_u) * 20
        energy_money_c = (self.energy_u + self.money_u) * 100
        energy_water_c = (self.energy_u + self.water_u) * 50
        
        text4_1 = Startup.font.render(f"{energy_shelter_c}", True, (0, 0, 0))
        textRec4_1 = text4_1.get_rect()
        textRec4_1.center = (450, 550)
        screen3.blit(text4_1, textRec4_1)
        text4_2 = Startup.font.render(f"{energy_money_c}", True, (0, 0, 0))
        textRec4_2 = text4_2.get_rect()
        textRec4_2.center = (450, 650)
        screen3.blit(text4_2, textRec4_2)
        text4_3 = Startup.font.render(f"{energy_water_c}", True, (0, 0, 0))
        textRec4_3 = text4_3.get_rect()
        textRec4_3.center = (450, 750)
        screen3.blit(text4_3, textRec4_3)
        
        text5 = Startup.font.render(f"Medics level:{self.medics_u}", True, (0, 0, 0))
        textRec5 = text5.get_rect()
        textRec5.center = (825, 475)
        screen3.blit(text5, textRec5)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [725, 500, 300, 300], 3)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [725, 800, 300, 50], 3)
        screen3.blit(moneyimage, (750, 530))
        screen3.blit(foodimage, (750, 630))
        screen3.blit(energyimage, (750, 730))
        #code to calculate medics upgrade cost
        medics_money_c = (self.medics_u + self.money_u) * 200
        medics_food_c = (self.medics_u + self.food_u) * 100
        medics_energy_c = (self.medics_u + self.energy_u) * 20
        
        text5_1 = Startup.font.render(f"{medics_money_c}", True, (0, 0, 0))
        textRec5_1 = text5_1.get_rect()
        textRec5_1.center = (850, 550)
        screen3.blit(text5_1, textRec5_1)
        text5_2 = Startup.font.render(f"{medics_food_c}", True, (0, 0, 0))
        textRec5_2 = text5_2.get_rect()
        textRec5_2.center = (850, 650)
        screen3.blit(text5_2, textRec5_2)
        text5_3 = Startup.font.render(f"{medics_energy_c}", True, (0, 0, 0))
        textRec5_3 = text5_3.get_rect()
        textRec5_3.center = (850, 750)
        screen3.blit(text5_3, textRec5_3)
        
        text6 = Startup.font.render(f"Shelter level:{self.shelter_u}", True, (0, 0, 0))
        textRec6 = text6.get_rect()
        textRec6.center = (1225, 475)
        screen3.blit(text6, textRec6)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [1125, 500, 300, 300], 3)
        pygame.draw.rect(screen3, (255, 0, 0),
                         [1125, 800, 300, 50], 3)
        screen3.blit(moneyimage, (1150, 530))
        screen3.blit(medicsimage, (1150, 630))
        screen3.blit(foodimage, (1150, 730))
        #code to calculate shelter upgrade cost
        shelter_money_c = (self.shelter_u + self.money_u) * 200
        shelter_medics_c = (self.shelter_u + self.medics_u) * 20
        shelter_food_c = (self.shelter_u + self.food_u) *100
        
        text6_1 = Startup.font.render(f"{shelter_money_c}", True, (0, 0, 0))
        textRec6_1 = text6_1.get_rect()
        textRec6_1.center = (1250, 550)
        screen3.blit(text6_1, textRec6_1)
        text6_2 = Startup.font.render(f"{shelter_medics_c}", True, (0, 0, 0))
        textRec6_2 = text6_2.get_rect()
        textRec6_2.center = (1250, 650)
        screen3.blit(text6_2, textRec6_2)
        text6_3 = Startup.font.render(f"{shelter_food_c}", True, (0, 0, 0))
        textRec6_3 = text6_3.get_rect()
        textRec6_3.center = (1250, 750)
        screen3.blit(text6_3, textRec6_3)
        
        hover_sound_played = {'food_b': False, 'water_b': False, 'money_b': False, 'energy_b': False, 'medics_b': False, 'shelter_b': False, 'upgrade_toggle': False}
        while self.play == True:
            upgradesimage = pygame.image.load('upgrades_m.PNG')
            screen3.blit(upgradesimage, (1860, 133))
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 325 <= mouse[0] <= 625 and 400 <= mouse[1] <= 450:#button positions for purchase buttons
                        if self.water >= food_water_c and self.energy >= food_energy_c and self.money >= food_money_c:
                            self.food_u += 1
                            self.water -= food_water_c
                            self.energy -= food_energy_c
                            self.money -= food_money_c
                            Upgrades.purchase_u(self)
                        else:
                            Upgrades.purchase_u(self)
                    elif 725 <= mouse[0] <= 1025 and 400 <= mouse[1] <= 450:
                        if self.money >= water_money_c and self.energy >= water_energy_c:
                            self.water_u += 1
                            self.money -= water_money_c
                            self.energy -= water_energy_c
                            Upgrades.purchase_u(self)
                        else:
                            Upgrades.purchase_u(self)
                    elif 1125 <= mouse[0] <= 1425 and 400 <= mouse[1] <= 450:
                        if self.shelter >= money_shelter_c and self.medics >= money_medics_c and self.food >= money_food_c and self.water >= money_water_c:
                            self.money_u += 1
                            self.shelter -= money_shelter_c
                            self.medics -= money_medics_c
                            self.food -= money_food_c
                            self.water -= money_water_c
                            Upgrades.purchase_u(self)
                        else:
                            Upgrades.purchase_u(self)
                    elif 325 <= mouse[0] <= 625 and 800 <= mouse[1] <= 850:
                        if self.shelter >= energy_shelter_c and self.money >= energy_money_c and self.water >= energy_water_c:
                            self.energy_u += 1
                            self.shelter -= energy_shelter_c
                            self.money -= energy_money_c
                            self.water -= energy_water_c
                            Upgrades.purchase_u(self)
                        else:
                            Upgrades.purchase_u(self)
                    elif 725 <= mouse[0] <= 1025 and 800 <= mouse[1] <= 850:
                        if self.money >= medics_money_c and self.food >= medics_food_c and self.energy >= medics_energy_c:
                            self.medics_u += 1
                            self.money -= medics_money_c
                            self.food -= medics_food_c
                            self.energy -= medics_energy_c
                            Upgrades.purchase_u(self)
                        else:
                            Upgrades.purchase_u(self)
                    elif 1125 <= mouse[0] <= 1425 and 800 <= mouse[1] <= 850:
                        if self.money >= shelter_money_c and self.medics >= shelter_medics_c and self.food >= shelter_food_c:
                            self.shelter_u += 1
                            self.money -= shelter_money_c
                            self.medics -= shelter_medics_c
                            self.food -= shelter_food_c
                            Upgrades.purchase_u(self)
                        else:
                            Upgrades.purchase_u(self)#purchase button positions end here  
                    elif 1800 <= mouse[0] <= 1900 and 75 <= mouse[1] <= 175:#button to return to game
                        Game.system(self)
                      
            pygame.draw.rect(screen3, color, [325, 400, 300, 50])  #Food upgrade purchase button code
            if 325 <= mouse[0] <= 625 and 400 <= mouse[1] <= 450:
                pygame.draw.rect(screen3, (255, 128, 128),
                                 [325, 400, 300, 50])
                pygame.draw.rect(screen3, (255, 0, 0),
                                 [325, 400, 300, 50], 3)
                screen3.blit(text7, (400, 410))
                
                if not hover_sound_played['food_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['food_b'] = True
            else:
                hover_sound_played['food_b'] = False
                pygame.draw.rect(screen3, (255, 0, 0), [325, 400, 300, 50], 3) 
                screen3.blit(text7, (400, 410))
            pygame.display.update()
            
            pygame.draw.rect(screen3, color, [725, 400, 300, 50])  #Water upgrade purchase button
            if 725 <= mouse[0] <= 1025 and 400 <= mouse[1] <= 450:
                pygame.draw.rect(screen3, (255, 128, 128),
                                 [725, 400, 300, 50])
                pygame.draw.rect(screen3, (255, 0, 0),
                                 [725, 400, 300, 50], 3)
                screen3.blit(text7, (800, 410))
                
                if not hover_sound_played['water_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['water_b'] = True
            else:
                hover_sound_played['water_b'] = False
                pygame.draw.rect(screen3, (255, 0, 0), [725, 400, 300, 50], 3)
                screen3.blit(text7, (800, 410))
            pygame.display.update()
            
            pygame.draw.rect(screen3, color, [1125, 400, 300, 50])  #Money upgrade purchase button
            if 1125 <= mouse[0] <= 1425 and 400 <= mouse[1] <= 450:
                pygame.draw.rect(screen3, (255, 128, 128),
                                 [1125, 400, 300, 50])
                pygame.draw.rect(screen3, (255, 0, 0),
                                 [1125, 400, 300, 50], 3)
                screen3.blit(text7, (1200, 410))
                
                if not hover_sound_played['money_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['money_b'] = True
            else:
                hover_sound_played['money_b'] = False
                pygame.draw.rect(screen3, (255, 0, 0), [1125, 400, 300, 50], 3)
                screen3.blit(text7, (1200, 410))
            pygame.display.update()
            
            pygame.draw.rect(screen3, color, [325, 800, 300, 50])  #Energy upgrade purchase button
            if 325 <= mouse[0] <= 625 and 800 <= mouse[1] <= 850:
                pygame.draw.rect(screen3, (255, 128, 128),
                                 [325, 800, 300, 50])
                pygame.draw.rect(screen3, (255, 0, 0),
                                 [325, 800, 300, 50], 3)
                screen3.blit(text7, (400, 810))
                
                if not hover_sound_played['energy_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['energy_b'] = True
            else:
                hover_sound_played['energy_b'] = False
                pygame.draw.rect(screen3, (255, 0, 0), [325, 800, 300, 50], 3)
                screen3.blit(text7, (400, 810))
            pygame.display.update()
            
            pygame.draw.rect(screen3, color, [725, 800, 300, 50])  #Medics upgrade purchase button
            if 725 <= mouse[0] <= 1025 and 800 <= mouse[1] <= 850:
                pygame.draw.rect(screen3, (255, 128, 128),
                                 [725, 800, 300, 50])
                pygame.draw.rect(screen3, (255, 0, 0),
                                 [725, 800, 300, 50], 3)
                screen3.blit(text7, (800, 810))
                
                if not hover_sound_played['medics_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['medics_b'] = True
            else:
                hover_sound_played['medics_b'] = False
                pygame.draw.rect(screen3, (255, 0, 0), [725, 800, 300, 50], 3)
                screen3.blit(text7, (800, 810))
            pygame.display.update()
            
            pygame.draw.rect(screen3, color, [1125, 800, 300, 50])  #Shelter upgrade purchase button
            if 1125 <= mouse[0] <= 1425 and 800 <= mouse[1] <= 850:
                pygame.draw.rect(screen3, (255, 128, 128),
                                 [1125, 800, 300, 50])
                pygame.draw.rect(screen3, (255, 0, 0),
                                 [1125, 800, 300, 50], 3)
                screen3.blit(text7, (1200, 810))
                
                if not hover_sound_played['shelter_b']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['shelter_b'] = True
            else:
                hover_sound_played['shelter_b'] = False
                pygame.draw.rect(screen3, (255, 0, 0), [1125, 800, 300, 50], 3)
                screen3.blit(text7, (1200, 810))
            pygame.display.update()
            
            pygame.draw.rect(screen3, color,[1850, 125, 50, 50])#code to toggle upgrade menu
            if 1850 <= mouse[0] <= 1900 and 125 <= mouse[1] <= 175:
                pygame.draw.rect(screen3, (255, 128, 128),
                                 [1850, 125, 50, 50])
                pygame.draw.rect(screen3, (255, 0, 0),
                                 [1850, 125, 50, 50], 3)
                
                if not hover_sound_played['upgrade_toggle']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['upgrade_toggle'] = True
            else:
                hover_sound_played['upgrade_toggle'] = False
                pygame.draw.rect(screen3, (255, 0, 0), [1850, 125, 50, 50], 3)
            pygame.display.update()
            
class Startup:
    pygame.font.init()
    font = pygame.font.SysFont('comicsans.tff', 40)
    font2 = pygame.font.SysFont('comicsans.tff', 30)
    fullscreen = True
    
    def __init__(self):
        pygame.init()
        self.volume = 1

    def menu(self):
        if Startup.fullscreen == True:
            screen = pygame.display.set_mode((1920, 1080))
        elif Startup.fullscreen == False:
            screen = pygame.display.set_mode((1080,720))
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        color = (135, 206, 235) #background colour of display
        screen.fill(color)
        
        icon = pygame.image.load('pixil-frame-0.png') #pixel image for game icon
        pygame.display.set_icon(icon)
        
        image = pygame.image.load('pixil-frame-1.png') #pixel image for background
        image_rec = image.get_rect(center = screen.get_rect().center)
        screen.blit(image, image_rec)
        
        pygame.draw.rect(screen, (255, 0, 0),#(R, G, B)
                         [325, 200, 400, 100], 3) #(x, y, width, length), thickness
        pygame.draw.rect(screen, (255, 0, 0),
                         [325, 350, 400, 100], 3)
        pygame.draw.rect(screen, (255, 0, 0),
                         [325, 500, 400, 100], 3)
 
        text1 = Startup.font.render('Play', True, (0, 0, 0))#initial box for play
        textRec1 = text1.get_rect()
        textRec1.center = (525, 250)
        screen.blit(text1, textRec1)
        
        text2 = Startup.font.render('Options', True, (0, 0, 0)) #initial box for options
        textRec2 = text2.get_rect()
        textRec2.center = (525, 400)
        screen.blit(text2, textRec2)
        
        text3 = Startup.font.render('Exit', True, (0, 0, 0)) #initial box for exit
        textRec3 = text3.get_rect()
        textRec3.center = (525, 550)
        screen.blit(text3, textRec3)
        
        pygame.display.set_caption('Natural Disaster Simulator') #name the window
        pygame.display.flip()
        
        hover_sound_played = {'play': False, 'options': False, 'exit': False}
        start = True
        while start:#while loop to check if a mouse has hovered/interacted with a box
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 325 <= mouse[0] <= 725 and 500 <= mouse[1] <= 600:
                        pygame.quit()
                    elif 325 <= mouse[0] <= 725 and 350 <= mouse[1] <= 450:
                        self.options(screen)
                    elif 325 <= mouse[0] <= 725 and 200 <= mouse[1] <= 300:
                        self.play = True
                        Game.world(self)
                        Game.disasters(self)
                        Defences.__init__(self)
                        Upgrades.__init__(self)
                        Game.__init__(self,Upgrades)
                        Game.system(self)

            pygame.draw.rect(screen, color, [325, 500, 400, 100])  # Fill the background
            if 325 <= mouse[0] <= 725 and 500 <= mouse[1] <= 600:
                pygame.draw.rect(screen, (255, 128, 128),
                                 [325, 500, 400, 100])
                pygame.draw.rect(screen, (255, 0, 0),
                                 [325, 500, 400, 100], 3) #mouse hover rectangle
                screen.blit(text3, textRec3)
                
                if not hover_sound_played['exit']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['exit'] = True
            else:
                hover_sound_played['exit'] = False
                pygame.draw.rect(screen, (255, 0, 0), [325, 500, 400, 100], 3) #non mouse hover rectangle
                screen.blit(text3, textRec3)
            pygame.display.update()
            
            pygame.draw.rect(screen, color, [325, 350, 400, 100])
            if 325 <= mouse[0] <= 725 and 350 <= mouse[1] <= 450:
                pygame.draw.rect(screen, (255, 128, 128), [325, 350, 400, 100])
                pygame.draw.rect(screen, (255, 0, 0), [325, 350, 400, 100], 3)
                screen.blit(text2, textRec2)
                
                if not hover_sound_played['options']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['options'] = True
            else:
                hover_sound_played['options'] = False
                pygame.draw.rect(screen, (255, 0, 0), [325, 350, 400, 100], 3)
                screen.blit(text2, textRec2)
            pygame.display.update()
            
            pygame.draw.rect(screen, color, [325, 200, 400, 100]) 
            if 325 <= mouse[0] <= 725 and 200 <= mouse[1] <= 300:
                pygame.draw.rect(screen, (255, 128, 128), [325, 200, 400, 100])
                pygame.draw.rect(screen, (255, 0, 0), [325, 200, 400, 100], 3)
                screen.blit(text1, textRec1)
                
                if not hover_sound_played['play']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['play'] = True
            else:
                hover_sound_played['play'] = False
                pygame.draw.rect(screen, (255, 0, 0), [325, 200, 400, 100], 3)
                screen.blit(text1, textRec1)
            pygame.display.update()

    def options(self, screen):
        if Startup.fullscreen == True:
            screen = pygame.display.set_mode((1920, 1080))
        elif Startup.fullscreen == False:
            screen = pygame.display.set_mode((1080,720))
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        hover_sound_played = {'back' : False}
        color = (124, 13, 34)
        run = True
        screen.fill(color)
        text1 = Startup.font.render('Volume' , True, (146, 255, 13)) #volume bar setup
        text1_rec = text1.get_rect(center=(540, 150))
        screen.blit(text1, text1_rec)
        vol_slider = pygame.Rect(400, 200, 300, 20)
        slider_stud = pygame.Rect(int(self.volume * 300) + 400, 200, 20, 20)
        
        pygame.draw.rect(screen, (255, 0, 0),
                         [325, 500, 400, 100], 3)#set up for back button
        text2 = Startup.font.render('Back', True, (0, 0, 0)) #initial box for back
        textRec2 = text2.get_rect()
        textRec2.center = (525, 550)
        screen.blit(text2, textRec2)
        
        text3 = Startup.font.render('Windowed', True, (0, 0, 0))#text box for Windowed checkbox
        text3_rec = text3.get_rect(center=(500, 300))
        screen.blit(text3, text3_rec)
        pygame.draw.rect(screen, (255, 0, 0),
                         [650, 275, 50, 50], 3)
        if Startup.fullscreen == False:
            pygame.draw.line(screen, (0, 0, 0),
                            [657, 277],
                            [692, 322], 10)
            pygame.draw.line(screen, (0, 0, 0),
                            [657, 322],
                            [692, 277], 10)
        while run == True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 325 <= mouse[0] <= 725 and 500 <= mouse[1] <= 600:
                        self.menu()
                    elif 650 <= mouse[0] <= 700 and 275 <= mouse[1] <= 325 and Startup.fullscreen == True:#code for changing the fullscreen option
                        pygame.draw.line(screen, (0, 0, 0),
                                    [657, 277],
                                    [692, 322], 10)
                        pygame.draw.line(screen, (0, 0, 0),
                                    [657, 322],
                                    [692, 277], 10)
                        Startup.fullscreen = False
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                    elif 650 <= mouse[0] <= 700 and 275 <= mouse[1] <= 325 and Startup.fullscreen == False:
                        Startup.fullscreen = True
                        pygame.draw.rect(screen, (124, 13, 34),
                                         [650, 275, 50, 50], 0)
                        pygame.draw.rect(screen, (255, 0, 0),
                                         [650, 275, 50, 50], 3)
                    elif event.button == 1 and slider_stud.collidepoint(event.pos): #elif statements for logic of volume slider
                        drag = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        drag = False
                elif event.type == pygame.MOUSEMOTION and drag == True:#elif to ensure the stud of the slider wont pass the vol_slider shape
                    new_x = event.pos[0] - slider_stud.width // 2
                    new_x = max(vol_slider.left, min(new_x, vol_slider.right - slider_stud.width))
                    slider_stud.x = new_x
                    self.volume = (slider_stud.x - vol_slider.left) / vol_slider.width
                    self.volume = max(0, min(self.volume, 1))
                    mixer.music.set_volume(self.volume)  
                    
                pygame.draw.rect(screen, (0, 255, 0), vol_slider)
                pygame.draw.rect(screen, (0, 0, 255), slider_stud)
                
            pygame.draw.rect(screen, color, [325, 500, 400, 100])  # Fill the background
            if 325 <= mouse[0] <= 725 and 500 <= mouse[1] <= 600:
                pygame.draw.rect(screen, (255, 128, 128), [325, 500, 400, 100])
                pygame.draw.rect(screen, (255, 0, 0), [325, 500, 400, 100], 3) #mouse hover rectangle
                screen.blit(text2, textRec2)
                
                if not hover_sound_played['back']:
                    mixer.music.load('mouse_hover.mp3')
                    mixer.music.set_volume(self.volume)
                    mixer.music.play()
                    hover_sound_played['back'] = True
            else:
                hover_sound_played['back'] = False
                pygame.draw.rect(screen, (255, 0, 0), [325, 500, 400, 100], 3) #non mouse hover rectangle
                screen.blit(text2, textRec2)
            pygame.display.update()
                
            pygame.display.flip()

upgrades1 = Upgrades()
game1 = Game(upgrades1)
start1 = Startup()
start1.menu()