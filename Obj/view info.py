import sublime, sublime_plugin
class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, view):
		sublime.set_clipboard('some message')
		sublime.status_message('some message')
		sublime.message_dialog('some message')