init offset = -1
transform character_1:
    maxsize (1280*1.25, 720*1.25)
    xalign 0.5
    yalign 1.0
    xpos 1280/3
    ypos 1080


transform character_2:
    maxsize (1280*1.25, 720*1.25)
    xalign 0.5
    yalign 1.0
    xpos 1280 / 2
    ypos 1080


transform character_3:
    maxsize (1280*1.25, 720*1.25)
    xalign 0.5
    yalign 1.0
    xpos 1280* 2/3
    ypos 1080

transform character_3_far:
    maxsize (1280*1.25, 720*1.25)
    xalign 1.0
    yalign 1.0
    xpos 1280
    ypos 1080


init python:
    import os
    def define_characters(characterImageFolder, excludeFirstXFolders=0, flip=True):
        for path in renpy.list_files():
            if path.startswith(characterImageFolder + "/"):
                path_list = path.split("/")
                if os.path.splitext(path_list[-1])[1] in ['.webp', '.png', '.jpg', '.jpeg']:
                    path_list[-1] = os.path.splitext(path_list[-1])[0]
                    path_list = path_list[:-1] + path_list[-1].split("_")
                    path_list = tuple(path_list[(min(excludeFirstXFolders, len(path_list) - 1)):])
                    renpy.image(path_list, path)
                    if flip:
                        renpy.image(path_list + ("flip", ), im.Flip(path, horizontal=True))

    def hard_pause(delay):
        checkpoint = False

        roll_forward = renpy.exports.roll_forward_info()
        if roll_forward not in [ True, False ]:
            roll_forward = None

        renpy.exports.mode('pause')

        afm = None

        renpy.ui.saybehavior(afm=afm, dismiss='dismiss_hard_pause')

        renpy.ui.pausebehavior(delay, True)

        rv = renpy.ui.interact(mouse='pause', type='pause')

        renpy.game.interface.do_with(None, None)

        return rv
