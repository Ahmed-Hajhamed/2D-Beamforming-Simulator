from email.charset import QP
from PyQt5.QtWidgets import (
     QGridLayout, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit, QRadioButton,
    QPushButton, QComboBox, QSlider
)
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class beam_Plot(FigureCanvas):
    def __init__(self, linear = True, parent=None, width=4, height=3, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        if linear:
            self.axes = self.fig.add_subplot(111)
        else:
            self.axes = self.fig.add_subplot(111, projection='polar')
        super().__init__(self.fig)


class ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Beamforming")
        MainWindow.setGeometry(100, 100, 1200, 800) 

        self.phase_shifts_sliders_values = [] 

        
        h_main_layout = QHBoxLayout()
        ############################################################
        v_layout_of_paramet = QVBoxLayout()
        # spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        # v_layout_of_paramet.addItem(spacer)
        # v_layout_of_paramet.setStrech(1)
        # v_layout_of_paramet.setSpacing(15)
        
        self.combo_box_of_senario = QComboBox()
        self.combo_box_of_senario.addItem("5G")
        self.combo_box_of_senario.addItem("Ultrasoundx")
        self.combo_box_of_senario.addItem("Tumor Ablation")

        self.applay_the_senario = QPushButton("Apply")

        h_layout_of_senario = create_layout_of_parameter(self.combo_box_of_senario, self.applay_the_senario)
        v_layout_of_paramet.addLayout(h_layout_of_senario)

        self.current_arrays_combo_box = QComboBox()
        self.current_arrays_combo_box.addItem("Add Array")
        self.button_of_add_new_array = QPushButton("Add Array")
        h_layout_current_array = create_layout_of_parameter( self.button_of_add_new_array, self.current_arrays_combo_box)
        v_layout_of_paramet.addLayout(h_layout_current_array)

        self.radio_button_of_linear = QRadioButton("Linear")
        self.radio_button_of_linear.setChecked(True)
        self.radio_button_of_linear.toggled.connect(self.change_type)

        self.radio_button_of_curve = QRadioButton("Curved")
        self.radio_button_of_curve.toggled.connect(self.change_type)
        
        h_layout_of_select = create_layout_of_parameter(self.radio_button_of_linear, self.radio_button_of_curve)
        v_layout_of_paramet.addLayout(h_layout_of_select)


        self.slider_of_transmiters_number = slider_creator(Maximum=16, Minimum=1)
        self.label_of_transmiters_number  = create_label("Transmitters")
        self.label_of_transmiters_number_value = create_label(str(self.slider_of_transmiters_number.value()))
        h_layout_transmiters_number = create_layout_of_parameter(self.label_of_transmiters_number, self.slider_of_transmiters_number, self.label_of_transmiters_number_value)
        v_layout_of_paramet.addLayout(h_layout_transmiters_number)

        self.slider_of_element_spacing = slider_creator(Maximum=8, Minimum=1)
        self.label_of_element_spacing  = create_label("Elements Spacing")
        self.label_of_element_spacing_vlaue = create_label(str(self.slider_of_element_spacing.value())+" λ")
        self.h_layout_element_spacing = create_layout_of_parameter(self.label_of_element_spacing, self.slider_of_element_spacing, self.label_of_element_spacing_vlaue)
        v_layout_of_paramet.addLayout(self.h_layout_element_spacing)


        self.frequencies_line_edit = create_line_edit(Maximum=100)
        self.label_frequencies = create_label("Frequecies")
        h_layout_of_frequencis = create_layout_of_parameter(self.label_frequencies, self.frequencies_line_edit)
        v_layout_of_paramet.addLayout(h_layout_of_frequencis)

        # self.wavelengths_line_edit = QLineEdit()
        # self.label_wavelengths = create_label("Wavelengths")
        # h_layout_of_wavelengths = create_layout_of_parameter(self.label_wavelengths, self.wavelengths_line_edit)
        # v_layout_of_paramet.addLayout(h_layout_of_wavelengths)

        self.array_position_x_line_edit = create_line_edit(Maximum=100, Minimum= -100)
        self.array_position_y_line_edit = create_line_edit(Maximum=100)
        self.label_position = create_label("Position")
        self.label_position_x = create_label("X")
        self.label_position_y = create_label("Y")
        h_layout_of_position = create_layout_of_parameter(self.label_position, self.label_position_x, self.array_position_x_line_edit, self.label_position_y, self.array_position_y_line_edit)
        v_layout_of_paramet.addLayout(h_layout_of_position)

        self.slider_of_steering_angle = slider_creator(Maximum=90, Minimum=-90)
        self.label_steering_angle = create_label("Steering Angle")
        self.label_steering_angle_value = create_label(str(self.slider_of_steering_angle.value())+"˚")
        h_layout_of_steering_angle = create_layout_of_parameter(self.label_steering_angle, self.slider_of_steering_angle, self.label_steering_angle_value)
        v_layout_of_paramet.addLayout(h_layout_of_steering_angle)

        self.radius_line_edit = create_line_edit(Maximum=100)
        self.label_of_radius = create_label("Radius")
        self.h_layout_of_Radius = create_layout_of_parameter(self.label_of_radius, self.radius_line_edit)
        v_layout_of_paramet.addLayout(self.h_layout_of_Radius)
        hide_layout(self.h_layout_of_Radius)

        self.slider_of_arc_angle = slider_creator(Maximum=120, Minimum=-120)
        self.label_arc_angle= create_label("Arc Angle")
        self.label_arc_angle_value = create_label(str(self.slider_of_arc_angle.value())+"˚")
        self.h_layout_of_arc_angle = create_layout_of_parameter(self.label_arc_angle, self.slider_of_arc_angle, self.label_arc_angle_value)
        v_layout_of_paramet.addLayout(self.h_layout_of_arc_angle)
        hide_layout(self.h_layout_of_arc_angle)
        
        self.array_name_line_edit = QLineEdit()
        self.label_of_array_name = create_label("Array Name")
        h_layout_of_array_name = create_layout_of_parameter(self.label_of_array_name, self.array_name_line_edit)
        v_layout_of_paramet.addLayout(h_layout_of_array_name)

        self.save_button = QPushButton("Save")
        self.remove_array_button = QPushButton("Remove")
        h_layout_of_save_remove = create_layout_of_parameter(self.save_button, self.remove_array_button)
        v_layout_of_paramet.addLayout(h_layout_of_save_remove)
        ##################################################
        v_layout_of_reciver_parameter = QVBoxLayout()

        self.current_recivers_combo_box = QComboBox()
        self.current_recivers_combo_box.addItem("Add Receiver")
        self.button_of_add_new_reciver = QPushButton("Add Reciver")
        h_layout_current_reciver = create_layout_of_parameter(self.button_of_add_new_reciver, self.current_recivers_combo_box)
        v_layout_of_reciver_parameter.addLayout(h_layout_current_reciver)

        # self.reciver_number = QComboBox()
        # self.reciver_number.addItem("Add Array")
        # self.label_of_reciver_number = create_label("Reciver")
        # h_layout_of_reciver_number = create_layout_of_parameter(self.label_of_reciver_number, self.reciver_number)
        # v_layout_of_reciver_parameter.addLayout(h_layout_of_reciver_number)

        self.reciver_position_x = create_line_edit(Maximum=100, Minimum= -100)
        self.reciver_position_y = create_line_edit(Maximum=100)
        self.label_of_reciver_position_x= create_label("X")
        self.label_of_reciver_position_y = create_label("Y")
        self.label_of_reciver_position = create_label("Position")
        h_layout_of_reciver_position = create_layout_of_parameter(self.label_of_reciver_position, self.label_of_reciver_position_x,
                                                                   self.reciver_position_x, self.label_of_reciver_position_y, self.reciver_position_y)
        v_layout_of_reciver_parameter.addLayout(h_layout_of_reciver_position)

        self.reciver_name = QLineEdit()
        self.label_of_reciver_name = create_label("Name")
        h_layout_of_reciver_name = create_layout_of_parameter(self.label_of_reciver_name, self.reciver_name)
        v_layout_of_reciver_parameter.addLayout(h_layout_of_reciver_name)

        self.save_button_of_reciver = QPushButton("Save")
        self.remove_button_of_reciver = QPushButton("Remove")
        h_layout_of_save_remove_of_reciver = create_layout_of_parameter(self.save_button_of_reciver, self.remove_button_of_reciver)
        v_layout_of_reciver_parameter.addLayout(h_layout_of_save_remove_of_reciver)
        
        
        
        v_layout_input =QVBoxLayout()
        
        v_layout_input.addLayout(v_layout_of_paramet)
        
        self.sperator_of_input = creat_separator("h")
        v_layout_input.addWidget(self.sperator_of_input)
        
        v_layout_input.addLayout(v_layout_of_reciver_parameter)

        # v_layout_input.addStretch()

        h_main_layout.addLayout(v_layout_input)
        #####################################################################
        
        self.sperator_between_input_and_output = creat_separator("v")
        h_main_layout.addWidget(self.sperator_between_input_and_output)
        self.grid_layout_of_change_info  = QGridLayout()


        self.slider_for_change_1 = slider_creator(Maximum=10)
        self.label_of_slider_for_change_transimter_number = QLabel("text label")
        self.label_of_slider_for_change_transimter_number_value = QLabel(str(self.slider_for_change_1.value()))
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_transimter_number, 0, 0)
        self.grid_layout_of_change_info.addWidget(self.slider_for_change_1, 0, 1)
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_transimter_number_value, 0, 2)
        

        self.slider_for_change_2 = slider_creator()
        self.label_of_slider_for_change_2 = QLabel("text label")
        self.label_of_slider_for_change_2_value = QLabel(str(self.slider_for_change_2.value()))
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_2, 1, 0)
        self.grid_layout_of_change_info.addWidget(self.slider_for_change_2, 1, 1)
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_2_value, 1, 2)

        self.slider_for_change_3 = slider_creator()
        self.label_of_slider_for_change_3 = QLabel("text label")
        self.label_of_slider_for_change_3_value = QLabel(str(self.slider_for_change_3.value()))
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_3, 2, 0)
        self.grid_layout_of_change_info.addWidget(self.slider_for_change_3, 2, 1)
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_3_value, 2, 2)

        self.slider_for_change_4 = slider_creator()
        self.label_of_slider_for_change_4 = QLabel("text label")
        self.label_of_slider_for_change_4_value = QLabel(str(self.slider_for_change_4.value()))
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_4, 3, 0)
        self.grid_layout_of_change_info.addWidget(self.slider_for_change_4, 3, 1)
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_4_value, 3, 2)

        self.slider_for_change_5 = slider_creator()
        self.label_of_slider_for_change_5 = QLabel("text label")
        self.label_of_slider_for_change_5_value = QLabel(str(self.slider_for_change_5.value()))
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_5, 4, 0)
        self.grid_layout_of_change_info.addWidget(self.slider_for_change_5, 4, 1)
        self.grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_5_value, 4, 2)

        h_main_layout.addLayout(self.grid_layout_of_change_info)
        #####################################################################
        
        grid_layout_of_output = QGridLayout()

        self.transmiters_recivers_plotter = beam_Plot()
        grid_layout_of_output.addWidget(self.transmiters_recivers_plotter, 1, 1)
        
        self.beam_profile = beam_Plot(linear= False)
        grid_layout_of_output.addWidget(self.beam_profile, 0, 1)
        
        self.heat_map = beam_Plot()
        grid_layout_of_output.addWidget(self.heat_map, 0, 0)

        #######################################################################
        grid_of_array_info = QGridLayout()
        
        self.label_title = QLabel("Array information")
        grid_of_array_info.addWidget(self.label_title, 0, 0)


        self.label_info_array = QLabel("Array Name : ")
        self.label_info_array_value = QComboBox()
        grid_of_array_info.addWidget(self.label_info_array, 1, 0)
        grid_of_array_info.addWidget(self.label_info_array_value, 1, 1)

        self.label_type = QLabel("Type  : ")
        self.label_of_which_type = QLabel("………")
        grid_of_array_info.addWidget(self.label_type, 2, 0)
        grid_of_array_info.addWidget(self.label_of_which_type, 2, 1)

        self.label_info_number_of_transmiter = QLabel("Transmiter Number : ")
        self.label_info_number_of_transmiter_value = QLabel("………")
        grid_of_array_info.addWidget(self.label_info_number_of_transmiter, 3, 0)
        grid_of_array_info.addWidget(self.label_info_number_of_transmiter_value, 3, 1)

        self.label_info_frequencies = QLabel("Frequencies") 
        self.label_info_frequencies_value = QLabel("………")
        grid_of_array_info.addWidget(self.label_info_frequencies, 4, 0)
        grid_of_array_info.addWidget(self.label_info_frequencies_value, 4, 1)

        self.label_info_raduis = QLabel("Raduis")
        self.label_info_raduis_value = QLabel("………")
        grid_of_array_info.addWidget(self.label_info_raduis, 5, 0)
        grid_of_array_info.addWidget(self.label_info_raduis_value, 5, 1)
        

        self.label_info_arc_angle = QLabel("Arc Angle : ")
        self.label_info_arc_angle_value = QLabel("………")
        grid_of_array_info.addWidget(self.label_info_arc_angle, 6, 0)
        grid_of_array_info.addWidget(self.label_info_arc_angle_value, 6, 1)

        grid_layout_of_output.addLayout(grid_of_array_info, 1, 0)

        self.heat_map.axes.set_title("Wave Field Visualization")
        self.heat_map.axes.set_xlabel("X Position (wavelengths)")
        self.heat_map.axes.set_ylabel("Y Position (wavelengths)")
        self.heat_map.axes.axis('equal')

        # Configure polar plot
        self.beam_profile.axes.set_title("Polar Beam Pattern", va='bottom')
        self.beam_profile.axes.set_ylim([-40, 0])  # Decibel range
        self.transmiters_recivers_plotter.axes.set_title("Array Elements and Receivers")
        self.transmiters_recivers_plotter.axes.set_xlabel("X Position (wavelengths)")
        self.transmiters_recivers_plotter.axes.set_ylabel("Y Position (wavelengths)")
        self.transmiters_recivers_plotter.axes.grid(True)
        self.transmiters_recivers_plotter.axes.axis('equal')

        h_main_layout.addLayout(grid_layout_of_output)

        #######################################################################

        container = QWidget()
        container.setLayout(h_main_layout)
        MainWindow.setCentralWidget(container)
    
    def save_array(self):
        pass

    def save_reciver(self):
        pass

    def change_type(self):
        if self.radio_button_of_linear.isChecked():
            hide_layout(self.h_layout_of_Radius)
            hide_layout(self.h_layout_of_arc_angle)
            show_layout(self.h_layout_element_spacing)
        else:
            hide_layout(self.h_layout_element_spacing)
            show_layout(self.h_layout_of_Radius)
            show_layout(self.h_layout_of_arc_angle)

    def remove_combobox_item(self, combo_box, text_to_remove):
        text_to_remove = text_to_remove
        index = combo_box.findText(text_to_remove)  # Find the index of the text
        if index != -1:  # Check if the text exists
            combo_box.removeItem(index)  # Remove the item


    def slider_creator(self, Mainwindow, number_of_slider):  ### not used yet###
        self.number_of_sliders = number_of_slider 
        band_layout = QGridLayout()
        self.gain = [1] * self.number_of_sliders
        self.phase_shifts_sliders_values.clear()
        for i in range(self.number_of_sliders):
            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(-90)
            slider.setMaximum(90)
            slider.setValue(int(np.degrees(Mainwindow.current_array.phase_shifts[i][0])))
            slider.setFixedWidth(100)
            self.phase_shifts_sliders_values.append(slider.value())
            slider.valueChanged.connect(lambda value, idx=i: Mainwindow.update_phase_shifts(value, idx))
            
            label = QLabel(str(f"Transmitter {i + 1}"))
            label.setObjectName(f"Transmitter_{i+1}_label")
            label.setFixedHeight(30)
            
            band_layout.addWidget(label, i, 0, 1, 1)
            band_layout.addWidget(slider, i, 1, 1, 1)
        
        return band_layout
    
    def clear_layout(self, layout):
        # Iterate and remove widgets
        while layout.count():
            item = layout.takeAt(0)  # Take the first item
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget
            else:
                # If it's a layout, clear it recursively
                sub_layout = item.layout()
                if sub_layout is not None:
                    self.clear_layout_recursive(sub_layout)

    def clear_layout_recursive(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                if sub_layout is not None:
                    self.clear_layout_recursive(sub_layout)

def create_line_edit(Maximum=None, Minimum=0, place_holder = None):
    line_edit = QLineEdit()
    if Maximum is not None:
        line_edit.setValidator(QIntValidator(Minimum , Maximum+1))
    if place_holder is not None:
        line_edit.setPlaceholderText(place_holder)
    return line_edit

def create_label(text:str):
    label = QLabel(text)
    label.setFixedHeight(60)
    return label

def creat_separator(type:str):
    separator = QFrame()
    if type == "h":
        separator.setFrameShape(QFrame.HLine)
    elif type == "v":
        separator.setFrameShape(QFrame.VLine)
    else : 
        return
    separator.setFrameShadow(QFrame.Sunken)
    separator.setStyleSheet("padding: 0px;")
    return separator

def slider_creator(type="h", Maximum=100, Minimum=0):
    if type == "v":
        slider = QSlider(Qt.Vertical)
        # slider.setFixedHeight(100)
    else:
        slider = QSlider(Qt.Horizontal)
        # slider.setFixedWidth(100)
    
    slider.setMinimum(Minimum)
    slider.setMaximum(Maximum)
    slider.setValue((Maximum+Minimum)//2)
    return slider

def create_layout_of_parameter(widget_1, widget_2, widget_3 = None, widget_4 = None, widget_5 = None):

    h_layout_of_parameter = QHBoxLayout()
    h_layout_of_parameter.addWidget(widget_1)
    h_layout_of_parameter.addWidget(widget_2)
    
    if widget_3 is not None:
        h_layout_of_parameter.addWidget(widget_3)
    
    if widget_4 is not None:
        h_layout_of_parameter.addWidget(widget_4)

    if widget_5 is not None:
        h_layout_of_parameter.addWidget(widget_5)
    
    return h_layout_of_parameter


def show_layout(layout):
    if layout is None:
        return
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget is not None:
            widget.show()  # Show each widget

def hide_layout(layout):
    if layout is None:
        return
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget is not None:
            widget.hide()
