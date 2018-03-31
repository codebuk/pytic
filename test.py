from tic import *
import time

if __name__ == '__main__':
    tic = TicDevice()
    # tic.open(vendor=0x1ffb, product=0x00b3)
    tic.open(vendor=0x1ffb, product=0x00bd, serial="00218293")

    # quick test
    tic.reset()
    tic.set_decay_mode(1212)
    tic.set_target_velocity(10000)
    tic.set_target_position(-400)
    time.sleep(.3)
    tic.halt_and_hold()
    tic.set_current_limit(1000)
    time.sleep(.3)
    tic.set_target_position(-400)
    time.sleep(3)
    tic.set_current_limit(2000)
    tic.exit_safe_start()
    tic.enter_safe_start()
    tic.clear_driver_error()
    tic.set_max_speed(100000)
    tic.set_starting_speed(100)
    tic.set_max_accel(100)
    tic.set_max_decel(100)
    tic.set_step_mode(1200)
    tic.deenergize()
    tic.reset_command_timeout()
    tic.energize()
    tic.reinitialize()
    # no need for this - use ticgui
    # tic.start_bootloader()

    # tic.set_target_position(-400)
    # tic.reset()
    # tic.halt_and_set_position(4000)

    # tic.deenergize()
    # tic.set_target_position(-400)
