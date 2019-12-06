#!/usr/bin/env python
# coding: utf-8

# In[119]:


import random
import time

#Using boolean to test different scenarios. On deployment these values will be taken from pedestrian sensors and EVAS respectively
pedestrian_click = False
emergency = False

#This class is used to collect data from external sources which will be used by the TCS
class TrafficData:
    def __init__(self):
        pass
    
    #Data from road sensors and traffic cameras
    def road_sensor():
        traffic_lane = []
        #Random generator for dummy traffic data
        for k in range(0,4):
            traffic_lane.append(random.randint(1,10))
        return traffic_lane
    
    #Data from EVAS. Currently using user input. On deployment will be using data from the EVAS system
    def evas():
        ev = 5
        while ev <=0 or ev > 4:
            ev = int(input('Which lane is the emergency vehicle approaching on? Choose between 1 to 4.\n'))
        return ev
    
    #Data from pedestrian button. Currently using user input. on deployment will be using data from the pedestrian button
    def pedestrian():
        ped = 5
        while ped <=0 or ped > 4:
            ped = int(input('Which lane is the pedestrian crossing? Choose between 1 to 4.\n'))
        return ped

#This class uses data from the TrafficData() class to manage traffic
class TrafficControl:
    def __init__(self, traffic_flow, pedestrian_alert=0):
        self.traffic_flow = traffic_flow
        self.pedestrian_alert = pedestrian_alert
        
    #Logic during regular traffic flow and pedestrian scenarios
    def normal_traffic(self):        
        #Loop to cycle between the 4 lanes
        for j in range(0,4):
            signal = ['Red', 'Red', 'Red', 'Red']
            #Time for pedestrians to cross the road
            timer_ped = 3
            
            #Logic for calculating green signal interval for each lane based on traffic density of those respective lanes
            timer_lane = self.traffic_flow[j] + 1
            
            #Checking to see if pedestrians need to cross the lane.
            if j != (self.pedestrian_alert - 1):
                signal[j] = 'Green'
                print(f'\nLane {j+1} changes to green while other lanes are in red\n{signal}\n')
                
                #Timer for traffic signal
                for i in range(0, timer_lane):
                    print(f'Green for {timer_lane - i} seconds')
                    time.sleep(1)
            #In case pedestrian needs to cross the lane        
            else:
                print(f'\nPedestrian crossing lane {self.pedestrian_alert}\n')
                #Timer for pedestrian crossing
                for i in range(0, timer_ped):
                    print(f'Pedestrian green for {timer_ped - i} seconds')
                    time.sleep(1)
                    
    #Logic during EVAS scenarios           
    def evas_alert(self, incoming_lane):
        self.incoming_lane = incoming_lane
        signal = ['Red', 'Red', 'Red', 'Red']
        signal[incoming_lane-1] = 'Green'
        return signal


traffic_data = TrafficData
road_sensor_data = traffic_data.road_sensor()

#For displaying the traffic density data and status of the system
for k in range(0,4):
        print(f'Traffic density in lane {k+1} is: {road_sensor_data[k]} vehicles/sec.')
print(f'\nEmergency status: {emergency}\nPedestrian status: {pedestrian_click}\n')

#Highest priority given to EVAS system by checking it first
if emergency == True:
    #Emergency vehicle operation mode:
    emergency_lane = traffic_data.evas()
    traffic = tcs.evas_alert(emergency_lane)
    print(f'\nAlert!\nEVAS override of traffic signals!\nChanging all lanes to RED except for oncoming emergency vehicle in lane {emergency_lane}\n{traffic}')

#Second highest priority given to pedestrians
elif pedestrian_click == True:
    #Pedestrian operation mode:
    pedestrian_lane = traffic_data.pedestrian()
    tcs = TrafficControl(road_sensor_data, pedestrian_lane)
    tcs.normal_traffic()

#Lowest priority for regular traffic flow
else:
    #Normal traffic operation mode:
    tcs = TrafficControl(road_sensor_data)
    tcs.normal_traffic()


# In[ ]:





# In[ ]:




