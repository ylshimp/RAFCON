import gtk
from gtkmvc import Controller, Observer
from mvc.controllers import StatePropertiesController, ContainerStateController, GraphicalEditorController,\
    StateDataPortEditorController, GlobalVariableManagerController, ExternalModuleManagerController,\
    SourceEditorController, SingleWidgetWindowController,StateEditorController, StateMachineTreeController,\
    LibraryTreeController
from mvc.models import StateModel
from statemachine.states.execution_state import ExecutionState


class MainWindowController(Controller):

    def __init__(self, root_state_model, view, em_module, gvm_model):
        Controller.__init__(self, root_state_model, view)

        left_v_pane = view["left_v_pane"]

        console_scroller = left_v_pane.get_child2()
        left_v_pane.remove(console_scroller)
        view.logging_view.get_top_widget().show()
        left_v_pane.add2(view.logging_view.get_top_widget())
        #console_scroller.add(view.logging_view["textview"])

        tree_notebook = view["tree_notebook"]
        #remove placeholder tab
        library_tree_tab = view['library_tree_placeholder']
        #print tree_notebook.get_tab_label(self.library_tree_tab).get_text()
        #print tree_notebook.page_num(self.library_tree_tab)
        page_num = tree_notebook.page_num(library_tree_tab)
        tree_notebook.remove_page(page_num)
        #append new tab
        self.library_controller = LibraryTreeController(None, view.library_tree)
        libraries_label = gtk.Label('Libraries')
        tree_notebook.insert_page(view.library_tree, libraries_label, page_num)

        #remove placeholder tab
        state_machine_tree_tab = view['state_machine_tree_placeholder']
        page_num = tree_notebook.page_num(state_machine_tree_tab)
        tree_notebook.remove_page(page_num)
        #append new tab
        self.state_machine_tree_controller = StateMachineTreeController(root_state_model, view.state_machine_tree)
        state_machine_label = gtk.Label('Statemachine Tree')
        tree_notebook.insert_page(view.state_machine_tree, state_machine_label, page_num)

        graphical_editor_frame = view['graphical_editor_frame']
        self.graphical_editor = GraphicalEditorController(root_state_model, view.graphical_editor_view)
        graphical_editor_frame.add(view.graphical_editor_view['main_frame'])
        #self.graphical_editor = GraphicalEditorController(model, view.graphical_editor_window.get_top_widget())
        #test = SingleWidgetWindowController(model, view.graphical_editor_window, GraphicalEditorController)

        em_global_notebook = view["em_global_notebook"]
        #remove placeholder tab
        external_modules_tab = view['external_modules_placeholder']
        page_num = em_global_notebook.page_num(external_modules_tab)
        em_global_notebook.remove_page(page_num)
        #append new tab
        self.external_modules_controller = ExternalModuleManagerController(em_module, view.external_module_manager_view)
        external_modules_label = gtk.Label('External Modules')
        em_global_notebook.insert_page(view.external_module_manager_view.get_top_widget(), external_modules_label, page_num)

        #remove placeholder tab
        global_variables_tab = view['global_variables_placeholder']
        page_num = em_global_notebook.page_num(global_variables_tab)
        em_global_notebook.remove_page(page_num)
        #append new tab
        self.external_modules_controller = GlobalVariableManagerController(gvm_model, view.global_var_manager_view)
        global_variables_label = gtk.Label('Global Variables')
        em_global_notebook.insert_page(view.global_var_manager_view.get_top_widget(), global_variables_label, page_num)

    def register_view(self, view):
        view['main_window'].connect('destroy', gtk.main_quit)

    def on_about_activate(self, widget, data=None):
        pass

    def on_backward_step_activate(self, widget, data=None):
        pass

    def on_step_activate(self, widget, data=None):
        pass

    def on_step_mode_activate(self, widget, data=None):
        pass

    def on_stop_activate(self, widget, data=None):
        pass

    def on_pause_activate(self, widget, data=None):
        pass

    def on_start_activate(self, widget, data=None):
        pass

    def on_grid_toggled(self, widget, data=None):
        pass

    def on_redo_activate(self, widget, data=None):
        pass

    def on_undo_activate(self, widget, data=None):
        pass

    def on_ungroup_states_activate(self, widget, data=None):
        pass

    def on_group_states_activate(self, widget, data=None):
        pass

    def on_delete_state_activate(self, widget, data=None):
        pass

    def on_add_state_activate(self, widget, data=None):
        pass

    def on_delete_activate(self, widget, data=None):
        pass

    def on_paste_activate(self, widget, data=None):
        pass

    def on_copy_activate(self, widget, data=None):
        pass

    def on_cut_activate(self, widget, data=None):
        pass

    def on_quit_activate(self, widget, data=None):
        pass

    def on_menu_properties_activate(self, widget, data=None):
        pass

    def on_save_as_activate(self, widget, data=None):
        pass

    def on_save_activate(self, widget, data=None):
        pass

    def on_open_activate(self, widget, data=None):
        pass

    def on_new_activate(self, widget, data=None):
        pass
