import subprocess

monitor_randr = {
    "normal": "left",
    "right-up": "inverted",
    "left-up": "normal",
    "bottom-up": "right",
}

MONITOR = "DSI-1"


def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b"")


def main():
    command = "monitor-sensor --accel".split()
    for line in run_command(command):
        print(str(line))
        for orientation in monitor_randr:
            if orientation in str(line):
                command = (
                    f"gnome-randr modify {MONITOR} -r {monitor_randr[orientation]}"
                ).split()
                run_command(command)


if __name__ == "__main__":
    main()
