ekf_filter_node:
    ros__parameters:
        frequency: 30.0
        sensor_timeout: 0.1
        two_d_mode: true
        transform_time_offset: 0.0
        transform_timeout: 0.0
        print_diagnostics: true
        debug: false
        debug_out_file: /path/to/debug/file.txt
        publish_tf: true
        publish_acceleration: false
        reset_on_time_jump: true

        map_frame: map                   # Defaults to "map" if unspecified
        odom_frame: odom                 # Defaults to "odom" if unspecified
        base_link_frame: base_footprint  # Defaults to "base_link" if unspecified
        world_frame: odom                # Defaults to the value of odom_frame if unspecified

        odom0: wheel/odometry

        odom0_config: [false, false, false,
                       false, false, false,
                       true,  true,  false,
                       false, false, true,
                       false, false, false]

        #        [x_pos   , y_pos    , z_pos,
        #         roll    , pitch    , yaw,
        #         x_vel   , y_vel    , z_vel,
        #         roll_vel, pitch_vel, yaw_vel,
        #         x_accel , y_accel  , z_accel]

        odom0_queue_size: 2
        odom0_nodelay: false
        odom0_differential: false
        odom0_relative: false
        odom0_pose_rejection_threshold: 5.0
        odom0_twist_rejection_threshold: 1.0

        imu0: imu/data
        imu0_config: [false, false, false,
                      true,  true,  true,
                      false, false, false,
                      true,  true,  true,
                      true,  true,  true]
        imu0_nodelay: false
        imu0_differential: false
        imu0_relative: true
        imu0_queue_size: 5
        imu0_pose_rejection_threshold: 0.8                 # Note the difference in parameter names
        imu0_twist_rejection_threshold: 0.8                #
        imu0_linear_acceleration_rejection_threshold: 0.8  #

        imu0_remove_gravitational_acceleration: true
        use_control: false
        stamped_control: false
        control_timeout: 0.2
        control_config: [true, false, false, false, false, true]
        acceleration_limits: [1.3, 0.0, 0.0, 0.0, 0.0, 3.4]
        deceleration_limits: [1.3, 0.0, 0.0, 0.0, 0.0, 4.5]
        acceleration_gains: [0.8, 0.0, 0.0, 0.0, 0.0, 0.9]
        deceleration_gains: [1.0, 0.0, 0.0, 0.0, 0.0, 1.0]

        process_noise_covariance: [0.05, 0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.05, 0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.06, 0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.03, 0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.03, 0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.06, 0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.025, 0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.025, 0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.04, 0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.01, 0.0,    0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.01, 0.0,    0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.02, 0.0,    0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.01, 0.0,    0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.01, 0.0,
                                   0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.015]

        initial_estimate_covariance: [1e-9, 0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    1e-9, 0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    1e-9, 0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    1e-9, 0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    1e-9, 0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    1e-9, 0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    1e-9, 0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    1e-9, 0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    1e-9, 0.0,     0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    1e-9,  0.0,     0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     1e-9,  0.0,     0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     1e-9,  0.0,    0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     1e-9, 0.0,    0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    1e-9, 0.0,
                                      0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,     0.0,     0.0,     0.0,    0.0,    1e-9]
