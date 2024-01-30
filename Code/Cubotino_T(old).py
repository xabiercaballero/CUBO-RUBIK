#!/usr/bin/python
# coding: utf-8

""" 
#############################################################################################################
#  Andrea Favero, 28 January 2024
#
#  This code relates to CUBOTino autonomous, a very small and simple Rubik's cube solver robot 3D printed.
#  CUBOTino autonomous is the 'Top version', of the CUBOTino robot series.
#  Demo at https://youtu.be/dEOLhvVMcUg
#  Instructions:https://www.instructables.com/CUBOTino-Autonomous-Small-3D-Printed-Rubiks-Cube-R/
#
#  This is the core script, that interacts with few other files.
#  Many functions of this code have been developed since 2021, for my previous robots (https://youtu.be/oYRXe4NyJqs).
#
#  The cube status is detected via a camera system (PiCamera) and OpenCV .
#  Kociemba solver is used foer the cube solution (from: https://github.com/hkociemba/RubiksCube-TwophaseSolver)
#  Credits to Mr. Kociemba for his great job !
#  Search for CUBOTino autonomous on www.instructables.com, to find more info about this robot.
#
#  Developped on:
#  - Raspberry Pi Zero2W and Raspberry Pi ZeroW
#  - Raspberry Pi OS 10 (A port of Debian Buster with security updates and desktop environment)
#    (Linux raspberry 5.10.103-v7+ #1529 SMP Tue 8 12:21:37 GMT 2022 armv71 GNU/Linux)
#  - OpenCV cv2 ver: 4.1.0
#  - PiCamera v1.3
#  - Numpy: 1.21.4
#
#  Updated for:
#  - Raspberry Pi OS 11 (A port of Debian Bulleys with security updates and desktop environment)
#
#############################################################################################################
"""


# __version__ variable
version = '6.5 (28 Jan 2024)'


################  setting argparser for robot remote usage, and other settings  #################
import argparse

# argument parser object creation
parser = argparse.ArgumentParser(description='CLI arguments for Cubotino_T.py')

# --version argument is added to the parser
parser.add_argument("-v", "--version", help='Shows the script version.', action='version',
                    version=f'%(prog)s ver:{version}')

# --debug argument is added to the parser
parser.add_argument("-f", "--twosteps", action='store_true',
                    help="From Flip-Up to close_cover in 2 movements instead of 1")

# --debug argument is added to the parser
parser.add_argument("-d", "--debug", action='store_true',
                    help="Activates printout of settings, variables and info for debug purpose")

# --cv_wow argument is added to the parser
parser.add_argument("--cv_wow", action='store_true',
                    help="Activates the cv_wow (image analysis steps) on screen")

# --F_deg argument is added to the parser
parser.add_argument("-F", "--F_deg", action='store_true',
                    help="CPU temperature in Fahrenheit degrees")

# --cycles argument is added to the parser
parser.add_argument("-c", "--cycles", type=int, 
                    help="Input the number of automated scrambling and solving cycles")

# --pause argument is added to the parser
parser.add_argument("-p", "--pause", type=int, 
                    help="Input the pause time, in secs, between automated cycles")

# --shutoff argument is added to the parser
parser.add_argument("-s", "--shutoff", action='store_true',
        disp.set_backlight(1)                             # display backlight is turned on, in case it wasn't
        disp.show_on_display('EXT. SCREEN', 'PRESENCE', fs1=16, fs2=19 )  #feedbak is print to to the display
        time.sleep(2)
        print('Screen related function are activated')    # feedback is printed to the terminal 
        if fixWindPos:                                    # case the graphical windows is forced to the top left monitor corner
            print('CV2 windows forced to top-left screen corner')    # feedback is printed to the terminal     
        
        if flip_to_close_one_step:                        # case the flip_to_close_one_step is set True
            print('From Flip-Up to close_cover in one continuos movement') # feedback is printed to the terminal
        else:                                             # case the flip_to_close_one_step is set False
            print('From Flip-Up to close_cover in two movements') # feedback is printed to the terminal
        
        if silent:                                        # case the silent variable is set True
            print('Servos deactivated after init')        # feedback is printed to the terminal
        else:                                             # case the silent variable is set False
            print('Servos are activated')                 # feedback is printed to the terminal
            
        if cv_wow:                                        # case the cv image analysis plot is set true
            print('CV image analysis is plot on screen')  # feedback is printed to the terminal 
        
        if timer:                                         # case the timer visualization is set true
            print('Timer is visualized after scrambling function')   # feedback is printed to the terminal 
        
        if frameless_cube == 'false':                               # case the frameless string variale equals to false
            print('\nCube status detection set for cube with black frame around the facelets')  # feedback is printed to the terminal 
        elif frameless_cube == 'true':                              # case the frameless string variale equals to 'true'
            print('\nCube status detection set for frameless cube') # feedback is printed to the terminal
        elif frameless_cube == 'auto':                              # case the frameless string variale equals to 'auto'
            print('\nCube status detection set for both cubes with and without black frame')   # feedback is printed to the terminal 
            print('This setting takes slightly longer time for the cube status detection\n')   # feedback is printed to the terminal
        
        if picamera_test:                                 # case picamera_test is set true (servos disabling)
            print(f'\nPiCamera test enabled')             # feedback is printed to the terminal
            test_picamera()                               # test_picamera func is called

        if not btn:                                       # case the btn is set False
            print(f'\nButton is ignored, solving cycles start automatically')   # feedback is printed to the terminal
    # ###############################################################################################
    
    
    
    ###################################    import libraries    ######################################
    print('\nImport libraries:')            # feedback is printed to the terminal    
    import_libraries()                      # imports libraries
    # ###############################################################################################
    
    
    
    #################################    startup  variables     #####################################
    print('\nOther settings and environment status:')  # feedback is printed to the terminal
    cycles_num = 0                          # zero is assigned to the (automated) cycles_num variable
    start_up(first_cycle = True)            # sets the initial variables, in this case it is the first cycle
    solv_cycle = 0                          # variable to count the solving cycles per session is set to zero
    scramb_cycle = 0                        # variable to count the scrambling cycles per session is set to zero
    quit_script = False
    print('\n#############################################################################\n')
    # ###############################################################################################
    
    

    ###########################  parsing arguments for robot remote usage  ##########################
    if args.cycles != None:                 # case the Cubotino_T.py has been launched with 'cycles' argument
        cycles_num = abs(int(args.cycles))  # the positive integer arg passed is assigned to the cycle_num variable
        if cycles_num > 0:                  # case the automated cycles request is more than zero
            print(f'\nAsked the robot to automatically scramble and solve the cube {cycles_num} times')
            automated = True                # automated variable is set true
        else:                               # case the automated cycles request equals zero
            automated = False               # automated variable is set false
    else:                                   # case the Cubotino_T.py has not been launched without 'cycles' argument
        automated = False                   # automated variable is set false
    
    if cycles_num > 0 and args.pause != None:  # case the Cubotino_T.py has been launched also with 'pause' argument
        
        # the positive integer arg passed, rounded to the closest upper multiple of 4, is assigned to the cycle_pause
        cycle_pause = 4*int(math.ceil(abs(int(args.pause))/4))  
        print(f'Asked the robot to pause {cycle_pause} seconds in between the automated cycles\n') 
    else:                                   # case the Cubotino_T.py has not been launched without 'pause' argument
        cycle_pause = 0                     # zero is assigned to the cycles_num variable
    # ###############################################################################################
        
    

    while True:                             # (outer) infinite loop, until the Rpi is shut-off
        robot_stop = False                  # flag used to stop or allow robot movements
        robot_idle = True                   # robot is idling
        timeout = False                     # flag used to limit the cube facelet detection time
        
        while not automated:                # while automated is false: (inner) infinite loop, until 'solve' process is chosen
            if btn:                         # case the variable btn is set True (touch button enables)
                print('\n\n\n\nWaiting for user to start a cycle')  # feedback is printed to the terminal
                cycle = press_to_start()    # request user to press the button to start a scrambling or solving cycle
            elif not btn:                   # case the variable btn is set False (testing without the touch button)
                print('\n\n\n\nCycle is started without using the touch sensor')  # feedback is printed to the terminal
                cycle = 'solve'             # string 'solve' is returned to start a solving cycle
            
            if cycle == 'scramble':         # case the chosen cycle is cube scrambling
                # scramble can be done more times within this inner while loop
                scramb_cycle += 1           # counter, for the number of scrambling cycles perfomed within a session, is incremented
                start_scrambling(scramb_cycle)  # start_scrambling function is called
            
            elif cycle == 'solve':          # case the chosen cycle is cube scrambling
                solv_cycle += 1             # counter, for the number of solving cycles perfomed within a session, is incremented
                start_solving(solv_cycle)   # start_solving function is called
                start_up(first_cycle = False)  # sets the initial variables, to use the camera in manual mode
                break      # (inner) infinite loop is interrupted once cube solving cycle is done or stopped
      
        if automated:                           # case automated variable is true
            for i in range(cycles_num):         # iteration over the number passed to the --cycles argument 
                start_automated_cycle(i+1, cycles_num, cycle_pause)  # start_automated_cycle finction is called
                
                if i+1 < cycles_num:            # case there is at least one more cycle to do
                    # preparing the camera and variables for the next solving cycle
                    robot_stop = False          # flag used to stop or allow robot movements
                    robot_idle = True           # robot is idling
                    timeout = False             # flag used to limit the cube facelet detection time       
                    close_camera()              # this is necessary to get rid of analog/digital gains previously used
                    time.sleep(0.5)             # little delay between the camera closing, and a new camera opening
                    camera, width, height = set_camera()  # camera has to be re-initialized, to removes previous settings
                
                if i+1 == cycles_num:           # case all the cycles have been done
                    # closing the automated cycles section
                    print('\n\n\n\n\n\n')       # prints some empty lines, on IDE terminal
                    clear_terminal()            # cleares the terminal
                    print(f'\nScrambled and solved the cube {cycles_num} times\n')
                    solv_cycle = cycles_num     # cycle_num is assigned to variable counting the solving cycles manually requested
                    scramb_cycle = cycles_num   # cycle_num is assigned to variable counting the scrambling cycles manually requested
                    
                    if args.shutoff:                  # case the --shutoff argument has been provided
                        quit_func(quit_script = True) # the script is terminated and, depending on Cubotino_T_bash.sh, it might shut the RPI off
                    else:                             # case the --shutoff argument has not been provided
                        automated = False             # automated variable is set false, robot waits for solve button commands
                
                start_up(first_cycle = False)  # sets the initial variables, to use the camera in manual mode
