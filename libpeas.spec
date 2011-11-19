%define api 1.0
%define major 0
%define girmajor	1.0

%define libname 	%mklibname peas %major
%define libgtk		%mklibname peas-gtk %major
%define develname	%mklibname -d peas
%define develgtk	%mklibname -d peas-gtk
%define girname		%mklibname %{oname}-gir %{girmajor}
%define girnamegtk	%mklibname %{oname}-gtk-gir %{girmajor}

Name:		libpeas
Version:	1.2.0
Release:	1
Summary:	Library for plugin handling
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(seed)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python-gobject-devel >= 2.28
BuildRequires:  vala-devel >= 0.11.1

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

%description -n %{libname}
This is GNOME's plugin handling library.

%package -n %{libgtk}
Summary:	Library plugin handling UI part
Group:		System/Libraries

%description -n %{libgtk}
This is GNOME's plugin handling library - user interface part.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{girnamegtk}
Summary:	GObject Introspection interface description for %{name}-gtk
Group:		System/Libraries
Requires:	%{libgtk} = %{version}-%{release}

%description -n %{girnamegtk}
GObject Introspection interface description for %{name}-gtk.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{develgtk}
Summary:	Development files for %{name}-gtk
Group:		Development/C
Requires:	%{libgtk} = %{version}-%{release}
Provides:	%{name}-gtk-devel = %{version}-%{release}

%description -n %{develgtk}
The %{name}-gtk-devel package contains libraries and header files for
developing applications that use %{name}-gtk.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la | xargs rm
%find_lang %{name}

%files data -f %{name}.lang
%doc AUTHORS
%{_datadir}/icons/hicolor/*/actions/*
%{_libdir}/%{name}-%api/loaders/libcloader.*
%{_libdir}/%{name}-%api/loaders/libpythonloader.*
%{_libdir}/%{name}-%api/loaders/libseedloader.*

%files -n %{libname}
%{_libdir}/libpeas-%api.so.%{major}*

%files -n %{libgtk}
%{_libdir}/libpeas-gtk-%api.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Peas-%api.typelib

%files -n %{girnamegtk}
%{_libdir}/girepository-1.0/PeasGtk-%api.typelib

%files -n %{develname}
%doc ChangeLog
%{_bindir}/peas-demo
%{_libdir}/peas-demo
%{_includedir}/libpeas/*
%{_libdir}/libpeas-1.0.so
%{_libdir}/pkgconfig/%{name}-%api.pc
%{_datadir}/gir-1.0/Peas-%api.gir

%files -n %{develgtk}
%{_includedir}/libpeas-gtk/*
%{_libdir}/libpeas-gtk-1.0.so
%{_libdir}/pkgconfig/%{name}-gtk-%api.pc
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gir-1.0/PeasGtk-%api.gir
