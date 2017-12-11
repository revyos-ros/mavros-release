Name:           ros-lunar-mavros
Version:        0.22.0
Release:        0%{?dist}
Summary:        ROS mavros package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       GeographicLib
Requires:       GeographicLib-devel
Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-lunar-diagnostic-msgs
Requires:       ros-lunar-diagnostic-updater
Requires:       ros-lunar-eigen-conversions
Requires:       ros-lunar-geographic-msgs
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-libmavconn
Requires:       ros-lunar-mavlink
Requires:       ros-lunar-mavros-msgs
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-nav-msgs
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-rosconsole-bridge
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
Requires:       ros-lunar-tf2-eigen
Requires:       ros-lunar-tf2-ros
BuildRequires:  GeographicLib
BuildRequires:  GeographicLib-devel
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-lunar-angles
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-diagnostic-msgs
BuildRequires:  ros-lunar-diagnostic-updater
BuildRequires:  ros-lunar-eigen-conversions
BuildRequires:  ros-lunar-geographic-msgs
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-libmavconn
BuildRequires:  ros-lunar-mavlink
BuildRequires:  ros-lunar-mavros-msgs
BuildRequires:  ros-lunar-nav-msgs
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-rosconsole-bridge
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-std-srvs
BuildRequires:  ros-lunar-tf2-eigen
BuildRequires:  ros-lunar-tf2-ros

%description
MAVROS -- MAVLink extendable communication node for ROS with proxy for Ground
Control Station.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Dec 11 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.22.0-0
- Autogenerated by Bloom

* Thu Nov 16 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.5-0
- Autogenerated by Bloom

* Wed Nov 01 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.4-0
- Autogenerated by Bloom

* Sat Oct 28 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.3-0
- Autogenerated by Bloom

* Mon Sep 25 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.2-0
- Autogenerated by Bloom

* Fri Sep 22 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.1-0
- Autogenerated by Bloom

* Thu Sep 14 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.0-0
- Autogenerated by Bloom

* Mon Aug 28 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.20.1-0
- Autogenerated by Bloom

* Wed Aug 23 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.20.0-0
- Autogenerated by Bloom

* Thu May 25 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.19.0-0
- Autogenerated by Bloom

