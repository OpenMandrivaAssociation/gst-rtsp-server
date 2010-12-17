%define git 20090124
%define api 0.10
%define major 0
%define libname %mklibname gstrtspserver %api %major
%define develname %mklibname -d gstrtspserver
%define oname gst-rtsp

Summary:	RTSP server library for the GStreamer framework
Name:		gst-rtsp-server
Version:	0.10.7
Release:	%mkrel 1
License:	LGPLv2+
URL:		http://people.freedesktop.org/~wtay/
Group:		System/Libraries
Source0:  	%{oname}-%{version}.tar.bz2
Patch1: gst-rtsp-0.10.6-py-link.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
#gw: must be patched for the typo in rtsp gir file
BuildRequires:	libgstreamer-plugins-base-devel >= 0.10.29
BuildRequires:	gettext-devel
BuildRequires:	gstreamer0.10-python-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	python-devel
BuildRequires:	vala-devel >= 0.10

%description
RTSP server based on GStreamer.

%package -n %libname
Summary:	RTSP server library for the GStreamer framework
Group:		System/Libraries

%description -n %libname
RTSP server based on GStreamer.

%package -n %develname
Summary:	RTSP server library for the GStreamer framework
Group:		Development/C
Requires:	%libname = %version-%release
Provides:	%name-devel = %version
Provides:	libgstrtspserver-devel = %version-%release

%description -n %develname
RTSP server based on GStreamer.

%package -n python-rtspserver
Group: Development/Python
Summary: Python bindings for the RTSP-Server
Requires: gstreamer0.10-python

%description -n python-rtspserver
This is the Python binding for GStreamer's RTSP Server.


%prep
%setup -q -n %oname-%version
%apply_patches
rm -f  common/m4/introspection.m4
aclocal -I common/m4
autoreconf -fi
%build

%configure2_5x --disable-static --enable-maintainer-mode --enable-gtk-doc 
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files -n %libname
%defattr(-,root,root)
%doc README AUTHORS
%_libdir/libgstrtspserver-%api.so.%{major}*
%_libdir/girepository-1.0/GstRtspServer-%api.typelib

%files -n %develname
%defattr(-,root,root)
%_libdir/libgstrtspserver-%api.so
%_libdir/libgstrtspserver-%api.la
%_libdir/pkgconfig/%name-%api.pc
%_includedir/gstreamer-%api/gst/rtsp-server
%_datadir/vala/vapi/%name-%api.deps
%_datadir/vala/vapi/%name-%api.vapi
%_datadir/gir-1.0/GstRtspServer-%api.gir

%files -n python-rtspserver
%defattr(-,root,root)
%py_platsitedir/gst-%api/gst/rtspserver.la
%py_platsitedir/gst-%api/gst/rtspserver.so
%_datadir/gst-rtsp
