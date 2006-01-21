Summary:	Programs for mounting, unmounting and ejecting storage devices
Name:		gnome-mount
Version:	0.3
Release:	1
License:	GPL v.2
Group:		Applications
Source0:	http://freedesktop.org/~david/%{name}-%{version}.tar.gz
# Source0-md5:	2bf5649b21e98378c49e44bbd42bf89d
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.31
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	hal-devel >= 0.5.5
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.1.5
BuildRequires:	libtool
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Programs for mounting, unmounting and ejecting storage devices.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-mount.schemas

%preun
%gconf_schema_uninstall gnome-mount.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/gnome-mount.schemas
