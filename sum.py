import os
import serial
import time

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import *                    # Uses Dynamixel SDK library

# Control table address
ADDR_X_TORQUE_ENABLE      = 64               # Control table address is different in Dynamixel model
ADDR_X_GOAL_POSITION      = 116
ADDR_X_PRESENT_POSITION   = 132

# Protocol version
PROTOCOL_VERSION            = 2.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL1_ID                      = 1                 # Dynamixel ID : 1
DXL2_ID                      = 2                 # Dynamixel ID : 2
DXL3_ID                      = 3                 # Dynamixel ID : 3
DXL4_ID                      = 4                 # Dynamixel ID : 4
BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
DEVICENAME                  = 'COM8'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
#DXL_MINIMUM_POSITION_VALUE  = 0           # Dynamixel will rotate between this value
#DXL_MAXIMUM_POSITION_VALUE  = 4000            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 5                # Dynamixel moving status threshold

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel ID1 Torque
dxl1_comm_result, dxl1_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_X_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl1_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl1_comm_result))
elif dxl1_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl1_error))
else:
    print("Dynamixel ID1 has been successfully connected")
 
# Enable Dynamixel ID2 Torque
dxl2_comm_result, dxl2_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_X_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl2_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl2_comm_result))
elif dxl2_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl2_error))
else:
    print("Dynamixel ID2 has been successfully connected") 
 
# Enable Dynamixel ID3 Torque
dxl3_comm_result, dxl3_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_X_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl3_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl3_comm_result))
elif dxl3_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl3_error))
else:
    print("Dynamixel ID3 has been successfully connected")  

while 1:
    print("Press any key to continue! (or press ESC to quit!)")
    if getch() == chr(0x1b):
        break
    
    # Input Goal position
    pos_x = input("Enter x coordinate: ")
    pos_y = input("Enter y coordinate: ")
    trans_needle = input("Enter Needle Moving Distance: ") 
    
    dxl1_goal_position = int(pos_x)
    dxl2_goal_position = int(pos_y)	
    dxl3_goal_position = int(trans_needle)
    
    # Write ID1 goal position
    dxl1_comm_result, dxl1_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_X_GOAL_POSITION, dxl1_goal_position)
    if dxl1_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl1_comm_result))
    elif dxl1_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl1_error))

    while 1:
        # Read ID1 present position
        dxl1_present_position, dxl1_comm_result, dxl1_error = packetHandler.read4ByteTxRx(portHandler, DXL1_ID, ADDR_X_PRESENT_POSITION)
        if dxl1_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl1_comm_result))
        elif dxl1_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl1_error))

        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL1_ID, dxl1_goal_position, dxl1_present_position))

        if not abs(abs(dxl1_goal_position) - abs(dxl1_present_position)) > DXL_MOVING_STATUS_THRESHOLD:
            break
    
    # Write ID2 goal position
    dxl2_comm_result, dxl2_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_X_GOAL_POSITION, dxl2_goal_position)
    if dxl2_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl2_comm_result))
    elif dxl2_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl2_error))

    while 1:
        # Read ID2 present position
        dxl2_present_position, dxl2_comm_result, dxl2_error = packetHandler.read4ByteTxRx(portHandler, DXL2_ID, ADDR_X_PRESENT_POSITION)
        if dxl2_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl2_comm_result))
        elif dxl2_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl2_error))

        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL2_ID, dxl2_goal_position, dxl2_present_position))

        if not abs(abs(dxl2_goal_position) - abs(dxl2_present_position)) > DXL_MOVING_STATUS_THRESHOLD:
            break
   
    # Write ID3 goal position
    dxl3_comm_result, dxl3_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_X_GOAL_POSITION, dxl3_goal_position)
    if dxl3_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl3_comm_result))
    elif dxl3_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl3_error))

    while 1:
        # Read ID3 present position
        dxl3_present_position, dxl3_comm_result, dxl3_error = packetHandler.read4ByteTxRx(portHandler, DXL3_ID, ADDR_X_PRESENT_POSITION)
        if dxl3_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl3_comm_result))
        elif dxl3_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl3_error))

        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL3_ID, dxl3_goal_position, dxl3_present_position))

        if not abs(abs(dxl3_goal_position) - abs(dxl3_present_position)) > DXL_MOVING_STATUS_THRESHOLD:
            break

# Disable Dynamixel ID1 Torque
dxl1_comm_result, dxl1_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_X_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl1_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl1_comm_result))
elif dxl1_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl1_error))
   
# Disable Dynamixel ID2 Torque
dxl2_comm_result, dxl2_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_X_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl2_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl2_comm_result))
elif dxl2_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl2_error))
  
# Disable Dynamixel ID3 Torque
dxl3_comm_result, dxl3_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_X_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl3_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl3_comm_result))
elif dxl3_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl3_error))

# Close port
portHandler.closePort()


# DC motor control
ser = serial.Serial('COM9',9600,timeout=1)

time.sleep(1.5) # can't be <= 1

ser.write('1'.encode())
time.sleep(0.5)

ser.write('0'.encode())
ser.close()

  