#IMPORTANT: every action label should return (<act as goTo>, [goTo label])

label hall_map_pre:
    python:
        storeroom_key = False
        lab_key = False
        jatsam_team = False
        store_story_read = False
        jatsam_just = False
        store_greenbottle = False
        store_report = False
label hall_map_before:
    $playerX = None
    $playerY = None
label hall_map:
    scene
    scene black_screen onlayer submaster
    window hide None
    play music "music/stone.ogg"
    python:
        ui.layer("mapEngine")
        hall_mapsprite = OverworldDisplayable(map_layout = lab_hall_layout, tileList = lab_tiles,
            portals = lab_hall_portals, portal_tiles = lab_hall_portal_tiles,
            enemy_layout = lab_hall_enemies_jatsam if jatsam_team else lab_hall_enemies, enemySprites = [],

            NPCSprites = [], #villagers, uses the same layout as enemies
            FollowerSprites = lab_followers if jatsam_team else [],
            groundLayout = lab_hall_ground,
            playerSprites = kapo_sprites, playerX = playerX, playerY = playerY,
            scrolling = True)
        ui.add(hall_mapsprite)
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        del hall_mapsprite
    stop music
    python:
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
    with dissolve
    return

label lab_hall_bookshelf_fake:
    $ bookshelf_book = renpy.random.randint(0,4)
    if bookshelf_book == 0:
        "找到一本奇怪的書:{p=0.3}《Ren\'Py 從入門到精通》"
        "「Ren'Py 是一個免費的跨平台電子小說引擎，它讓文字、圖案、聲音組成的視覺小說或生活模擬遊戲變得更為簡單……」"
        show kapo at character_2
        kapo "老師到底要用它來幹甚麼呢？"
    elif bookshelf_book == 1:
        "找到一本奇怪的書:{p=0.3}《百合的法則》"
        "封面有一對妹子親吻着"
        if jatsam_team:
            show jatsam flip at character_1
            show kapo at character_3
            two "……！！"
        else:
            show kapo at character_2
            kapo "……！！"
    elif bookshelf_book == 2:
        "找到一本奇怪的書:{p=0.3}《新高中生活與物理》"
        "封面有一隻小鳥在水面"
        show kapo at character_2
        kapo "看來老師對科學真的很有研究呢"
    elif bookshelf_book == 3:
        "找到一本奇怪的書:{p=0.3}《Stay with Marble》"
        "一本只有波子作為封面的書，沒有內容"
        show kapo at character_2
        kapo "額……"
    return

label lab_hall_bookshelf:
    "找到一本奇怪的書:{p=0.3}《獸耳娘合成計劃報告》"
    "「第一天進行實驗，交換身體結構果然不容易，排斥反應一直發生，{p=0.5}但動物結構確實與實驗體神經成功融合，相信是個好開始。」"
    if jatsam_team:
        show jatsam flip at character_1
        show kapo at character_3
        "嘉寶打量着一心的身軀"
        jatsam "？"
        kapo "一心……你是男的吧？"
        jatsam "是啊"
        jatsam "恐怕我並非「老師」的主要實驗品"
        kapo "喔……"
    else:
        show kapo at character_2
        kapo "看來實驗並不容易，希望我也可以幫忙研究。"
    if not storeroom_key:
        kapo "咦？"
        "書櫃裏有一條鑰匙"
        $ storeroom_key = True
        "{color=#0000ff}獲得儲物室鑰匙{/color}"
    return (False, None)

label lab_hall_book_fake:
    "《獸耳娘-萌》---一本繪畫着不同種類的獸耳娘的繪本，很可愛！"
    show kapo at character_2
    kapo "這是...參考資料？"
    if jatsam_team:
        show kapo at character_3 with ease
        show jatsam flip at character_1 with dissolve
        jatsam "恐怕只是「老師」的惡趣味罷了"
        kapo "額......"
    return (False, None)

label lab_hall_to_storeroom:
    if not storeroom_key:
        "{color=#0000ff}儲物室 已上鎖{/color}"
        return (False, None)
    else:
        return (True, "lab_storeroom_map_pre")

label lab_hall_to_lab:
    if not lab_key:
        "{color=#0000ff}實驗室 已上鎖{/color}"
        return (False, None)
    else:
        return (True, "lab_lab_map_pre")
label lab_storeroom_map_pre:
    $playerX = None
    $playerY = None
    python:
        if store_story_read:
            renpy.jump("lab_storeroom_map_controllable")
        else:
            renpy.jump("lab_storeroom_map_story")
label lab_storeroom_map_story:
    scene
    scene black_screen onlayer submaster
    window hide None
    play music "music/school.ogg"
    python:
        ui.layer("mapEngine")
        storeroom_mapsprite_playonly = OverworldPlayOnlyDisplayable(map_layout = lab_storeroom_layout, tileList = lab_store_tiles,
            charSprites = [
            ["player", kapo_sprites, "up"],
            ["jatsam", jatsam_sprites, "left"],
            ["monster", monster_sprites, "right"],
            ],
            groundLayout = lab_storeroom_ground,
            scrolling = True)
        ui.add(storeroom_mapsprite_playonly)
        ui.close()
        pkapo = storeroom_mapsprite_playonly.characterList["player"]
        pkapo.setPos(128,448)
        pkapo.setVisible(True)
        pkapo.queueDest(128,352)
        pkapo.queueDest(320,352)
        renpy.pause(delay=2.0,hard=True)
    show kapo at character_2
    kapo "哇……好暗……這裏面到底是收藏什麼東西的？"
    unknown "{size=+10}{cps=*0.25}過……來………{/cps}{/size}"
    show kapo frownsmile at character_2
    kapo "那個……裏面有人嗎？"
    unknown "{size=+10}{cps=*0.25}是……啊……過……來……{/cps}{/size}"
    hide kapo
    python:
        pkapo.setDest(576,352,0.5)
        renpy.pause(delay=1.8,hard=True)
        pmonst = storeroom_mapsprite_playonly.characterList["monster"]
        pmonst.setPos(1024,352)
        pmonst.setVisible(True)
        pmonst.setDest(704,352,2.5)
        renpy.pause(delay=0.5,hard=True)
    show kapo flip at character_1
    show monster flip at character_3
    monster "{size=+10}{cps=*0.25}過來，讓我好好看看，今晚的獵物！{/cps}{/size}"
    show kapo cry flip at character_1
    kapo "不要啊啊啊啊啊啊！"
    hide kapo
    hide monster
    python:
        pjatsam = storeroom_mapsprite_playonly.characterList["jatsam"]
        pjatsam.setPos(1024,352)
        pjatsam.setVisible(True)
        pjatsam.queueDest(576,352,2.5)
        pjatsam.queueDest(577,352)
        renpy.pause(delay=0.8,hard=True)
        pkapo.queueDest(535,352,1.5)
        pkapo.queueDest(536,352)
        renpy.pause(delay=0.75,hard=True)
    #$ pkapo.setDest(536,352)
    show kapo flip at character_1
    show jatsam flip at character_2
    show monster flip at character_3_far behind kapo, jatsam
    unknown "請你住手！這孩子是無辜的"
    monster "休想阻止我！！我要讓更多的人和我一樣！成為這個實驗的犧牲品！！！"
    unknown "是嗎……那麼……"
    hide kapo
    hide jatsam
    hide monster
    python:
        pjatsam.setDest(704,352,3)
        renpy.pause(delay=0.30,hard=True)
    show red_screen_a with ComposeTransition(trans=hpunch, after=Dissolve(0.2))
    hide red_screen_a with Dissolve(0.2)
    python:
        pmonst.setDying(True)
        renpy.pause(delay=0.5,hard=True)
    show kapo flip at character_1
    show jatsam flip at character_2
    unknown "抱歉，但我必須阻止這個實驗……不能再讓更多人犧牲！"
    show jatsam flip at character_3 with ease
    show jatsam at character_3 with Dissolve(0.2)
    unknown "已經沒事了，嚇到你真的十分抱歉。"
    kapo "不……謝謝你"
    jatsam "我叫一心，你來到這裏相信你也大概明白這裏正進行生化實驗，我和剛才的狼人，都是實驗品之一。"
    show kapo frownsmile flip at character_1
    kapo "不可能……"
    jatsam "可能要你相信我仍需一點時間，但你留在這裏也很危險。"
    jatsam "看來你也只是誤打誤撞進來的，這樣吧，我護送你到外面，你以後都別再接近那位『老師』了。"
    hide kapo
    hide jatsam
    python:
        closeMap()
        del storeroom_mapsprite_playonly
        del pkapo
        del pjatsam
        del pmonst
    stop music
    python:
        playerX = None
        playerY = None
        store_story_read = True
        jatsam_just = True
        jatsam_team = True
        renpy.jump("lab_storeroom_map_controllable")
    with dissolve
    return
label lab_storeroom_map_controllable:
    scene
    scene black_screen onlayer submaster
    window hide None
    play music "music/school.ogg"
    python:
        ui.layer("mapEngine")
        storeroom_mapsprite = OverworldDisplayable(map_layout = lab_storeroom_layout, tileList = lab_store_tiles,
            portals = lab_storeroom_portals, portal_tiles = [],
            enemy_layout = lab_storeroom_enemies, enemySprites = [],
            NPCSprites = [], #villagers, uses the same layout as enemies
            FollowerSprites = lab_followers,
            groundLayout = lab_storeroom_ground,
            playerSprites = kapo_sprites, playerX = playerX, playerY = playerY,
            scrolling = True)
        ui.add(storeroom_mapsprite)
        ui.close()
    if jatsam_just:
        show kapo flip at character_1
        show jatsam at character_3
        jatsam "你記得進來時的路嗎？"
        kapo "不…我一醒來就在這裹了…"
        jatsam "….好吧，我們四處找找"
        hide kapo
        hide jatsam
        $ jatsam_just = False
    python:
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        del storeroom_mapsprite
    stop music
    python:
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
    with dissolve
    return

label lab_store_greenbottle:
    show jatsam flip at character_1
    show kapo at character_3
    kapo "這是什麼…好噁心…"
    "找到一瓶綠色的液體，裏面泡着一塊血肉模糊的肉塊"
    jatsam "大概是實驗用的器官吧，說不定會放在我體內..."
    $ store_greenbottle = True
    return

label lab_store_report:
    show item labreport at truecenter with dissolve
    pause
    hide item labreport with dissolve
    show jatsam flip at character_1
    show kapo at character_3
    kapo "這……."
    jatsam "看來這些就是受害者名單…都是孤兒和獨身人士…即使突然消失也無人知曉……"
    kapo "可是活人實驗本身也有問題……"
    $ store_report = True
    return

label lab_store_trygetkey:
    if lab_key:
        "(已經找過了)"
    elif store_greenbottle and store_report:
        $ lab_key = True
        "{color=#0000ff}已獲得 實驗室鑰匙{/color}"
    else:
        "(還是先到處找找吧)"
    return

label lab_storeroom_to_hall:
    return (True, "hall_map_before")

label lab_lab_map_pre:
    pass
label lab_lab_map:
    stop music
    "aaaaaaaaaa"
    "bbbbbbbbb"
    "cccccccccc"
