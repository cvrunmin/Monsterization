init python:
    pass
    # from Queue import Queue
    # class OverworldPlayOnlyDisplayable(renpy.Displayable):
    #     class OverworldCharacter(object):
    #         def __init__(self, x, y, sprites, facing):
    #             self.northFrames = sprites[0]
    #             self.southFrames = sprites[1]
    #
    #             self.eastFrames = sprites[2]
    #             self.westFrames = sprites[3]
    #             self.age = 0
    #             self.zLayer = 2
    #             self.facing = facing
    #             if facing == 'up':
    #                 self.image = Image(self.northFrames[0])
    #                 self.frames = self.northFrames
    #             elif facing == 'left':
    #                 self.image = Image(self.westFrames[0])
    #                 self.frames = self.westFrames
    #             elif facing == 'right':
    #                 self.image = Image(self.eastFrames[0])
    #                 self.frames = self.eastFrames
    #             else:
    #                 self.image = Image(self.southFrames[0])
    #                 self.frames = self.southFrames
    #             self.Walking = False
    #
    #             self.rect = pygame.Rect((x, y), (sprites[4][0], sprites[4][1]))
    #             self.actionChoices = NonUniformRandom( [('stand', 15), ('walk', 1)] )
    #             self.posLocked = False
    #             self.dests = Queue()
    #             self.destX = None #The x coordinate of our destination
    #             self.destY = None #The y coordinate of our destination
    #             self.speed = 1
    #             self.visible = True
    #             self.dying = False
    #         def __reduce__(self):
    #             state = self.__dict__.copy()
    #             return (_NestedClassGetter(),
    #                 (OverworldPlayOnlyDisplayable, self.__class__.__name__, ),
    #                 state,
    #                 )
    #         def setDying(self,flag):
    #             self.dying = flag
    #
    #         def setVisible(self, flag):
    #             self.visible = flag
    #
    #         def setPos(self,x,y):
    #             self.rect.x = x
    #             self.rect.y = y
    #
    #         def queueDest(self,x,y,speed=1):
    #             self.dests.put((x,y,speed))
    #
    #         def setDest(self,x,y,speed=1):
    #             self.destX = x
    #             self.destY = y
    #             self.speed = speed
    #
    #         def move(self):
    #
    #             #Move towards destination
    #             if self.destX is not None and self.destY is not None: #Do we have a destination?
    #                 if not self.Walking:
    #                     self.Walking = True
    #                 if self.destX == self.rect.x and self.destY == self.rect.y:#Are we there?
    #                     self.stop() #stop!
    #
    #                 else: #if we're not there yet, keep going
    #
    #                     if self.destX < self.rect.x: #if the destination is to our left...
    #                         if self.rect.x - self.destX < 8*self.speed:
    #                             self.rect.x = self.destX
    #                         else:
    #                             self.rect.x-= 8*self.speed #move left
    #                         if self.frames <> self.westFrames: #make sure our frames match up, just in case something happened.
    #                             self.frames = self.westFrames
    #
    #                     if self.destX > self.rect.x: #do the same for right...
    #                         if -(self.rect.x - self.destX) < 8*self.speed:
    #                             self.rect.x = self.destX
    #                         else:
    #                             self.rect.x+= 8*self.speed
    #                         if self.frames <> self.eastFrames:
    #                             self.frames = self.eastFrames
    #
    #                     if self.destY < self.rect.y: #...up..
    #                         if self.rect.y - self.destY < 8*self.speed:
    #                             self.rect.y = self.destY
    #                         else:
    #                             self.rect.y-= 8*self.speed
    #                         if self.frames <> self.northFrames:
    #                             self.frames = self.northFrames
    #
    #                     if self.destY > self.rect.y: #...down
    #                         if -(self.rect.y - self.destY) < 8*self.speed:
    #                             self.rect.y = self.destY
    #                         else:
    #                             self.rect.y+= 8*self.speed
    #                         if self.frames <> self.southFrames:
    #                             self.frames = self.southFrames
    #
    #             elif not self.dests.empty():
    #                 nx,ny,nspeed = self.dests.get()
    #                 self.destX = nx
    #                 self.destY = ny
    #                 self.speed = nspeed
    #             else: #if we have no desination set, just skip this method
    #                 pass
    #
    #         def stop(self):
    #             #Stop everything
    #             self.Walking = False
    #             self.posLocked = False
    #             self.destX = None
    #             self.destY = None
    #
    #         def snapToGrid(self,array):
    #             #Intermittently make sure we're on the grid. This should prevent most collision issues with roaming.
    #             for i in array:
    #                 if i%TILESIZE <> 0: #is our coordinate divisible by the tilesize? If not..
    #                     multBy = int(i/TILESIZE) #divide it and get int, to get closest multiple
    #                     i = TILESIZE*multBy #multiply this by tilesize to get closest tile
    #
    #         # def snapToRange(self):
    #         #     #snap NPC's back into range if they are nudged out
    #         #     if self.rect.y < self.rangeTop:
    #         #         self.rect.y = self.rangeTop
    #         #     if self.rect.y > self.rangeBottom:
    #         #         self.rect.y = self.rangeBottom
    #         #     if self.rect.x < self.rangeLeft:
    #         #         self.rect.x = self.rangeLeft
    #         #     if self.rect.x > self.rangeRight:
    #         #         self.rect.x = self.rangeRight
    #
    #         def walk_animation(self):
    #             if self.age < len(self.frames):
    #                 pass
    #             else:
    #                 self.age = 0
    #             self.image = Image(self.frames[int(self.age // 1)])
    #
    #
    #         def update(self):
    #             self.move()
    #
    #             if self.Walking:
    #                 self.age += 0.25 #increment walking frame
    #                 self.walk_animation() #animate
    #             elif not self.Walking:
    #                 self.image = Image(self.frames[0])
    #
    #
    #
    #     class PlayOnlyScenery(object):
    #          #SCENERY, A class for objects like buildings and trees
    #         def __init__(self, x, y, image, width, height, zLayer, hasRoof, label, actionLabel):
    #
    #             self.image = Image(image)
    #
    #
    #             self.rect = pygame.Rect((x, y), (width, height))
    #
    #             self.zLayer = zLayer #what layer in the z ordering will this item be on?
    #             self.hasRoof = hasRoof #does it have a roof?
    #             self.goToLabel = label #Where the player will be redirected on contact
    #             self.actionLabel = actionLabel #An action, usually a description, fired when the player inspects the object
    #
    #         def __reduce__(self):
    #             state = self.__dict__.copy()
    #             return (_NestedClassGetter(),(OverworldPlayOnlyDisplayable, self.__class__.__name__, ),state,)
    #
    #     def getOffset(self): #get player's current position for re-entering map
    #         self.playerX = self.player.rect.x
    #         self.playerY = self.player.rect.y
    #
    #
    #
    #     def __init__(self, map_layout = None, tileList = None, charSprites = None, groundLayout = None, scrolling = True):
    #
    #         renpy.Displayable.__init__(self)
    #         self.zList = []
    #
    #
    #         self.goTo = None
    #
    #         self.buildings = []
    #         self.rooves = []
    #
    #         self.characterList = {}
    #
    #         self.enemyList = []
    #         self.npcList = []
    #
    #
    #         self.playerList = []
    #         self.sceneryList = []
    #
    #         # self.playerX = playerX
    #         # self.playerY = playerY
    #
    #         self.talking = False
    #         self.scrolling = scrolling
    #
    #         #start generating map from assets
    #         if map_layout is not None:
    #             x = 0 #start at top left corner
    #             y = 0
    #             bldngCount = 0
    #             roofCount = 0
    #
    #             for row in map_layout: #go into a row
    #                 for col in row: #now each individual item
    #                     for tile in tileList:
    #                         if col == tile[0]: #make buildings
    #                             self.buildings.append(OverworldPlayOnlyDisplayable.PlayOnlyScenery(x,y, tile[1] + ".png", tile[2][0], tile[2][1], 2, tile[4], tile[5], tile[6]))
    #                             self.sceneryList.append(self.buildings[bldngCount])
    #                             self.zList.append(self.buildings[bldngCount])
    #
    #                             if self.buildings[bldngCount].hasRoof: #if building has roof, make roof as well
    #                                 self.rooves.append(OverworldPlayOnlyDisplayable.PlayOnlyScenery(x,y, tile[1] + "_roof.png", tile[3][0], tile[3][1], 3, False, None, None))
    #                                 self.zList.append(self.rooves[roofCount])
    #                                 #adjust building position to match
    #                                 self.buildings[bldngCount].rect.x += (self.rooves[roofCount].rect.width - self.buildings[bldngCount].rect.width)/2
    #                                 self.buildings[bldngCount].rect.y += (self.rooves[roofCount].rect.height - self.buildings[bldngCount].rect.height)
    #                                 roofCount +=1
    #                             bldngCount += 1
    #
    #                     x += TILESIZE #move over one tile after placing
    #
    #                 y += TILESIZE #row cleared, move down
    #                 x = 0 #reset x position
    #
    #         if charSprites is not None:
    #             for c in charSprites:
    #                 occ = OverworldPlayOnlyDisplayable.OverworldCharacter(-1,-1,c[1],c[2])
    #                 occ.setVisible(False)
    #                 self.characterList[c[0]] = occ
    #                 self.zList.append(occ)
    #                 if c[0] == "player":
    #                     self.player = occ
    #
    #
    #         #finally, make ground tiles
    #         if groundLayout is not None:
    #             x = 0
    #             y = 0
    #             groundCount = 0
    #             self.groundList = []
    #             for row in groundLayout:
    #                 for col in row:
    #                     for tile in tileList:
    #                         if col == tile[0]:
    #                             self.groundList.append(OverworldPlayOnlyDisplayable.PlayOnlyScenery(x,y, tile[1] + ".png", tile[2][0], tile[2][1], 2, tile[4], tile[5],tile[6]))
    #                             groundCount +=1
    #
    #
    #                     x += TILESIZE
    #
    #                 y += TILESIZE
    #                 x = 0
    #
    #
    #     def render(self, width, height, st, at):
    #         ret = renpy.display.render.Render(width, height) #The main rendering screen, don't blit directly to this!
    #         map_child = renpy.Render(width, height, st, at) #The map itself, a separate child object blitted to ret. Blit to this!
    #
    #         self.zList.sort(key=lambda x: x.rect.y, reverse=False) #sort everything according to y position. This determines the order in which they will be rendered.
    #         for g in self.groundList: #ground is rendered first, with no sorting.
    #              map_child.blit(renpy.render(g.image, g.rect.width, g.rect.height, st, at), (g.rect.x, g.rect.y))
    #         for zl in self.zList: #layer 2 has pretty much everything else
    #             if zl.zLayer == 2:
    #                 if (isinstance(zl, OverworldPlayOnlyDisplayable.OverworldCharacter) and zl.visible):
    #                     if zl.dying:
    #                         map_child.blit(renpy.render(Transform(child=zl.image, rotate=min(10*at,90)), zl.rect.width, zl.rect.height, st, at), (zl.rect.x, zl.rect.y))
    #                     else:
    #                         map_child.blit(renpy.render(zl.image, zl.rect.width, zl.rect.height, st, at), (zl.rect.x, zl.rect.y))
    #                 elif not isinstance(zl,OverworldPlayOnlyDisplayable.OverworldCharacter):
    #                     map_child.blit(renpy.render(zl.image, zl.rect.width, zl.rect.height, st, at), (zl.rect.x, zl.rect.y))
    #         for zl in self.zList: #and finally, higher altitude items like roofs
    #             if zl.zLayer == 3:
    #                 map_child.blit(renpy.render(zl.image, zl.rect.width, zl.rect.height, st, at), (zl.rect.x, zl.rect.y))
    #
    #         #update everything, unless we're talking. Trying to update while talking results in a stack overflow, and is a little too busy anyway.
    #
    #         for e in self.characterList.values():
    #             e.update()
    #
    #         if self.scrolling: #if it's a scrolling area, update the child render's coordinates
    #             x,y = self.panMap()
    #         else:
    #             x,y = 0,0 #if not, keep them in place
    #         ret.blit(map_child, (x, y)) #render the child at new coordinates
    #         renpy.redraw(self, .03)
    #         return ret
    #     def panMap(self): #Get the necessary offset to keep player centered
    #         newY = (HEIGHT *.5) - self.player.rect.y
    #         newX = (WIDTH *.5) - self.player.rect.x
    #         return (newX, newY)
    #
    #     # Handles events.
    #     def event(self, ev, x, y, st):
    #         pass
