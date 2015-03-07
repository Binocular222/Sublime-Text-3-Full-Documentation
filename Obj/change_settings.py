import sublime, sublime_plugin
class change_settings(sublime_plugin.TextCommand):
    def run(self, view):
        if self.view.settings().get('word_wrap') == 'true' :
            self.view.settings().set('word_wrap', 'false')
        else:
            self.view.settings().set('word_wrap', 'true')

#Other examples:
    def run(self, view):
        self.view.run_command("toggle_setting", {"setting": "word_wrap"})
        self.view.settings().set('syntax', 'Packages/Tidea/Tidea.tmLanguage')