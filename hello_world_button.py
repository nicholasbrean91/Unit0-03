




import ui

def hello_world_button(sender):
	view['Hello_world_label'].text = ("Hello, World!")


view = ui.load_view()
view.present('sheet')
