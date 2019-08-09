#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thermal_daemon
Version  : 1.9
Release  : 27
URL      : https://github.com/intel/thermal_daemon/archive/v1.9.tar.gz
Source0  : https://github.com/intel/thermal_daemon/archive/v1.9.tar.gz
Summary  : The "Linux Thermal Daemon" program from 01.org
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0
Requires: thermal_daemon-bin = %{version}-%{release}
Requires: thermal_daemon-config = %{version}-%{release}
Requires: thermal_daemon-data = %{version}-%{release}
Requires: thermal_daemon-license = %{version}-%{release}
Requires: thermal_daemon-man = %{version}-%{release}
Requires: thermal_daemon-services = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd-dev
Patch1: 0001-Add-add-udev-rule-to-start-thermald-just-when-the-ba.patch
Patch2: 0002-Add-thermal-conf-example-for-KBL-NUC.patch

%description
Thermal Daemon monitors and controls platform temperature.

%package bin
Summary: bin components for the thermal_daemon package.
Group: Binaries
Requires: thermal_daemon-data = %{version}-%{release}
Requires: thermal_daemon-config = %{version}-%{release}
Requires: thermal_daemon-license = %{version}-%{release}
Requires: thermal_daemon-services = %{version}-%{release}

%description bin
bin components for the thermal_daemon package.


%package config
Summary: config components for the thermal_daemon package.
Group: Default

%description config
config components for the thermal_daemon package.


%package data
Summary: data components for the thermal_daemon package.
Group: Data

%description data
data components for the thermal_daemon package.


%package extras-thermald-autostart
Summary: extras-thermald-autostart components for the thermal_daemon package.
Group: Default

%description extras-thermald-autostart
extras-thermald-autostart components for the thermal_daemon package.


%package license
Summary: license components for the thermal_daemon package.
Group: Default

%description license
license components for the thermal_daemon package.


%package man
Summary: man components for the thermal_daemon package.
Group: Default

%description man
man components for the thermal_daemon package.


%package services
Summary: services components for the thermal_daemon package.
Group: Systemd services

%description services
services components for the thermal_daemon package.


%prep
%setup -q -n thermal_daemon-1.9
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565314626
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1565314626
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/thermal_daemon
cp COPYING %{buildroot}/usr/share/package-licenses/thermal_daemon/COPYING
cp tools/thermal_monitor/qcustomplot/GPL.txt %{buildroot}/usr/share/package-licenses/thermal_daemon/tools_thermal_monitor_qcustomplot_GPL.txt
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/dbus-1/system.d
install -p -D -m 644 data/org.freedesktop.thermald.conf %{buildroot}/usr/share/dbus-1/system.d/org.freedesktop.thermald.conf
mkdir -p %{buildroot}/usr/lib/udev/rules.d/
install -p -D -m 644 90-thermald-on-battery.rules %{buildroot}/usr/lib/udev/rules.d/90-thermald-on-battery.rules
mkdir -p %{buildroot}/usr/share/thermald/
install -p -D -m 644 thermal-conf.KBL_NUC.xml %{buildroot}/usr/share/thermald/thermal-conf.KBL_NUC.xml
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../thermald.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/thermald

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/90-thermald-on-battery.rules

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.freedesktop.thermald.service
/usr/share/dbus-1/system.d/org.freedesktop.thermald.conf
/usr/share/thermald/thermal-conf.KBL_NUC.xml

%files extras-thermald-autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/thermald.service

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/thermal_daemon/COPYING
/usr/share/package-licenses/thermal_daemon/tools_thermal_monitor_qcustomplot_GPL.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/thermal-conf.xml.5
/usr/share/man/man8/thermald.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/thermald.service
