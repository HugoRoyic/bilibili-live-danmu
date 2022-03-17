from HeadlessMainWindow import HeadlessMainWindow
from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection


TOOLTIP = "A headless mainwindow (Python)"
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    HeadlessMainWindow, module="headlessmainwindow", tool_tip=TOOLTIP)
