%define oname		peas

%define api		1.0
%define major		0
%define libname		%mklibname %{oname} %{api} %{major}
%define libnamegtk	%mklibname %{oname}-gtk %{api} %{major}
%define develname	%mklibname %{oname} %{api} -d

%define girmajor	1.0
%define girname		%mklibname %{oname}-gir %{girmajor}
%define girnamegtk	%mklibname %{oname}-gtk-gir %{girmajor}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		libpeas
Version:	1.4.0
Release:	1
Summary:	Library for plugin handling
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		libpeas-pkgconfig-variable.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(seed)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90
BuildRequires:	pkgconfig(gjs-internals-1.0) >= 1.31.11
BuildRequires:	pkgconfig(gladeui-2.0)
BuildRequires:	vala >= 0.14.0.22
BuildRequires:	gettext-devel

%description
This is GNOME's plugin handling library.

#--------------------------------------------------------------------

%package data
Summary:	Library for plugin handling - data files
Group:		System/Libraries

%description data
This is GNOME's plugin handling library - data files

%files data -f %{name}.lang
%{_datadir}/icons/hicolor/*/actions/*
%{_datadir}/glade/catalogs/libpeas-gtk.xml

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Library plugin handling
Group:		System/Libraries
Requires:	%{name}-data = %{version}-%{release}
Provides:	%{mklibname %{oname} %{major}} = %{version}-%{release}
Obsoletes:	%{mklibname %{oname} %{major}} < 1.1.1

%description -n %{libname}
This is GNOME's plugin handling library.

%files -n %{libname}
%doc AUTHORS
%{_libdir}/%{name}-%{api}.so.%{major}*
%{_libdir}/%{name}-%{api}/loaders/libpythonloader.so
%{_libdir}/%{name}-%{api}/loaders/libseedloader.so
%{_libdir}/%{name}-%{api}/loaders/libgjsloader.so
#--------------------------------------------------------------------
%package -n %{libnamegtk}
Summary:	Library plugin handling UI part
Group:		System/Libraries
Requires:	%{name}-data = %{version}-%{release}
Provides:	%{mklibname %{oname}-gtk %{major}} = %{version}-%{release}
Obsoletes:	%{mklibname %{oname}-gtk %{major}} < 1.1.1

%description -n %{libnamegtk}
This is GNOME's plugin handling library - user interface part.

%files -n %{libnamegtk}
%{_libdir}/lib%{oname}-gtk-%{api}.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnamegtk} = %{version}-%{release}
Provides:	%{name}-devel = %version-%release
Provides:	%{oname}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d %{oname} } < 1.1.1

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -n %{develname}
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

#--------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Peas-%{girmajor}.typelib

#--------------------------------------------------------------------

%package -n %{girnamegtk}
Summary:	GObject Introspection interface description for %{name}-gtk
Group:		System/Libraries
Requires:	%{libnamegtk} = %{version}-%{release}

%description -n %{girnamegtk}
GObject Introspection interface description for %{name}-gtk.

%files -n %{girnamegtk}
%{_libdir}/girepository-1.0/PeasGtk-%{girmajor}.typelib

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
intltoolize -f
autoreconf
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

# we don't want these
find %{buildroot} -name "*.la" -delete
