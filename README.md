## PlaneEFIv3.9
### Implementation of EFI over UAVCAN based on Ardupilot's Plane 3.9.5 firmware.

#### Details of what have been done so far:

1. Forked Arduplane 3.9.5
2. Added API_EFI library from [PR #6438](https://github.com/ArduPilot/ardupilot/pull/6438)
3. Worked through the AP_EFI rebase from [David Ingraham](https://github.com/DavidIngraham/ardupilot/tree/AP_EFI_Plane_385b2)

#### Expected output:

1. Preview EFI data messages on GCS virtual horizon.

##### Data Messages from Engine Include:
engine_load_percent                   
engine_speed_rpm                       
spark_dwell_time_ms                 
atmospheric_pressure_kpa               
intake_manifold_pressure_kpa         
intake_manifold_temperature         
coolant_temperature                 
oil_pressure                               
oil_temperature                    
fuel_pressure                        
fuel_consumption_rate_cm3pm                               
estimated_consumed_fuel_volume_cm3      
throttle_position_percent                     
ecu_index 
        
###### Data Messages from Cylinder Head Include:
ignition_timing_deg        
injection_time_ms         
cylinder_head_temperature   
exhaust_gas_temperature     
lambda_coefficient         
ecu_index
        
2. Preview RPM on MissionPlanner RPM dials
3. Output of data messages over UAVCAN from CAN port of Pixhawk 2.1.
