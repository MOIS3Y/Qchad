# █▀▀ █░█ █▀ ▀█▀ █▀█ █▀▄▀█   █░█░█ █ █▀▄ █▀▀ █▀▀ ▀█▀ █▀
# █▄▄ █▄█ ▄█ ░█░ █▄█ █░▀░█   ▀▄▀▄▀ █ █▄▀ █▄█ ██▄ ░█░ ▄█
# -----------------------------------------------------
from libqtile import bar, hook
from libqtile.log_utils import logger
from libqtile.widget import base
from libqtile.command import lazy


class CurrentLayout(base._TextBox):
    """
    Display the name of the current layout of the current group of the screen,
    the bar containing the widget, is on.
    """

    def __init__(self, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, "", width, **config)

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        layout_id = self.bar.screen.group.current_layout
        self.text = self.bar.screen.group.layouts[layout_id].name
        self.setup_hooks()

        self.add_callbacks(
            {
                "Button1": lazy.next_layout(),
                "Button3": lazy.prev_layout(),
            }
        )

    def _replace_name_layout(self, layout_name):
        layout_symbols = {
            'bsp': '[]=',
        }
        if layout_name == 'bsp':
            return layout_symbols['bsp']
        else:
            return layout_name

    def hook_response(self, layout, group):
        if group.screen is not None and group.screen == self.bar.screen:
            self.text = self._replace_name_layout(layout.name)
            self.bar.draw()

    def setup_hooks(self):
        hook.subscribe.layout_change(self.hook_response)

    def remove_hooks(self):
        hook.unsubscribe.layout_change(self.hook_response)

    def finalize(self):
        self.remove_hooks()
        base._TextBox.finalize(self)
