init offset = -1

screen tips(content):
    style_prefix "tips"
    fixed:
        #style "tips_vbox"
        yalign 1
        xalign 0.5

        add "gui/button/choice_idle_background.png" xalign 0.5 yalign 0.0
        text content id "content" xalign 0.5 yalign 0.0

# style tips_vbox:
#     xalign 0.5
#     yalign 0.0
#     background Image("gui/button/choice_idle_background.png",xalign=0.5,yalign=0.0)

screen choice_timed(items, timelimit, limitaction):
    style_prefix "choice"

    vbox:
        timer timelimit action limitaction
        for i in items:
            textbutton i.caption action i.action
