import math
import ctre
import wpilib
import seamonsters as sea
import dashboard

class PracticeBot(sea.GeneratorBot):

    def robotInit(self):
        #set up drivetrain
        self.drivetrain = self.initDrivetrain()
        sea.setSimulatedDrivetrain(self.drivetrain)

        #set up dashboard
        self.app = None
        sea.startDashboard(self, dashboard.PracticeDashboard)

    def teleop(self):
        yield from self.updateDashboardGenerator()

    #creates and returns the drivetrain
    def initDrivetrain(self):
        drivetrain = sea.SuperHolonomicDrive()

        #configure talons
        leftTalon = ctre.WPI_TalonSRX(2)
        rightTalon = ctre.WPI_TalonSRX(1)
        for talon in [leftTalon, rightTalon]:
            talon.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder, 0, 0)

        #create wheels
        left = sea.AngledWheel(leftTalon, -0.75, 0, math.pi/2, 31527.59199, 16)
        right = sea.AngledWheel(rightTalon, 0.75, 0, math.pi/2, 31527.59199, 16)

        #add wheels to drivetrain
        drivetrain.addWheel(left)
        drivetrain.addWheel(right)

        return drivetrain

    #does the events called by the dashboard
    def updateDashboardGenerator(self):
        if self.app is not None:
            self.app.clearEvents()
        while True:
            v = None
            if self.app is not None:
                v = self.app.doEvents()
            yield v
    
    #dashboard callbacks
    @sea.queuedDashboardEvent
    def c_driveForward(self, button):
        self.drivetrain.drive(16, math.pi/2, 0)

    @sea.queuedDashboardEvent
    def c_stop(self, button):
        self.drivetrain.drive(0,0,0)

if __name__ == "__main__":
    wpilib.run(PracticeBot)