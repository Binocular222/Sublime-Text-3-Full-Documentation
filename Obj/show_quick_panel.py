import sublime, sublime_plugin

class examplCommand(sublime_plugin.TextCommand):
    def run(self, view):
        self.list_items = ["abc", "xyz", "123"]
        sublime.active_window().show_quick_panel(self.list_items, self._on_select)

    def _on_select(self, idx):
        if idx > -1:
            selected = self.list_items[idx]
            sublime.message_dialog(selected)
