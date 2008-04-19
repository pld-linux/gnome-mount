Summary:	Programs for mounting, unmounting and ejecting storage devices
Summary(pl.UTF-8):	Programy do montowania, odmontowywania i wysuwania urządzeń przechowujących dane
Name:		gnome-mount
Version:	0.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	562ec9d0196e5e000bdd249a04a3aa6a
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.1
BuildRequires:	gnome-keyring-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.12.9
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libnotify-devel >= 0.3.0
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.22.0
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
Requires:	nautilus >= 2.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Programs for mounting, unmounting and ejecting storage devices.

%description -l pl.UTF-8
Programy do montowania, odmontowywania i wysuwania urządzeń
przechowujących dane.

%package devel
Summary:	gnome-mount development files
Summary(pl.UTF-8):	Pliki programistyczne gnome-mount
Group:		X11/Development/Libraries
Requires:	hal-devel >= 0.5.9
Requires:	pkgconfig

%description devel
This is the package containing gnome-mount development files.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne gnome-mount.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-nautilus-extension
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-mount.schemas

%preun
%gconf_schema_uninstall gnome-mount.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gnome-eject
%attr(755,root,root) %{_bindir}/gnome-mount
%attr(755,root,root) %{_bindir}/gnome-umount
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libgnome-mount.so
%{_datadir}/%{name}
%{_mandir}/man1/gnome-mount.1*
%{_sysconfdir}/gconf/schemas/gnome-mount.schemas

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/gnome-mount.pc
