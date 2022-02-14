import os
import inkex
from inkex.command import inkscape


APP_ICON_SIZES = [
    20, 29, 40, 58, 60, 76, 87,
    80, 120, 152, 167, 180, 1024
]


class AppIconExportExtension(inkex.EffectExtension):
    def effect(self):
        if len(self.options.ids) == 0:
            self.msg("No object selected")
            return
        
        node_id = self.options.ids[0]
        for size in APP_ICON_SIZES:
            self.export_size(node_id, size)

    def export_size(self, node_id, size):
        kwargs = {
            'export-id': node_id,
            'export-filename': f"{os.path.expanduser('~/Desktop')}/AppIcon_{size}.png",
            'export-height': str(size),
            'export-width': str(size),
        }
        svg_file = self.options.input_file 
        inkscape(svg_file, **kwargs)


if __name__ == "__main__":
    AppIconExportExtension().run()
