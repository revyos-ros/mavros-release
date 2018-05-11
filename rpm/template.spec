Name:           ros-melodic-mavros
Version:        0.25.0
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
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-eigen-conversions
Requires:       ros-melodic-geographic-msgs
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-libmavconn
Requires:       ros-melodic-mavlink
Requires:       ros-melodic-mavros-msgs
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-rosconsole-bridge
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf2-eigen
Requires:       ros-melodic-tf2-ros
BuildRequires:  GeographicLib
BuildRequires:  GeographicLib-devel
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-eigen-conversions
BuildRequires:  ros-melodic-geographic-msgs
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-libmavconn
BuildRequires:  ros-melodic-mavlink
BuildRequires:  ros-melodic-mavros-msgs
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-rosconsole-bridge
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf2-eigen
BuildRequires:  ros-melodic-tf2-ros

%description
MAVROS -- MAVLink extendable communication node for ROS with proxy for Ground
Control Station.

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
* Fri May 11 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.25.0-0
- Autogenerated by Bloom

* Mon May 07 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.24.0-0
- Autogenerated by Bloom

