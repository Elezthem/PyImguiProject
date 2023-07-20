import imgui

def menu():

    imgui.set_next_window_size(250, 250)
    #imgui.set_next_window_position(0, 0)
    imgui.begin(
        "Hello World",
       # flags=imgui.WINDOW_NO_MOVE |
       #       imgui.WINDOW_NO_RESIZE |
       #       imgui.WINDOW_NO_SAVED_SETTINGS
    )
    imgui.text("Welcome to Hell")
    imgui.button("Click me!")
    
    imgui.end()