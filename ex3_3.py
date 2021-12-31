import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    m = 1500
    l_f = 1.1
    l_r = 1.6
    k_f = 55*10**3
    k_r = 60*10**3
    delta_0 = 0.04

    if l_f*k_f - l_r*k_r > 0:
        print("Over-steer")
    else:
        print("Under-steer")
    #turning radius vs speed
    v = np.linspace(0, 60, num=1000)
    l = l_f + l_r
    rho = (1 - m/(2*l**2) * (l_f*k_f-l_r*k_r)/(k_f*k_r)*v**2)*(l/delta_0)
    plt.plot(v, rho)
    plt.legend(['turning radius'])
    plt.title('Turning radius vs velocity')
    plt.xlabel('vehicle speed m/s')
    plt.ylabel('turning radius m')
    plt.grid()
    plt.show()

    r = 1 / (1 - m/(2*l**2) * (l_f*k_f-l_r*k_r)/(k_f*k_r)*v**2) * v/l*delta_0
    plt.plot(v, r)
    plt.legend(['yaw rate'])
    plt.title('yaw rate')
    plt.xlabel('vehicle speed m/s')
    plt.ylabel('yaw rate rad/s')
    plt.grid()
    plt.show()

    beta = ( 1 - m/(2*l**2)*l_f/(l_r*k_r)*v**2 ) / (1 - m/(2*l**2) * (l_f*k_f-l_r*k_r)/(k_f*k_r)*v**2) * l_r/l*delta_0
    plt.plot(v, beta)
    plt.legend(['side slip angle'])
    plt.title('side slip angle')
    plt.xlabel('vehicle speed m/s')
    plt.ylabel('side slip angle rad')
    plt.grid()
    plt.show()
