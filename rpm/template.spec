Name:           ros-jade-imu-filter-madgwick
Version:        1.1.2
Release:        0%{?dist}
Summary:        ROS imu_filter_madgwick package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/imu_filter_madgwick
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-message-filters
Requires:       ros-jade-nodelet
Requires:       ros-jade-pluginlib
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf2
Requires:       ros-jade-tf2-geometry-msgs
Requires:       ros-jade-tf2-ros
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rosunit
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf2
BuildRequires:  ros-jade-tf2-geometry-msgs
BuildRequires:  ros-jade-tf2-ros

%description
Filter which fuses angular velocities, accelerations, and (optionally) magnetic
readings from a generic IMU device into an orientation. Based on code by
Sebastian Madgwick,
http://www.x-io.co.uk/node/8#open_source_ahrs_and_imu_algorithms.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Sep 07 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.2-0
- Autogenerated by Bloom

* Wed Sep 07 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.1-0
- Autogenerated by Bloom

* Mon Apr 25 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

* Mon Apr 25 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.11-1
- Autogenerated by Bloom

* Fri Apr 22 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.11-0
- Autogenerated by Bloom

* Fri Apr 08 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.9-0
- Autogenerated by Bloom

