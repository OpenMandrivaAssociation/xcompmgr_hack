%define name	xcompmgr_hack
%define oname xcompmgr
%define version	2.02
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Sample X Compositing Manager
Source:		http://baghira.sourceforge.net/%{oname}-%{version}.tar.bz2
URL:		http://baghira.sourceforge.net/
License:	GPL
Group:		System/X11
BuildRoot:	%{_tmppath}/%{oname}-buildroot
BuildRequires:  X11-devel
Conflicts:      xcompmgr

%description
Patched version of xcompmgr 
Sample X Compositing Manager.
This is an unofficiall patched
version from http://baghira.sourceforge.net/


%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING ChangeLog INSTALL
%{_bindir}/%{oname}
%{_mandir}/man1/%{oname}.1*

