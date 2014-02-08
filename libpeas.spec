%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define oname	peas
%define api	1.0
%define major	0
%define libname	%mklibname %{oname} %{api} %{major}
%define libgtk	%mklibname %{oname}-gtk %{api} %{major}
%define devname	%mklibname %{oname} %{api} -d
%define girname	%mklibname %{oname}-gir %{api}
%define girgtk	%mklibname %{oname}-gtk-gir %{api}
%define _disable_ld_no_undefined 1

Summary:	Library for plugin handling
Name:		libpeas
Version:	1.8.1
Release:	2
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libpeas/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		libpeas-1.8.1-link-plugins.patch

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	vala >= 0.14.0.22
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gjs-internals-1.0)
BuildRequires:	pkgconfig(gladeui-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(seed)

%description
This is GNOME's plugin handling library.

%package data
Summary:	Library for plugin handling - data files
Group:		System/Libraries

%description data
This is GNOME's plugin handling library - data files

%package -n %{libname}
Summary:	Library plugin handling
Group:		System/Libraries
Requires:	%{name}-data = %{version}-%{release}

%description -n %{libname}
This is GNOME's plugin handling library.

%package -n %{libgtk}
Summary:	Library plugin handling UI part
Group:		System/Libraries
Requires:	%{name}-data = %{version}-%{release}

%description -n %{libgtk}
This is GNOME's plugin handling library - user interface part.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{girgtk}
Summary:	GObject Introspection interface description for %{name}-gtk
Group:		System/Libraries

%description -n %{girgtk}
GObject Introspection interface description for %{name}-gtk.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgtk} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Requires:	%{girgtk} = %{version}-%{release}
Provides:	%{name}-devel = %version-%release
Provides:	%{oname}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%apply_patches
autoreconf

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files data -f %{name}.lang
%doc AUTHORS
%{_iconsdir}/hicolor/*/actions/*
%{_datadir}/glade/catalogs/libpeas-gtk.xml

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*
%{_libdir}/%{name}-%{api}/loaders/libpythonloader.so
%{_libdir}/%{name}-%{api}/loaders/libseedloader.so
%{_libdir}/%{name}-%{api}/loaders/libgjsloader.so

%files -n %{libgtk}
%{_libdir}/lib%{oname}-gtk-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Peas-%{api}.typelib

%files -n %{girgtk}
%{_libdir}/girepository-1.0/PeasGtk-%{api}.typelib

%files -n %{devname}
%doc ChangeLog	
%doc %{_datadir}/gtk-doc/html/%{name}
%{_bindir}/peas-demo
%{_libdir}/peas-demo
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-gtk-%{api}.pc
%{_datadir}/gir-1.0/Peas-%{api}.gir
%{_datadir}/gir-1.0/PeasGtk-%{api}.gir

