from time import sleep

class TrafficLight:
    color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
         i = 0
         while i < 3:
             print(f'Светофор переключается \n '
                   f'{TrafficLight.color[i]}')
             print('\r', end='')
             if i == 0:
                 sleep(7)
             elif i == 1:
                 sleep(5)
             elif i == 2:
                 sleep(3)
             i += 1

TrafficLight = TrafficLight()
TrafficLight.running()