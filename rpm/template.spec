Name:           ros-melodic-imu-complementary-filter
Version:        1.2.0
Release:        0%{?dist}
Summary:        ROS imu_complementary_filter package

Group:          Development/Libraries
License:        BSD
URL:            http://www.mdpi.com/1424-8220/15/8/19302
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-message-filters
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-message-filters
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-tf

%description
Filter which fuses angular velocities, accelerations, and (optionally) magnetic
readings from a generic IMU device into a quaternion to represent the
orientation of the device wrt the global frame. Based on the algorithm by
Roberto G. Valenti etal. described in the paper &quot;Keeping a Good Attitude: A
Quaternion-Based Orientation Filter for IMUs and MARGs&quot; available at
http://www.mdpi.com/1424-8220/15/8/19302 .

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri May 25 2018 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.2.0-0
- Autogenerated by Bloom

