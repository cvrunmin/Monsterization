# 您可以在此編寫遊戲的腳本。

# image命令可用於定義一個圖像。
# eg. image eileen happy = "eileen_happy.png"
image teacher_living_room = "bg/teacher_living_room.png"
image black_screen = "#000"
image red_screen_a = "#ff00007f"
init 10 python:
    define_characters("images", 2)
    difficulty = -1


# define命令可定義遊戲中出現的角色名稱與對應文本顏色。
define kapo = Character(_('嘉寶'), image='kapo')
define jatsam = Character(_('一心'), image='jatsam')
define teacher = Character(_('老師'), image='teacher')
define unknown = Character('???')
define girl = Character(_('女孩'))
define maid = Character(_('獸女'), image='maid')
define boy = Character(_('男孩'))
define monster = Character(_('怪物'))
define two = Character(_('二人'))

# 遊戲從這裡開始。
label start:

    jump prior

    jump end


label end:
    return

label prior_search:
    $ chance = 3
    while chance > 0:
        if chance == 1:
            "{color=#ff0000}老師好像快要回來了，要快點了。{/color}"
        menu:
            "調查書櫃":
                jump prior.books
            "調查窗戶":
                "老師的家對出是一片翠綠的草地"
                "外面有一隻麻雀降落，{w=1.0}又起飛了"
            "調查桌子":
                "弗蕾雅牌木質桌子。"
                "老師買回來的時候，連價錢標籤都沒有撕掉"
                "上面寫着：「特價$233.3」"
        $ chance -= 1
    show teacher at character_1 with dissolve
    show kapo at character_3 with ease
    teacher "抱歉，聊電話聊太久了，我們繼續吧"
    kapo smile "好的老師！"
    jump ending_normal_person


label prior:
    scene teacher_living_room
    play music "music/summer.ogg" loop
    show teacher at character_1
    show kapo at character_3
    teacher "這裏，關於兩棲類生物的問題懂嗎？"
    kapo "嗯，已經沒問題了，感謝老師的教導！"
    menu:
        kapo "生物科......"
        "我已經瞭如指掌了！":
            $ difficulty = 3
            kapo smile "我已經瞭如指掌了！"
            teacher smile "哈哈，別這樣"
        "我想我明白了不少了":
            $ difficulty = 2
            kapo smile "我想我明白了不少了"
            teacher smile "那就好"
        "幸好有老師你的幫助，我才明白多一點":
            $ difficulty = 1
            kapo "幸好有老師你的幫助，我才明白多一點"
            teacher "不用謝"
        "我差點就放棄了":
            $ difficulty = 0
            kapo frownsmile "我差點就放棄了"
            teacher "別說晦氣說話"
    teacher "你對生物科很有天份，我很期待你的表現喔。"
    kapo "是！我會加油的！"
    play sound "<from 1 to 2.5>sound/ringtone.ogg" loop
    "在廚房裡的電話突然響起"
    teacher "抱歉，我先去接個電話。"
    show teacher at offscreenleft
    show kapo at character_2
    with ease
    stop sound
    kapo "老師的家……"

    jump prior_search

    label .books:
        "書櫃上有一排書，在藍色書列中有一本書是紅色的"
        "嘉寶把它拿了下來"
        kapo "這本書……《獸耳娘合成計劃》……？"
        "隨便翻開一頁，上面寫着："
        "實驗1：抽取動物身體上不同部份的細胞，通過植入改變人體構造，使人類能擁有動物的身體部位……"

        show teacher smile at character_1 with dissolve
        show kapo at character_3 with ease

        teacher "嘉寶……你看了那本筆記？"
        kapo "是的，沒想到老師你居然在研究這種實驗！雖然我不是很懂，但如果成功了，人類就會大進化了！對吧？"
        teacher "沒錯喔，你覺得如何？"
        kapo "真厲害！我會全力支持老師你的實驗！"
        teacher "喔……是嗎？"
        teacher "我猜你補習得有點累了，先喝杯水吧。"
        kapo "謝謝老師！"
        show kapo at character_3 with hpunch
        kapo "咦……"
        stop music fadeout 1
        hide kapo
        show teacher_badsmile at character_1
        with Dissolve(0.2)
        teacher "你的答案，老師很滿意喔……那就拜託你囉——"
        scene black_screen with fade
        jump chapter_1

label chapter_1:
    scene basement_bedroom with fade
    play music "music/thinking.ogg"
    show kapo at character_2 with Dissolve(0.2)
    kapo "這裏……是……？"
    "床邊有一張便條{w=0.5}，看來是老師留下來的"
    show item teachernote at truecenter with dissolve
    pause
    hide item teachernote with dissolve
    kapo "剛才我是貧血暈倒了？{p=0.5}但現在感覺身體沒什麼不舒服，而且老師叫我好好在房間等他回來，就說明老師不在家？"
    kapo bigsmile "好！趕快去老師家探險！"
    scene basement_hall with dissolve
    kapo "走出房間是比客廳更大且沒有窗戶的房間，難道是地下實驗室？！"
    kapo bigsmile "喔喔！更有探險的感覺了！"
    jump hall_map_pre
