Name:           ros-melodic-libmavconn
Version:        0.31.0
Release:        1%{?dist}
Summary:        ROS libmavconn package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python2-devel
Requires:       console-bridge-devel
Requires:       ros-melodic-mavlink
BuildRequires:  boost-devel
BuildRequires:  boost-python2-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-mavlink
BuildRequires:  ros-melodic-rosunit

%description
MAVLink communication library. This library provide unified connection handling
classes and URL to connection object mapper. This library can be used in
standalone programs.

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
* Fri Jun 07 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.31.0-1
- Autogenerated by Bloom

* Mon May 20 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.30.0-1
- Autogenerated by Bloom

* Wed Mar 06 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.29.2-0
- Autogenerated by Bloom

* Sun Mar 03 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.29.1-0
- Autogenerated by Bloom

* Sat Feb 02 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.29.0-0
- Autogenerated by Bloom

* Thu Jan 03 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.28.0-0
- Autogenerated by Bloom

* Mon Nov 12 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.27.0-0
- Autogenerated by Bloom

* Sat Nov 10 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.3-1
- Autogenerated by Bloom

* Tue Aug 21 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.3-0
- Autogenerated by Bloom

* Wed Aug 08 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.2-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.1-0
- Autogenerated by Bloom

* Wed Jun 06 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.0-0
- Autogenerated by Bloom

* Mon May 14 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.25.1-0
- Autogenerated by Bloom

* Fri May 11 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.25.0-0
- Autogenerated by Bloom

* Mon May 07 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.24.0-0
- Autogenerated by Bloom

