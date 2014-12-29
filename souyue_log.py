from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
import os
import commands
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
    Log.d("DXANALYSE","com.zhongsou.souyue")
    
#dr.alert("list")
