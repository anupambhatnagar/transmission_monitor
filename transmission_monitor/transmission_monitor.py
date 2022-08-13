#!/usr/bin/env python3

import logging
import os
import signal
import shlex
from subprocess import Popen, PIPE, STDOUT
import tkinter as tk

def display(pgid, tail_process, app_name):
    def update():

        # generator to read the data one line at a time
        def helper():
            for line in tail_process.stdout:
                line = line.decode('utf-8').strip()
                if app_name in line:
                    yield line

        result = helper()

        data = next(result)
        data = data.split(",")
        received, sent = round(int(data[2])/128,2), round(int(data[3])/128, 2)
        label2['text'] = "Received = {} Kbps \n Sent = {} Kbps".format(received, sent)
        transmission_info_window.after(1000, update)

    transmission_info_window = tk.Tk()
    transmission_info_window.title("Transmission Info")
    label2 = tk.Label(transmission_info_window)
    label2.pack()

    transmission_info_window_width = 200
    transmission_info_window_height = 50
    screen_width = transmission_info_window.winfo_screenwidth()
    update()
    transmission_info_window.geometry(f'{transmission_info_window_width}x{transmission_info_window_height}+{screen_width-transmission_info_window_width}+{0}')

    transmission_info_window.mainloop()
    os.killpg(pgid, signal.SIGTERM)


def start_nettop(app_name):
    filename = "rxtx_new.log"
    log_file = open(filename, "w")

    # start nettop process
    nettop_cmd = "nettop -x -P -J bytes_in,bytes_out -d -L 0 "
    nettop_process = Popen(shlex.split(nettop_cmd), stdout=log_file, text=True)

    # start tail process
    tail_stdout_cmd = "tail -f %s" % filename
    tail_process = Popen(shlex.split(tail_stdout_cmd), stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    # the nettop process and tail process belong to the same process group. killing the process
    # group terminates both the nettop and tail processes.
    pgid = os.getpgid(nettop_process.pid)
    
    # change the print into a logging.warn
    # print("Process Group ID = %s" % pgid)
    display(pgid, tail_process, app_name)

def main():
    window = tk.Tk()
    window.title('Transmission Monitor')

    label1 = tk.Label(window, text = "Select Application")
    label1.pack()

    workchat_button = tk.Button(window, text='Work Chat', command=lambda: [window.destroy(), start_nettop('Workplace Chat')])
    workchat_button.pack()

    zoom_button = tk.Button(window, text='Zoom', command=lambda: [window.destroy(), start_nettop('zoom.us')])
    zoom_button.pack()
    
    transmission_monitor_window_width = 250
    transmission_monitor_window_height = 100
    screen_width = window.winfo_screenwidth()

    window.geometry(f'{transmission_monitor_window_width}x{transmission_monitor_window_height}+{screen_width-transmission_monitor_window_width}+{0}') 
    window.mainloop()

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
main()
