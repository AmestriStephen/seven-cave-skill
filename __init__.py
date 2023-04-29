from mycroft import MycroftSkill, intent_file_handler


class SevenCave(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cave.seven.intent')
    def handle_cave_seven(self, message):
        self.speak_dialog('cave.seven')


def create_skill():
    return SevenCave()

