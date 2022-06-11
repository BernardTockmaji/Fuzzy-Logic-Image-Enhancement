import enhance_image
import gui

if __name__ == '__main__':
    gui.renderGUI()

    enhance_image.enhance_image(gui.fileName)
