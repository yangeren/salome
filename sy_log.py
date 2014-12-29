#! /usr/bin/env monkeyrunner
import time
import subprocess

# Imports the monkeyrunner modules
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connects to the current device, returning a MonkeyDevice object
dr = MonkeyRunner.waitForConnection()

dr.startActivity(component="com.zhongsou.souyue/com.zhongsou.souyue.activity.SplashActivity")
MonkeyRunner.sleep(5)
while True:
    MonkeyRunner.sleep(5)
    dr.touch(675,1845,"DOWN_AND_UP")
    MonkeyRunner.sleep(10)
    dr.touch(426,834,"DOWN_AND_UP")
    MonkeyRunner.sleep(10)
    dr.touch(84,162,"DOWN_AND_UP")
    MonkeyRunner.sleep(5)
#    Log.d("DXANALYSE","com.zhongsou.souyue")

    p = subprocess.Popen([ "adb", "logcat", "TEST:V", "*:S" ], shell=False,
            stdout=subprocess.PIPE)
    i = 0
    while True:
        dr.shell("log -t TEST This is line %d" % i)
        i += 1
        print p.stdout.readline()
        time.sleep(1)
