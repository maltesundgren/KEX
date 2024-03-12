class Pid_controller:
    def __init__(self, dt, Kp, Ki, Kd, e0=0):
        self.dt = dt
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.int = 0
        self.e = e0

    def update(self, ref, val, old_val):
        """ 'val' means FIOAI[k] and 'old_val' means FIOAI[k-1] """
        wind_up_min = -0.1
        wind_up_max = 0.5
        e_new = ref-val
        self.int = self.int + self.Ki*self.dt*e_new
        self.int = clip_func(self.int, wind_up_min, wind_up_max)
        
        dy = (val-old_val)/self.dt
        self.e = e_new
        print(f'int: {self.int}')
        print(f'e: {self.e}')
        return self.Kp*e_new + self.int + self.Kd*dy # PID regulator
    
    
    
def clip_func(x, x1,x2):
    """function that saturates the output to be y1 if less than x1 and y2 if more than x2"""
    if x<x1:
        return x1
    elif x>x2:
        return x2
    else:
        return x


