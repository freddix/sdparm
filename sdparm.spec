Summary:	sdparm - listing and changing SCSI disk parameters
Name:		sdparm
Version:	1.08
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://sg.danny.cz/sg/p/%{name}-%{version}.tgz
# Source0-md5:	be5786f37499018ef44f409597c92d42
URL:		http://sg.danny.cz/sg/sdparm.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sdparm is a utility for listing and potentially changing SCSI disk
parameters. More generally it can be used on any device that uses a
SCSI command set. Apart from SCSI disks, examples of devices that use
SCSI command sets are ATAPI CD/DVD drives, SCSI and ATAPI tape drives
and SCSI enclosures.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/s*
%{_mandir}/man8/s*.8*

