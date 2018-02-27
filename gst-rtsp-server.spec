%define api 1.0
%define major 0
%define libname %mklibname gstrtspserver %{api} %{major}
%define develname %mklibname -d gstrtspserver

Summary:	RTSP server library for the GStreamer framework
Name:		gst-rtsp-server
Version:	1.13.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gstreamer.freedesktop.org/
Source0:  	http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	gettext-devel
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	python-gstreamer1.0
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(python)

%description
RTSP server based on GStreamer.

%package -n %{libname}
Summary:	RTSP server library for the GStreamer framework
Group:		System/Libraries

%description -n %{libname}
RTSP server based on GStreamer.

%package -n %develname
Summary:	RTSP server library for the GStreamer framework
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}
Provides:	libgstrtspserver-devel = %{version}-%{release}

%description -n %{develname}
RTSP server based on GStreamer.

%prep
%setup -q
%apply_patches

%build
%configure \
	--with-pic \
	--enable-maintainer-mode \
	--enable-gtk-doc 
%make

%install
%makeinstall_std

%files -n %{libname}
%doc README AUTHORS
%{_libdir}/libgstrtspserver-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/GstRtspServer-%{api}.typelib
%{_libdir}/gstreamer-1.0/libgstrtspclientsink.so

%files -n %{develname}
%{_libdir}/libgstrtspserver-%{api}.so
%{_libdir}/pkgconfig/gstreamer-rtsp-server-%{api}.pc
%{_includedir}/gstreamer-%{api}/gst/rtsp-server
%{_datadir}/gir-1.0/GstRtspServer-%{api}.gir
%{_datadir}/gtk-doc/html/gst-rtsp-server-%{api}

