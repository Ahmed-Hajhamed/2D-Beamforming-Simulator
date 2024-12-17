from PhasedArray import Array
from Receiver import Receiver
arrays = {}
receivers = {}

def tumor_ablation(meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y):
    buttom_array = Array("Buttom Array", "Linear", 8, 1, 0, [0, 0], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    top_array = Array("Top Array", "Linear", 8, 1, 180, [0, 8], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    left_array = Array("Left Array", "Linear", 8, 1, 90, [-8, 4], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    right_array = Array("Right Array", "Linear", 8, 1, -90, [8, 4], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    tumor_receiver = Receiver("Tumor", [0, 4])
    arrays["Buttom Array"] = buttom_array
    arrays["Top Array"] = top_array
    arrays["Left Array"] = left_array
    arrays["Right Array"] = right_array
    receivers["Tumor"] = tumor_receiver
    return arrays, receivers

def ultrasound(meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y):
    transducer_array = Array("Transducer", "Curved", 64, 1, 0, [0, 0], meshgrid_x, meshgrid_y, beam_profile_x, 
                             beam_profile_y, element_spacing=None, radius=1, arc_angle=120)
    arrays["Transducer"] = transducer_array
    for i in range(8):
        receivers[f"Receiver_{i}"] = Receiver(f"Receiver_{i}",  [(-20 + 5 * i), 8])
    return arrays, receivers

def five_G(meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y):
    sender_array = Array("Sender Array", "Linear", 16, 1, 0, [0, 0], 
                         meshgrid_x, meshgrid_y, beam_profile_x, beam_profile_y, 0.5, radius= None, arc_angle= None)
    receivers["Receiver_1"] = Receiver("Receiver_1", [-8, 8])
    receivers["Receiver_2"] = Receiver("Receiver_2", [8, 8])
    arrays["Sender Array"] = sender_array
    return arrays, receivers
