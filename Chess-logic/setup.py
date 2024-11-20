# for chess_robot_player.py
CAMERA = "left"
SQUARE_SIZE = 0.050
Z_ABOVE_BOARD = 0.25  # 0.25
Z_TO_PIECE = 0.095  # 0.15
Z_DROP = 0.004
X_OFFSET = -0.03
Y_OFFSET = 0.01
ROBOT = "panda" 
# fast
ACC = 0.8
VEL = 0.7

# for camera_config.py 
MARKER_SIZE = 0.025
MARKER_TYPE = "DICT_4X4_50"
CAM_IP = "192.168.0.106"

# for chess_commander.py
MODEL_PATH = "/home/charles/panda/catkin_ws/src/move_chess_panda/scripts/chessrec/runs/aftermove"

MODE = "stockfish15" # stockfish15 | maia | stockfish16

ELO = 2200
DEPTH = 20

# Poses for chess robot execution
LOW_CAM_JOINTS = [
    -0.0002861509839998449,
    -1.5649661966610398,
    0.001571490184083701,
    -2.441184105685472,
    0.009147199263040286,
    1.397496153041122,
    0.785220506046326,
    0.017489660531282425,
    0.017489660531282425,
]

HIGH_CAM_JOINTS = [
    0.00015898450553431174,
    -0.2909451232551228,
    0.00025142004909806066,
    -1.5919965450139177,
    0.0003605799753592121,
    1.3144894863848386,
    0.785866691948467,
    0.01748703420162201,
    0.01748703420162201,
]

LEFT_CAM_JOINTS = [
    -0.06616944939147938,
    -1.5526289022237463,
    0.5461460406923571,
    -2.424159722067252,
    0.2610135964060131,
    1.4384150299219005,
    1.0994914650048637,
    0.0407392717897892,
    0.0407392717897892,
]

RIGHT_CAM_JOINTS = [
    0.030806058988522757,
    -1.4778349875477093,
    -0.6622232789328013,
    -2.420708685489011,
    -0.30581781720616746,
    1.4800959099526354,
    0.2875588180604471,
    0.040736645460128784,
    0.040736645460128784,
]

LOOK_AT_HUMAN = [
    -0.013366096853392505,
    -1.5770862280739022,
    0.015311006135396885,
    -2.4558152854993334,
    0.009796439154703237,
    1.7455670635771343,
    0.86815584582908,
    0.04074616730213165,
    0.04074616730213165,
]

LOOK_AWAY = [
    -0.013417151374830709,
    -1.5770978355178171,
    0.015234067152183702,
    -2.455841507907426,
    -0.4892774688835677,
    1.397887450594359,
    0.8681612076450472,
    0.04074616730213165,
    0.04074616730213165,
]

LOOK_AWAY_R = [
    -0.013417151374830709,
    -1.5770978355178171,
    0.015234067152183702,
    -2.455841507907426,
    0.4892774688835677,
    1.397887450594359,
    0.8681612076450472,
    0.04074616730213165,
    0.04074616730213165,
]

ROTATE_LEFT = [
    0.00426556653928077,
    -1.5657198262465628,
    0.0070904803803484686,
    -2.4536077158153278,
    0.00771298555822836,
    1.4017696044445036,
    0.3001453456124784,
]


ROTATE_RIGHT = [
    0.00426556653928077,
    -1.5657198262465628,
    0.0070904803803484686,
    -2.4536077158153278,
    0.00771298555822836,
    1.4017696044445036,
    0.9822690132626678,
]
