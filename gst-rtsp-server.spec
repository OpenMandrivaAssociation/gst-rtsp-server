%define git 20090103

Summary:	RTSP server based on GStreamer
Name:		gst-rtsp-server
Version:	0.%{git}
Release:	%mkrel 0.1
License:	LGPLv2+
URL:		http://git.collabora.co.uk/?p=gst-rtsp-server.git;a=summary	
Group:		System/Servers
Source0:  	%{name}-%{git}.tar.gz	
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	gettext-devel

%description
RTSP server based on GStreamer.

%prep
%setup -q -n %{name} 

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/%{name}