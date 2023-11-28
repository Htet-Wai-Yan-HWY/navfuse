#include <Arduino.h>
// The micro_ros_platformio library provides the functions to communicate with ROS2
#include <Arduino.h>
// The micro_ros_platformio library provides the functions to communicate with ROS2
#include <micro_ros_arduino.h>
#include <TinyGPS++.h>

#define GPS_BAUDRATE 9600

// These are core ROS2 libraries for creating nodes, publishers, and executors
#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>

#include <micro_ros_utilities/type_utilities.h>
#include <micro_ros_utilities/string_utilities.h>


#include <sensor_msgs/msg/imu.h>
#include <sensor_msgs/msg/nav_sat_fix.h>

// Basic demo for accelerometer readings from Adafruit MPU6050
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu; //object of imu
TinyGPSPlus gps;  // the TinyGPS++ object


#if !defined(ESP32) && !defined(TARGET_PORTENTA_H7_M7) && !defined(ARDUINO_NANO_RP2040_CONNECT) && !defined(ARDUINO_WIO_TERMINAL)
#error This example is only avaible for Arduino Portenta, Arduino Nano RP2040 Connect, ESP32 Dev module and Wio Terminal
#endif

rcl_publisher_t publisher_imu;
rcl_publisher_t publisher_gps;
sensor_msgs__msg__Imu imu_msg;
sensor_msgs__msg__NavSatFix gps_msg;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;


#define LED_PIN 13

#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}


  char *SSID =const_cast<char*>("Zyme"); // WIFI SSID
  char* PASSWORD=const_cast<char*>("lolspaw7"); //WIFI PASSWORD
  char* HOST_IP =const_cast<char*>("192.168.19.102"); //host_ip

void error_loop(){
  while(1){
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    delay(100);
  }
}

void setup(void) {
  Serial.begin(115200);
  Serial2.begin(GPS_BAUDRATE);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");
  Serial.println(F("ESP32 - GPS module - connected"));

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: ");
  switch (mpu.getAccelerometerRange()) {
  case MPU6050_RANGE_2_G:
    Serial.println("+-2G");
    break;
  case MPU6050_RANGE_4_G:
    Serial.println("+-4G");
    break;
  case MPU6050_RANGE_8_G:
    Serial.println("+-8G");
    break;
  case MPU6050_RANGE_16_G:
    Serial.println("+-16G");
    break;
  }
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    Serial.println("+- 2000 deg/s");
    break;
  }

  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
  case MPU6050_BAND_260_HZ:
    Serial.println("260 Hz");
    break;
  case MPU6050_BAND_184_HZ:
    Serial.println("184 Hz");
    break;
  case MPU6050_BAND_94_HZ:
    Serial.println("94 Hz");
    break;
  case MPU6050_BAND_44_HZ:
    Serial.println("44 Hz");
    break;
  case MPU6050_BAND_21_HZ:
    Serial.println("21 Hz");
    break;
  case MPU6050_BAND_10_HZ:
    Serial.println("10 Hz");
    break;
  case MPU6050_BAND_5_HZ:
    Serial.println("5 Hz");
    break;
  }

  Serial.println("");
  delay(100);
    set_microros_wifi_transports(SSID, PASSWORD, HOST_IP, 8888);

  pinMode(LED_PIN, OUTPUT);


  delay(2000);

  allocator = rcl_get_default_allocator();

  //create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  // create node
  RCCHECK(rclc_node_init_default(&node, "micro_ros_imu_fusion", "", &support));

  // create publisher
  RCCHECK(rclc_publisher_init_default(
    &publisher_imu,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(sensor_msgs, msg, Imu),
    "/imu/micro"));

  RCCHECK(rclc_publisher_init_default(
    &publisher_gps,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(sensor_msgs, msg, NavSatFix),
    "/gps/micro"));
  
}

void loop() {

  if (Serial2.available() > 0 ){
    if (gps.encode(Serial2.read())){
      if (gps.location.isValid()){
        gps_msg.latitude = gps.location.lat();
        gps_msg.longitude = gps.location.lng();
      }
      else {
        Serial.println("-location INVALID");
      }
    }
  }
  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  /* Print out the values */
  // Serial.print("Acceleration X: ");
  // Serial.print(a.acceleration.x);
  // Serial.print(", Y: ");
  // Serial.print(a.acceleration.y);
  // Serial.print(", Z: ");
  // Serial.print(a.acceleration.z);
  // Serial.println(" m/s^2");

  // Serial.print("Rotation X: ");
  // Serial.print(g.gyro.x);
  // Serial.print(", Y: ");
  // Serial.print(g.gyro.y);
  // Serial.print(", Z: ");
  // Serial.print(g.gyro.z);
  // Serial.println(" rad/s");

  // Serial.print("Temperature: ");
  // Serial.print(temp.temperature);
  // Serial.println(" degC");
  // static unsigned long microsec = micros();

  // unsigned long sec = microsec/1000000;                    // time 
  // unsigned long nsec = (microsec - sec*1000000)*1000;
  // imu_msg.header.stamp.sec = sec;
  // imu_msg.header.stamp.nanosec = nsec;
  imu_msg.header.frame_id =  micro_ros_string_utilities_set(imu_msg.header.frame_id, "imu_link");
  // imu_msg.header.stamp = rmw_uros_epoch_millis();  //time syc to ros2 node need 

  imu_msg.linear_acceleration.x = a.acceleration.x;
  imu_msg.linear_acceleration.y = a.acceleration.y;
  imu_msg.linear_acceleration.z = a.acceleration.z;

  imu_msg.angular_velocity.x = g.gyro.x;
  imu_msg.angular_velocity.y = g.gyro.y;
  imu_msg.angular_velocity.z = g.gyro.z;
  RCSOFTCHECK(rcl_publish(&publisher_imu, &imu_msg, NULL));
  RCSOFTCHECK(rcl_publish(&publisher_gps, &gps_msg, NULL));
  // Serial.println("");
  // delay(500);
}