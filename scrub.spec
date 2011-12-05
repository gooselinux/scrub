Name:		scrub
Version:	2.2
Release:	1%{?dist}
Summary:	Disk scrubbing program
License:	GPLv2+
Group:		System Environment/Base
URL:		http://code.google.com/p/diskscrub/
Source0:	http://diskscrub.googlecode.com/files/scrub-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Scrub writes patterns on files or disk devices to make
retrieving the data more difficult.  It operates in one of three
modes: 1) the special file corresponding to an entire disk is scrubbed
and all data on it is destroyed;  2) a regular file is scrubbed and
only the data in the file (and optionally its name in the directory
entry) is destroyed; or 3) a regular file is created, expanded until
the file system is full, then scrubbed as in 2).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS ChangeLog DISCLAIMER COPYING
%{_bindir}/scrub
%{_mandir}/man1/scrub.1*

%changelog
* Wed Jan 13 2010 Steve Grubb <sgrubb@redhat.com> 2.2-1
- initial package for RHEL 
