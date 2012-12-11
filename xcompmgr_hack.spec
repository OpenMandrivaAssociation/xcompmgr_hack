%define name	xcompmgr_hack
%define oname xcompmgr
%define version	2.02
%define release %mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Sample X Compositing Manager
Source:		http://baghira.sourceforge.net/%{oname}-%{version}.tar.bz2
URL:		http://baghira.sourceforge.net/
License:	GPL
Group:		System/X11
BuildRoot:	%{_tmppath}/%{oname}-buildroot
BuildRequires:  libx11-devel
BuildRequires:	libxcomposite-devel
BuildRequires:	libxdamage-devel
BuildRequires:	libxfixes-devel
BuildRequires:	libxrender-devel
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
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING ChangeLog INSTALL
%{_bindir}/%{oname}
%{_mandir}/man1/%{oname}.1*



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 2.02-8mdv2011.0
+ Revision: 634893
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.02-7mdv2010.0
+ Revision: 435069
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 2.02-6mdv2009.0
+ Revision: 262282
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.02-5mdv2009.0
+ Revision: 256679
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 2.02-3mdv2008.1
+ Revision: 140953
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Aug 24 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-24 15:37:53 (57891)
- Increase release
- Fix Group

* Thu Aug 03 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-03 13:14:18 (43289)
import xcompmgr_hack-2.02-2mdk

* Wed Feb 22 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.02-2mdk
annual rebuidl
- use mkrel

* Fri Feb 04 2005 Nicolas Lécureuil <neoclust@mandrake.org> 2.02-1mdk
- From Sebastien savarin <plouf@zarb.org>
              - initial release

