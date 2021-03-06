Name: nova-agent
Summary: Python nova-agent (Python 3)
Version: %{version}
Release: 1%{?dist}
License: Proprietary or GPL-2
Group: Applications/System
Source0: nova-agent.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python3-devel

%if "%{?dist}" == ".el7"
Requires: python36-cryptography
%else
Requires: python3-cryptography
%endif

%description
Python xenstore agent for Rackspace cloud servers
 This package installs the Python 3 version
%prep
%setup -q
%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py pyz --version %{version}
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp usr/nova-agent.pyz $RPM_BUILD_ROOT/usr/bin/nova-agent
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
cp etc/nova-agent.service $RPM_BUILD_ROOT/%{_unitdir}/nova-agent.service
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root,-)
/usr/bin/nova-agent
%{_unitdir}/nova-agent.service
%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service
