%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-libmavconn
Version:        1.6.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS libmavconn package

License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       console-bridge-devel
Requires:       ros-noetic-mavlink
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-mavlink
BuildRequires:  ros-noetic-rosunit
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
MAVLink communication library. This library provide unified connection handling
classes and URL to connection object mapper. This library can be used in
standalone programs.

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
* Mon Feb 15 2021 Vladimir Ermakov <vooon341@gmail.com> - 1.6.0-1
- Autogenerated by Bloom

* Tue Feb 02 2021 Vladimir Ermakov <vooon341@gmail.com> - 1.5.2-1
- Autogenerated by Bloom

* Mon Jan 04 2021 Vladimir Ermakov <vooon341@gmail.com> - 1.5.1-1
- Autogenerated by Bloom

* Wed Nov 11 2020 Vladimir Ermakov <vooon341@gmail.com> - 1.5.0-1
- Autogenerated by Bloom

* Fri Sep 11 2020 Vladimir Ermakov <vooon341@gmail.com> - 1.4.0-1
- Autogenerated by Bloom

* Sat Aug 08 2020 Vladimir Ermakov <vooon341@gmail.com> - 1.3.0-1
- Autogenerated by Bloom

* Tue May 26 2020 Vladimir Ermakov <vooon341@gmail.com> - 1.2.0-1
- Autogenerated by Bloom

