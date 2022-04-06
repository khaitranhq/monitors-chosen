import subprocess
import os

HOME = os.environ["HOME"]
PLANK_CONFIG_PATH = f'{HOME}/.config/dconf/user.conf'

def main():
    monitors = subprocess.run(
        'xrandr | grep " connected "', shell=True, stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    number_monitors = len(monitors.split("\n")) - 1

    subprocess.run(f"dconf dump / >{PLANK_CONFIG_PATH}", shell=True)

    plank_config = ""
    with open(f"{PLANK_CONFIG_PATH}") as fin:
        for line in fin.readlines():
            if line.__contains__("enabled-docks="):
                dock_arr = ["dock".__add__(str(x + 1)) for x in range(number_monitors)]
                dock_arr = '"{0}"'.format('","'.join(dock_arr))
                line = f"enabled-docks=[{dock_arr}]"
            plank_config += line
    print(plank_config)

    fout = open(f'{PLANK_CONFIG_PATH}', 'w')
    fout.write(plank_config)

    subprocess.run(f'dconf load / <{PLANK_CONFIG_PATH}', shell=True)
    subprocess.run('sudo killall plank', shell=True)
    subprocess.run('nohup plank &', shell=True)

    if number_monitors == 2:
        subprocess.run(
            "xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --output DP-3 --mode 1920x1080 --pos 1920x0",
            shell=True,
        )
    if number_monitors == 3:
        subprocess.run(
            "xrandr --output DP-1 --mode 1920x1080 --pos 0x0 --output DP-3 --mode 1920x1080 --pos 1920x0 --output eDP-1 --mode 1920x1080 --pos 3840x0",
            shell=True,
        )

if __name__ == "__main__":
    main()
