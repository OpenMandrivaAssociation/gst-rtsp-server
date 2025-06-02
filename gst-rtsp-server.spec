%define api	1.0
%define major	0
%define oname	gst-rtsp-server

%define libname %mklibname gstrtspserver %{api} %{major}
%define girname %mklibname gstrtspserver-gir %{api}
%define develname %mklibname -d gstrtspserver

Summary:	RTSP server library for the GStreamer framework
Name:		gstreamer1.0-rtsp-server
Version:	1.26.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		https://gstreamer.freedesktop.org/
Source0:  	https://gstreamer.freedesktop.org/src/%{oname}/%{oname}-%{version}.tar.xz
BuildRequires:	meson
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(libcgroup)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-bad-1.0)

%ifnarch %{riscv}
BuildRequires:	pkgconfig(valgrind)
%endif

%description
RTSP server based on GStreamer.

%package -n %{libname}
Summary:	RTSP server library for the GStreamer framework
Group:		System/Libraries

%description -n %{libname}
RTSP server based on GStreamer1.0.

%package -n %{develname}
Summary:	RTSP server library for the GStreamer framework
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}
Provides:	libgstrtspserver-devel = %{version}-%{release}

%description -n %{develname}
RTSP server based on GStreamer1.0.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gstrtspserver1.0_0 < 1.8.0

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n gstreamer%{api}-rtspclientsink
Summary:	rtspclientsink plugin for gstreamer%{api}
Group:		Networking/Other

%description -n gstreamer%{api}-rtspclientsink
rtspclientsink is an element that uses RECORD to send streams to an
RTSP server.

%prep
%setup -q -n %{oname}-%{version}

%build
%meson \
	-Ddoc=disabled \
	--buildtype=release
%meson_build

%install
%meson_install

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n gstreamer%{api}-rtspclientsink
%{_libdir}/gstreamer-1.0/libgstrtspclientsink.so

%files -n %{libname}
%doc README AUTHORS
%{_libdir}/libgstrtspserver-%{api}.so.%{major}{,.*}

%files -n %{girname}
%{_libdir}/girepository-1.0/GstRtspServer-%{api}.typelib

%files -n %{develname}
%{_libdir}/libgstrtspserver-%{api}.so
%{_libdir}/pkgconfig/gstreamer-rtsp-server-%{api}.pc
%{_includedir}/gstreamer-%{api}/gst/rtsp-server
%{_datadir}/gir-1.0/GstRtspServer-%{api}.gir
