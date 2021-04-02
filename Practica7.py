class salidas:
    de crear(self):
    project = QgsProject.instance()
    #get a reference to the layout manager
    manager = project.layoutManager()
    #make a new print layout object
    layout = QgsPrintLayout(project)
    layoutName = "PrintLayout"
    layouts_list = manager.printLayouts()
    for layout in layouts_list:
    if layout.name() == layoutName:
    manager.removeLayout(layout)
    layout = QgsPrintLayout(project)
    #needs to call this according to API documentaiton
    layout.initializeDefaults()
    layout.setName(layoutName)
    layout_page = QgsLayoutItemPage(layout)
    layout_page.setPageSize(QgsLayoutSize(210, 297, QgsUnitTypes.LayoutMillimeters))
    layout_page.decodePageOrientation('Portrait')
    #add layout to manager