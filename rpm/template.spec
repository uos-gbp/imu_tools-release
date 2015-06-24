Name:           ros-hydro-rviz-imu-plugin
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS rviz_imu_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rviz_imu_plugin
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-rviz
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-rviz

%description
RVIZ plugin for IMU visualization

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Jun 24 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.5-0
- Autogenerated by Bloom

* Wed May 06 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.4-0
- Autogenerated by Bloom

* Thu Jan 29 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

* Tue Jan 27 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.2-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Martin Günther <martin.guenther1980@gmail.com> - 1.0.1-0
- Autogenerated by Bloom

* Fri Nov 28 2014 Ivan Dryanovski <ivan.dryanovski@gmail.com> - 1.0.0-1
- Autogenerated by Bloom

* Fri Nov 28 2014 Ivan Dryanovski <ivan.dryanovski@gmail.com> - 1.0.0-0
- Autogenerated by Bloom

