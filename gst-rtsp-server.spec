%define api 0.10
%define major 0
%define libname %mklibname gstrtspserver %{api} %{major}
%define develname %mklibname -d gstrtspserver
%define oname gst-rtsp

Summary:	RTSP server library for the GStreamer framework
Name:		gst-rtsp-server
Version:	0.10.8
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://people.freedesktop.org/~wtay/
Source0:  	http://people.freedesktop.org/~wtay/%{oname}-%{version}.tar.bz2
Patch0:		gst-rtsp-pygobject.patch
Patch1:		gst-rtsp-0.10.6-py-link.patch

BuildRequires:	gtk-doc
BuildRequires:	gettext-devel
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gst-python-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
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

%package -n python-rtspserver
Group: Development/Python
Summary: Python bindings for the RTSP-Server
Requires: gstreamer0.10-python

%description -n python-rtspserver
This is the Python binding for GStreamer's RTSP Server.

%prep
%setup -qn %oname-%{version}
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
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

%files -n %{develname}
%{_libdir}/libgstrtspserver-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_includedir}/gstreamer-%{api}/gst/rtsp-server
%{_datadir}/gir-1.0/GstRtspServer-%{api}.gir
%{_datadir}/gtk-doc/html/gst-rtsp-server-0.10
%{_datadir}/vala/vapi/%{name}-%{api}.deps
%{_datadir}/vala/vapi/%{name}-%{api}.vapi

%files -n python-rtspserver
%{py_platsitedir}/gst-%{api}/gst/rtspserver.so
%{_datadir}/gst-rtsp

