import sublime, sublime_plugin

class DynCodeListener(sublime_plugin.EventListener):
	def on_post_save(self,view):		
		if view.file_name() :
			first_line = view.substr(view.line(0)).split(' ')
			first_line = first_line.replace('\\','/')
			if first_line[0] == '#DYNCODE' :
				file_name = view.file_name().split('/')[-1]
				execute = ("curl " + first_line[1] + "/" + file_name + " -X POST --data-binary @" + view.file_name()).split(' ')
				view.window().run_command("exec",{"cmd":execute})

