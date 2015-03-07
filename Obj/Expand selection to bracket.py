import sublime, sublime_plugin                              # import 2 modules (collections of Classes)
class expand_to_bracketCommand(sublime_plugin.TextCommand): # initiate TextCommand Class (collection of methods). Resolved command name = "expand_to_bracket"
    def run(self, edit):
        braces = False
        sels = self.view.sel()                              # Method sel() provided by View Class → Return region of current selections
        for sel in sels:                                    # Loop through each region (user may have multiple selection)
            if self.view.substr(sel).find('{') != -1:       # Method substr(sel) return string inside "sel" region. Method find('{') check if there's "{" Then:
                braces = True
        if not braces:                                      # After looping through all "sels" region, if no "{" found (braces = False)
            new_sels = []
            for sel in sels:
                new_sels.append(self.view.find('\}', sel.end()))
            sels.clear()
            for sel in new_sels:
                sels.add(sel)
            self.view.run_command("expand_selection", {"to": "brackets"})
