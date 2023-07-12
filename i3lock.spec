Summary:	Improved screen locker
Name:		i3lock
Version:	2.14.1
Release:	1
License:	BSD
Group:		Applications
Source0:	https://i3wm.org/i3lock/%{name}-%{version}.tar.xz
# Source0-md5:	33d4bc8256a1566fbac911e405e53fdd
Source1:	%{name}.pam
URL:		https://i3wm.org/i3lock/
BuildRequires:	cairo-devel >= 1.14.4
BuildRequires:	libev-devel
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.45.0
BuildRequires:	ninja
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-xrm-devel
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
Requires:	cairo >= 1.14.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimalist screen locker based on slock.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/i3lock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE CHANGELOG
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/i3lock
%attr(755,root,root) %{_bindir}/i3lock
%{_mandir}/man1/i3lock.1*
