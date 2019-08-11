import pathlib

root_folder = pathlib.Path(__file__).parent
stylesheet_folder = root_folder/"stylesheet"

stylesheets = {
	"default": (stylesheet_folder/"stylesheet.qss").resolve()
}