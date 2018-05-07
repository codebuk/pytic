#no longer maintained

from tic import *
import time

if __name__ == '__main__':
    ticdev = TicDevice()
    ticdev.open(vendor=0x1ffb, product=0x00b3)
    #tic.open(vendor=0x1ffb, product=0x00bd)
    #, serial="00218293")

    # quick test
    #tic.get_variables()
    #log.debug (v)
    #v= tic.get_firmware_mod_array()
    #log.debug ("v:" + str(v))
    ticdev.reset()
    ticdev.set_max_speed(20000000)
    ticdev.set_max_accel(200000)
    ticdev.set_max_decel(800000)
    ticdev.exit_safe_start()
    #ticdev.set_decay_mode(constants.TIC_DECAY_MODE_T825_MIXED)
    ticdev.set_current_limit(800)
    ticdev.set_starting_speed(10)
    ticdev.halt_and_set_position(0)
    ticdev.energize()
    ticdev.set_target_position(-11650)
    ticdev.wait_for_move_complete()
    ticdev.set_current_limit(800)
    ticdev.halt_and_set_position(0)
    ticdev.set_target_position(100)
    ticdev.wait_for_move_complete()
    ticdev.halt_and_set_position(0)
    time.sleep(1)
    v = ticdev.get_variables()
    log.debug (v)

'''
    while True:
        ticdev.set_target_position(1501)
        ticdev.wait_for_move_complete()
        ticdev.set_target_position(0)
        ticdev.wait_for_move_complete()

    ticdev.set_decay_mode(11)
    ticdev.set_target_velocity(10000)
    ticdev.set_target_position(-400)
    time.sleep(.3)
    ticdev.halt_and_hold()
    ticdev.set_current_limit(4000)
    time.sleep(.3)
    ticdev.set_target_position(-400)
    time.sleep(3)
    ticdev.set_current_limit(2000)
    ticdev.exit_safe_start()
    ticdev.enter_safe_start()
    ticdev.clear_driver_error()
    ticdev.set_max_speed(100000)
    ticdev.set_starting_speed(100)
    ticdev.set_max_accel(100)
    ticdev.set_max_decel(100)
    ticdev.set_step_mode(1200)
    ticdev.deenergize()
    ticdev.reset_command_timeout()
    ticdev.energize()
    ticdev.set_current_limit(100)
    #ticdev.reinitialize()
    # no need for this - use ticgui
    # ticdev.start_bootloader()

    # ticdev.set_target_position(-400)
    # ticdev.reset()
    # ticdev.halt_and_set_position(4000)

    # ticdev.deenergize()
    # ticdev.set_target_position(-400)
    '''
