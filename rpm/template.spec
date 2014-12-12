Name:           ros-indigo-imu-filter-madgwick
Version:        1.0.1
Release:        0%{?dist}
Summary:        ROS imu_filter_madgwick package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/imu_filter_madgwick
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf

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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
* Fri Dec 12 2014 Martin Günther <martin.guenther1980@gmail.com> - 1.0.1-0
- Autogenerated by Bloom

