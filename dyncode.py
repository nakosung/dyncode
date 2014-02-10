import sublime, sublime_plugin

class DynCodeListener(sublime_plugin.EventListener):
	def on_post_save(self,view):		
		if view.file_name() and view.substr(view.line(0)) == '#LIVE':
			file_name = view.file_name().split('/')[-1]
			ext = file_name.split('.')[-1]
			if ext == 'coffee':
				execute = ("curl http://localhost:8080/coffee/" + file_name + " -X POST --data-binary @" + view.file_name()).split(' ')
				view.window().run_command("exec",{"cmd":execute})


