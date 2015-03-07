import sublime, sublime_plugin                      # import 2 modules (collections of Classes)
class ExampleCommand(sublime_plugin.TextCommand):   # initiate TextCommand Class (collection of methods). Resolved command name = "example"
    def run(self, edit):                            # Initiate "edit" object to be used by TextCommand
        self.view.insert(edit, 0, "Hello, World!")  # method insert(edit, point, string) in View Class [[Sublime Text.API.View.Method.txt]]


#Other example:  Insert 'this char' at the beginning and end of selected text
	def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            self.view.insert(edit, sel.end(), 'this char')
            self.view.insert(edit, sel.begin(), 'this char')