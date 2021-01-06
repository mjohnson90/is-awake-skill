from mycroft import MycroftSkill, intent_file_handler


class IsAwake(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('awake.is.intent')
    def handle_awake_is(self, message):
        self.speak_dialog('awake.is')


def create_skill():
    return IsAwake()

