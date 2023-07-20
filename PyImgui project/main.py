import glfw
import OpenGL.GL as gl

import imgui
from imgui.integrations.glfw import GlfwRenderer
import menu

def main():
    imgui.create_context()
    window = impl_glfw_init()
    impl = GlfwRenderer(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        imgui.push_style_var(imgui.STYLE_WINDOW_ROUNDING, 0.0)
        imgui.core.style_colors_light()

        imgui.new_frame()

        menu.menu()

        gl.glClearColor(0.3, 0.3, 0.3, 0.3)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.terminate()


def impl_glfw_init():
    if not glfw.init():
        print("not initialize OpenGL context")
        exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(
        int(1280), int(720), "Application", None, None
    )
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("not initialize Window")
        exit(1)

    return window

if __name__ == "__main__":
    main()