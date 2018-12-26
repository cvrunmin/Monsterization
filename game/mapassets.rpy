init python:

    class Dummy: #a dummy class used in place of a battle. Normally this should be integrated with Jake's battle engine, instead of using a dummy class.
        def __init__(self,won):
            self.won = won


    ari_battle = Dummy(False)
    #sprite arrays should always be in north, south, east, west order.
    map_on = False #Is a map being displayed? This governs whether the "yesno" screen is modal.

    #SPRITES
    kapo_sprites = [["images/rpg/kapo/kapo_n.png","images/rpg/kapo/kapo_n1.png","images/rpg/kapo/kapo_n2.png"],
    ["images/rpg/kapo/kapo_s.png","images/rpg/kapo/kapo_s1.png","images/rpg/kapo/kapo_s2.png"],
    ["images/rpg/kapo/kapo_e.png","images/rpg/kapo/kapo_e1.png","images/rpg/kapo/kapo_e2.png"],
    ["images/rpg/kapo/kapo_w.png","images/rpg/kapo/kapo_w1.png","images/rpg/kapo/kapo_w2.png"],
    (64,64)
    ]
    jatsam_sprites = [["images/rpg/jatsam/jatsam_n.png","images/rpg/jatsam/jatsam_n1.png","images/rpg/jatsam/jatsam_n2.png"],
    ["images/rpg/jatsam/jatsam_s.png","images/rpg/jatsam/jatsam_s1.png","images/rpg/jatsam/jatsam_s2.png"],
    ["images/rpg/jatsam/jatsam_e.png","images/rpg/jatsam/jatsam_e1.png","images/rpg/jatsam/jatsam_e2.png"],
    ["images/rpg/jatsam/jatsam_w.png","images/rpg/jatsam/jatsam_w1.png","images/rpg/jatsam/jatsam_w2.png"],
    (72,72)
    ]
    teacher_sprites = [["images/rpg/teacher/teacher_n.png","images/rpg/teacher/teacher_n1.png","images/rpg/teacher/teacher_n2.png"],
    ["images/rpg/teacher/teacher_s.png","images/rpg/teacher/teacher_s1.png","images/rpg/teacher/teacher_s2.png"],
    ["images/rpg/teacher/teacher_e.png","images/rpg/teacher/teacher_e1.png","images/rpg/teacher/teacher_e2.png"],
    ["images/rpg/teacher/teacher_w.png","images/rpg/teacher/teacher_w1.png","images/rpg/teacher/teacher_w2.png"],
    (64,64)
    ]
    maid_sprites = [["images/rpg/maid/maid_n.png","images/rpg/maid/maid_n1.png","images/rpg/maid/maid_n2.png"],
    ["images/rpg/maid/maid_s.png","images/rpg/maid/maid_s1.png","images/rpg/maid/maid_s2.png"],
    ["images/rpg/maid/maid_e.png","images/rpg/maid/maid_e1.png","images/rpg/maid/maid_e2.png"],
    ["images/rpg/maid/maid_w.png","images/rpg/maid/maid_w1.png","images/rpg/maid/maid_w2.png"],
    (64,64)
    ]
    monster_sprites = [["images/rpg/monster/monster_n.png","images/rpg/monster/monster_n1.png","images/rpg/monster/monster_n2.png"],
    ["images/rpg/monster/monster_s.png","images/rpg/monster/monster_s1.png","images/rpg/monster/monster_s2.png"],
    ["images/rpg/monster/monster_e.png","images/rpg/monster/monster_e1.png","images/rpg/monster/monster_e2.png"],
    ["images/rpg/monster/monster_w.png","images/rpg/monster/monster_w1.png","images/rpg/monster/monster_w2.png"],
    (64,64)
    ]

    #TILESETS
    #IMPORTANT: every action label should return (<act as goTo>, [goTo label])
    #signifier, base name, building size, roof size, has roof, goToLabel, actionLabel (used for descriptions)
    lab_tiles = [
    ["t", "images/rpg/basement_floor", (64,64), None, False, None, None],
    ["w", "images/rpg/basement_wall", (64,64), None, False, None, None],
    ["s", "images/rpg/bookshelf", (64,128), None, False, None, "lab_hall_bookshelf_fake"],
    ["z", "images/rpg/bookshelf", (64,128), None, False, None, "lab_hall_bookshelf"],
    ["b", "images/rpg/lab_hall_desk", (128,64), None, False, None, "lab_hall_book_fake"],
    ["l", "images/rpg/lab_door", (64,128), None, False, None, "lab_hall_to_lab"],
    ["r", "images/rpg/lab_door", (64,128), None, False, None, "lab_hall_to_storeroom"],
    ]
    lab_store_tiles = [
    ["t", "images/rpg/basement_floor", (64,64), None, False, None, None],
    ["w", "images/rpg/basement_wall", (64,64), None, False, None, None],
    ["1", "images/rpg/lab_store_basket", (64,64), None, False, None, None],
    ["2", "images/rpg/lab_store_greenbottle", (64,64), None, False, None, "lab_store_greenbottle"],
    ["@", "images/rpg/lab_store_greenbottle", (64,64), None, False, None, None],
    ["3", "images/rpg/lab_store_duoble", (64,64), None, False, None, None],
    ["4", "images/rpg/lab_store_sbasket", (64,64), None, False, None, "lab_store_trygetkey"],
    ["$", "images/rpg/lab_store_sbasket", (64,64), None, False, None, None],
    ["5", "images/rpg/lab_store_sbasket2", (64,64), None, False, None, None],
    ["s", "images/rpg/lab_store_sidecabinat", (64,128), None, False, None, "lab_store_report"],
    ["l", "images/rpg/lab_door", (64,128), None, False, None, "lab_storeroom_to_hall"],
    ]


    #signifier, range, roaming,  sprite set, facing, associated battle label, associated battle
    #moordell_enemies = [
    #["a", (512,512), True, ari_sprites, "down", "ari_caught", ari_battle],
    #]

    #signifier, range, roaming,  sprite set, facing, conversation label
    #moordell_villagers = [
    #["v", (256,256), True, villager_sprites, "down", "talky_label"], #example of roaming NPC
    #["b",None, False, villager_sprites,  "down", "talky2"], #example of static NPC
    #]
    lab_followers = [
    ["y",None,True, jatsam_sprites, "down", None]
    ]

    #[signifier, goToLabel]
    lab_hall_portal_tiles = [['s', 'lab_hall_to_storeroom'],['l', 'lab_hall_to_lab']]
    #moordell_portal_tiles = [['p', 'leave_city']]


    #MAP LAYOUTS
    #these maps should align for ease of use.
    #If they don't look square, switch to a monospace font like consolas!

    lab_hall_layout =[
    "wwwwlwwwwwwwwwwwrwwwww",
    "wwwwowwwwwwwwwwwowwwww",
    "wooooobosssszsooooooow",
    "wooooooooooooooo+oooow",
    "woooooooooooooooooooow",
    "woooooooooooooooooooow",
    "woooooooooooooooooooow",
    "wwwwwwwwwwwwwwwwwwwwww",
    ]
    lab_hall_ground =[
    "tttttttttttttttttttttt",
    "tttttttttttttttttttttt",
    "tttttttttttttttttttttt",
    "tttttttttttttttttttttt",
    "tttttttttttttttttttttt",
    "tttttttttttttttttttttt",
    "tttttttttttttttttttttt",
    "tttttttttttttttttttttt",
    ]
    lab_hall_portals =[
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    ]
    lab_hall_enemies =[
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    ]
    lab_hall_enemies_jatsam =[
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooyoooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    "oooooooooooooooooooooo",
    ]
    lab_storeroom_layout =[
    "wwwwwwwwwwwwwwwww",
    "woooo12345ooooosw",
    "wooooooooooooooow",
    "wooooooooooooooow",
    "woooo1@3$5oooooow",
    "wo+ooooooooooooow",
    "wooooooooooooooow",
    "wwlwwwwwwwwwwwwww",
    "wwowwwwwwwwwwwwww",
    ]
    lab_storeroom_ground =[
    "ttttttttttttttttt",
    "ttttttttttttttttt",
    "ttttttttttttttttt",
    "ttttttttttttttttt",
    "ttttttttttttttttt",
    "ttttttttttttttttt",
    "ttttttttttttttttt",
    "ttttttttttttttttt",
    "ttttttttttttttttt",
    ]
    lab_storeroom_portals =[
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    ]

    lab_storeroom_enemies =[
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooyoooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    ]

    moordell_layout =[
    "nnnnnnnonnnnnnn",
    "w3oo*ooo2oo1ooe",
    "woooooo+ooooooe",
    "woooooooooooooe",
    "w3oooooo1oooooe",
    "woooooooooooooe",
    "woooooooooooooe",
    "w2o3ooooo1oo2oe",
    "woooooooooooooe",
    "woooooooooooooe",
    "w3ooo1o3o2oo1oe",
    "woooooooooooooe",
    "woooooooooooooe",
    "w1o2o2ooo3o1ooe",
    "woooooooooooooe",
    "woooooooooooooe",
    "sssssssssssssss",
    ]

    moordell_portals =[
    "ooooooopooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    ]


    moordell_ground =[
    "gggggggpggggggg",
    "gggggggpggggggg",
    "gggggggpggggggg",
    "ppppppppppppppp",
    "gggggggpggggggg",
    "gggggggpggggggg",
    "ppppppppppppppp",
    "gggggggpggggggg",
    "gggggggpggggggg",
    "ppppppppppppppp",
    "gggggggggggggpg",
    "gggggggggggggpg",
    "gggggggggggggpg",
    "ppppppppppppppp",
    "ggggggggggggggg",
    "ggggggggggggggg",
    "ggggggggggggggg",
    ]


    moordell_enemies_layout =[
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooovooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooboooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "oooooaooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    ]
