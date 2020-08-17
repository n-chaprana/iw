Name:           iw
Version:        5.4
Release:        0
License:        ISC License
Summary:        CLI configuration utility for wireless devices
Url:            http://kernel.org/pub/software/network/iw/
Group:          Network & Connectivity/test
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)

%description
iw is a new nl80211 based CLI configuration utility for wireless devices. It
supports all new drivers that have been added to the kernel recently. The
old tool iwconfig, which uses Wireless Extensions interface, is deprecated
and it's strongly recommended to switch to iw and nl80211.

Like the rest of the Linux kernel, iw is still under development. Features are
added 'as we go'. The only documentation for iw is this page and output
from 'iw help'. Please help expand this page.

There is a page listing use cases with iwconfig and iw: replacing iwconfig.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
cp %{_builddir}/%{name}-%{version}/iw %{buildroot}%{_bindir}

%post

%preun

%postun

%files
%manifest iw.manifest
%attr(500,root,root) %{_bindir}/iw
%license COPYING
