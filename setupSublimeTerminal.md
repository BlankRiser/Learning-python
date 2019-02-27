## Installing Interactive terminal in Sublime Text 3
> SublimeREPL enables you to interactively use the terminal unlike the default terminal provided by Sublime
> With SublimeREPL, you can use input without any issues.


1. Download SublimeREPL from package manager
    * Open sublime and press Ctrl+Shift+P and serach "InstallPackage" and press Enter.
    * Search SublimREPL and press Enter.

2. Making SublimeREPL the default build to be executed
    * Go to Tools -> Build System _> New Build System
    * Paste the below code:
     ```
     {
      "target": "run_existing_window_command", 
      "id": "repl_python_run",
      "file": "config/Python/Main.sublime-menu"
     }
     ``` 
     * Save the file as "PythonREPL.json".
     * Go to Tools -> Build System -> PythonREPL and select it.

3. Using SublimeREPL
    * Create/Open any Python script on Sublime.
    * Press Ctrl+B.
    * Another window pops up with the result.
