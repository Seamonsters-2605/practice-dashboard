import seamonsters as sea
import ctre
import wpilib
import dashboard

class PracticeBot(sea.GeneratorBot):

    def robotInit(self):
        #set up motors
        self.leftFront = ctre.WPI_TalonSRX(2)
        self.rightFront = ctre.WPI_TalonSRX(1)
        self.leftBack = ctre.WPI_TalonSRX(0)
        self.rightBack = ctre.WPI_TalonSRX(3)

        #set up dashboard
        self.app = None
        sea.startDashboard(self, dashboard.PracticeDashboard)

    def teleop(self):
        yield from self.updateDashboardGenerator()

    #does the events called by the dashboard
    def updateDashboardGenerator(self):
        if self.app is not None:
            self.app.clearEvents()
        while True:
            v = None
            if self.app is not None:
                v = self.app.doEvents()
            yield v

    def driveForward(self):
        self.leftFront.set(1)
        self.rightFront.set(-1)
        self.leftBack.set(1)
        self.rightBack.set(-1)
        """
        yield from sea.wait(100)
        self.leftFront.set(0)
        self.rightFront.set(0)
        self.leftBack.set(0)
        self.rightBack.set(0)
        """

    #dashboard callback
    @sea.queuedDashboardEvent
    def c_driveForward(self, button):
        self.driveForward()

if __name__ == "__main__":
    wpilib.run(PracticeBot, physics_enabled=True)