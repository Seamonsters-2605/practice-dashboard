import remi.gui as gui
import seamonsters as sea

class PracticeDashboard(sea.Dashboard):

    def main(self, robot, appCallback):
        self.robot = robot

        root = gui.VBox(width = 600)
        driveForwardButton = gui.Button("Drive Forward")
        driveForwardButton.set_on_click_listener(self.robot.c_driveForward)
        root.append(driveForwardButton)

        appCallback(self)
        return root