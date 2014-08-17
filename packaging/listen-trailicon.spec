%define name listen-trailicon
%define version 0.0.1
%define unmangled_version 0.0.1
%define release 1

Summary: Sugar trail icon for the sugarlistens program
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: sugarlistens
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rodrigo Parra <rodpar07@gmail.com>

%description
Sugar trail icon for the sugarlistens program

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/sugar/extensions/deviceicon/
cp -r  $RPM_BUILD_DIR/%{name}-%{version}/speech $RPM_BUILD_ROOT/usr/share/sugar/extensions/deviceicon/
install -m644 $RPM_BUILD_DIR/%{name}-%{version}/listen.py $RPM_BUILD_ROOT/usr/share/sugar/extensions/deviceicon/

mkdir -p $RPM_BUILD_ROOT/usr/share/icons/sugar/scalable/device
install -m644 $RPM_BUILD_DIR/%{name}-%{version}/icons/listen.svg $RPM_BUILD_ROOT/usr/share/icons/sugar/scalable/device
install -m644 $RPM_BUILD_DIR/%{name}-%{version}/icons/listen-muted.svg $RPM_BUILD_ROOT/usr/share/icons/sugar/scalable/device

%post
gtk-update-icon-cache /usr/share/icons/sugar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/share/icons/sugar/scalable/device/listen-muted.svg
/usr/share/icons/sugar/scalable/device/listen.svg
/usr/share/sugar/extensions/deviceicon/listen.py
/usr/share/sugar/extensions/deviceicon/listen.pyc
/usr/share/sugar/extensions/deviceicon/listen.pyo
/usr/share/sugar/extensions/deviceicon/speech/en/dictionary.dic
/usr/share/sugar/extensions/deviceicon/speech/en/language.fsg
/usr/share/sugar/extensions/deviceicon/speech/en/language.gram
