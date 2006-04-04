Summary:	SELinux policy generation scripts and tools
Summary(pl):	Skrypty i narzêdzia do generowania polityk SELinuksa
Name:		polgen
Version:	1.3
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.mitre.org/tech/selinux/%{name}-%{version}-src.tar.gz
# Source0-md5:	a1857eb58ea6f2485bb1f6cddce6977f
Patch0:		%{name}-info.patch
URL:		http://www.nsa.gov/selinux/
BuildRequires:	flex
BuildRequires:	libselinux-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	texinfo
%pyrequires_eq	python-libs
# contains SELinux-enhanced version of strace
Obsoletes:	strace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
polgen is a collection of scripts and tools developed by the MITRE
corporation to automate the SELinux policy generation process.

%description -l pl
polgen to zestaw skryptów i narzêdzi stworzonych przez firmê MITRE w
celu zautomatyzowania procesu generowania polityk SELinuksa.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/polgen.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*.info*
