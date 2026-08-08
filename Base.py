from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.robotics import DriveBase
from umath import pi



TIRE_DIAMETER = 62.4
AXLE_TRACK = 160 

STRAIGHT_SPEED = 400  
STRAIGHT_ACCEL = 500
TURN_RATE = 150
TURN_ACCEL = 270



# robot = DriveBase(
#     leftDriveMotor,
#     rightDriveMotor,
#     TIRE_DIAMETER,
#     AXLE_TRACK,
# )


global hub, leftAttachmentMotor, leftDriveMotor, rightDriveMotor, rightAttacment, Drive_base
hub = PrimeHub()
hub.system.set_stop_button(Button.CENTER)
rightDriveMotor = Motor(Port.A, Direction.CLOCKWISE) 
leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE) #E
rightAttachmentMotor = Motor(Port.B) #F
leftAttachmentMotor = Motor(Port.F) #b
# Chassis_sensor = ColorSensor(Port.c) 

Drive_base = DriveBase(leftDriveMotor, rightDriveMotor, wheel_diameter=56, axle_track=95)
Drive_base.use_gyro(True)
Drive_base.settings(turn_rate=60 * 3.6)
timer_move = StopWatch()

def Gyro():
    Gyro = hub.imu.heading()
    Gyro = Gyro % 360
    if  Gyro > 180:
        Gyro -= 360
    return Gyro

def pd_Drive(Power, Kp, Kd, last_error, is_wait = True):
    angle_B = leftDriveMotor.angle()-2
    angle_C = rightDriveMotor.angle()
    error = angle_B - angle_C

    P = Kp * error
    D = Kd * (error - last_error)
    pid_adj = P + D

    leftDriveMotor.dc(Power - pid_adj)
    rightDriveMotor.dc(Power + pid_adj)

    wait(10)
    return error



# def main_pid(target_angle, Kp = 1.9, Ki = 0, Kd = 2):

#     error = target_angle - 




#right_att

def sigma_Drive(Power, Kp, Kd, Deg, Brake=True):
    last_error = 0
    leftDriveMotor.reset_angle(0)
    rightDriveMotor.reset_angle(0)

    while (abs(leftDriveMotor.angle()) + abs(rightDriveMotor.angle())) / 2 <= Deg:
        last_error = pd_Drive(Power, Kp, Kd, last_error)

    if Brake:
        Drive_base.stop()


def move_time(Power_B, Power_C, ms, Brake=True):
    timer_move.reset()
    while timer_move.time() < ms:
        leftDriveMotor.dc(Power_B)
        rightDriveMotor.dc(Power_C)
    if Brake:
        Drive_base.stop()


def move_deg(Power_B, Power_C, Deg, Brake=True):
    leftDriveMotor.reset_angle(0)
    rightDriveMotor.reset_angle(0)
    while (abs(leftDriveMotor.angle()) + abs(rightDriveMotor.angle())) / 2 <= Deg:
        leftDriveMotor.dc(Power_B)
        rightDriveMotor.dc(Power_C)
    if Brake:
        Drive_base.stop()






def left_att(Power, Deg, is_wait=True):
    leftAttachmentMotor.run_angle(Power * 11, Deg, wait=is_wait)



def right_att(Power, Deg, is_wait=True):
    rightAttachmentMotor.run_angle(Power * 11, Deg, wait=is_wait)


def arm_pd(deg, sigma = True, kp = 2, kd = 1.2):
    Arm.reset_angle(0)
    last_error = 0
    while abs(Arm.angle()) <= deg:
        # print(Arm.angle())
        error = deg - Arm.angle()
        derivative = error - last_error

        correction = (kp * error) + (kd * derivative)
        if sigma == True:
            Arm.dc(correction)
        else:
            Arm.dc(-correction)
        wait(10)


def grabber_pd(deg, speed, sigma = True, kp = 2, kd = 1.2):
    grabber.reset_angle(0)
    last_error = 0
    while abs(grabber.angle()) <= deg:
        # print(grabber.angle())
        error = deg - grabber.angle()
        derivative = error - last_error

        correction = (kp * error) + (kd * derivative)
        if sigma == True:
            grabber.run(speed - correction)
        else:
            grabber.run(correction - speed)
        wait(10)






def bc_stop():
    leftDriveMotor.dc(0)
    rightDriveMotor.dc(0)

def map_value(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low


def PidDrive(distance, speed=600, Kp=1.5, Ki=0, Kd=0.05, Mp=3.1, Mi=0.005, Md=0.45, stop=Stop.BRAKE):
    hub.imu.reset_heading(0)

    leftDriveMotor.reset_angle(0)
    rightDriveMotor.reset_angle(0)


    integral = 0
    last_error = 0

    disI = 0
    lastDisE = 0

    isDone = True;
    # robot.reset()

    while isDone:

        dis = Drive_base.distance()

        error = 0 - hub.imu.heading()
        integral += error
        derivative = error - last_error
        correction = Kp * error + Ki * integral + Kd * derivative
        last_error = error

        disE = -dis + distance
        disI += disE
        disD = disE - lastDisE
        mSpeed = Mp * disE + Mi * disI + Md * disD
        lastDisE = disE
        # print("dis: " + str(dis))

        if mSpeed>speed : 
            mSpeed = speed
        elif mSpeed<-speed :
            mSpeed = -speed


        left_speed = mSpeed + correction
        right_speed = mSpeed - correction

        leftDriveMotor.run(left_speed)
        rightDriveMotor.run(right_speed)
        isDone = abs(dis - distance)>5
        wait(10)
            

    leftDriveMotor.stop()
    rightDriveMotor.stop()


def Pid_povorot(angle1,Tp = 1):
        hub.imu.reset_heading(0)
        leftDriveMotor.reset_angle(0)
        rightDriveMotor.reset_angle(0)

        t = 1

        Kp = 4.4
    
        Ki = 0.2
        integral = 0.0

        derivative = 0.0 
        lastError = 0.0 
        Kd = 4 
    
        while (t == 1):
            angle = hub.imu.heading()
            error = angle - angle1
            if (error < 0.01 ):
                integral = 0.0
            else:
                integral = integral + error 
            
            derivative = error - lastError  

            correction = (Kp*(error) + Ki*(integral) + Kd*derivative)

            power = correction * Tp 

            leftDriveMotor.run(-power)
            rightDriveMotor.run(power) 
            
            lastError = error  

            #print("error " + str(error) + "; correction " + str(correction)  + "; integral " + str(integral)  + "; derivative " + str(derivative)+ "; power_left " + str(power))   
            #wait(10.0)
            if (abs(angle - angle1) < 1):
                t = 0

        leftDriveMotor.stop()
        rightDriveMotor.stop()
        hub.imu.reset_heading(0)
        leftDriveMotor.reset_angle(0)
        rightDriveMotor.reset_angle(0)

def Pid_povorot_left(angle1,Tp = 1):
        hub.imu.reset_heading(0)
        leftDriveMotor.reset_angle(0)
        rightDriveMotor.reset_angle(0)
        angle1 = - angle1
        t = 1

        Kp = 4.1 #4.1
    
        Ki = 0.1 #0.1
        integral = 0.0

        derivative = 0.0 
        lastError = 0.0 
        Kd = 4 #4
    
        while (t == 1):
            angle = hub.imu.heading()
            error = angle - angle1 
            if (error > 0.01 ):
                integral = 0.0
            else:
                integral = integral + error 
            
            derivative = error - lastError  

            correction = (Kp*(error) + Ki*(integral) + Kd*derivative)

            power = correction * Tp 

            leftDriveMotor.run(-power)
            rightDriveMotor.run(power) 
            
            lastError = error  

            # print("error " + str(error) + "; correction " + str(correction)  + "; integral " + str(integral)  + "; derivative " + str(derivative)+ "; power_left " + str(power))   
            #wait(10.0)
            if (abs(angle - angle1) < 1):
                t = 0

        leftDriveMotor.stop()
        rightDriveMotor.stop()
        hub.imu.reset_heading(0)
        leftDriveMotor.reset_angle(0)
        rightDriveMotor.reset_angle(0)


def GyroDrive(distance, speed=STRAIGHT_SPEED, then=Stop.COAST_SMART, wait=True, accel=200):
        
    #print("Left motor angle:", self.leftDriveMotor.angle())
    #print("Right motor angle:", self.rightDriveMotor.angle())
    if speed > 540:
            speed = 540
    if speed < -540:
        speed = -540    
    Drive_base.settings(speed, accel, TURN_RATE, TURN_ACCEL)
    Drive_base.straight(distance, then, wait)
    Drive_base.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)



def GyroTurn(angle, then=Stop.COAST, wait=True, speed=TURN_RATE):
    Drive_base.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, speed, TURN_ACCEL)
    Drive_base.turn(angle, then, wait)
    Drive_base.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)



def LQR_povorot(target_angle,
                #   mass = 1.0,
                  k1=2, #0.9 2.2
                  k2=0.1, #0.15 0.35
                  max_power=60, #80
                  min_power=20,
                  tolerance=0.2):

    hub.imu.reset_heading(0)

    wait(200)

    while True:
        angle = hub.imu.heading()              # deg
        err = target_angle - angle

        gyro_z = hub.imu.angular_velocity()[2] # deg/s

        power = k1 * err + k2 * gyro_z #-

        if power > max_power:
            power = max_power
        elif power < -max_power:
            power = -max_power

        if abs(power) < min_power:
            power = min_power if power > 0 else -min_power

        leftDriveMotor.dc(power)
        rightDriveMotor.dc(-power)

        # print(hub.imu.heading())

        if abs(err) < tolerance:
            break

        
        wait(1) #10
        
        

    #Drive_base.stop()
    leftDriveMotor.hold()
    rightDriveMotor.hold()

    TLA = hub.imu.heading() #ваще прикольная штука(ещё в разроботке)

    hub.imu.reset_heading(0)


# print(TLA)




def Curve(radius, angle, stop=Stop.BRAKE, wait=True, speed=STRAIGHT_SPEED):
        Drive_base.settings(speed, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
        Drive_base.curve(radius, angle, stop, wait)

def backward(target_heading, final_angle, start_speed, max_speed, end_speed, decel_start_angle, accel_rate, kp_base=1.5, ki_base=0.001, kd_base=0, reset_gyro=True, stall_stop=False):
    adapt_rate = 0.0001 #0.0001 
    loop_counter = 0  
    stopwatch = StopWatch() 
    last_movement_time = stopwatch.time()  
    if reset_gyro:
        hub.imu.reset_heading(0)
    leftDriveMotor.reset_angle(0)
    rightDriveMotor.reset_angle(0)
    current_speed = -start_speed
    max_speed = -max_speed
    end_speed = -end_speed
    accel_rate = accel_rate
    integral_error = 0
    prev_error = 0
    kp_min, kp_max = 0.5 * kp_base, 2 * kp_base
    ki_min, ki_max = 0.5 * ki_base, 2 * ki_base
    kd_min, kd_max = 0.5 * kd_base, 2 * kd_base
    while abs(leftDriveMotor.angle()) < final_angle:
        
        left_angle = abs(leftDriveMotor.angle()) 
        remaining_distance = final_angle - left_angle 
        if left_angle >= decel_start_angle:
            scale = remaining_distance / (final_angle - decel_start_angle)
            current_speed = end_speed + (max_speed - end_speed) * scale
        else:
            if current_speed > max_speed:
                current_speed += accel_rate
                current_speed = max(current_speed, max_speed)
        error = hub.imu.heading() - target_heading
        integral_error += error  
        kp = kp_base + adapt_rate * abs(error)
        ki = ki_base + adapt_rate * abs(integral_error)
        kd = kd_base + adapt_rate * abs(error - prev_error)
        kp = max(kp_min, min(kp, kp_max)) 
        ki = max(ki_min, min(ki, ki_max))
        kd = max(kd_min, min(kd, kd_max))
        correction = kp * error + ki * integral_error + kd*(error - prev_error)
        loop_counter += 1
        if loop_counter % 100 == 0:
            wait(10)  
        
        if stall_stop:
            if abs(left_angle - abs(rightDriveMotor.angle())) > 100:
                break
            current_time = stopwatch.time()
            left_sp = abs(leftDriveMotor.speed())
            if (current_time - last_movement_time) > 200 and left_sp < 10:
                break
            if left_sp > 10:
                last_movement_time = current_time
        
        leftDriveMotor.dc(current_speed - correction)
        rightDriveMotor.dc(current_speed + correction)
        prev_error = error
        #for diagnostics
        # print(hub.imu.heading())
    leftDriveMotor.hold()
    rightDriveMotor.hold()



def forward(target_heading, final_angle, start_speed, max_speed, end_speed, decel_start_angle, accel_rate, kp_base=1, ki_base=0.0001, kd_base=0, reset_gyro=True, stall_stop=False):
    adapt_rate = 0.0001 #0.0001 
    loop_counter = 0  
    stopwatch = StopWatch() 
    last_movement_time = stopwatch.time()  
    if reset_gyro:
        hub.imu.reset_heading(0)
    leftDriveMotor.reset_angle(0)
    rightDriveMotor.reset_angle(0)
    # wait(100)
    current_speed = abs(start_speed)
    #current_speed = start_speed
    max_speed = abs(max_speed)
    end_speed = abs(end_speed)
    accel_rate = abs(accel_rate)
    integral_error = 0
    prev_error = 0
    kp_min, kp_max = 0.5 * kp_base, 2 * kp_base
    ki_min, ki_max = 0.5 * ki_base, 2 * ki_base
    kd_min, kd_max = 0.5 * kd_base, 2 * kd_base
    while abs(leftDriveMotor.angle()) < final_angle:
        
        left_angle = abs(leftDriveMotor.angle()) 
        remaining_distance = final_angle - left_angle 
        if left_angle >= decel_start_angle:
            scale = remaining_distance / (final_angle - decel_start_angle)
            current_speed = end_speed + (max_speed - end_speed) * scale
        else:
            if current_speed < max_speed:
                current_speed += accel_rate
                current_speed = min(current_speed, max_speed)
        error = hub.imu.heading() - target_heading
        integral_error += error  
        kp = kp_base + adapt_rate * abs(error)
        ki = ki_base + adapt_rate * abs(integral_error)
        kd = kd_base + adapt_rate * abs(error - prev_error)
        kp = max(kp_min, min(kp, kp_max)) 
        ki = max(ki_min, min(ki, ki_max))
        kd = max(kd_min, min(kd, kd_max))
        correction = kp * error + ki * integral_error + kd * (error - prev_error)
        loop_counter += 1
        if loop_counter % 100 == 0:
            wait(5)  
            '''
        if stall_stop:
            if abs(left_angle - abs(rightDriveMotor.angle())) > 100:
                break
            current_time = stopwatch.time()
            left_sp = abs(leftDriveMotor.speed())
            if (current_time - last_movement_time) > 200 and left_sp < 10:
                break
            if left_sp > 10:
                last_movement_time = current_time
                '''
        leftDriveMotor.dc(current_speed - correction)
        rightDriveMotor.dc(current_speed + correction)
        prev_error = error
    leftDriveMotor.hold()
    rightDriveMotor.hold()





right = True
left = False

def LQR_pivot(target_angle, k1=3, k2=0.3, max_power=60, min_power=25, direction = right, tolerance=0.5):

    hub.imu.reset_heading(0)

    wait(150)

    while True:
        angle = hub.imu.heading()              # deg
        err = target_angle - angle

        gyro_z = hub.imu.angular_velocity()[2] # deg/s

        power = k1 * err + k2 * gyro_z #-

        if power > max_power:
            power = max_power
        elif power < -max_power:
            power = -max_power

        if abs(power) < min_power:
            power = min_power if power > 0 else -min_power


        if direction == right:
            leftDriveMotor.dc(power)
        
        if direction == left:
            rightDriveMotor.dc(-power)

        if abs(err) < tolerance:
            break

        wait(1) #10
        # print(hub.imu.heading())

    PLA = hub.imu.heading() #ваще прикольная штука(ещё в разроботке)
    Drive_base.brake()

def right_att_dc(power, deg):
    rightAttachmentMotor.reset_angle(0)
    wait(100)
    while (abs(rightAttachmentMotor.angle()) < deg):
        rightAttachmentMotor.dc(power)
        wait(5)
        #print(rightAttachmentMotor.angle())
    rightAttachmentMotor.brake()





def LPD(final_angle, base_speed=100, kp=0.9, kd=3.5, TARGET=60, MAX_CORRECTION=400, wait=True):

    previous_error = 0
    # color_sensor = ColorSensor(Port.C)
    hub.imu.reset_heading(0)
    leftDriveMotor.reset_angle(0)
    rightDriveMotor.reset_angle(0)

    while abs(leftDriveMotor.angle()) < final_angle:
        
        reflection = ColorSensor.reflection(ColorSensor(Port.D))
        error = TARGET - reflection
        derivative = error - previous_error
        correction = kp * error + kd * derivative
        
        if correction > MAX_CORRECTION:
            correction = MAX_CORRECTION
        if correction < -MAX_CORRECTION:
            correction = -MAX_CORRECTION
        
        base = base_speed - abs(error) * 0.3
        if base < 30:
            base = 30
        
        left_speed = base + correction
        right_speed = base - correction
        leftDriveMotor.run(left_speed)
        rightDriveMotor.run(right_speed)
        
        previous_error = error

def LPD_scibidi(base_speed=100, kp=0.9, kd=3.5, TARGET=60, MAX_CORRECTION=400, wait=True):

    previous_error = 0
    # color_sensor = ColorSensor(Port.C)
    hub.imu.reset_heading(0)
    leftDriveMotor.reset_angle(0)
    rightDriveMotor.reset_angle(0)


    reflection = ColorSensor.reflection(ColorSensor(Port.D))
    error = TARGET - reflection
    derivative = error - previous_error
    correction = kp * error + kd * derivative
        
    if correction > MAX_CORRECTION:
        correction = MAX_CORRECTION
    if correction < -MAX_CORRECTION:
        correction = -MAX_CORRECTION
        
    base = base_speed - abs(error) * 0.3
    if base < 30:
        base = 30
        
    left_speed = base + correction
    right_speed = base - correction
    leftDriveMotor.run(left_speed)
    rightDriveMotor.run(right_speed)
        
    previous_error = error



def line_follow_2_sensors_acc(
    distance,
    Acc=200,
    Dec=200,
    LowPower=100,
    HighPower=200,
    EndPower=50,
    Kp=1.6,
    Kd=0.4,
    Brake=True
):
    Drive_base.reset()
    prev_error = 0

    while Drive_base.distance() < distance:

        # 📏 Пройденное расстояние
        dist = Drive_base.distance()

        # ⚡ Разгон / торможение
        if Acc < dist < distance - Dec:
            speed = HighPower
        else:
            if dist < distance / 2:
                speed = map_value(dist, 0, Acc, LowPower, HighPower)
            else:
                speed = map_value(dist, distance - Dec, distance, HighPower, EndPower)

        # 👀 Датчики
        right = ColorSensor.reflection(ColorSensor(Port.D))
        left = ColorSensor.reflection(ColorSensor(Port.C))

        error = left - right

        derivative = error - prev_error

        turn = Kp * error + Kd * derivative

        Drive_base.drive(speed, turn)

        prev_error = error
        wait(5)

    if Brake:
        Drive_base.brake()
    else:
        Drive_base.stop()


