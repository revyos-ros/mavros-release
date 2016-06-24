Name:           ros-kinetic-mavros
Version:        0.18.1
Release:        0%{?dist}
Summary:        ROS mavros package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-eigen-conversions
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-libmavconn
Requires:       ros-kinetic-mavlink
Requires:       ros-kinetic-mavros-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-rosconsole-bridge
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf2-ros
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-eigen-conversions
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-libmavconn
BuildRequires:  ros-kinetic-mavlink
BuildRequires:  ros-kinetic-mavros-msgs
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-rosconsole-bridge
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-tf2-ros

%description
MAVROS -- MAVLink extendable communication node for ROS with proxy for Ground
Control Station.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Jun 24 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.1-0
- Autogenerated by Bloom

* Thu Jun 23 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.0-0
- Autogenerated by Bloom

* Fri May 20 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.17.3-0
- Autogenerated by Bloom

* Sun May 15 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.17.2-1
- Autogenerated by Bloom

* Fri Apr 29 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.17.2-0
- Autogenerated by Bloom

