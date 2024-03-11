class Pid_controller:
    def __init__(self, dt, Kp, Ki, Kd, e0=0):
        self.dt = dt
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.int = 0
        self.e = e0

    def __update__(self, ref, val):
        e_new = ref-val
        self.int = self.int + self.dt*e_new
        dy = (e_new-self.e)/self.dt
        self.e = e_new
        return self.Kp*e_new + self.Ki*self.int + self.Kd*dy # PID regulator

