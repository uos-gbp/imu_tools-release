%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-imu-complementary-filter
Version:        1.2.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS imu_complementary_filter package

License:        BSD
URL:            http://www.mdpi.com/1424-8220/15/8/19302
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-message-filters
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Filter which fuses angular velocities, accelerations, and (optionally) magnetic
readings from a generic IMU device into a quaternion to represent the
orientation of the device wrt the global frame. Based on the algorithm by
Roberto G. Valenti etal. described in the paper &quot;Keeping a Good Attitude: A
Quaternion-Based Orientation Filter for IMUs and MARGs&quot; available at
http://www.mdpi.com/1424-8220/15/8/19302 .

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Apr 09 2021 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.2.3-1
- Autogenerated by Bloom

* Mon May 25 2020 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.2.2-1
- Autogenerated by Bloom

