Name:           ros-indigo-imu-complementary-filter
Version:        1.0.12
Release:        1%{?dist}
Summary:        ROS imu_complementary_filter package

Group:          Development/Libraries
License:        BSD
URL:            http://www.mdpi.com/1424-8220/15/8/19302
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-filters
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf

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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 07 2016 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.0.12-1
- Autogenerated by Bloom

* Wed Sep 07 2016 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.0.12-0
- Autogenerated by Bloom

* Fri Apr 22 2016 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.0.10-0
- Autogenerated by Bloom

* Fri Oct 16 2015 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.0.9-0
- Autogenerated by Bloom

* Wed Oct 07 2015 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.0.8-0
- Autogenerated by Bloom

* Tue Oct 06 2015 Roberto G. Valenti <robertogl.valenti@gmail.com> - 1.0.6-0
- Autogenerated by Bloom

