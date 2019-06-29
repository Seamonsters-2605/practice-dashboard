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

        #create wheels
        frontLeft = sea.AngledWheel(ctre.WPI_TalonSRX(2), -0.75, 1.25, math.pi/2, 31527.59199, 16)
        frontRight = sea.AngledWheel(ctre.WPI_TalonSRX(1), 0.75, 1.25, math.pi/2, 31527.59199, 16)
        backLeft = sea.AngledWheel(ctre.WPI_TalonSRX(0), -0.75, -1.25, math.pi/2, 31527.59199, 16)
        backRight = sea.AngledWheel(ctre.WPI_TalonSRX(3), 0.75, -1.25, math.pi/2, 31527.59199, 16)

        #add wheels to drivetrain
        drivetrain.addWheel(frontLeft)
        drivetrain.addWheel(frontRight)
        drivetrain.addWheel(backLeft)
        drivetrain.addWheel(backRight)

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