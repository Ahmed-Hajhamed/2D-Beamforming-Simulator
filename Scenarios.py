from PhasedArray import Array
from Receiver import Receiver
arrays_scenarios = {}
receivers_scenarios = {}
steering_angle_increment_of_ultrasound = 5

def tumor_ablation(meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y):
    arrays_scenarios.clear()
    receivers_scenarios.clear()
    buttom_array = Array("Buttom Array", "Linear", 8, [1], 0, [0, 10], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    top_array = Array("Top Array", "Linear", 8, [1], 180, [0, 18], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    left_array = Array("Left Array", "Linear", 8, [1], 90, [-8, 14], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    right_array = Array("Right Array", "Linear", 8, [1], -90, [8, 14], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    tumor_receiver = Receiver("Tumor", [0, 4])
    arrays_scenarios["Buttom Array"] = buttom_array
    arrays_scenarios["Top Array"] = top_array
    arrays_scenarios["Left Array"] = left_array
    arrays_scenarios["Right Array"] = right_array
    receivers_scenarios["Tumor"] = tumor_receiver

def ultrasound(meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y):
    arrays_scenarios.clear()
    receivers_scenarios.clear()
    transducer_array = Array("Transducer", "Curved", 64, [1], 0, [0, 0], meshgrid_x, meshgrid_y, beam_profile_x, 
                             beam_profile_y, element_spacing=None, radius=1, arc_angle=120)
    arrays_scenarios["Transducer"] = transducer_array
    for i in range(8):
        receivers_scenarios[f"Receiver_{i}"] = Receiver(f"Receiver_{i}",  [(-20 + 5 * i), 8])

def five_G(meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y):
    arrays_scenarios.clear()
    receivers_scenarios.clear()
    sender_array = Array("Sender Array", "Linear", 16, [1], 0, [0, 0], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    receivers_scenarios["Receiver_1"] = Receiver("Receiver_1", [-8, 8])
    receivers_scenarios["Receiver_2"] = Receiver("Receiver_2", [8, 8])
    arrays_scenarios["Sender Array"] = sender_array
