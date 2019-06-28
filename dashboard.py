import math
import remi.gui as gui
import seamonsters as sea

class PracticeDashboard(sea.Dashboard):

    def main(self, robot, appCallback):
        self.robot = robot

        root = gui.VBox(gui.Label("Drive"), width = 600, margin = "0px auto")  

        driveBox = gui.HBox()
        root.append(driveBox)

        driveForwardButton = gui.Button("Drive Forward")
        driveForwardButton.set_on_click_listener(self.robot.c_driveForward)
        driveBox.append(driveForwardButton)

        stopButton = gui.Button("Stop")
        stopButton.set_on_click_listener(self.robot.c_stop)
        driveBox.append(stopButton)

        appCallback(self)
        return root