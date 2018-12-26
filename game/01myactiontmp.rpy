init -1500 python:
    ##########################################################################
    # File contstants.

    _weekday_name_long = [
        _("{#weekday}Monday"),
        _("{#weekday}Tuesday"),
        _("{#weekday}Wednesday"),
        _("{#weekday}Thursday"),
        _("{#weekday}Friday"),
        _("{#weekday}Saturday"),
        _("{#weekday}Sunday"),
    ]


    _weekday_name_short = [
        _("{#weekday_short}Mon"),
        _("{#weekday_short}Tue"),
        _("{#weekday_short}Wed"),
        _("{#weekday_short}Thu"),
        _("{#weekday_short}Fri"),
        _("{#weekday_short}Sat"),
        _("{#weekday_short}Sun"),
    ]

    _month_name_long = [
        _("{#month}January"),
        _("{#month}February"),
        _("{#month}March"),
        _("{#month}April"),
        _("{#month}May"),
        _("{#month}June"),
        _("{#month}July"),
        _("{#month}August"),
        _("{#month}September"),
        _("{#month}October"),
        _("{#month}November"),
        _("{#month}December"),
    ]


    _month_name_short = [
        _("{#month_short}Jan"),
        _("{#month_short}Feb"),
        _("{#month_short}Mar"),
        _("{#month_short}Apr"),
        _("{#month_short}May"),
        _("{#month_short}Jun"),
        _("{#month_short}Jul"),
        _("{#month_short}Aug"),
        _("{#month_short}Sep"),
        _("{#month_short}Oct"),
        _("{#month_short}Nov"),
        _("{#month_short}Dec"),
    ]

    def _strftime(format, t):
        """
        A version of strftime that's meant to work with Ren'Py's translation
        system.
        """
        rv = format

        month = t[1] - 1
        wday = t[6]

        rv = rv.replace("%a", __(_weekday_name_short[wday]))
        rv = rv.replace("%A", __(_weekday_name_long[wday]))
        rv = rv.replace("%b", __(_month_name_short[month]))
        rv = rv.replace("%B", __(_month_name_long[month]))

        if "%" in rv:
            import time
            rv = time.strftime(rv.encode("utf-8"), t).decode("utf-8")

        return rv


    ##########################################################################
    # File functions

    config.linear_saves_page_size = None
    config.quicksave_slots = 10

    # The number of file pages per folder.
    config.file_pages_per_folder = 100

    if persistent._file_page is None:
        persistent._file_page = "1"

    if persistent._file_folder is None:
        persistent._file_folder = 0

    if persistent._file_page_name is None:
        persistent._file_page_name = { }

    config.file_page_names = [ ]

    config.predict_file_pages = True

    def __slotname(name, page=None, slot=False):

        if slot:
            return name

        if page is None:
            page = persistent._file_page

        try:
            page = int(page)
            page = page + persistent._file_folder * config.file_pages_per_folder
        except ValueError:
            pass

        if config.linear_saves_page_size is not None:
            try:
                page = int(page)
                name = int(name)
                return str((page - 1) * config.linear_saves_page_size + name)
            except ValueError:
                pass

        return str(page) + "-" + str(name)

    def __newest_slot():
        """
        Returns the name of the newest slot.
        """

        return renpy.newest_slot(r'\d+')

    def __unused_slot_name(page):
        """
        Returns an unused name of a slot on the current page. (This will
        likely be a very big number, as it's based on the current unix time.)
        """

        import time

        rv = int(time.time())

        while True:
            if not renpy.can_load(__slotname(str(rv), page)):
                return str(rv)

            rv += 1
    class MyFileSave(Action, DictEquality):
        """
         :doc: file_action

         Saves the file.

         The button with this slot is selected if it's marked as the
         newest save file.

         `name`
             The name of the slot to save to. If None, an unused slot
             (a large number based on the current time) will be used.

         `confirm`
             If true, then we will prompt before overwriting a file.

         `newest`
             Ignored.

         `page`
             The name of the page that the slot is on. If None, the current
             page is used.

         `cycle`
             If true, then saves on the supplied page will be cycled before
             being shown to the user. :var:`config.quicksave_slots` slots are
             used in the cycle.

         `slot`
             If True, `name` is taken to be a slot name, and `page` is ignored.
         """

        alt = "Save slot [text]"
        slot = None

        def __init__(self, name, confirm=True, newest=True, page=None, cycle=False, slot=False):
            if name is None:
                name = __unused_slot_name(page)

            self.name = name
            self.confirm = confirm
            self.page = page
            self.cycle = cycle
            self.slot = slot

            try:
                self.alt = __("Save slot %s: [text]") % (name,)
            except:
                self.alt = "Save slot %s: [text]" % (name,)

        def __call__(self):

            if not self.get_sensitive():
                return

            fn = __slotname(self.name, self.page, self.slot)

            if renpy.scan_saved_game(fn):
                if self.confirm:
                    layout.yesno_screen(layout.OVERWRITE_SAVE, FileSave(self.name, False, False, self.page, cycle=self.cycle, slot=self.slot))
                    return

            if self.cycle:
                renpy.renpy.loadsave.cycle_saves(self.page + "-", config.quicksave_slots)

            myloadsave.save(fn, extra_info=save_name)

            renpy.restart_interaction()

        def get_sensitive(self):
            if _in_replay:
                return False
            elif main_menu:
                return False
            elif (self.page or persistent._file_page) == "auto":
                return False
            else:
                return True

        def get_selected(self):
            if not self.confirm:
                return False

            return __newest_slot() == __slotname(self.name, self.page, self.slot)

    def MyFileAction(name, page=None, **kwargs):
        """
         :doc: file_action

         "Does the right thing" with the file. This means loading it if the
         load screen is showing (current screen is named "load"), and saving
         otherwise.

         `name`
             The name of the slot to save to or load from. If None, an unused slot
             (a large number based on the current time) will be used.

         `page`
             The page that the file will be saved to or loaded from. If None, the
             current page is used.

         Other keyword arguments are passed to FileLoad or FileSave.
         """

        if renpy.current_screen().screen_name[0] == "load":
            return FileLoad(name, page=page, **kwargs)
        else:
            return MyFileSave(name, page=page, **kwargs)
