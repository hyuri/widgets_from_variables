# Widgets From Variables
Automatically generate widgets from variables, based on their types.

![screenshot](https://user-images.githubusercontent.com/18584014/62830911-3d346d00-bbed-11e9-925b-62d7fbe7b901.png)

It's still in a prototype phase and, right now, the variables in the script are not getting updated if you change the corresponding values in the widget(no binding happening). Also, script is not getting aexec and its not doing anything
It's just something I've been wanting to do for some time but never got the time to do it. Plus, it was an opportunity for me to get my feet wet with Qt(PySide2), and, in the end, it's also going to be very useful for future utilities that myself—or anyone, now—might write.

### TODO:
...
- Expand the widget set to include all kinds of type-widget mappings, like color wheels for color types/classes/objects;
- Improve the design of the type-widget mapping system;
- Add button, at the bottom of the stack, to load/add new script;
- Add button to Panel, to unload or disable a script;

- Future: Perhaps even try to infer the type based on the value("#808080"—or rgba(0.5, 0.5, 0.5, 1.0)(hopefully linear color from the start)—would be inferred as of a color type, for example. We could even have plugins register what widgets they have available or want to use, and make available the ability to choose which widget is to be mapped to a given compatible type e.g.: which color widget to map to type "color").
