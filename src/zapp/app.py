import toga
from toga.style.pack import COLUMN, ROW, CENTER


class ZApp(toga.App):
    def startup(self):
        dirname = self.app_dir
        label = self.toga.Label(
            dirname,
            style = Pack(
                alignment = CENTER
            )
        )
        main_box = toga.Box(
            children = [label],
            style = Pack(direction = COLUMN, padding = 10)
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return ZApp()
