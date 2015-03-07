import sublime, sublime_plugin, subprocess, os

class view_scope(sublime_plugin.TextCommand):
	def run(self, view):
		CursorLocation = self.view.sel()[0]
		ScopeName = self.view.scope_name(CursorLocation.a)
		ScopeText = self.view.substr(self.view.extract_scope(CursorLocation.a))
		sublime.set_clipboard(ScopeName)
		sublime.status_message(ScopeName)

