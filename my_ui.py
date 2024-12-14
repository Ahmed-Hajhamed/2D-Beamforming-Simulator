from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit, 
    QPushButton, QComboBox, QSlider, QFileDialog, QProgressBar, QGraphicsView, QGraphicsScene, QCheckBox, QTabWidget
)
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
from qt_material import apply_stylesheet

class beam_Plot(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # self.no_label = True 
        # self.vmin, self.vmax= 0, 0
        super().__init__(fig)


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
    slider.setValue(Maximum//2)
    return slider

def create_layout_of_parameter(label, widget):
    # h_layout_of_parameter = f"h_layout_of_{label.Text()}"
    # globals()[h_layout_of_parameter] = QVBoxLayout()

    h_layout_of_parameter = QHBoxLayout()
    h_layout_of_parameter.addWidget(label)
    h_layout_of_parameter.addWidget(widget)

    return h_layout_of_parameter



class ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beamforming")
        self.setGeometry(100, 100, 1200, 800) 

        self.slider_values = [] 

        
        h_main_layout = QHBoxLayout()
        ############################################################
        v_layout_of_paramet = QVBoxLayout()
        
        self.combo_box_of_type = QComboBox()
        self.combo_box_of_type.addItem("Linear")
        self.combo_box_of_type.addItem("Curve")
        self.label_select = QLabel("Aelect Array")
        h_layout_of_select = create_layout_of_parameter(self.label_select, self.combo_box_of_type)
        v_layout_of_paramet.addLayout(h_layout_of_select)


        self.slider_of_transmiters_number = slider_creator()
        self.label_of_transmiters_number  = QLabel("transmiter")
        h_layout_transmiters_number = create_layout_of_parameter(self.label_of_transmiters_number, self.slider_of_transmiters_number)
        v_layout_of_paramet.addLayout(h_layout_transmiters_number)


        self.frequencies_line_edit = QLineEdit()
        self.label_frequencies = QLabel("Frequecies")
        h_layout_of_frequencis = create_layout_of_parameter(self.label_frequencies, self.frequencies_line_edit)
        v_layout_of_paramet.addLayout(h_layout_of_frequencis)

        self.position_line_edit = QLineEdit()
        self.label_position = QLabel("Positoin")
        h_layout_of_position = create_layout_of_parameter(self.label_position, self.position_line_edit)
        v_layout_of_paramet.addLayout(h_layout_of_position)

        self.slider_of_steering_angle = slider_creator(Maximum=90, Minimum=-90)
        self.label_steering_angle = QLabel("Steering Angle")
        h_layout_of_steering_angle = create_layout_of_parameter(self.label_steering_angle, self.slider_of_steering_angle)
        v_layout_of_paramet.addLayout(h_layout_of_steering_angle)

        self.radius_line_edit = QLineEdit()
        self.radius_line_edit.setValidator(QIntValidator(0, 100))
        self.label_of_radius = QLabel("Radius")
        h_layout_of_Radius = create_layout_of_parameter(self.label_of_radius, self.radius_line_edit)
        v_layout_of_paramet.addLayout(h_layout_of_Radius)

        self.slider_of_arc_angle = slider_creator(Maximum=90, Minimum=-90)
        self.label_arc_angle= QLabel("Arc Angle")
        h_layout_of_arc_angle = create_layout_of_parameter(self.label_arc_angle, self.slider_of_arc_angle)
        v_layout_of_paramet.addLayout(h_layout_of_arc_angle)
        
        self.array_name_line_edit = QLineEdit()
        self.label_of_array_name = QLabel("Array Name")
        h_layout_of_array_name = create_layout_of_parameter(self.label_of_array_name, self.array_name_line_edit)
        v_layout_of_paramet.addLayout(h_layout_of_array_name)

        self.save_button = QPushButton("Save")
        self.remove_button = QPushButton("Remove")
        h_layout_of_save_remove = create_layout_of_parameter(self.save_button, self.remove_button)
        v_layout_of_paramet.addLayout(h_layout_of_save_remove)
        
        ##################################################
        v_layout_of_reciver_parameter = QVBoxLayout()

        self.reciver_number = QLineEdit()
        self.label_of_reciver_number = QLabel("Reciver")
        h_layout_of_reciver_number = create_layout_of_parameter(self.label_of_reciver_number, self.reciver_number)
        v_layout_of_reciver_parameter.addLayout(h_layout_of_reciver_number)

        self.reciver_position = QLineEdit()
        self.label_of_reciver_position = QLabel("Position")
        h_layout_of_reciver_position = create_layout_of_parameter(self.label_of_reciver_position, self.reciver_position)
        v_layout_of_reciver_parameter.addLayout(h_layout_of_reciver_position)

        self.reciver_name = QLineEdit()
        self.label_of_reciver_name = QLabel("Name")
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


        h_main_layout.addLayout(v_layout_input)
        #####################################################################
        
        self.sperator_between_input_and_output = creat_separator("v")
        h_main_layout.addWidget(self.sperator_between_input_and_output)
        grid_layout_of_change_info  = QGridLayout()

        self.slider_for_change_transimter_number = slider_creator(Maximum=10)
        self.label_of_slider_for_change_transimter_number = QLabel("transmiter ")
        grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_transimter_number, 0, 0)
        grid_layout_of_change_info.addWidget(self.slider_for_change_transimter_number, 0, 1)
        

        self.slider_for_change_2 = slider_creator()
        self.label_of_slider_for_change_2 = QLabel("text label")
        grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_2, 1, 0)
        grid_layout_of_change_info.addWidget(self.slider_for_change_2, 1, 1)

        self.slider_for_change_3 = slider_creator()
        self.label_of_slider_for_change_3 = QLabel("text label")
        grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_3, 2, 0)
        grid_layout_of_change_info.addWidget(self.slider_for_change_3, 2, 1)

        self.slider_for_change_4 = slider_creator()
        self.label_of_slider_for_change_4 = QLabel("text label")
        grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_4, 3, 0)
        grid_layout_of_change_info.addWidget(self.slider_for_change_4, 3, 1)

        self.slider_for_change_5 = slider_creator()
        self.label_of_slider_for_change_5 = QLabel("text label")
        grid_layout_of_change_info.addWidget(self.label_of_slider_for_change_5, 4, 0)
        grid_layout_of_change_info.addWidget(self.slider_for_change_5, 4, 1)

        h_main_layout.addLayout(grid_layout_of_change_info)
        #####################################################################
        
        grid_layout_of_output = QGridLayout()

        self.heat_map = beam_Plot()
        grid_layout_of_output.addWidget(self.heat_map, 0, 0)

        self.transmiters_recivers_plotter = beam_Plot()
        grid_layout_of_output.addWidget(self.transmiters_recivers_plotter, 1, 1)
        
        self.beam_profile = beam_Plot()
        grid_layout_of_output.addWidget(self.beam_profile, 0, 1)
        

        #######################################################################
        grid_of_array_info = QGridLayout()
        
        self.label_title = QLabel("Array information")
        grid_of_array_info.addWidget(self.label_title, 0, 0)

        self.label_info_array = QLabel("Array Name : ")
        self.label_info_array_value = QLabel("………")
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


        h_main_layout.addLayout(grid_layout_of_output)

        #######################################################################

        container = QWidget()
        container.setLayout(h_main_layout)
        self.setCentralWidget(container)


    def slider_creator(self, number_of_slider):  ### not used yet###
        self.number_of_sliders = 10 
        band_layout = QGridLayout()
        self.gain = [1] * self.number_of_sliders
        self.slider_values.clear()
        for i in range(self.number_of_sliders):
            slider = QSlider(Qt.Vertical)
            slider.setMinimum(-90)
            slider.setMaximum(90)
            slider.setValue(0)
            slider.setFixedWidth(100)
            self.slider_values.append(slider.value())
            slider.valueChanged.connect(lambda value, idx=i: self.apply_gain(value, idx))
            
            label = QLabel(str(self.names[i]))
            label.setObjectName("slider_1_label")
            label.setFixedHeight(30)
            
            band_layout.addWidget(label, i, 0, 1, 1)
            band_layout.addWidget(slider, i, 1, 1, 1)
        
        return band_layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, "dark_purple.xml")
    window = ui()
    window.show()
    sys.exit(app.exec_())
        
