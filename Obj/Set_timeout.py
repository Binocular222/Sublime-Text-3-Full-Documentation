import sublime, sublime_plugin

class TestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_timeout_async(lambda: self.view.run_command("sub"), 100)

class SubCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        n = sublime.active_window().new_file()
        n.set_scratch(True)
        n.insert(edit, 0, 'In here')